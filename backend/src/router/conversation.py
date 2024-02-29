from fastapi import APIRouter
from pydantic import BaseModel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.memory import VectorStoreRetrieverMemory
from langchain.chains import LLMChain
from ..config import OPENAI_API_KEY, OPENAI_BASE_URL, POSTGRES_CONNECTION_STRING
from ..memory import Memory
from ..templates import default
import datetime

router = APIRouter()


class ConversationRequest(BaseModel):
    message: str
    user_id: str
    conversation_id: str


class ConversationResponse(BaseModel):
    message: str


@router.post("/conversation")
def conversation(request: ConversationRequest) -> ConversationResponse:
    output_parser = StrOutputParser()
    template = default.DEFAULT_TEMPLATE
    prompt = PromptTemplate(input_variables=["history", "input"], template=template)

    collection_name = request.user_id + request.conversation_id
    memory: VectorStoreRetrieverMemory = Memory.get_pgvector_memory(
        connection_string=POSTGRES_CONNECTION_STRING,
        collection_name=collection_name,
        k=10,
    )

    relevant_docs = memory.retriever.get_relevant_documents(request.message)

    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        base_url=OPENAI_BASE_URL,
        openai_api_key=OPENAI_API_KEY,
    )

    chain = LLMChain(llm=llm, output_parser=output_parser, prompt=prompt)

    try:
        output = chain.invoke(
            input={"input": request.message, "history": relevant_docs},
            return_only_outputs=True,
        )

        # Save to memory
        new_docs = memory._form_documents(
            inputs={"input": request.message}, outputs=output
        )

        ct = datetime.datetime.now()
        new_docs[0].metadata = {"created_at": ct.timestamp()}
        memory.retriever.add_documents(new_docs)

        # Return response
        return ConversationResponse(message=output["text"])

    except BaseException as e:
        raise e

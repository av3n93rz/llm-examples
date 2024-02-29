from fastapi import APIRouter
from pydantic import BaseModel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI, OpenAI, OpenAIEmbeddings
from langchain.memory import VectorStoreRetrieverMemory
from langchain.chains import LLMChain, ConversationChain
from langchain_core.documents import Document
from ..config import OPENAI_API_KEY, OPENAI_BASE_URL, POSTGRES_CONNECTION_STRING
from ..memory import Memory
from ..templates import default
from langchain_core.runnables import RunnableConfig

router = APIRouter()


class ConversationRequest(BaseModel):
    message: str


class ConversationResponse(BaseModel):
    message: str


""" memory: VectorStoreRetrieverMemory = Memory.get_inmemory_vectorstore_memory(
    embedding_size=1536, k=10
) """


@router.post("/conversation")
async def conversation(request: ConversationRequest) -> ConversationResponse:
    output_parser = StrOutputParser()
    template = default.DEFAULT_TEMPLATE
    memory: VectorStoreRetrieverMemory = Memory.get_pgvector_memory(
        connection_string=POSTGRES_CONNECTION_STRING,
        collection_name="UserID+ConversationId",
        k=10,
    )
    """ 
    res = await memory.retriever.aadd_documents(
        [Document(page_content="asd:)", metadata={"name": "Avi"})]
    )
    print("IDDDDSS", res) """

    prompt = PromptTemplate(input_variables=["history", "input"], template=template)

    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        base_url=OPENAI_BASE_URL,
        openai_api_key=OPENAI_API_KEY,
    )

    chain = LLMChain(llm=llm, output_parser=output_parser, memory=memory, prompt=prompt)

    output = await chain.ainvoke(input=request.message, return_only_outputs=True)
    # response = chain.predict(input=request.message)
    return ConversationResponse(message=output["text"])

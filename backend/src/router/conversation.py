from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from ..config import OPENAI_API_KEY, OPENAI_BASE_URL, POSTGRES_CONNECTION_STRING
from ..templates import default
from ..custom_memory.memory import CustomCombinedMemory
from langchain_openai import OpenAIEmbeddings
import uuid

router = APIRouter()


class ConversationRequest(BaseModel):
    message: str
    user_id: str
    conversation_id: str


class ConversationResponse(BaseModel):
    message: str


@router.post("/conversation")
def conversation(request: ConversationRequest) -> ConversationResponse:
    message = request.message
    conversation_id = request.conversation_id
    user_id = request.user_id

    output_parser = StrOutputParser()
    template = default.DEFAULT_TEMPLATE
    prompt = PromptTemplate(
        input_variables=["history", "input", "last_messages"], template=template
    )

    custom_memory = CustomCombinedMemory(
        connection_string=POSTGRES_CONNECTION_STRING,
        embedding_function=OpenAIEmbeddings(),
    )

    has_access = custom_memory.check_user_access(
        user_id=user_id, conversation_id=conversation_id
    )

    if has_access is False:
        raise HTTPException(
            status_code=404,
            detail="The conversation you are trying to message does not exist",
        )

    # Long term memory
    relevant_docs = custom_memory.get_relevant_documents(
        query=message, conversation_id=conversation_id
    )
    relevant_docs = custom_memory.concat_documents(documents=relevant_docs)

    # Short term memory
    last_messages = custom_memory.get_short_term_memory(conversation_id=conversation_id)
    last_messages = custom_memory.concat_documents(
        documents=last_messages if last_messages is not None else []
    )

    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        base_url=OPENAI_BASE_URL,
        openai_api_key=OPENAI_API_KEY,
    )

    chain = LLMChain(llm=llm, output_parser=output_parser, prompt=prompt)

    try:
        output = chain.invoke(
            input={
                "input": message,
                "history": relevant_docs,
                "last_messages": last_messages,
            },
            return_only_outputs=True,
        )

        # Save to memory
        custom_memory.save_conversation(
            user_id=user_id,
            conversation_id=uuid.UUID(conversation_id),
            input=message,
            output=output["text"],
        )

        # Return response
        return ConversationResponse(message=output["text"])

    except BaseException as e:
        raise e

import faiss
from langchain_openai import OpenAIEmbeddings
from langchain.memory import VectorStoreRetrieverMemory
from langchain_community.docstore import InMemoryDocstore
from langchain_community.vectorstores.pgvector import PGVector
from langchain_community.vectorstores import FAISS


class Memory:
    def get_pgvector_memory(
        connection_string: str, collection_name: str, k: int
    ) -> VectorStoreRetrieverMemory:
        vectorstore = PGVector(
            collection_name=collection_name,
            connection_string=connection_string,
            embedding_function=OpenAIEmbeddings(),
        )
        retriever = vectorstore.as_retriever(search_kwargs=dict(k=k))
        return VectorStoreRetrieverMemory(retriever=retriever)

    def get_inmemory_vectorstore_memory(
        embedding_size: int, k: int
    ) -> VectorStoreRetrieverMemory:
        index = faiss.IndexFlatL2(embedding_size)
        vectorstore = FAISS(OpenAIEmbeddings(), index, InMemoryDocstore({}), {})
        retriever = vectorstore.as_retriever(search_kwargs=dict(k=k))
        return VectorStoreRetrieverMemory(retriever=retriever)

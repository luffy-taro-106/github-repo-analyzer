
from langchain.vectorstores import Chroma
from langchain.embeddings import JinaEmbeddings
from langchain.document_loaders import DirectoryLoader
def get_vectorstore(path="./cloned_repo"):
    loader = DirectoryLoader(path, glob="**/*.py")
    docs = loader.load()
    embeddings = JinaEmbeddings()
    return Chroma.from_documents(docs, embeddings)


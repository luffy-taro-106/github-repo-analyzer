
from rich.console import Console
from langchain.chains import RetrievalQA
from retriever.vector_store import get_vectorstore
from langchain.llms import ChatGroq

def run_terminal_qa():
    console = Console()
    vectorstore = get_vectorstore()
    llm = ChatGroq(model="llama3-70b")  # ADK agent
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())
    while True:
        query = input("[User] > ")
        if query in ["exit", "quit"]: break
        answer = qa.run(query)
        console.print(f"[bold green]Answer:[/bold green] {answer}")


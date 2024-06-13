from langchain.agents import Tool
from langchain.chains import LLMMathChain
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv

class Calculator():
    def __init__(self):
        load_dotenv()
        self.model = ChatOpenAI(model="gpt-4o")
        self.llm_math = LLMMathChain.from_llm(self.model)
        self.math_tool = Tool(
            name ='Calculator',
            func = self.llm_math.run,
            description ='Useful for when you need to answer questions about math.'
        )
        self.agent_executor = create_react_agent(self.model, [self.math_tool])

    def run(self, query: str):
        response = self.agent_executor.invoke(
            {"messages": [
                SystemMessage(content="You are a calculator that can solve math problems, please answer user's question and give the answer directly."),
                HumanMessage(content=query)
            ]}
        )
        return response["messages"][-1].content
    
if __name__ == "__main__":
    calc = Calculator()
    print(calc.run("What is the result of 794 multiply by 354?"))
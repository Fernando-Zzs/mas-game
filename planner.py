from prompts import PLANNER_PROMPT
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

class Planner:
    def __init__(self):
        self.model = ChatOpenAI(model="gpt-4o")
        self.prompt = PromptTemplate(
            input_variables=["character", "location", "hp", "hunger", "thirst", "balance", "task"],
            template=PLANNER_PROMPT
        )

    def plan(self, character, location, hp, hunger, thirst, balance, task):
        filled_prompt = self.prompt.format(
            character=character,
            location=location,
            hp=hp,
            hunger=hunger,
            thirst=thirst,
            balance=balance,
            task=task
        )
        return self.model.invoke(filled_prompt)

if __name__ == "__main__":
    planner = Planner()
    result = planner.plan("John", "the park", 10, 15, 10, 100, "Go to a restaurant and then go home")
    print(result)
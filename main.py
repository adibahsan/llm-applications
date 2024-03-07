from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()


def generate_pet_names():
    llm = OpenAI()

    name = llm("I want to generate a pet name for my cat. Suggest Me three cool names.")
    return name


if __name__ == "__main__":
    print("Hello World")
    print(generate_pet_names())

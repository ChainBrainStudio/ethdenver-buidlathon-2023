
import importlib
from backend.services.openAI.prompts import PROTOCOL_TO_PROMPTS


PRE_PROMPT = """
You are an AI that helps write GraphQL queries on the Graph Protocol.
In the coming prompts I'll feed you questions that you need to turn into graphQL queries that work.
Note that it's important that if you don't have some specific data (like dates or IDs), just add placeholders.
Show only code and do not use sentences.
{}"""

SAMPLE_QUERIES_PRE_PROMPT = """
Here are a list of example queries based on various graphQL schemas.
{}"""



class GraphPromptFactory:
    def __init__(self, protocol):
        self.protocol = protocol

    def build_prompt_for_subgraph(self, input):
        examples = PROTOCOL_TO_PROMPTS[self.protocol]

        prompt_string = ", ".join([prompt.to_str() for prompt in examples])
        print("======= PROMPT STRING ========")
        print(prompt_string)
        return self._generate_prompt(input, prompt_string)

    def _generate_prompt(self, input, examples):
        """
        Take in query from user and prepend sample queries
        """

        return (
            examples
            + PRE_PROMPT.format(input)
        )

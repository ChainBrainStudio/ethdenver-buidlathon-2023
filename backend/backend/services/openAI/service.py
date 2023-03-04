import openai

from backend.config import OPENAI_API_KEY
from backend.services.graph.graphql_examples import LIST_OF_EXAMPLES


def generate_prompt(input):
    """
    Take in query from user and prepend sample queries
    """
    sample_queries = LIST_OF_EXAMPLES
    return (
        sample_queries
        + f"""
Query: Using the above queries, Write a GraphQL query to find: {input}
Results:"""
    )


class OpenAIService:
    def __init__(self, use_prompt=0):
        openai.api_key = OPENAI_API_KEY

    def request_gql_for_graph(self, input_query, subgraph, generic=False):
        prompt = input_query if generic else generate_prompt(input_query)
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(input_query),
            temperature=0.6,
            max_tokens=2048,
        )
        openai_result = response.choices[0].text
        print("==========openai response:==========\n", openai_result)
        # strip any unnecessary text prepended and/or postpended to the gql query
        openai_result = openai_result[
            openai_result.find("{") : openai_result.rfind("}") + 1
        ]
        print("==========openai response (formatted):==========\n", openai_result)
        return openai_result
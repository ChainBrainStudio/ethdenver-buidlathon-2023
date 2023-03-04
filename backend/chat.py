CHAT = """
what was the result for proposal 86?
"""

from backend.services.openAI.service import OpenAIService

ai = OpenAIService()
ai.request_gql_for_graph_llama(CHAT, subgraph="uniswap-governance", generic=True)

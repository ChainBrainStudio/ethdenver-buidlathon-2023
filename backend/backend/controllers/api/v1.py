import openai


from backend.services.openAI.service import OpenAIService
from backend.services.graph.service import GraphService
from backend.services.dashboard.service import DashboardService
from backend.models.dashboard import DashboardQueryResult


def QUERY_API_RESPONSE_FORMATTER(id, chatgpt_gql, output):
    return {
        "id": id,
        "chatgpt_gql": chatgpt_gql,
        "output": output
    }


class APIV1Controller:

    def handle_query_for_dashboard(self, input_sentence, subgraph, wallet_address):
        """Get data for query

        Parameters:
        ----------
        input_sentence : _type_
        """
        ai_service = OpenAIService()
        gql = ai_service.request_gql_for_graph_llama(input_sentence, subgraph)
        graph_service = GraphService(protocol=subgraph)
        try:
            result = graph_service.query_thegraph(gql)
        except:
            import pdb;pdb.set_trace()
            return QUERY_API_RESPONSE_FORMATTER("-1", gql, [])


        dashboard_query_result = DashboardQueryResult(user_input=input_sentence,
                                                      subgraph=subgraph,
                                                      chatgpt_gql=str(gql),
                                                      output=result,
                                                      gql_valid=-1,
                                                      user_id=wallet_address
                                                      )

        DashboardService().save_dashboard_query_result(dashboard_query_result)
        return QUERY_API_RESPONSE_FORMATTER(dashboard_query_result.id, gql, result)

    def get_dashboard(self, dashboard_id):
        return DashboardQueryResult.query.get(dashboard_id).to_dict()

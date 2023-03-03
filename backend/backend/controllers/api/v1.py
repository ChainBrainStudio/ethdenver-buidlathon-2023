import openai


from backend.services.openAI.service import OpenAIService
from backend.services.graph.service import GraphService
from backend.services.dashboard.service import DashboardService
from backend.models.dashboard import DashboardQueryResult


class APIV1Controller:

    def handle_query_for_dashboard(self, input_sentence, subgraph):
        """Get data for query

        Parameters
        ----------
        input_sentence : _type_
        """
        ai_service = OpenAIService()
        gql = ai_service.request_gql_for_graph(input_sentence, subgraph)
        graph_service = GraphService(protocol=subgraph)
        result = graph_service.query_thegraph(gql)

        dashboard_query_result = DashboardQueryResult(user_input=input_sentence,
                                                      subgraph=subgraph,
                                                      chatgpt_gql=str(gql),
                                                      output=result,
                                                      gql_valid=-1,
                                                      user_id=-1
                                                      )

        DashboardService().save_dashboard_query_result(dashboard_query_result)
        return result

    def get_dashboard(self, dashboard_id):
        return DashboardQueryResult.query.get(dashboard_id).to_dict()

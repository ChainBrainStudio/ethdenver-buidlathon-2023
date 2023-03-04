from backend.services.openAI.graph_prompt import GraphPromptBase as Prompt


EXAMPLES = [

Prompt(
q="What is the aave proposal with the most votes?",
o="""query MostVotedProposal {
  proposals(orderBy: totalWeightedVotes, orderDirection: desc, first: 1 ) {
    id
    totalWeightedVotes
  }
}"""),
Prompt(
q="Count the votes for and against the last 10 aave proposals",
o="""query {
  proposals(orderBy: creationTime, orderDirection: desc, first: 10) {
    forWeightedVotes
    againstWeightedVotes
  }
}"""),


]

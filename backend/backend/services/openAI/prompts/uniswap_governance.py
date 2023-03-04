from backend.services.openAI.graph_prompt import GraphPromptBase as Prompt


EXAMPLES = [

Prompt(
q="Who are the top delegates by voting power?",
o="""query{
  votes(orderBy: voter__tokenHoldersRepresentedAmount, orderDirection: desc) {
    voter {
      tokenHoldersRepresentedAmount
      id
    }}}
    """),
Prompt(
q="What is the total number of proposals, number of proposals queued for execution, number of proposals executed, and number of proposals canceled for a governance with the ID 11?",
o="""query {
  proposal(id: "11") {
    description
    state
    quorumVotes
    tokenHoldersAtStart
    delegatesAtStart
    againstDelegateVotes
    forDelegateVotes
    abstainDelegateVotes
    totalDelegateVotes
    againstWeightedVotes
    forWeightedVotes
    abstainWeightedVotes
    totalWeightedVotes
    governanceFramework {
      id
      name
      type
      version
    }
  }
}
"""),
Prompt(
q="How many votes did proposal 11 have?",
o="""query{
  proposals(where: {id: "11"}) {
    abstainWeightedVotes
    againstWeightedVotes
    forWeightedVotes
  }
}"""),
Prompt(
q="Query: What was the voting timeline for for, against, and abstain votes for proposal 11?",
o="""query {
  voteDailySnapshots(
    where: {proposal_: {id: "11"}
    }
    orderBy: timestamp
    orderDirection: desc
  ) {
    blockNumber
    abstainWeightedVotes
    againstWeightedVotes
    forWeightedVotes
    timestamp
    proposal {
      id
    }
  }
}"""),
Prompt(
q="Count the votes for and against the last 10 proposals",
o="""query {
  proposals(orderBy: creationTime, orderDirection: desc, first: 10) {
    forWeightedVotes
    againstWeightedVotes
  }
}""")
]

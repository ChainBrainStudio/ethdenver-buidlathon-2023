from backend.services.openAI.graph_prompt import GraphPromptBase as Prompt


EXAMPLES = [
    Prompt(
        q="What were the results for proposal 86?",
        o="""{
          proposals(where: {id: "86"}) {
            abstainWeightedVotes
            againstWeightedVotes
            forWeightedVotes
          }
        }""",
    ),
    Prompt(
        q="How many votes did proposal 86 have?",
        o="""{
          proposals(where: {id: "86"}) {
            totalWeightedVotes
          }
        }""",
    ),
    Prompt(
        q="Query: What was the voting timeline for for, against, and abstain votes for proposal 86?",
        o="""{
          voteDailySnapshots(
            where: {proposal_: {id: "86"}
            }
            orderBy: timestamp
            orderDirection: desc
          ) {
            abstainWeightedVotes
            againstWeightedVotes
            forWeightedVotes
            timestamp
          }
        }""",
    ),
    Prompt(
        q="Summarize proposal with ID = 86?",
        o="""{
          proposal(id: "86") {
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
        }""",
    ),
    Prompt(
        q="Who are the top delegates by voting power?",
        o="""{
          votes(orderBy: voter__tokenHoldersRepresentedAmount, orderDirection: desc) {
            voter {
              tokenHoldersRepresentedAmount
              id
            }
          }
        }""",
    ),
    Prompt(
        q="What proposal has the most votes?",
        o="""{
          proposals(orderBy: totalWeightedVotes, orderDirection: desc, first: 1) {
            id
            totalWeightedVotes
          }
        }""",
    ),
]

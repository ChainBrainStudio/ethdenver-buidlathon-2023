from backend.services.openAI.graph_prompt import GraphPromptBase as Prompt


EXAMPLES = [
    Prompt(
        q="Show me 0x8a7ff4d8573fe8549f8d4aff392273ece9f5f6be's position",
        o="""{
            userPosition(id:"0x8a7ff4d8573fe8549f8d4aff392273ece9f5f6be") {
                id
                totalDeposited
                totalAllotments
                purchases {
                    id
                }
            }
        }""",
    ),
    Prompt(
        q="Show me the wallet addresses of the top 5 depositors",
        o="""{
            userPositions(first: 5, orderBy: totalDeposited, orderDirection: desc) {
                id
            }
        }""",
    )
]

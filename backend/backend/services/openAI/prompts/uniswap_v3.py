from backend.services.openAI.graph_prompt import GraphPromptBase as Prompt


EXAMPLES = [

Prompt(
q="How much trading volume was there on June 1, 2022?",
o="""query {
  uniswapDayDatas(where: { date: 1654041600 }) {
    volumeUSD
   }
  }"""),
Prompt(
q="How much trading volume was there on June 1, 2022?",
o="""query {
  start: factory(
    id: "0x1F98431c8aD98523631AE4a59f267346ea31F984"
    block: { number: 14881677 }
  ) {
    totalVolumeUSD
  }
  end: factory(
    id: "0x1F98431c8aD98523631AE4a59f267346ea31F984"
    block: { number: 14887796 }
  ) {
    totalVolumeUSD
  }
}"""),


]

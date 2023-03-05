<div align="center">
  <h1 align="center">ChatWithTheGraph</h1>
  <img src="images/chainbrainlogo.jpg" height="200">
  <h2 align="center">A solution to view NFTs across protocols with comprehensive subgraphs by training ChatGPT</h2>
  <h2 align="center">Our submission for the ETH Denver Hackathon 2023</h2>
</div>

## About

ChainBrain is an open-source data visualization tool that allows users to search and generate dashboards for any on-chain data question. With ChainBrain, users can quickly identify patterns, track trends, and discover new insights to help them optimize their strategy and operations. We are using ChatGPT to turn the users' questions into a GraphQL query that we send to various subgraphs by the Graph Protocol. We then pull in the user-requested data and display the results on the frontend. Users can connect with their crypto wallet to sign-in and save visualizations to their personal dashboards.

## Subgraphs We Used: 

**New Subgraphs:** We indexed our own new, subgraph for the SporkDAO Token contract: https://thegraph.com/hosted-service/subgraph/marissaposner/sporkdao-token

Here is the link to the github repo: https://github.com/marissaposner/sporkdao-token-subgraph

**Existing Subgraphs:** As far as existing subgraphs, we created a submodule in our github repo to automatically update with the Messari Subgraphs (https://github.com/messari/subgraphs). We chose these subgraphs because they have a more standardized schema than other subgraphs and were easier to build an abstraction layer on top of them. 

Some of the subgraphs in our demo include AAVE-Governance, Uniswap-V3, Uniswap-governance, Compound-governance, and OpenSea. 

We fed each subgraph's schema and a list of example queries for each schema into ChatGPT to provide it with context for that specific subgraph and its mappings. 

Example graph queries for each subgraph are defined here: https://github.com/ChainBrainStudio/ethdenver-buidlathon-2023/tree/main/backend/backend/services/openAI/prompts

Youtube Link to Demo: https://www.youtube.com/watch?v=DmnDch1C8EA

Link to our Notion page: https://www.notion.so/ETH-Denver-2023-Hackathon-Project-40b594f5274e49148fbf9b5cae9cc213

## Getting Started

This is split between 2 services, a frontend and a backend

# Running the backend
- Install Python version management tool: [pyenv](https://github.com/pyenv/pyenv) or [asdf](https://github.com/asdf-vm/asdf)
- Install `Python 3.9.14` using the Python version management tool and activate that version
- Setup the backend, ensure you have python 3.9 or great installed
- `git submodule update --init --recursive` to clone (or update) the `subgraphs` repo in `backend/`
- `cd backend` and run the following steps:
  - run `pip install -r requirements.txt` (Install app requirements)
  - run `pip install -e .` (Install the 'backend' package)
  - Setup .env by copying .env.example to .env and seed with correct data
  - Setup the database with `flask db upgrade`
  - Start the backend app with `flask run`
- Visit http://localhost:5000

## Database Debugging
### Database issues "sqlalchemy.exc.StatementError: (builtins.ValueError) Value"
Try deleting your `backend/instance` folder, then `flask db upgrade` to bring a new database up to
the latest app schema.


# Running the frontend

- For the frontend:`cd frontend` and then run `npm install` (note if you run into any issues you can run `npm install --force`)

### Prerequisites

## Roadmap

See the [open issues](https://github.com/marissaposner/graph-hackathon-2023/issues) for
a list of proposed features (and known issues).

## Project assistance

If you want to say **thank you** or/and support active development:

- Add a [GitHub Star](https://github.com/marissaposner/graph-hackathon-2023) to the
  project.
- Write interesting articles about the project on [Dev.to](https://dev.to/),
  [Medium](https://medium.com/) or your personal blog.

Together, we can make ChainBrain **better**!

## Contributing

First off, thanks for taking the time to contribute! Contributions are what make
the open-source community such an amazing place to learn, inspire, and create.
Any contributions you make will benefit everybody else and are **greatly
appreciated**.

Please read [our contribution guidelines](docs/CONTRIBUTING.md), and thank you
for being involved!

## Authors & contributors

For a full list of all authors and contributors, see
[the contributors page](https://github.com/gosuto-inzasheru/ethdenver-buidlathon-2023/graphs/contributors).

## Security

ChainBrain follows good practices of security, but 100% security cannot be assured.
ChainBrain is provided **"as is"** without any **warranty**. Use at your own risk.

_For more information and to report security issues, please refer to our
[security documentation](docs/SECURITY.md)._

## License

This project is licensed under the **MIT license**.

See [LICENSE](LICENSE) for more information.

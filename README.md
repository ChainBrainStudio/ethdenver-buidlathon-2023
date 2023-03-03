<div align="center">
  <h1 align="center">ChatWithTheGraph</h1>
  <h2 align="center">A solution to view NFTs across protocols with comprehensive subgraphs by training ChatGPT</h2>
  <h2 align="center">Our submission for the Graph Hackathon at CU Boulder February 2023</h2>

  <br />
</div>

<div align="center">
<br />

[![GitHub Workflow Status](https://github.com/keep-starknet-strange/garaga/actions/workflows/test.yml/badge.svg)](https://github.com/keep-starknet-strange/garaga/actions/workflows/test.yml)
[![Project license](https://img.shields.io/github/license/keep-starknet-strange/garaga.svg?style=flat-square)](LICENSE)
[![Pull Requests welcome](https://img.shields.io/badge/PRs-welcome-ff69b4.svg?style=flat-square)](https://github.com/keep-starknet-strange/garaga/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22)

</div>

## About

ChatWithTheGraph is an open-source project built for The Graph Protocol ecosystem that allows users to ask ChatGPT to visualize their data and then our frontend displays the results.

We queried the Messart NFT Marketplace subgraphs defined in this schema: https://github.com/messari/subgraphs/blob/master/schema-nft-marketplace.graphql
Such as:
https://thegraph.com/explorer/subgraphs/AwoxEZbiWLvv6e3QdvdMZw4WDURdGbvPfHmZRc8Dpfz9?view=Playground&chain=mainnet

https://thegraph.com/explorer/subgraphs/GvgkY82DTAkYqRShBbPQMjF1WJyUcknXre3QPWiXrPnS?view=Playground&chain=mainnet

Example graph queries are defined here: https://github.com/marissaposner/graph-hackathon-2023/blob/main/graphql_examples.py

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

Together, we can make ChatWithTheGraph **better**!

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

ChatWithTheGraph follows good practices of security, but 100% security cannot be assured.
ChatWithTheGraph is provided **"as is"** without any **warranty**. Use at your own risk.

_For more information and to report security issues, please refer to our
[security documentation](docs/SECURITY.md)._

## License

This project is licensed under the **MIT license**.

See [LICENSE](LICENSE) for more information.

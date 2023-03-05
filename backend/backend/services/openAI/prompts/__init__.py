from .governor_alpha_bravo import EXAMPLES as governor_alpha_bravo_examples
from .opensea import EXAMPLES as opensea_examples
from .sporkdao_token import EXAMPLES as sporkdao_token_examples
from .uniswap_v3 import EXAMPLES as uniswap_v3_examples

PROTOCOL_TO_PROMPTS = {
    "aave-governance": governor_alpha_bravo_examples,
    "compound-governance": governor_alpha_bravo_examples,
    "uniswap-governance": governor_alpha_bravo_examples,
    "opensea-v2": opensea_examples,
    "uniswap-v3": uniswap_v3_examples,
    "sporkdao-token": sporkdao_token_examples,
}

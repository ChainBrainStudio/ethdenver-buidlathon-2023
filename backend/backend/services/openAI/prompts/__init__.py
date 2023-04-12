from .aave_governance import EXAMPLES as aave_governance_examples
from .opensea import EXAMPLES as opensea_examples
from .sporkdao_token import EXAMPLES as sporkdao_token_examples
from .uniswap_v3 import EXAMPLES as uniswap_v3_examples
from .compound_governance import EXAMPLES as compound_governance_examples
from .uniswap_governance import EXAMPLES as uniswap_governance_examples
from .savvy_lge import EXAMPLES as savvy_lge_examples


PROTOCOL_TO_PROMPTS = {
    "aave-governance": aave_governance_examples,
    "opensea-v2": opensea_examples,
    "uniswap-v3": uniswap_v3_examples,
    "sporkdao-token": sporkdao_token_examples,
    "compound-governance": compound_governance_examples,
    "uniswap-governance": uniswap_governance_examples,
    "savvy-lge": savvy_lge_examples,
}

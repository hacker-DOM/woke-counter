from woke_tests.common import *

from pytypes.contracts.Counter import Counter

class Init(FuzzTest):
    chain: Chain
    paccs: Tuple[Account, ...]
    users: Tuple[Account, ...]
    state: State # pyright: ignore [reportUninitializedInstanceVariable]

    # put your contracts here
    # tokens: List[ERC20]
    counter: Counter

    def __init__(s):
        # ===== Initialize accounts =====
        super().__init__()
        s.chain = default_chain
        s.paccs = tuple(s.chain.accounts[i] for i in range(NUM_PACCS))
        s.users = s.chain.accounts[NUM_PACCS:NUM_PACCS+NUM_USERS]


        # ===== Add labels =====
        for idx, usr in enumerate(s.users):
            usr.label = crypto_names[idx]


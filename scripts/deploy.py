import os

from woke.deployment import *

from pytypes.contracts.Counter import Counter

NODE_URL = os.getenv("ETH_NODE_URL")
if NODE_URL is None:
    raise Exception("ETH_NODE_URL is not set")


@default_chain.connect(NODE_URL)
def main():
    default_chain.set_default_accounts(Account.from_alias("deploy-counter"))
    counter = Counter.deploy()
    print(counter)
    print(counter.number())


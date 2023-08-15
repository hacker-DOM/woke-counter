from .e_flows import *

class Invariants(Flows):
    @invariant()
    def inv_one_equals_one(s):
        assert 1 == 1

    @invariant()
    def inv_check_number(s):
        assert s.counter.number() == s.state.number

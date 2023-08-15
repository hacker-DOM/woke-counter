from .d_impl import *

class Flows(Impl):
    @flow()
    def flow_random_int(s):
        # ===== Randomize =====
        x = random_int(0, 10)

        # ===== Implement =====
        s.impl_random_int(x)

    @flow()
    def flow_inc(s):
        s.counter.increment(from_=s.users[0])
        s.state.number += 1

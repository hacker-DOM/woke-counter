from .b_helpers import *

class Hooks(Helpers):
    @override
    def pre_sequence(s):
        s.state = State()
        if os.getenv('ETH_NODE_URL'):
            s.counter = Counter('0xF186C3ce9317F919ba74D5Da669c96986F3038dA')
        else:
            s.counter = Counter.deploy(from_=s.paccs[0])
        # s.state.number += 1


    @override
    def pre_flow(s, flow: Callable[..., None]):
        with open(csv, 'a') as f:
            _ = f.write(f'{s.sequence_num},{s.flow_num},{flow.__name__}\n')

    @override
    def post_sequence(s):
        ...

from .turnstile import Turnstile


class TurnstileWithLog(Turnstile):
    def __init__(self):
        super().__init__()
        self.history = [self.state]

    def on_state_change(self, state):
        assert self.state == state
        if self.history[-1] != state:
            self.history.append(state)

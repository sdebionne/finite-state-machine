import functools
from .exceptions import ConditionNotMet, InvalidStartState


class StateMachine:
    def __init__(self):
        try:
            self.state
        except AttributeError:
            raise ValueError("Need to set a state instance variable")


def transition(source, target, conditions=None):
    if isinstance(source, str):
        source = [source]
    if not isinstance(source, list):
        raise ValueError("Source can be a string or list")
    if not isinstance(target, str):
        raise ValueError("Target needs to be a string")
    if not conditions:
        conditions = []
    if not isinstance(conditions, list):
        raise ValueError("Conditions needs to be a list")

    def transition_decorator(func):
        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            try:
                self, rest = args
            except ValueError:
                self = args[0]

            if self.state not in source:
                raise InvalidStartState

            for condition in conditions:
                if not condition(self):
                    raise ConditionNotMet(condition)

            result = func(*args, **kwargs)
            self.state = target
            return result

        return _wrapper

    return transition_decorator
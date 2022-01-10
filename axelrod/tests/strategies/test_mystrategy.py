import axelrod as axl

from .test_player import TestPlayer

C, D = axl.Action.C, axl.Action.D

class TestMyStrategy(TestPlayer):

    name = "MyStrategy"
    player = axl.mystrategy
    expected_classifier = {
        "memory_depth": 1,
        "stochastic": False,
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def test_strategy(self):
        # First move is random.
        actions = [(C, C), (C, D), (D, C)]
        self.versus_test(
            opponent=axl.Alternator(), expected_actions=actions, seed=1
        )
        actions = [(C, C), (C, D), (D, C)]
        self.versus_test(
            opponent=axl.Alternator(), expected_actions=actions, seed=2
        )
        actions = [(C, C), (C, C), (C, C)]
        self.versus_test(
            opponent=axl.Cooperator(), expected_actions=actions, seed=1
        )
        actions = [(C, D), (D, D), (D, D)]
        self.versus_test(
            opponent=axl.Defector(), expected_actions=actions, seed=2
        )

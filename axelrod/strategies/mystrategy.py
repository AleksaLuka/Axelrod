from axelrod.action import Action
from axelrod.player import Player

C, D = Action.C, Action.D


class MyStrategy(Player):

    """
    A strategy where the player goes back and forth between using
    the normal TitForTat strategy and the Zero Determinant - Generous
    TitForTat strategy.
    """

    name = "MyStrategy"

    classifier = {
        "memory_depth": 1,
        "stochastic": False,
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def strategy(opponent):

        # nice strategy, so start with C
        if len(self.history) == 0:
            return C

        # play TFT
        elif ((len(self.history)/30)%2) == 0:
            return opponent.history[-1]

        # play ZD-GTFT2
        else:
            if (opponent.history[-1] == C and self.history[-1] == C):
                return C

            elif (opponent.history[-1] == D and self.history[-1] == C):
                p = random.random()
                if (p <= 0.125):
                    return C
                else:
                    return D

            elif (opponent.history[-1] == C and self.history[-1] == D):
                return C

            else:
                p = random.random()
                if (p <= 0.25):
                    return C
                else:
                    return D

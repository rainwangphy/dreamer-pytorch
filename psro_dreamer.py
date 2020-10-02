"""
This is going to implement the PSRO with pytorch
we focus on poker games and soccer environments
"""

import numpy as np
import pyspiel

game = pyspiel.load_game("leduc_poker")
state = game.new_initial_state()

while not state.is_terminal():
    legal_actions = state.legal_actions()
    print(state)
    if state.is_chance_node():
        # Sample a chance event outcome.
        outcomes_with_probs = state.chance_outcomes()
        action_list, prob_list = zip(*outcomes_with_probs)
        action = np.random.choice(action_list, p=prob_list)
        state.apply_action(action)
    else:
        # The algorithm can pick an action based on an observation (fully observable
        # games) or an information state (information available for that player)
        # We arbitrarily select the first available action as an example.
        action = legal_actions[0]
        print(action)
        state.apply_action(action)

import pandas as pd
import numpy as np
import analysis.utils as utils

def get_pile(pounds, seed=42):
    """Returns a list of bill denominations comprising `pounds` of US bills """

    # Rough distribution of bills. Totally arbitrary.
    denominations = {
        1: 0.05,
        5: 0.10,
        10: 0.10,
        20: 0.40,
        50: 0.10,
        100: 0.25,
    }

    # Make random deterministic
    np.random.seed(seed)

    # Pull actuall bill counts for pile.
    counts = np.random.multinomial(
        utils.bills_per_pound * pounds,
        list(denominations.values())
    )

    # Turn `counts` into a list of bill denominations
    pile = sum([[x] * y for x, y in zip(denominations.keys(), counts)], [])

    return np.random.permutation(pile)


if __name__ == '__main__':
    (
        pd
        .DataFrame({
            'denomination': get_pile(200),
        })
        .to_csv(utils.pile_path, index=False)
    )

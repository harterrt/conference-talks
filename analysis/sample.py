import pandas as pd
import analysis.utils as utils
import plotnine as pn


def get_estimate(pile, seed):
    sample = pile.sample(utils.bills_per_pound, random_state=seed)
    sample_value = sum(sample['denomination'])

    return(sample_value * 200)


def get_estimate_distribution():
    pile = utils.read_pile()
    return(pd.DataFrame({
        'estimates': [get_estimate(pile, x) for x in range(1000)]
    }))


def plot_estimate_distribution(dist):
    return(pn.ggplot(dist, pn.aes(x='estimates')) + pn.geom_histogram())


if __name__ == '__main__':
    (
        plot_estimate_distribution(get_estimate_distribution())
        .save('slides/static/distribution.png')
    )

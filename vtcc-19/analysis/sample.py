import pandas as pd
import numpy as np
import analysis.utils as utils
import plotnine as pn

pile = utils.read_pile()

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
    return(
        pn.ggplot(dist, pn.aes(x='estimates'))
        + pn.geom_histogram(bins = 25)
        + pn.geom_vline(
            xintercept=sum(pile['denomination']),
            color="#FF5500",
            size=2,
        )
        + pn.geom_vline(
            xintercept=3363400,
            color="#FF5500",
            size=2,
            linetype='dotted',
        )
    )


def plot_dist_with_ci(dist):
    return(
        pn.ggplot(dist, pn.aes(x='estimates'))
        + pn.geom_histogram(bins = 25)
        + pn.geom_vline(
            xintercept=dist.quantile(0.025),
            color="#FF5500",
            size=2,
            linetype='dotted',
        )
        + pn.geom_vline(
           xintercept=dist.quantile(0.975),
            color="#FF5500",
            size=2,
            linetype='dotted',
        )
        +pn.ggtitle("${0:,.0f} ({1:,.0f}, {2:,.0f})".format(
            np.mean(dist.estimates),
            dist.estimates.quantile(0.025),
            dist.estimates.quantile(0.975),
        ))
    )


if __name__ == '__main__':
    print(plot_estimate_distribution(get_estimate_distribution()))
    (
        plot_estimate_distribution(get_estimate_distribution())
        .save('slides/static/distribution.png')
    )
    (
        plot_dist_with_ci(get_estimate_distribution())
        .save('slides/static/confidence_interval.png')
    )

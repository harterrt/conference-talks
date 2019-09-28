import pandas as pd
import numpy as np
import analysis.utils as utils
import plotnine as pn

pile = utils.read_pile()

def get_sample_stat(pile, size, seed):
    sample = pile.sample(size, random_state=seed)
    sample_value = sum(sample['denomination'])

    return(sample_value * len(pile) / size)


def get_sample_dist(pile, size):
    print('Working on {0}'.format(size))
    dist = pd.Series([get_sample_stat(pile, size, x) for x in range(1000)])

    return({
        'size': size,
        'mean': dist.mean(),
        'lower': dist.quantile(0.025),
        'upper': dist.quantile(0.975),
    })


def plot_convergence(pile):
    stops = range(100, int(len(pile) / 10), utils.bills_per_pound)
    dist_stats = pd.DataFrame([get_sample_dist(pile, size) for size in stops])

    return(
        pn.ggplot(dist_stats)
        + pn.geom_line(pn.aes(x='size', y='mean'))
        + pn.geom_line(
            pn.aes(x='size', y='lower'),
            color='#FF5500',
            linetype='dotted'
        )
        + pn.geom_line(
            pn.aes(x='size', y='upper'),
            color='#FF5500',
            linetype='dotted'
        )
        + pn.scale_x_continuous(breaks=stops)
        + pn.theme(axis_text_x = pn.element_text(angle = 270, hjust = 1))
    )


if __name__ == '__main__':
    (
        plot_convergence(pile)
        .save('slides/static/convergence.png')
    )

import pandas as pd
import analysis.utils as utils
import analysis.sample as sample
import plotnine as pn

def resample(sample, seed):
    resample = sample.sample(frac=1.0, replace=True, random_state=seed)
    estimate = sum(resample['denomination']) * 200

    return(estimate)



def get_resample_distribution(sample):
    return(pd.DataFrame({
        'estimates': [resample(sample, x) for x in range(1000)]
    }))

def get_bs_sim():
    pile = utils.read_pile()
    samp = pile.sample(utils.bills_per_pound, random_state=42)

    dist = get_resample_distribution(samp)
    plot = sample.plot_estimate_distribution(dist)

    return(pile)


def join_distributions():
    resampled = get_resample_distribution()
    resampled['type'] = 'bootstrapped'

    sampled = sample.get_estimate_distribution()
    sampled['type'] = 'sampled'

    return(pd.unionAll(resampled, sampled))


if __name__ == '__main__':
    pile = utils.read_pile()
    samp = pile.sample(utils.bills_per_pound, random_state=42)
    dist = get_resample_distribution(samp)

    (
        sample.plot_estimate_distribution(dist)
        .save('slides/static/bootstrap.png')
    )
    (
        sample.plot_dist_with_ci(dist)
        .save('slides/static/bootstrap_ci.png')
    )


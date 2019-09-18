import pandas as pd
import analysis.utils as utils
import analysis.sample as sample
import plotnine as pn

def resample(sample, seed):
    resample = sample.sample(frac=1.0, replace=True, random_state=seed)
    estimate = sum(resample['denomination']) * 200

    return(estimate)


def get_resample_distribution():
    sample = utils.read_pile().sample(utils.bills_per_pound, random_state=42)

    return(pd.DataFrame({
        'estimates': [resample(sample, x) for x in range(1000)]
    }))


if __name__ == '__main__':
    (
        sample.plot_estimate_distribution(get_resample_distribution())
        .save('slides/static/bootstrap.png')
    )


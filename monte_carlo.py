from numpy.random import normal
import numpy as np

import math


def monte_carlo_step(previous, rate, stdv):
    return previous * math.exp(normal(rate, stdv))


def build_monte_carlo_array(previous, rate, stdv, depth, addition=None):
    sim_series = [monte_carlo_step(previous, rate, stdv)]
    if addition:
        for i in range(depth-1):
            sim_series.append(monte_carlo_step(sim_series[i]+addition[i], rate, stdv))
    for i in range(depth):
        sim_series.append(monte_carlo_step(sim_series[i], rate, stdv))
    return np.array([sim_series])


def build_donations_array(start, rate, stdv, depth)

from numpy.random import normal
from numpy import array
import numpy

import math


def monte_carlo_step(previous, rate, stdv):
    return previous * math.exp(normal(rate, stdv))

def build_monte_carlo_array(previous, rate, stdv, depth):
    sim_series = [monte_carlo_step(previous, rate, stdv)]
    for i in range(depth):
        sim_series.append(monte_carlo_step(sim_series[i], rate, stdv))
    return array([sim_series])

import numpy as np

# Flip each bit independently with probability p to find whether it is corrupted.
def bsc(bits, p, rng):
    bits = np.asarray(bits)
    errors = rng.random(bits.shape) < p
    return np.bitwise_xor(bits, errors.astype(int))

#Return number of errors or expected errors in each packet using binomial.
def packet_errors(n_pkt, n_bits, p, rng):
    return rng.binomial(n_bits, p, size=n_pkt)

#Return the number of attempts until first clean packet using geometric.
def attempts_until_clean(n_trials, q, rng):
    return rng.geometric(q, size=n_trials)

#Calculate total variation distance for errors or success by using two probability distributions.
def tv_distance(pmf1, pmf2):
    pmf1 = np.asarray(pmf1)
    pmf2 = np.asarray(pmf2)
    return 0.5 * np.sum(np.abs(pmf1 - pmf2))
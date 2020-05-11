import numpy as np
import math
import cvxopt


def sir_simulation(b, g, t=100, i0=1, pop=6000000):
    # b = beta, g = gamma, t = time steps,
    # I0 = No. of infection on day 1, pop = population,
    # return S, I, R, N and R_e

    # Initialization
    ss = [None] * t
    ii = [None] * t
    rr = [None] * t
    nn = [None] * (t - 1)

    ii[0] = i0
    ss[0] = pop - ii[0]
    rr[0] = 0

    # SIR simulation
    for i in range(t - 1):
        nn[i] = b[i] * ss[i] * ii[i] / pop
        ss[i + 1] = ss[i] - nn[i]
        ii[i + 1] = ii[i] + nn[i] - g[i] * ii[i]
        rr[i + 1] = rr[i] + g[i] * ii[i]

    # N_sir
    inf = [0] * t
    inf[0] = 1
    inf[1:] = nn
    n_sir = np.array(inf)

    # R_sir
    r0_sir = np.array(b) / np.array(g)
    sus_ratio = np.array(ss[:-1]) / pop
    r_sir = sus_ratio * r0_sir

    return np.array(ss), np.array(ii), np.array(rr), n_sir, r_sir


def find_growth(nn, m):

    growth = [None] * (len(nn) - 1)
    growth_m = [None] * (len(nn) - m)

    for i in range(len(growth)):
        growth[i] = nn[i+1]/nn[i]

    for i in range(len(growth_m)):
        growth_m[i] = nn[i+m]/nn[i]

    return np.array(growth), np.array(growth_m)


def find_n(n_cum):
    # calculate N and growth rates c from N_cum

    n = len(n_cum)
    N = [None] * n
    N[0] = n_cum[0]
    c = [None] * (n-1)

    for i in range(n-1):
        N[i+1] = n_cum[i+1] - n_cum[i]

    for i in range(n-1):
        c[i] = n_cum[i+1] / n_cum[i]

    return np.array(N), np.array(c)


def find_n_cum(nn):
    # calculate N_cum and growth rates c from N

    t = len(nn)

    # cumulative infected
    n_cum = [None] * t
    for i in range(t):
        n_cum[i] = np.sum(nn[0:(i + 1)])

    # growth rate
    c = [0] * (t-1)
    for i in range(t - 1):
        c[i] = n_cum[i + 1] / n_cum[i]

    return np.array(n_cum), np.array(c)


def deaths_sir(rr, dr0, pp, iso_to_death_max, iso_to_death_min):
    # find deaths(t) from SIR simulation

    dr = [None] * len(rr)
    dr[0] = 0
    for i in range(len(rr) - 1):
        dr[i + 1] = rr[i + 1] - rr[i]

    dd = [0] * (len(dr) + iso_to_death_max - 1)

    for i in range(len(dr)):
        dd[(i + iso_to_death_min):(i + iso_to_death_max)] = \
            dd[(i + iso_to_death_min):(i + iso_to_death_max)] \
            + pp * dr[i] * dr0

    return np.array(dd)


def find_pq_S(deaths, p, N_max, dr):
    # deaths = death data starting from >10,
    # p = the probabilities of dying in each possible day after infected
    # N_max = last estimation for N
    # (depends on the distribution of death delay)
    # dr(t) = death rate on day t, t = 1,...,N_max
    # return P and q to be used in QP solver, and M to calculate errors

    t_death = len(deaths)

    p_mat = np.zeros((t_death, N_max))
    dr_mat = np.zeros((t_death, N_max))
    for i in np.arange(t_death):
        p_mat[i, i:(i + len(p))] = p[::-1]
        dr_mat[i, :] = dr
    M = p_mat * dr_mat

    weight_mat = np.zeros((len(deaths), len(deaths)))
    for i in range(len(deaths)):
        weight_mat[i, i] = 1 / deaths[i]
    M1 = np.dot(weight_mat, M)
    deaths1 = np.dot(weight_mat, deaths)

    S_mat = np.zeros((N_max, N_max))
    S_mat[0, 0] = 1
    for i in range(N_max - 1):
        S_mat[i + 1, i:i + 2] = -1, 1
    M2 = np.dot(M1, S_mat)

    P = np.dot(M2.transpose(), M2)
    q = -np.dot(M2.transpose(), np.array(deaths1))

    return M, P, q


def find_gh_S(N_max, S_ini, max_growth, min_growth, pol_dates,
              c_max_val, c_min_val, m, max_growth_m, min_growth_m):
    # S_ini = maximum of S(1),
    # c_min(t) < exponential growth rate(t) < c_max(t)
    # min_growth < N_n+1/N_n < max_growth
    # return G and h, the constraints in QP

    c_max = np.full(N_max - 1, None, dtype='float64')
    c_min = np.full(N_max - 1, None, dtype='float64')
    for i in range(len(pol_dates) - 1):
        c_max[pol_dates[i]:pol_dates[i + 1]] = c_max_val[i]
        c_min[pol_dates[i]:pol_dates[i + 1]] = c_min_val[i]

    G0 = np.zeros(N_max)
    G0[0] = 1

    G1 = np.zeros((N_max - 1, N_max))
    G2 = np.zeros((N_max - 1, N_max))

    for i in np.arange(N_max - 1):
        G1[i, i], G1[i, i + 1] = min_growth + 1, -1
        G2[i, i], G2[i, i + 1] = -max_growth - 1, 1

    for i in np.arange(N_max - 2):
        G1[i + 1, i] = -min_growth
        G2[i + 1, i] = max_growth

    G3 = np.zeros((N_max - 1, N_max))
    G4 = np.zeros((N_max - 1, N_max))

    for i in range(N_max - 1):
        G3[i, i:i + 2] = c_min[i], -1
        G4[i, i:i + 2] = -c_max[i], 1

    G5 = np.zeros((N_max - m, N_max))
    G6 = np.zeros((N_max - m, N_max))

    for i in np.arange(N_max - m):
        G5[i, i], G5[i, i + m - 1], G5[i, i + m] = min_growth_m, 1, -1
        G6[i, i], G6[i, i + m - 1], G6[i, i + m] = -max_growth_m, - 1, 1

    for i in np.arange(N_max - m - 1):
        G5[i + 1, i] = -min_growth_m
        G6[i + 1, i] = max_growth_m

    G = np.vstack((G0, G1, G2, G3, G4, G5, G6))
    h = np.zeros(G.shape[0])
    h[0] = S_ini

    return c_max, c_min, G, h


def cvxopt_solve_qp(P, q, G=None, h=None, A=None, b=None):
    # prepare matrices to be used in cvxopt
    # this is the QP solver

    P = .5 * (P + P.T)  # make sure P is symmetric
    args = [cvxopt.matrix(P), cvxopt.matrix(q)]

    if G is not None:
        args.extend([cvxopt.matrix(G), cvxopt.matrix(h)])
        if A is not None:
            args.extend([cvxopt.matrix(A), cvxopt.matrix(b)])
    sol = cvxopt.solvers.qp(*args)

    if 'optimal' not in sol['status']:
        return None

    return np.array(sol['x']).reshape((P.shape[1],))


def find_r(N, p_iso_delay):
    n = len(N)
    max_iso_delay = len(p_iso_delay)
    I0 = np.full((n - 1, n - 1), 0.)

    for i in range(n - 1):
        iso_delay = N[i] * p_iso_delay
        for j in range(max_iso_delay):
            I0[j, i] = N[i] - np.sum(iso_delay[:j + 1])

    I_cul_inf = np.full((n - 1, n - 1), 0.)

    for i in range(n - 1):
        I_cul_inf[i:n, i] = I0[:n - i - 1, i]

    I_row_sum = np.sum(I_cul_inf, 1)
    I_weight = np.full((n - 1, n - 1), None, dtype='float64')

    for i in range(n - 1):
        I_weight[i] = I_cul_inf[i] / I_row_sum[i]

    R0 = np.dot(N[1:, ], I_weight) / N[:-1]

    return I_cul_inf, R0


def smooth(n, smooth_scale):

    deaths_smooth = np.zeros(len(n) - smooth_scale + 1)

    for i in range(len(deaths_smooth)):
        deaths_smooth[i] = np.mean(n[i:i + smooth_scale])

    return deaths_smooth

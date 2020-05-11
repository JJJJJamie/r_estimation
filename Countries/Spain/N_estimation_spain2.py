# death delay probabilities
shape1 = (1/0.86)**2
scale1 = 5.1/shape1
shape2 = (1/0.45)**2
scale2 = 12.8/shape2

death_delay = np.random.gamma(shape1, scale1, 10000000) + \
              np.random.gamma(shape2, scale2, 10000000)
death_delay_min = math.floor(np.quantile(death_delay, 0.01))
death_delay_max = math.ceil(np.quantile(death_delay, 0.95))

p = np.histogram(death_delay,
                 bins=np.arange(death_delay_min, death_delay_max+1),
                 density=True)[0]

# deaths
deaths = deaths_spain

# N_max
N_max = len(deaths)+(death_delay_max-1)-death_delay_min

# corresponding starting index of N_sir
NN_start = deaths_start - dt.timedelta(days=death_delay_max-1)

# death rates
dr = np.repeat(0.03, N_max)

# restriction matrix G & h
S_ini = 100  # max N_1
max_growth = 1.6  # max N_n+1/N_n
min_growth = 1/max_growth  # min N_n+1/N_n
m = 2
max_growth_m = 2
min_growth_m = 0.8

pol_dates = [0,
             20,
             40,
             60,
             80,
             N_max-1]  # policy dates
c_max_val = [1.7, max_growth, max_growth, max_growth, max_growth]  # max grow rates
c_min_val = [1.3, 1, 1.0, 1.0, 1.0]  # min grow rates
# c_max_val = [1.7, 1.41, 1.41, 1.41, 1.41]  # max grow rates
# c_min_val = [1.1, 1.1, 1.0, 1.0, 1.0]  # min grow rates

#############################################################################
# N estimation
# solve QP
M, P, q = find_pq_S(deaths, p, N_max, dr)
c_max, c_min, G, h = find_gh_S(N_max, S_ini, max_growth, min_growth,
                               pol_dates, c_max_val, c_min_val,
                               m, max_growth_m, min_growth_m)
S0 = cvxopt_solve_qp(P, q, G, h)
smooth_S0 = 15
S0 = smooth(S0, smooth_S0)
N00, c = find_n(S0)
NN_start = NN_start + dt.timedelta(days=(smooth_S0-1)/2)
# cut off last (death_delay_max-death_delay_min-1) estimations
cut_off_1 = death_delay_max-death_delay_min-1

S1 = S0[:-cut_off_1+20]
N11 = N00[:-cut_off_1+20]

S2 = S0[:-cut_off_1+14]
N22 = N00[:-cut_off_1+14]

S3 = S0[:-cut_off_1+7]
N33 = N00[:-cut_off_1+7]

S4 = S0[:-cut_off_1]
N44 = N00[:-cut_off_1]

# test results
# plt.plot(S0)
#
# plt.plot(np.log(S0))
#
# plt.plot(N00)
#
# plt.plot(c)
# plt.plot(c_max[:len(c)])
# plt.plot(c_min[:len(c)])
#
# plt.plot(np.dot(M, N00))
# plt.plot(deaths)

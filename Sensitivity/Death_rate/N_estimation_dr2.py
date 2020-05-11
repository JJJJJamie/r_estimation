# death delay probabilities
shape1 = (1/0.86)**2
scale1 = 5.1/shape1
shape2 = (1/0.45)**2
scale2 = 18.8/shape2

death_delay = np.random.gamma(shape1, scale1, 10000000) + \
              np.random.gamma(shape2, scale2, 10000000)
death_delay_min = math.floor(np.quantile(death_delay, 0.01))
death_delay_max = math.ceil(np.quantile(death_delay, 0.95))

p = np.histogram(death_delay,
                 bins=np.arange(death_delay_min, death_delay_max+1),
                 density=True)[0]

# N_max
N_max = len(deaths)+(death_delay_max-1)-death_delay_min

# corresponding starting index of N_sir
N_start = ind_min-death_delay_max+1

# death rates
dr2 = np.repeat(0.1, N_max)

# restriction matrix G & h
S_ini = 100  # max N_1
max_growth = 1.5  # max N_n+1/N_n
min_growth = 1/1.5  # min N_n+1/N_n
m = 2
max_growth_m = 2
min_growth_m = 0.5

pol_dates = [0,
             pol_list[0]-N_start+1,
             pol_list[1]-N_start+1,
             pol_list[2]-N_start+1,
             pol_list[3]-N_start+1,
             N_max-1]  # policy dates

c_max_val = [1.7, 1.41, 1.41, 1.41, 1.41]  # max grow rates
c_min_val = [1.1, 1.1, 1.0, 1.0, 1.0]  # min grow rates
# c_max_val = [1.7, 1.31, 1.31, 1.31, 1.31]  # max grow rates
# c_min_val = [1.25, 1.25, 1.0, 1.0, 1.0]  # min grow rates

#############################################################################
# N estimation
# solve QP
M_dr2, P, q = find_pq_S(deaths, p, N_max, dr2)
c_max, c_min, G, h = find_gh_S(N_max, S_ini, max_growth, min_growth,
                               pol_dates, c_max_val, c_min_val,
                               m, max_growth_m, min_growth_m)
S0 = cvxopt_solve_qp(P, q, G, h)
N0_dr2, c = find_n(S0)

S_dr2 = S0+0.
N_dr2 = N0_dr2+0.
c = c+0.
N_range = np.arange(N_start, N_start+len(N))

# cut off last (death_delay_max-death_delay_min-1) estimations
# S_dr2 = S0[:-(death_delay_max-death_delay_min-1)]
# N_dr2 = N0_dr2[:-(death_delay_max-death_delay_min-1)]
# c = c[:-(death_delay_max-death_delay_min-1)]
# N_range = np.arange(N_start, N_start+len(N))

# test results
# plt.plot(S0)
# plt.plot(nn_cum[N_start:N_start+len(S0)])
#
# plt.plot(np.log(S0))
# plt.plot(np.log(nn_cum[N_start:N_start+len(S0)]))
#
# plt.plot(N0)
# plt.plot(nn[N_start:N_start+len(S0)], linestyle='dashed', linewidth=4)
#
# plt.plot(c)
# plt.plot(c_max[:len(c)])
# plt.plot(c_min[:len(c)])
# plt.plot(cc[N_start:N_start+len(c)])
#
# plt.plot(np.dot(M_dr2, N0_dr2))
# plt.plot(deaths)

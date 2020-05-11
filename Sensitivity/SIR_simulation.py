#############################################################################
# Parameters
t = 200
shape2 = (1/0.45)**2
scale2 = 18.8/shape2

# gamma(t)
g_value = 1/5.1
g = [g_value] * (t-1)

# beta(t)
b = [None] * (t-1)
R0_list = [2.2, 2.4, 2.5, 1.7, 1.1, 0.75]
# R0_list = [2.3, 1.9, 1.7, 1.75, 1.78, 1.8]
pol_list = [20, 40, 50, 75, t-1]
b_value = np.array(R0_list) * g_value

b[:pol_list[0]] = np.linspace(b_value[0], b_value[1], len(b[:pol_list[0]]))
for i in range(len(pol_list)-1):
    b[pol_list[i] - 1:pol_list[i+1]] = np.linspace(
        b_value[i+1], b_value[i+2], len(b[pol_list[i] - 1:pol_list[i+1]]))

# iso to death probabilities
iso_to_death = np.random.gamma(shape2, scale2, 10000000)
iso_to_death_max = math.ceil(np.quantile(iso_to_death, 0.95))
iso_to_death_min = math.floor(np.quantile(iso_to_death, 0.01))

pp = np.histogram(iso_to_death,
                  bins=np.arange(iso_to_death_min, iso_to_death_max+1),
                  density=True)[0]

# death rate
dr0 = 0.03

#############################################################################
# SIR simulation
ss, ii, rr, nn, re = sir_simulation(b, g, t)
nn_cum, cc = find_n_cum(nn)
dd = deaths_sir(rr, dr0, pp, iso_to_death_max, iso_to_death_min)
# deaths >= 10
ind_min = next(x for x, val in enumerate(dd) if val > 10)
# deaths = dd[ind_min:len(dd)-10]
deaths = dd[ind_min:124]
deaths_range = np.arange(ind_min, ind_min+len(deaths))

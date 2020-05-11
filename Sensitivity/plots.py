import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['axes.labelsize'] = 30
mpl.rcParams['xtick.labelsize'] = 30
mpl.rcParams['ytick.labelsize'] = 30
mpl.rcParams['legend.fontsize'] = 30

# SIR plot
ax = [i for i in range(len(ss))]
plt.plot(ax, ss)
plt.plot(ax, ii)
plt.plot(ax, rr)

#################################################################
# baseline plot
# N
fig, ax1 = plt.subplots()

ax1.set_xlabel('number of days after first infection')
ax1.set_ylabel('N: estimated number of newly infected cases')
ax1.plot(nn[:120], linestyle='dashed', linewidth=6,
         label='true N(t) from simulation',)
ax1.plot(N_range, N, linewidth=4,
         label='N(t) est')
ax1.legend(loc='upper left')

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
ax2.set_ylabel('daily deaths', color='black')  # we already handled the x-label with ax1
ax2.plot(deaths_range, deaths, color='black', linestyle=':',
         label='deaths data')
ax2.legend(loc='upper right')

# R
input_sir, = plt.plot(re[:118], linestyle=':', linewidth=4, color='black')
r_sir, = plt.plot(R[:118], linestyle='dashed', linewidth=4)
est, = plt.plot(R0_range, R0)

plt.xlabel('number of days after first infection')
plt.ylabel('R: estimated effective reproduction number')
plt.legend([input_sir, r_sir, est],
           ['true R(t) used in simulation',
            'R(t) est from true N(t) from simulation',
            'R(t) est ({:.2%})'.format(baseline_error)])

#################################################################
# distributions
# N
fig2, ax1 = plt.subplots()

ax1.set_xlabel('number of days after first infection')
ax1.set_ylabel('N: estimated number of newly infected cases')
ax1.plot(nn[:120], linestyle='dashed', linewidth=6,
         label='true N(t) from simulation',)
ax1.plot(N_range, N, linestyle='-.', linewidth=4,
         label='N(t) est, Gamma(mean=18.8,shape=4.94) (true)')
ax1.plot(N1_range, N1,
         label='N(t) est, Gamma(mean=15.8,shape=4.94)')
ax1.plot(N2_range, N2,
         label='N(t) est, Gamma(mean=21.8,shape=4.94)')
ax1.plot(N3_range, N3,
         label='N(t) est, Gamma(mean=18.8,shape=2.78)')
ax1.plot(N4_range, N4,
         label='N(t) est, Gamma(mean=18.8,shape=6.93)')
ax1.plot(N5_range, N5,
         label='N(t) est, Gaussian(mean=18.8,s.d=3)')
ax1.plot(N6_range, N6,
         label='N(t) est, Gaussian(mean=18.8,s.d=6)')
ax1.legend(fontsize=21, loc='upper left')

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
ax2.set_ylabel('daily deaths', color='black')  # we already handled the x-label with ax1
ax2.plot(deaths_range, deaths, color='black', linestyle=':',
         label='deaths data')
ax2.legend(loc='upper right')

# R
input_sir, = plt.plot(re[:range_max], linestyle=':', linewidth=4, color='black')
r_sir, = plt.plot(R[:range_max], linestyle='dashed', linewidth=4)
r, = plt.plot(R0_range, R0, linestyle='-.', linewidth=4,)
r1, = plt.plot(R1_range, R1)
r2, = plt.plot(R2_range, R2)
r3, = plt.plot(R3_range, R3)
r4, = plt.plot(R4_range, R4)
r5, = plt.plot(R5_range, R5)
r6, = plt.plot(R6_range, R6)

plt.xlabel('number of days after first infection')
plt.ylabel('R: estimated reproduction number')
plt.legend(['true R(t) used in simulation',
            'R(t) est from true N(t) from simulation',
            'R(t) est, Gamma(mean=18.8,shape=4.94) ({:.2%})'.format(distribution_error[0]),
            'R(t) est, Gamma(mean=15.8,shape=4.94) ({:.2%})'.format(distribution_error[1]),
            'R(t) est, Gamma(mean=21.8,shape=4.94) ({:.2%})'.format(distribution_error[2]),
            'R(t) est, Gamma(mean=18.8,shape=2.78) ({:.2%})'.format(distribution_error[3]),
            'R(t) est, Gamma(mean=18.8,shape=6.93) ({:.2%})'.format(distribution_error[4]),
            'R(t) est, Gaussian(mean=18.8,s.d=3) ({:.2%})'.format(distribution_error[5]),
            'R(t) est, Gaussian(mean=18.8,s.d=6) ({:.2%})'.format(distribution_error[6])],
           fontsize=23)

#################################################################
# noise
# N
fig3, ax1 = plt.subplots()

ax1.set_xlabel('number of days after first infection')
ax1.set_ylabel('N: estimated number of newly infected cases')
ax1.plot(nn[:120], linestyle='dashed', linewidth=6,
         label='true N(t) from simulation',)
ax1.plot(N_range, N, linestyle='-.', linewidth=4,
         label='N(t) est, no noise')
ax1.plot(N_range, N_noise_5,
         label='N(t) est, 5% noise')
ax1.plot(N_range, N_noise_10,
         label='N(t) est, 10% noise')
ax1.plot(N_range, N_noise_20,
         label='N(t) est, 20% noise')
ax1.legend(loc='upper left')

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
ax2.set_ylabel('daily deaths', color='black')  # we already handled the x-label with ax1
ax2.plot(deaths_range, deaths, color='black', linestyle=':',
         label='deaths data')
ax2.legend(loc='upper right')

# S
nn_cum_noise_plot, = plt.plot(np.log(nn_cum[:N_range_max]), linestyle='dashed', linewidth=6)
S_noise_0_plot, = plt.plot(N_range, np.log(S), linestyle='-.', linewidth=4)
S_noise_5_plot, = plt.plot(N_range, np.log(S_noise_5))
S_noise_10_plot, = plt.plot(N_range, np.log(S_noise_10))
S_noise_20_plot, = plt.plot(N_range, np.log(S_noise_20))

plt.xlabel('number of days after first infection')
plt.ylabel('N_cum: estimated number of cumulative infection')
plt.legend(['true N_cum(t) from simulation',
            'N_cum(t) est, no noise',
            'N_cum(t) est, 5% noise',
            'N_cum(t) est, 10% noise',
            'N_cum(t) est, 20% noise'])

# R
input_sir_noise, = plt.plot(re[:range_max], linestyle=':', linewidth=4, color='black')
r_sir_noise, = plt.plot(R[:range_max], linestyle='dashed', linewidth=4)
r_noise_0, = plt.plot(R_noise_range, R0, linestyle='-.', linewidth=4)
r_noise_5, = plt.plot(R_noise_range, R_noise_5)
r_noise_10, = plt.plot(R_noise_range, R_noise_10)
r_noise_20, = plt.plot(R_noise_range, R_noise_20)

plt.xlabel('number of days after first infection')
plt.ylabel('R: estimated reproduction number')
plt.legend(['true R(t) used in simulation',
            'R(t) est from true N(t) from simulation',
            'R(t) est, no noise, ({:.2%})'.format(noise_error[0]),
            'R(t) est, 5% noise, ({:.2%})'.format(noise_error[1]),
            'R(t) est, 10% noise, ({:.2%})'.format(noise_error[2]),
            'R(t) est, 20% noise, ({:.2%})'.format(noise_error[3])])

#################################################################
# death rate
# N
fig4, ax1 = plt.subplots()

ax1.set_xlabel('number of days after first infection')
ax1.set_ylabel('N: estimated number of newly infected cases (log scale)', fontsize=25)
ax1.plot(np.log(nn[:N_range_max]), linestyle='dashed', linewidth=6,
         label='true N(t) from simulation',)
ax1.plot(N_range, np.log(N), linestyle='-.', linewidth=4,
         label='N(t) est, death rate=3% (True)')
ax1.plot(N_range, np.log(N_dr1),
         label='N(t) est, death rate=0.25%')
ax1.plot(N_range, np.log(N_dr2),
         label='N(t) est, death rate=10%')
ax1.legend(loc='upper left', fontsize=23)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
ax2.set_ylabel('daily deaths', color='black')  # we already handled the x-label with ax1
ax2.plot(deaths_range, deaths, color='black', linestyle=':',
         label='deaths data')
ax2.legend(loc='upper right')

# R
input_sir_dr, = plt.plot(re[:range_max], linestyle=':', linewidth=4, color='black')
r_sir_dr, = plt.plot(R[:range_max], linestyle='dashed', linewidth=4)
r_dr, = plt.plot(R0_range, R0, linestyle='-.', linewidth=4)
r_dr1, = plt.plot(R0_range, R_dr1)
r_dr2, = plt.plot(R0_range, R_dr2)

plt.xlabel('number of days after first infection')
plt.ylabel('R: estimated reproduction number')
plt.legend(['true R(t) used in simulation',
            'R(t) est from true N(t) from simulation',
            'R(t) est, death rate=3%',
            'R(t) est, death rate=0.25%',
            'R(t) est, death rate=10%'])

# import matplotlib as mpl
# mpl.rcParams['lines.linewidth'] = 2
#
# S0_range = np.arange(N_start, N_start + len(S0))
#
# plt.ylim([0., np.max(S0)*1.1])
# plt.plot(S0_range, S0, linewidth=4)
# plt.plot(S0_range, nn_cum[S0_range], linestyle='dashed', linewidth=6)
#
# S0_x = [S0_range[-1]-cut_off_1,
#         S0_range[-1]-cut_off_1+10,
#         S0_range[-1]-cut_off_1+20,
#         S0_range[-1]-cut_off_1+30,
#         S0_range[-1]]
# S0_y = [None] * len(S0_x)
# for i in range(len(S0_x)):
#     S0_y[i] = S0[S0_x[i]-N_start]
#
# plt.scatter(S0_x, S0_y, marker='^', s=200, c='r', zorder=100)
# plt.vlines(S0_x, 0, S0_y, linestyle="dashed")
#
# for i in range(len(S0_x)-1):
#     plt.annotate('cut off={}'.format(S0_x[-1]-S0_x[i]),  # this is the text
#                  (S0_x[i], S0_y[i]),  # this is the point to label
#                  textcoords="offset points",  # how to position the text
#                  xytext=(-60, 0),  # distance from text to points (x,y)
#                  ha='center',
#                  fontsize=20)  # horizontal alignment can be left, right or center
#
# plt.xticks(list(plt.xticks()[0][1:-2]) + [S0_range[0]] + S0_x)
# plt.xlabel('No. of day', fontsize=20)
# plt.ylabel('N_cum', fontsize=20)
# plt.tick_params(labelsize=13)
# plt.legend(['N_cum(t) from SIR simulation',
#             'N_cum(t) calculated from estimated N(t)'],
#            fontsize=20)
#
# # plt.plot(np.log(S0))
# # plt.plot(np.log(nn_cum[N_start:N_start+len(S0)]))
#
# #######################################################################
# N0_range = np.arange(N_start, N_start + len(N0))
#
# plt.ylim([0., np.max(N0)*1.1])
# plt.plot(N0_range, N0, linewidth=4)
# plt.plot(N0_range, nn[N0_range], linestyle='dashed', linewidth=6)
#
# N0_y = [None] * len(S0_x)
# for i in range(len(S0_x)):
#     N0_y[i] = N0[S0_x[i]-N_start]
#
# plt.scatter(S0_x, N0_y, marker='^', s=200, c='r', zorder=100)
# plt.vlines(S0_x, 0, N0_y, linestyle="dashed")
#
# for i in range(len(S0_x)-1):
#     plt.annotate('cut off={}'.format(S0_x[-1]-S0_x[i]),  # this is the text
#                  (S0_x[i], N0_y[i]),  # this is the point to label
#                  textcoords="offset points",  # how to position the text
#                  xytext=(-60, -10),  # distance from text to points (x,y)
#                  ha='center',
#                  fontsize=20)  # horizontal alignment can be left, right or center
#
# plt.xticks(list(plt.xticks()[0][1:-1]) + [5] + S0_x)
# plt.xlabel('No. of day', fontsize=20)
# plt.ylabel('N', fontsize=20)
# plt.tick_params(labelsize=13)
# plt.legend(['N(t) from SIR simulation',
#             'N(t) calculated from estimated N(t)'],
#            fontsize=20)

#######################################################################
fig, ax1 = plt.subplots()

ax1.set_xlabel('number of days after first infection')
ax1.set_ylabel('R: estimated reproduction number')
# ax1.plot(re[:range_max], linestyle=':', linewidth=4, color='black',
#          label='true R(t) used in simulation')
ax1.plot(R[:range_max], linestyle='dashed', linewidth=4,
         label='R(t) est from true N(t) from simulation')
ax1.plot(R0_range, R0,
         label='R(t) est until {} days before the last available death'.format(dates_before_deaths[0]))
ax1.plot(R1_range, R1,
         label='R(t) est until {} days before the last available death'.format(dates_before_deaths[1]))
ax1.plot(R2_range, R2,
         label='R(t) est until {} days before the last available death'.format(dates_before_deaths[2]))
ax1.plot(R3_range, R3,
         label='R(t) est until {} days before the last available death'.format(dates_before_deaths[3]))
ax1.plot(R4_range, R4,
         label='R(t) est until {} days before the last available death'.format(dates_before_deaths[4]))
ax1.legend(fontsize=20, loc="lower left")

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
ax2.set_ylabel('daily deaths', color='black')  # we already handled the x-label with ax1
ax2.plot(deaths_range, deaths_noise_5, color='black', linestyle=':', label='deaths data')
ax2.legend()

plt.show()
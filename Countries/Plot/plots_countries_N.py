N00_range = mdates.drange(NN_start, NN_start + dt.timedelta(days=len(N00)), dt.timedelta(days=1))
N0_range = mdates.drange(N_start, N_start + dt.timedelta(days=len(N0)), dt.timedelta(days=1))

fig, ax1 = plt.subplots()

ax1.set_xlabel('date')
ax1.set_ylabel('N: estimated number of newly infected cases')
plt.plot(N00_range, N00,
         label='N(t) est, mean delay from isolation to death = 12.8 days')
plt.plot(N0_range, N0,
         label='N(t) est, mean delay from isolation to death = 18.8 days')
ax1.legend(fontsize=17, loc="upper left")
ax1.xaxis.set_tick_params(labelsize=23)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
ax2.set_ylabel('N: reported number of newly infected cases', color='black')
ax2.plot(N_reported_range, N_reported_spain, color='black', linestyle=':',
         label='N(t) reported')
ax2.legend()

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
plt.gcf().autofmt_xdate()
plt.show()

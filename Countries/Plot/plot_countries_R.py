fig, ax1 = plt.subplots()

ax1.set_xlabel('date')
ax1.set_ylabel('R: estimated effective reproduction number')
p1 = ax1.plot(R0_range, R0, color='purple',
              label='R(t) est until {} days before the last available death'.format(dates_before_deaths[0]))
p2 = ax1.plot(R1_range, R1, color='b',
              label='R(t) est until {} days before the last available death'.format(dates_before_deaths[1]))
p3 = ax1.plot(R2_range, R2, color='orange',
              label='R(t) est until {} days before the last available death'.format(dates_before_deaths[2]))
p4 = ax1.plot(R3_range, R3, color='g',
              label='R(t) est until {} days before the last available death'.format(dates_before_deaths[3]))
p5 = ax1.plot(R4_range, R4, color='r',
              label='R(t) est until {} days before the last available death'.format(dates_before_deaths[4]))
p6 = ax1.plot(R00_range, R00, color='purple', linestyle='-.', linewidth=1,
              label='R(t) est until {} days before the last available death'.format(dates_before_deaths[5]))
p7 = ax1.plot(R11_range, R11, color='b', linestyle='-.', linewidth=1,
              label='R(t) est until {} days before the last available death'.format(dates_before_deaths[6]))
p8 = ax1.plot(R22_range, R22, color='orange', linestyle='-.', linewidth=1,
              label='R(t) est until {} days before the last available death'.format(dates_before_deaths[7]))
p9 = ax1.plot(R33_range, R33, color='g', linestyle='-.', linewidth=1,
              label='R(t) est until {} days before the last available death'.format(dates_before_deaths[8]))
p10 = ax1.plot(R44_range, R44, color='r', linestyle='-.', linewidth=1,
               label='R(t) est until {} days before the last available death'.format(dates_before_deaths[9]))

ax1.xaxis.set_tick_params(labelsize=23)
ax1.legend(fontsize=17, loc="lower left")
ax1.annotate('mean delay from\nisolation to death = 18.8 days', xy=(R4_range[20], R4[20]), xycoords='data',
             xytext=(-260, -60), textcoords='offset points', fontsize=15,
             arrowprops=dict(arrowstyle='->'))
ax1.annotate('mean delay from\nisolation to death = 12.8 days', xy=(R44_range[20], R44[20]), xycoords='data',
             xytext=(30, 50), textcoords='offset points', fontsize=15,
             arrowprops=dict(arrowstyle='->'))

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
ax2.set_ylabel('daily deaths', color='black')  # we already handled the x-label with ax1
ax2.plot(deaths_range, deaths, color='black', linestyle=':', label='deaths data')
ax2.legend()

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
plt.gcf().autofmt_xdate()
plt.show()

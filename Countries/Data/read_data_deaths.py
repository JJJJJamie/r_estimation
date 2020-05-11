import pandas as pd
import matplotlib.dates as mdates
import datetime as dt

d = pd.read_csv('Countries/Data/deaths.csv')

deaths_cum_italy = np.array(d.iloc[:, 1])
deaths_italy, c_italy = find_n(smooth(deaths_cum_italy, 3))
deaths_italy = deaths_italy[8:]
deaths_start = dt.datetime(2020, 3, 1)  # starting from 3/1
deaths_range = mdates.drange(deaths_start, deaths_start+dt.timedelta(days=len(deaths_italy)), dt.timedelta(days=1))

deaths_cum_spain = np.array(d.iloc[11:, 2])
deaths_spain, c_spain = find_n(smooth(deaths_cum_spain, 7))
deaths_spain = deaths_spain[4:]
deaths_start = dt.datetime(2020, 3, 10)  # starting from 3/10
deaths_range = mdates.drange(deaths_start, deaths_start+dt.timedelta(days=len(deaths_spain)), dt.timedelta(days=1))

# deaths_cum_uk = np.array(d.iloc[14:, 3])
# deaths_uk, c_uk = find_n(smooth(deaths_cum_uk, 7))
# deaths_uk = deaths_uk[6:]
# deaths_start = dt.datetime(2020, 3, 15)  # starting from 3/15
# deaths_range = mdates.drange(deaths_start, deaths_start+dt.timedelta(days=len(deaths_uk)), dt.timedelta(days=1))

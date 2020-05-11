import pandas as pd
import matplotlib.dates as mdates
import datetime as dt

rep = pd.read_csv('Countries/Data/N_reported.csv')

N_cum_reported_italy = np.array(rep.iloc[:, 1])
N_reported_italy, _ = find_n(smooth(N_cum_reported_italy, 3))
N_reported_start = dt.datetime(2020, 2, 21)  # starting from 2/21
N_reported_range = mdates.drange(N_reported_start, N_reported_start+dt.timedelta(days=len(N_reported_italy)),
                                 dt.timedelta(days=1))

N_cum_reported_spain = np.array(rep.iloc[:, 2])
N_reported_spain, _ = find_n(smooth(N_cum_reported_spain, 7))
N_reported_start = dt.datetime(2020, 2, 23)  # starting from 2/23
N_reported_range = mdates.drange(N_reported_start, N_reported_start+dt.timedelta(days=len(N_reported_spain)),
                                 dt.timedelta(days=1))

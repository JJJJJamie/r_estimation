# isolation delay probabilities
iso_delay_data = np.random.gamma(shape1, scale1, 10000000)
iso_delay_max = math.ceil(np.quantile(iso_delay_data, 0.95))
p_iso_delay = np.histogram(iso_delay_data,
                           bins=np.arange(-1, iso_delay_max + 1), density=True)[0]

#############################################################################
# R estimation
_, R0 = find_r(N0, p_iso_delay)
_, R1 = find_r(N1, p_iso_delay)
_, R2 = find_r(N2, p_iso_delay)
_, R3 = find_r(N3, p_iso_delay)
_, R4 = find_r(N4, p_iso_delay)

_, R00 = find_r(N00, p_iso_delay)
_, R11 = find_r(N11, p_iso_delay)
_, R22 = find_r(N22, p_iso_delay)
_, R33 = find_r(N33, p_iso_delay)
_, R44 = find_r(N44, p_iso_delay)

smooth_scale = 1
cut_off = np.int((smooth_scale - 1) / 2)
R_start = N_start + dt.timedelta(days=cut_off)
RR_start = NN_start + dt.timedelta(days=cut_off)

R0 = smooth(R0, smooth_scale)
R1 = smooth(R1, smooth_scale)
R2 = smooth(R2, smooth_scale)
R3 = smooth(R3, smooth_scale)
R4 = smooth(R4, smooth_scale)

R00 = smooth(R00, smooth_scale)
R11 = smooth(R11, smooth_scale)
R22 = smooth(R22, smooth_scale)
R33 = smooth(R33, smooth_scale)
R44 = smooth(R44, smooth_scale)

R0_range = mdates.drange(R_start, R_start + dt.timedelta(days=len(R0)), dt.timedelta(days=1))
R1_range = mdates.drange(R_start, R_start + dt.timedelta(days=len(R1)), dt.timedelta(days=1))
R2_range = mdates.drange(R_start, R_start + dt.timedelta(days=len(R2)), dt.timedelta(days=1))
R3_range = mdates.drange(R_start, R_start + dt.timedelta(days=len(R3)), dt.timedelta(days=1))
R4_range = mdates.drange(R_start, R_start + dt.timedelta(days=len(R4)), dt.timedelta(days=1))

R00_range = mdates.drange(RR_start, RR_start + dt.timedelta(days=len(R00)), dt.timedelta(days=1))
R11_range = mdates.drange(RR_start, RR_start + dt.timedelta(days=len(R11)), dt.timedelta(days=1))
R22_range = mdates.drange(RR_start, RR_start + dt.timedelta(days=len(R22)), dt.timedelta(days=1))
R33_range = mdates.drange(RR_start, RR_start + dt.timedelta(days=len(R33)), dt.timedelta(days=1))
R44_range = mdates.drange(RR_start, RR_start + dt.timedelta(days=len(R44)), dt.timedelta(days=1))

dates_before_deaths = list(map(int, [deaths_range[-1] - R0_range[-1],
                                     deaths_range[-1] - R1_range[-1],
                                     deaths_range[-1] - R2_range[-1],
                                     deaths_range[-1] - R3_range[-1],
                                     deaths_range[-1] - R4_range[-1],
                                     deaths_range[-1] - R00_range[-1],
                                     deaths_range[-1] - R11_range[-1],
                                     deaths_range[-1] - R22_range[-1],
                                     deaths_range[-1] - R33_range[-1],
                                     deaths_range[-1] - R44_range[-1],
                                     ]))

# plt.plot(R0)
# plt.plot(R1)
# plt.plot(R2)
# plt.plot(R3)

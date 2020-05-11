# isolation delay probabilities
shape1 = (1/0.86)**2
scale1 = 5.1/shape1
iso_delay_data = np.random.gamma(shape1, scale1, 10000000)
iso_delay_max = math.ceil(np.quantile(iso_delay_data, 0.95))
p_iso_delay = np.histogram(iso_delay_data,
                           bins=np.arange(-1, iso_delay_max+1), density=True)[0]

#############################################################################
# R estimation
_, R0 = find_r(N0, p_iso_delay)
_, R = find_r(nn, p_iso_delay)
_, R1 = find_r(N1, p_iso_delay)
_, R2 = find_r(N2, p_iso_delay)
_, R3 = find_r(N3, p_iso_delay)
_, R4 = find_r(N4, p_iso_delay)

smooth_scale = 1
cut_off = np.int((smooth_scale-1)/2)

R0 = smooth(R0, smooth_scale)
R1 = smooth(R1, smooth_scale)
R2 = smooth(R2, smooth_scale)
R3 = smooth(R3, smooth_scale)
R4 = smooth(R4, smooth_scale)

R0_range = np.arange(N_start + cut_off, N_start + cut_off + len(R0))
R1_range = np.arange(N_start + cut_off, N_start + cut_off + len(R1))
R2_range = np.arange(N_start + cut_off, N_start + cut_off + len(R2))
R3_range = np.arange(N_start + cut_off, N_start + cut_off + len(R3))
R4_range = np.arange(N_start + cut_off, N_start + cut_off + len(R4))

deaths_range = np.arange(ind_min, ind_min+len(deaths))

dates_before_deaths = [deaths_range[-1] - R0_range[-1],
                       deaths_range[-1] - R1_range[-1],
                       deaths_range[-1] - R2_range[-1],
                       deaths_range[-1] - R3_range[-1],
                       deaths_range[-1] - R4_range[-1]]

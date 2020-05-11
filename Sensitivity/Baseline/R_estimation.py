# isolation delay probabilities
shape1 = (1/0.86)**2
scale1 = 5.1/shape1
iso_delay_data = np.random.gamma(shape1, scale1, 10000000)
iso_delay_max = math.ceil(np.quantile(iso_delay_data, 0.95))
p_iso_delay = np.histogram(iso_delay_data,
                           bins=np.arange(-1, iso_delay_max+1), density=True)[0]

#############################################################################
# R estimation
_, R0 = find_r(N, p_iso_delay)
_, R = find_r(nn, p_iso_delay)

leave_out = 0
smooth_scale = 3
cut_off = np.int((smooth_scale-1)/2) + leave_out

R0 = smooth(R0[leave_out:], smooth_scale)
R0_range = np.arange(N_start + cut_off, N_start + cut_off + len(R0))

baseline_error = np.mean(np.abs((R0-R[R0_range])/R[R0_range]))

# plt.plot(R[N_start:N_start+len(R0)])
# plt.plot(R0)

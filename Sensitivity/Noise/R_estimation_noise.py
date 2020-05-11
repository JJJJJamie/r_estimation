# isolation delay probabilities
shape1 = (1 / 0.86) ** 2
scale1 = 5.1 / shape1
iso_delay_data = np.random.gamma(shape1, scale1, 10000000)
iso_delay_max = math.ceil(np.quantile(iso_delay_data, 0.95))
p_iso_delay = np.histogram(iso_delay_data,
                           bins=np.arange(-1, iso_delay_max + 1), density=True)[0]

#############################################################################
# R estimation
_, R = find_r(nn, p_iso_delay)

leave_out = 0
smooth_scale = 9
cut_off = np.int((smooth_scale - 1) / 2) + leave_out

_, R0 = find_r(N, p_iso_delay)
_, R_noise_5 = find_r(N_noise_5, p_iso_delay)
_, R_noise_10 = find_r(N_noise_10, p_iso_delay)
_, R_noise_20 = find_r(N_noise_20, p_iso_delay)

R0 = smooth(R0[leave_out:], smooth_scale)
R_noise_5 = smooth(R_noise_5[leave_out:], smooth_scale)
R_noise_10 = smooth(R_noise_10[leave_out:], smooth_scale)
R_noise_20 = smooth(R_noise_20[leave_out:], smooth_scale)

R_noise_range = np.arange(N_start + cut_off, N_start + cut_off + len(R0))

noise_error = [np.mean(np.abs((R0 - R[R_noise_range]) / R[R_noise_range])),
               np.mean(np.abs((R_noise_5 - R[R_noise_range]) / R[R_noise_range])),
               np.mean(np.abs((R_noise_10 - R[R_noise_range]) / R[R_noise_range])),
               np.mean(np.abs((R_noise_20 - R[R_noise_range]) / R[R_noise_range]))]

# plt.plot(R0)
# plt.plot(R_noise_5)
# plt.plot(R_noise_10)
# plt.plot(R_noise_20)

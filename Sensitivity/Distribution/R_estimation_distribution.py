# isolation delay probabilities
shape1 = (1/0.86)**2
scale1 = 5.1/shape1
iso_delay_data = np.random.gamma(shape1, scale1, 10000000)
iso_delay_max = math.ceil(np.quantile(iso_delay_data, 0.95))
p_iso_delay = np.histogram(iso_delay_data,
                           bins=np.arange(-1, iso_delay_max+1), density=True)[0]

#############################################################################
# R estimation
_, R = find_r(nn, p_iso_delay)

leave_out = 0
smooth_scale = 3
cut_off = np.int((smooth_scale-1)/2) + leave_out

_, R0 = find_r(N, p_iso_delay)
_, R1 = find_r(N1, p_iso_delay)
_, R2 = find_r(N2, p_iso_delay)
_, R3 = find_r(N3, p_iso_delay)
_, R4 = find_r(N4, p_iso_delay)
_, R5 = find_r(N5, p_iso_delay)
_, R6 = find_r(N6, p_iso_delay)

R0 = smooth(R0[leave_out:], smooth_scale)
R1 = smooth(R1[leave_out:], smooth_scale)
R2 = smooth(R2[leave_out:], smooth_scale)
R3 = smooth(R3[leave_out:], smooth_scale)
R4 = smooth(R4[leave_out:], smooth_scale)
R5 = smooth(R5[leave_out:], smooth_scale)
R6 = smooth(R6[leave_out:], smooth_scale)

R0_range = np.arange(N_start + cut_off, N_start + cut_off + len(R0))
R1_range = np.arange(N1_start + cut_off, N1_start + cut_off + len(R1))
R2_range = np.arange(N2_start + cut_off, N2_start + cut_off + len(R2))
R3_range = np.arange(N3_start + cut_off, N3_start + cut_off + len(R3))
R4_range = np.arange(N4_start + cut_off, N4_start + cut_off + len(R4))
R5_range = np.arange(N5_start + cut_off, N5_start + cut_off + len(R5))
R6_range = np.arange(N6_start + cut_off, N6_start + cut_off + len(R6))

N_range_max = np.max(np.array([np.max(N_range), np.max(N1_range), np.max(N2_range), np.max(N3_range),
                               np.max(N4_range), np.max(N5_range), np.max(N6_range)]))+1

range_max = np.max(np.array([np.max(R0_range), np.max(R1_range), np.max(R2_range), np.max(R3_range),
                             np.max(R4_range), np.max(R5_range), np.max(R6_range)]))+1

# % error
distribution_error = [np.mean(np.abs((R0-R[R0_range])/R[R0_range])),
                      np.mean(np.abs((R1-R[R1_range])/R[R1_range])),
                      np.mean(np.abs((R2-R[R2_range])/R[R2_range])),
                      np.mean(np.abs((R3-R[R3_range])/R[R3_range])),
                      np.mean(np.abs((R4-R[R4_range])/R[R4_range])),
                      np.mean(np.abs((R5-R[R5_range])/R[R5_range])),
                      np.mean(np.abs((R6-R[R6_range])/R[R6_range]))]

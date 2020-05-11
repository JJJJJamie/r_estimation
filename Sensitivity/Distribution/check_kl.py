import numpy as np
from scipy.stats import norm
from scipy.stats import gamma


def kl_divergence(p, q):
    pq = p/q
    pq0 = pq[np.where(p != 0)]
    p0 = p[np.where(p != 0)]
    return np.sum(p0 * np.log(pq0))


shape2_0 = (1/0.45)**2
scale2_0 = 18.8/shape2_0
shape2_1 = (1/0.45)**2
scale2_1 = 15.8/shape2_1
shape2_2 = (1/0.45)**2
scale2_2 = 21.8/shape2_2
shape2_3 = (1/0.6)**2
scale2_3 = 18.8/shape2_3
shape2_4 = (1/0.38)**2
scale2_4 = 18.8/shape2_4

dens = 0.0001
b = np.arange(dens, 75, dens)

p_gamma_0 = gamma.pdf(b, shape2_0, 0, scale2_0)
p_gamma_1 = gamma.pdf(b, shape2_1, 0, scale2_1)
p_gamma_2 = gamma.pdf(b, shape2_2, 0, scale2_2)
p_gamma_3 = gamma.pdf(b, shape2_3, 0, scale2_3)
p_gamma_4 = gamma.pdf(b, shape2_4, 0, scale2_4)

p_gauss_1 = norm.pdf(b, 18.8, 3)
p_gauss_2 = norm.pdf(b, 18.8, 6)

kl = [kl_divergence(p_gamma_0, p_gamma_1)*dens,
      kl_divergence(p_gamma_0, p_gamma_2)*dens,
      kl_divergence(p_gamma_0, p_gamma_3)*dens,
      kl_divergence(p_gamma_0, p_gamma_4)*dens,
      kl_divergence(p_gamma_0, p_gauss_1)*dens,
      kl_divergence(p_gamma_0, p_gauss_2)*dens]

p0 = plt.plot(0, 0)
p1, = plt.plot(b[:500000], p_gamma_0[:500000], linestyle='dashed', linewidth=6)
p2, = plt.plot(b[:500000], p_gamma_1[:500000], linewidth=2)
p3, = plt.plot(b[:500000], p_gamma_2[:500000], linewidth=2)
p4, = plt.plot(b[:500000], p_gamma_3[:500000], linewidth=2)
p5, = plt.plot(b[:500000], p_gamma_4[:500000], linewidth=2)
p6, = plt.plot(b[:500000], p_gauss_1[:500000], linewidth=2)
p7, = plt.plot(b[:500000], p_gauss_2[:500000], linewidth=2)

plt.xlabel('delay between isolation and death (day)')
plt.ylabel('probability density')
plt.legend([p1, p2, p3, p4, p5, p6, p7],
           ["Gamma(mean=18.8,shape=4.94), true distribution ({:.2%})".format(distribution_error[0]),
            "Gamma(mean=21.8,shape=4.94), kl={:.2f} ({:.2%})".format(kl[0], distribution_error[1]),
            "Gamma(mean=15.8,shape=4.94), kl={:.2f} ({:.2%})".format(kl[1], distribution_error[2]),
            "Gamma(mean=18.8,shape=2.78), kl={:.2f} ({:.2%})".format(kl[2], distribution_error[3]),
            "Gamma(mean=18.8,shape=6.93), kl={:.2f} ({:.2%})".format(kl[3], distribution_error[4]),
            "Gauss(mean=18.8,s.d=3), kl={:.2f} ({:.2%})".format(kl[4], distribution_error[5]),
            "Gauss(mean=18.8,s.d=6), kl={:.2f} ({:.2%})".format(kl[5], distribution_error[6])],
           fontsize=20)

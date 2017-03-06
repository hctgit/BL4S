import pybdsim
import matplotlib.pyplot as plt
import numpy as np

a = pybdsim.Data.Load("optics.root")

f = plt.figure()
# Plot sqrt Beta_x
plt.plot(a.S(),np.sqrt(a.Sigma_x()),'.-',label='X')
plt.plot(a.S(),np.sqrt(a.Sigma_y()),'.-',label='Y')
#plt.errorbar(a.S(), a.Sigma_x(), yerr=a.Sig_Sigma_x())
#plt.errorbar(a.S(), a.Sigma_x(), yerr=a.Sig_Sigma_x())

# labels and legend:
plt.xlabel('$s$ [m]')
plt.ylabel('$\sqrt{\\beta_{x,y}\\epsilon}$ [m]')
plt.legend(loc=0)

f = plt.figure(2)
# Plot sqrt Beta_x
plt.plot(a.S(),np.sqrt(a.Beta_x()),'.-',label='$\\beta_x$')
plt.plot(a.S(),np.sqrt(a.Beta_y()),'.-',label='$\\beta_y$')
#plt.errorbar(a.S(), a.Sigma_x(), yerr=a.Sig_Sigma_x())
#plt.errorbar(a.S(), a.Sigma_x(), yerr=a.Sig_Sigma_x())

# labels and legend:
plt.xlabel('$s$ [m]')
plt.ylabel('$\\beta_{x,y}$ [m]')
plt.legend(loc=0)

plt.show()

# save figure
#f.savefig("sqrtbetax.png")


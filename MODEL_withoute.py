import numpy as np
import matplotlib
from scipy.integrate import odeint
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
y0 = [1, 0.01, 0, 0,]	#fACING PROBLEM IN FINDING C0,N0,D0
t = np.linspace(0, 48, num=24)
alpha = 0.0017
beta = 0.28
k_NF = 1.2
d_MF = 0.32
k_C = 0.38
k_CD = 0.31
delta_C = 0.066
delta_N = 0.061
alpha_D_Dv = 0.017	
k_ND = 0.0069
delta_D = 0.1


params = [alpha, beta, k_NF, d_MF, k_C, k_CD, delta_C, delta_N, alpha_D_Dv, k_ND, delta_D]

def sim(variables, t, params):
	F = variables[0]	# IT IS GIVEN AS 10^6
	C = variables[1]    
	N = variables[2]
	D = variables[3]    
	Nv =  150             #IT IS GIVEN WRT 10^6 CELLS
        # Dv = variable[5] taken with alpha_D  
	M = 0.3       #got

	alpha = params[0]
	beta = params[1]
	k_NF = params[2]
	d_MF = params[3]
	k_C = params[4]
	k_CD = params[5]
	delta_C = params[6]
	delta_N = params[7]
	alpha_D_Dv = params[8]
	k_ND = params[9]
	delta_D = params[10]


	dFdt = beta*F - k_NF*N*F - d_MF*M*F
	dCdt = k_C*M*F + k_CD*D - delta_C*C
	dNdt = alpha*Nv*C - k_NF*N*F - delta_N*N                        #only F,C,C,D only initial conditions
	dDdt = alpha_D_Dv*C - k_ND*N*D - delta_D*D

	return([dFdt, dCdt, dNdt, dDdt]) 


y = odeint(sim, y0, t, args=(params,))
a1 = y[:,0]
a2 = y[:,1]
a3 = y[:,2]
a4 = y[:,3]     

plt.plot(t,a1, color ='blue')
plt.plot(t,a2, color ='cyan')
plt.plot(t,a3, color ='red')
plt.plot(t,a4, color ='pink')

plt.show()


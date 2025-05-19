import numpy as np 
import matplotlib.pyplot as plt


#simulate a Weiner process 
def simulate_wiener_paths(T,n_paths,n):
    
        W = np.zeros([n_paths, n+1])
        dt = T/n
        times = np.linspace(0,T,n+1)

        epsilon = np.random.randn( n_paths,n)
        print(epsilon)
        for i in range(0,n):

                W[:,i+1] = W[:,i] + np.sqrt(dt)*epsilon[:,i]

        return W, times 


# : means "all rows"
# i means column i
# so w[:,i] means the values of all n_paths at tumes time step i 

def plot_wiener( T,n ):
        W,times = simulate_wiener_paths(T,1,n)
        plt.plot(times, W[0,:], label = '{} steps'.format(n))

for n in [50,100,500,1000,5000,10000]:
        plot_wiener(1,n)


plt.legend(); 
plt.show()
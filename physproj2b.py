import matplotlib.pyplot as plt
import numpy as np





def plot_trace(xg, yg,k,m):

        # acceleration of gravity
        g = 9.8195


        # change size for figure
        fig = plt.figure(figsize=(8, 8))
        ax=plt.axes()
        ax.grid()

        tf=10
        ef=np.exp(-k*tf/m)
        tgalpha=(yg*k*k-g*m*m*(1-ef)+g*tf*k*m)/(xg*k*k)
        alpha=np.arctan(tgalpha)
        v0=(xg*k)/(m*(1-ef)*np.cos(alpha))

        t=np.linspace(0,tf,1000)
        e=np.exp(-k*t/m)
        x=m/k*v0*np.cos(alpha)*(1-e)
        y=(m/k)*((v0*np.sin(alpha)+m*g/k)*(1-e)-t*g)

        plt.plot(x,y)

        # axis labels
        ax.set_xlabel('x, м', labelpad=20)
        ax.set_ylabel('y, м', labelpad=20)
        plt.show()


plot_trace(3, 4, 0.1, 2)
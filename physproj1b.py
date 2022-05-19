from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-poster')




def plot_trace(xg, yg, **kwargs):
        # calculating length
        l = (xg ** 2 + yg ** 2) ** 0.5
        # acceleration of gravity
        g = 9.8195

        deg2rad=np.pi/180

        # change size for figure
        fig = plt.figure(figsize=(8, 8))
        ax=plt.axes()
        ax.grid()

        for thetta in range(1,90,1):
            v0=((xg**2*g)/(xg*np.sin(2*thetta*deg2rad)-2*yg*np.cos(thetta*deg2rad)**2))**0.5
            # time to max height
            tp = v0 * np.sin(thetta*deg2rad) / g

            if yg==0:
                # full time
                t = np.linspace(0, 2 * tp, 100)
                x = v0 * np.cos(thetta*deg2rad) * t
                y = v0 * np.sin(thetta*deg2rad) * t - g * (t ** 2) / 2
            else:
                # full time
                toime=xg/(v0*np.cos(thetta*deg2rad))
                t = np.linspace(0,toime, 100)
                x = v0 * np.cos(thetta*deg2rad) * t
                y = v0 * np.sin(thetta*deg2rad) * t - g * (t ** 2) / 2

            print(v0,' ',thetta)
            plt.plot(x,y)


        # axis labels
        ax.set_xlabel('x, м', labelpad=20)
        ax.set_ylabel('y, м', labelpad=20)


        plt.show()


plot_trace(1, 1, color='m')
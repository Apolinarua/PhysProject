from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-poster')




def plot_trace(v0, alpha, **kwargs):

        # acceleration of gravity
        g = 9.8195

        alphax=alpha*np.pi/180
        # time to max height
        tp = v0 * np.sin(alphax) / g

        # change size for figure
        fig = plt.figure(figsize=(8, 8))
        ax = plt.axes(projection='3d')
        ax.grid()



        # converting to time range
        t = np.linspace(0, 2 * tp, 1000)
        for thetta in range(1, 360, 8):
            # x axis
            x = v0 * np.cos(alphax) * t * np.cos(thetta*np.pi/180)

            # y axis
            y = v0 * np.cos(alphax) * t * np.sin(thetta*np.pi/180)

            # z axis
            z = v0 * np.sin(alphax) * t - g * (t ** 2) / 2
            ax.plot3D(x, y, z)




        # calculating length
        l = v0 ** 2 * np.sin(2 * alphax) / g



        # axis labels
        ax.set_xlabel('x, м', labelpad=20)
        ax.set_ylabel('y, м', labelpad=20)
        ax.set_zlabel('z, м', labelpad=20)

        # chart title
        plt.title(f'v0 = {v0} м/с, α = {alpha} , l = {round(l,3)} м', fontsize=32)
        plt.grid(True)
        plt.show()


plot_trace(30, 45, color='m')

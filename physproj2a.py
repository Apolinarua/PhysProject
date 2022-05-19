import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-poster')




def plot_trace(v0, alpha, k, m,**kwargs):

        # acceleration of gravity
        g = 9.8195

        alphax = alpha * np.pi / 180

        #time equation
        tp=v0 * np.sin(alphax) / g

        # degrees to radians
        deg2rad=np.pi/180


        if alpha == 90:
                cosa = 0
        else:
                cosa = np.cos(alphax)



        # change size for figure
        fig = plt.figure(figsize=(8, 8))
        ax = plt.axes(projection='3d')
        ax.grid()

        # converting to time range
        t = np.linspace(0,2.7, 1000)






        for thetta in range(1,360,10):
                # x axis
                x = (-v0*cosa / k*m*np.exp(-k/m*t) + v0*cosa / k*m)* np.cos(thetta*deg2rad)

                # y axis
                y = (-v0*cosa / k*m*np.exp(-k/m*t) + v0*cosa / k*m)*np.sin(thetta*deg2rad)

                # z axis
                z = (v0*np.sin(alphax) + g / k) / k*(1- np.exp(-k*t)) - g*t / k
                ax.plot3D(x, y, z)



        # calculating length
        l = v0 ** 2 * np.sin(2 * alphax) / g



        # chart title
        ax.set_xlabel('x, м', labelpad=20)
        ax.set_ylabel('y, м', labelpad=20)
        ax.set_zlabel('z, м', labelpad=20)
        plt.title(f'v0 = {v0} м/с, α = {alpha} ', fontsize=32)
        plt.show()


plot_trace(30, 45, 2,1,color='m')

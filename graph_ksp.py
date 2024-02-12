import matplotlib.pyplot as plt
import time
import krpc


try:
    conn = krpc.connect()
    vessel = conn.space_center.active_vessel
    flight_info = vessel.flight()

except ConnectionRefusedError:
    print("Не удалось подключиться")  
    exit(1)

periapsis = 70000
speed = []
height = []
t = 0

while vessel.orbit.periapsis_altitude < periapsis:
    height.append(flight_info.mean_altitude)
    speed.append(flight_info.true_air_speed)
    t += 1
    time.sleep(1)

fig, axs = plt.subplots(nrows = 2, ncols = 1)

axs[0].plot(range(1, t + 1), height)
axs[1].plot(range(1, t + 1), speed)

axs[0].set(xlabel='время, с', ylabel='высота, м')
axs[1].set(xlabel='время, с', ylabel='скорость, м/с')

axs[0].set_title("График изменения высоты")
axs[1].set_title("График изменения скорости")

plt.show()
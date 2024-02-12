from math import log, sin, exp, tan, pi
import matplotlib.pyplot as plt


mass = 538_000
time = 0.0
thrust = 6_424_230
current_thrust = thrust
air_molar_mass = 0.029
R = 8.314
current_temperature = 304
g = 9.806
a = 0
current_speed = 0
square = 140
friction = 0
k_friction = 0.3
density = 0
pressure = 100_000
k_thrust = (1350_000 - 1310_000) * 5 / 40
delta_mass = 2255.5
height = 0
impuls = 0
gravi_speed = g
alpha = 90
delta_time = 0.5
distance = 0
graph_speed = []
graph_height = []


for time in range(41):
    density = 1.29 * exp(-height * 1.25 * (10**-4))
    friction = k_friction * (density * current_speed**2) / 2 * square
    current_thrust = thrust - friction
    impuls = current_thrust / (delta_mass * g)
    current_speed += impuls * g * log(mass / (mass - delta_mass)) - gravi_speed
    mass -= delta_mass
    thrust += k_thrust
    height += current_speed
    pressure = 100_000 * exp(-height / 5000)

    if 2000 <= height <= 2500:
        current_temperature = 303
    print(f"{time}:\n Height: {height}\n Speed: {current_speed}\n Current thrust: {current_thrust}\n Impuls: {impuls}")

    graph_speed.append(current_speed)
    graph_height.append(height)


while time <= 100:
    gravi_speed = g * sin(alpha)
    density = 1.29 * exp(-height * 1.25 * (10**-4))
    friction = k_friction * (density * current_speed**2) / 2 * square

    if height <= 17000:
        k_friction += 0.001 * delta_time
    else:
        k_friction += 0.003 * delta_time

    g = 9.806 - ((height / 3000) * 0.1)

    current_thrust = thrust - friction
    impuls = current_thrust / (delta_mass * g)
    current_speed += ((impuls * g * log(mass / (mass - delta_mass * delta_time)) - gravi_speed * delta_time)) * delta_time

    mass -= delta_mass * delta_time

    if height <= 3000:
        thrust += k_thrust
    elif 3000 <= height <= 4000:
        thrust += (6_604_000 - 6_576_000) * ((height - 3000) / 1000)
    elif 4000 <= height <= 5000:
        thrust += (6_576_000 - 6_626_700) * ((height - 4000) / 1000)
    elif 5000 <= height <= 6000:
        thrust += -(6_626_700 - 6_645_400) * ((height - 5000) / 1000)
    elif 6000 <= height <= 7000:
        thrust += -(6_645_400 - 6_661_300) * ((height - 6000) / 1000)
    elif 7000 <= height <= 8000:
        thrust += -(6_661_300 - 6_675_000) * ((height - 7000) / 1000)
    elif 8000 <= height <= 9000:
        thrust += -(6_675_000 - 6_687_000) * ((height - 8000) / 1000)
    elif 9000 <= height <= 10000:
        thrust += -(6_687_000 - 6_697_000) * ((height - 9000) / 1000)
    elif 10000 <= height <= 12000:
        thrust += -(6_697_300 - 6_713_000) * ((height - 10000) / 2000)
    elif 12000 <= height <= 14000:
        thrust += -(6_713_000 - 6_724_000) * ((height - 12000) / 2000)
    elif 14000 <= height <= 16000:
        thrust += -(6_724_000 - 6_732_000) * ((height - 14000) / 2000)
    elif 16000 <= height <= 18000:
        thrust += -(6_732_000 - 6_732_000) * ((height - 16000) / 2000)
    elif 18000 <= height <= 20000:
        thrust += -(6_738_000 - 6_741_000) * ((height - 18000) / 2000)
    elif 20000 <= height <= 24000:
        thrust += -(6_741_000 - 6_746_000) * ((height - 20000) / 4000)
    elif 24000 <= height <= 28000:
        thrust += -(6_746_000 - 6_748_000) * ((height - 24000) / 4000)
    elif 28000 <= height <= 32000:
        thrust += -(6_748_000 - 6_749_000) * ((height - 28000) / 4000)
    else:
        thrust = 6_750_000

    height += current_speed * delta_time

    if height <= 10000:
        current_temperature = 303 - ((height / 2500) * 0.5)
    else:
        current_temperature = 301 - ((height / 5000) * 15)

    distance = height / tan(alpha * pi / 180)

    if 2500 <= height <= 17000:
        alpha -= 0.5 * delta_time
    elif alpha >= 0:
        alpha -= 1.3 * delta_time

    square = 140 + 520 * ((90 - alpha) / 90) * delta_time
    pressure = 100_000 * exp(-height / 5000)

    if int(time) == (time):
        print(f"{(time)}:\n Height: {height}\n Speed: {current_speed}\n Impuls: {impuls}")
        print(f" Current_thrust: {current_thrust}\n Friction: {friction}\n Distance: {distance}")
        print(f"{time}:\n Speed: {current_speed}\n Height: {height}\n Array_speed: {graph_speed[int(time) - 1]}")
        graph_height.append(height)
        graph_speed.append(current_speed)

    time = int((time + delta_time) * 100) / 100


fig, axs = plt.subplots(nrows=2, ncols=1)

axs[0].plot(range(len(graph_height)), graph_height)
axs[1].plot(range(len(graph_speed)), graph_speed)

axs[0].set(xlabel="время, с", ylabel="высота, м")
axs[1].set(xlabel="время, с", ylabel="скорость, м/с")

axs[0].set_title("График изменения высоты")
axs[1].set_title("График изменения скорости")

plt.show()

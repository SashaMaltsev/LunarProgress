import krpc
import time


def connection():

    global vessel
    global flight_info

    try:
        conn = krpc.connect()
        vessel = conn.space_center.active_vessel
        flight_info = vessel.flight()

    except ConnectionRefusedError:
        print("Не удалось подключиться")  
        exit(1)

     
def start(end_height):

    vessel.auto_pilot.target_pitch_and_heading(90, 90)
    vessel.auto_pilot.engage()

    vessel.control.throttle = 1
    vessel.control.activate_next_stage()

    while flight_info.mean_altitude < end_height:
        pass


def turn90(start_height, final_height):

    while True: 
        turn_angle = 90 * (flight_info.mean_altitude - start_height) / (final_height - start_height)
        time.sleep(1)
        vessel.auto_pilot.target_pitch_and_heading(90 - turn_angle, 90)
        if 90 - turn_angle < 0:
            break
        

def entering_orbit(start_height, periapsis):

    while flight_info.mean_altitude < start_height:
        pass 
    vessel.control.activate_next_stage()
    vessel.control.throttle = 0

    st = time.time() 
    while time.time() - st < 60:
        pass 
    
    vessel.control.throttle = 1
    
    while vessel.orbit.periapsis_altitude < periapsis:
        time.sleep(1)
        pass 


if __name__ == "__main__":
    connection()
    start(2500)
    turn90(2500, 50000)
    entering_orbit(55000, 70000) 


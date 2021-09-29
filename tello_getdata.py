from djitellopy import Tello
import time

tello = Tello()

tello.connect()
tello.takeoff()

print(f"Battery Life Pecentage: {tello.get_battery()}")
time.sleep(3)

print(int(tello.query_height()))

#print(f"Tello height: {tello.query_height()}")

print(f"Tello temperature: {tello.get_temperature()} F")

print(tello.get_flight_time())

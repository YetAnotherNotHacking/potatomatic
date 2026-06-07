# Quick scrappy python controller for the potatomatic project, just a simple web gui talking to the arduino. I will expand on this once the rest of the project has been constructed.
from flask import Flask, request, redirect
import serial
import time

app = Flask(__name__)

# connecting to the arduino
SERIAL_PORT = "/dev/ttyUSB0"
BAUD = 115200
ser = serial.Serial(SERIAL_PORT, BAUD, timeout=1)
time.sleep(2) # wait for finalization

state = {
    "speed": 800, # base speed for movement
    "turn_ratio": 165/16 # ratio of pan drive pulley to the moving pulley.
}

# send a motor command to the arduino controller
def send(motor, steps):
    cmd = f"{motor} {int(steps)}\n"
    ser.write(cmd.encode())

# turn with ratio
def scaled_turn(steps):
    return steps * state["turn_ratio"]

# serve the scrappy web pannel to control it
@app.route("/", methods=["GET"])
def index():
    return f"""
    <h1>turret controller</h1>

    <form action="/move" method="post">
        <input name="steps" value="100">
        <input name="speed" value="{state['speed']}">
        <button name="action" value="turn_left">Turn Left</button>
        <button name="action" value="turn_right">Turn Right</button>
        <button name="action" value="tilt_up">Tilt Up</button>
        <button name="action" value="tilt_down">Tilt Down</button>
        <button name="action" value="tilt2_up">Tilt2 Up</button>
        <button name="action" value="tilt2_down">Tilt2 Down</button>
    </form>

    <form action="/speed" method="post">
        <input name="speed" placeholder="speed">
        <button>Set Speed</button>
    </form>
    """
# set speed from update
@app.route("/speed", methods=["POST"])
def speed():
    state["speed"] = int(request.form["speed"])
    return redirect("/")
# handle a move
@app.route("/move", methods=["POST"])
def move():
    steps = int(request.form["steps"])
    action = request.form["action"]

    if action == "turn_left":
        send(0, -scaled_turn(steps))

    elif action == "turn_right":
        send(0, scaled_turn(steps))

    elif action == "tilt_up":
        send(1, steps)

    elif action == "tilt_down":
        send(1, -steps)

    elif action == "tilt2_up":
        send(2, -steps)   # inverted, ones mirror

    elif action == "tilt2_down":
        send(2, steps)    # inverted, ones mirror

    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

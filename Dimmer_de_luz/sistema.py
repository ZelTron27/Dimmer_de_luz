from flask import Flask, request, jsonify, render_template
import time
import webbrowser

app = Flask(__name__)

#Sistema
pot_value = 0
led_intensity = 0
rele_state = False

#Limite para ativação
RELE_THRESHOLD = 600 

#Transição suave
def smooth_transition(current, target):
    step = 1 if target > current else -1

    for value in range(current, target, step):
        time.sleep(0.002)
        current = value

    return target


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/update", methods=["POST"])
def update():
    global pot_value, led_intensity, rele_state

    data = request.json
    pot_value = int(data["pot"])

    #Converte 0-1023 (ADC do ESP32) para 0-100% (que pode ser lido pelo navegador)
    target_intensity = int((pot_value / 1023) * 100)

    led_intensity = smooth_transition(led_intensity, target_intensity)

    rele_state = pot_value >= RELE_THRESHOLD

    return jsonify({
        "pot": pot_value,
        "led": led_intensity,
        "rele": rele_state
    })


if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True)
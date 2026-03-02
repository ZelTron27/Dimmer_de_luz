from flask import Flask, request, jsonify, render_template
import time
import webbrowser

app = Flask(__name__)

#Sistema
valor_potencio = 0 # Valor do potenciômetro (0-1023)
intensidade_led = 0 # Intensidade da luz 
estado_rele = False # Estado do relé (ativo ou inativo)

#Limite para ativação
limitador_rele = 600 

#Transição suave
def transicao_suave(current, target):
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
    global valor_potencio, intensidade_led, estado_rele

    data = request.json
    valor_potencio = int(data["pot"])

    #Converte 0-1023 (ADC do ESP32) para 0-100% (que pode ser lido pelo navegador)
    target_intensity = int((valor_potencio / 1023) * 100)

    intensidade_led = transicao_suave(intensidade_led, target_intensity)

    estado_rele = valor_potencio >= limitador_rele

    return jsonify({
        "pot": valor_potencio,
        "led": intensidade_led,
        "rele": estado_rele
    })


if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True, use_reloader=False) # Use reloader=False para evitar abrir duas janelas no navegador.

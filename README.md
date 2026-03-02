# Dimmer_de_luz
Dimmer_de_luz é um simulador web de controle de luminosidade inspirado em sistemas IoT.

O projeto simula o funcionamento de:
- Um potenciômetro com leitura de 0 a 1023
- Controle de intensidade de um LED (0% a 100%)
- Acionamento automático de um relé quando o valor ultrapassa um limite definido
- Uma lâmpada que acende somente quando o relé está ativado
- Um efeito visual de sobrecarga quando a intensidade atinge o valor máximo

O objetivo é demonstrar conceitos básicos de leitura analógica, lógica digital e integração entre backend e frontend.

## Tecnologias utilizadas

- Python
- Flask
- HTML
- CSS
- JavaScript
- Visual Studio Code

## Requisitos

Para executar o projeto é necessário:
- Extensão Python instalada
- Flask instalado no ambiente do projeto

### Instalação do Flask

``` No terminal, execute:
pip install flask
```
## Funcionamento do sistema

O valor do potenciômetro é enviado ao servidor Flask, que converte o valor analógico em porcentagem.
A intensidade do LED é ajustada proporcionalmente.
Quando o valor ultrapassa o limite definido, o relé é ativado e a lâmpada acende.
Ao atingir 100% de intensidade, o sistema exibe um efeito visual simulando sobrecarga.

# webapp.py
from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Главная страница

@app.route('/play')
def play():
    # Генерируем случайный коэффициент от 1.2 до 10
    coefficient = round(random.uniform(1.2, 10), 2)
    return render_template('play.html', coefficient=coefficient)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def name():
    return "Миссия Колонизация Марса"


@app.route('/index')
def slogan():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    text = ["Человечество вырастает из детства.",
            "Человечеству мала одна планета.",
            "Мы сделаем обитаемыми безжизненные пока планеты.",
            "И начнем с Марса!",
            "Присоединяйся!"]
    return "<br>".join(text)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

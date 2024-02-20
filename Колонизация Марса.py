from flask import Flask, url_for, request

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


@app.route('/image_mars')
def mars_image():
    return f"""<!doctype html>
                 <html lang="en">
                   <head>
                     <meta charset="utf-8">
                     <title>Привет, Марс!</title>
                   </head>
                   <body>
                     <h1>Жди нас, Марс!</h1>
                     <img src="{url_for('static', filename='img/mars.png')}"
                     alt="здесь должна была быть картинка, но не нашлась">
                     <p>Вот она какая, красная планета</p>
                   </body>
                 </html>"""


@app.route('/promotion_image')
def promotion_with_image():
    return f"""<!doctype html>
                 <html lang="en">
                   <head>
                     <meta charset="utf-8">
                     <meta name="viewport" content="width=device-width, initial-scale=1">
                     <link rel="stylesheet" 
                     href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                     integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                     crossorigin="anonymous">   
                     <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                     <title>Колонизация</title>
                   </head>
                   <body>
                     <h1>Жди нас, Марс!</h1>
                     <img src="{url_for('static', filename='img/mars.png')}"
                     alt="здесь должна была быть картинка, но не нашлась">
                     <div class="alert alert-secondary" role="alert">
                       Человечество вырастает из детства.
                     </div>
                     <div class="alert alert-success" role="alert">
                       Человечеству мала одна планета.
                     </div>
                     <div class="alert alert-info" role="alert">
                       Мы сделаем обитаемыми безжизненные пока планеты.
                     </div>
                     <div class="alert alert-warning" role="alert">
                       И начнем с Марса!
                     </div>
                     <div class="alert alert-danger" role="alert">
                       Присоединяйся!
                     </div>
                   </body>
                 </html>"""


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h2>на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="surname" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <br>
                                    <div class="form-group">
                                        <label for="professionSelect">Какое у вас образование</label>
                                        <select class="form-control" id="professionSelect" name="education">
                                          <option>начальное</option>
                                          <option>основное</option>
                                          <option>среднее</option>
                                          <option>высшее</option>
                                        </select>
                                     </div>
                                    <br>
                                    <label for="form-check">Какие у вас есть профессии?</label>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="pilot">
                                        <label class="form-check-label" for="acceptRules">пилот</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="builder">
                                        <label class="form-check-label" for="acceptRules">строитель</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="exobiologist">
                                        <label class="form-check-label" for="acceptRules">экзобиолог</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="doctor">
                                        <label class="form-check-label" for="acceptRules">врач</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="terraforming_engineer">
                                        <label class="form-check-label" for="acceptRules">инженер по терраформированию</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="climatologist">
                                        <label class="form-check-label" for="acceptRules">климатолог</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="radiation_protection_specialist">
                                        <label class="form-check-label" for="acceptRules">специалист по радиационной защите</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="astrogeologist">
                                        <label class="form-check-label" for="acceptRules">астрогеолог</label>
                                    </div>
                                    <br>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <br>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <br>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <br>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе</label>
                                    </div>
                                    <br>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''

    elif request.method == 'POST':
        # print(request.form.get('accept'))
        print(request.form.get('surname'))
        print(request.form.get('name'))
        print()
        print(request.form.get('email'))
        print()
        print(request.form.get('education'))
        print()
        print(request.form.get('pilot'))
        print(request.form.get('builder'))
        print(request.form.get('exobiologist'))
        print(request.form.get('doctor'))
        print(request.form.get('terraforming_engineer'))
        print(request.form.get('climatologist'))
        print(request.form.get('radiation_protection_specialist'))
        print(request.form.get('astrogeologist'))
        print()
        print(request.form.get('sex'))
        print()
        print(request.form.get('about'))
        print()
        print(request.form.get('file'))
        print()
        print(request.form.get('accept'))
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

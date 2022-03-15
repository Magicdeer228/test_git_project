from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def start():
    return render_template('base.html')


@app.route('/index')
def index():
    return render_template('index.html', text=['И на марсе будут яблони цвести!'])


@app.route('/promotion')
def promotion():
    with open('db/promotion.txt', 'r', encoding='UTF-8') as text:
        return render_template('index.html', text=text.readlines())


@app.route('/image_mars')
def image_mars():
    image_url = url_for('static', filename='img/img.jpg')
    return render_template('for_picture.html', img_url=image_url)


@app.route('/promotion_image')
def promotion_image():
    with open('db/promotion.txt', 'r', encoding='UTF-8') as text:
        image_url = url_for('static', filename='img/img.jpg')
        style = url_for('static', filename='css/style.css')
        return render_template('promotion_image.html', text=text.readlines(), img_url=image_url, style=style)


@app.route('/astronaut_selection')
def astronaut_selection():
    style = url_for('static', filename='css/style.css')
    return render_template('astronaut_selection_form.html', style=style)


@app.route('/choice/<planet_name>')
def choice(planet_name):
    planets_text = {
        'Марс': ['Эта планета близка к Земле;', 'На ней много необходимых ресурсов;', 'На ней есть вода и атмосфера;',
                 'На ней есть небольшое магнитное поле;', 'Наконец, она просто красива!'],
        'Меркурий': ['Он ближайшая к Солнцу планета;', 'Она движется по небу быстрее других планет;',
                     'Он относится к планетам земной группы;', 'Летим на Меркурий?']}

    if planet_name in planets_text:
        text = planets_text[planet_name]
    else:
        text = []
    return render_template('choice_planet.html', planet=planet_name, text=text)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return render_template('results.html', nickname=nickname, level=level, rating=rating)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

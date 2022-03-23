from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/training/<prof>')
def training(prof):
    if prof in ["Инженер-исследователь",  # инженеры
                "Инженер",
                "Пилот",
                "Строитель",
                "Инженер по терраформированию",
                "Пилот дронов",
                "Штурман",
                "Киберинженер",
                "Специалист по радиационной защите"]:
        text = 'Инженерные тренажеры'

    elif prof in ["Экзобиолог",  # научные сотрудники
                  "Врач",
                  "Астрогеолог",
                  "Климатолог"]:
        text = 'Научные симуляторы'

    else:
        text = "Извините, профессия не найдена"

    param = {"prof": f"{prof}", "text": text, "title": f"http://127.0.0.1:8080/training/{prof}"}
    return render_template('base.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

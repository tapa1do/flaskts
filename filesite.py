from flask import Flask, render_template

app = Flask(__name__)

menu= ['Установка', 'Первое приложение', 'Обратная связь']

@app.route('/')
def index():
    return render_template('index.html', title='Про Flask', menu=menu)


@app.route('/about')
def about():
    return render_template('about.html', title='О сайте')

if __name__ == '__main__':
    app.run(debug=True)
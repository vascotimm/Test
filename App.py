from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world ():
    return 'Hello World!'


@app.route('/home')
@app.route('/index')
def index ():
    return render_template('index.html')


@app.route('/about')
def about ():

    person = {
        "age": 23,
        "name": "Mustang",
        "surname": "Mustang",
        "Birth": 1996,
    }

    return render_template('about.html', person=person)


@app.route('/edit/<book>')
def hello_name(name):
    return 'name %s!' % book


if __name__ == '__main__':
    app.run()

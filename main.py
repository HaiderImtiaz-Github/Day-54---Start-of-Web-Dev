from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style = "text-align: center" >Hello World!</h1> <p> This is a paragraph </p> <img src=<iframe src="https://giphy.com/embed/tXL4FHPSnVJ0A" width="480" height="322" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/kim-novak-tXL4FHPSnVJ0A">via GIPHY</a></p>'

@app.route('/bye')
def bye():
    return 'Bye'

@app.route('/<name>/<int:age>')
def greet(name, age):
    return f'Hello {name} you are {age} years old'



if __name__=="__main__":
    app.run(debug=True)


    
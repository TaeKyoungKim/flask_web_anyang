from flask import Flask , render_template
from data import Articles

app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    articles = Articles()
    return render_template('index.html' , articles =articles )

if __name__ == '__main__': 
    app.run() 
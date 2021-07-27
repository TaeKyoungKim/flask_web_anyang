import re
from flask import Flask , render_template , request
from data import Articles

app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    articles = Articles()
    # print(articles)

    for  i in articles:
        print(i['title'])
    return render_template('index.html' , articles =articles )

@app.route('/<id>/article', methods=['GET', 'POST'])
def detail(id):
    if request.method == 'GET':
        articles = Articles()
        print(articles[int(id)-1])
        return render_template('detail.html' , article=articles[int(id)-1] )

@app.route('/article/add',methods=['GET', 'POST'] )
def add_article():
    if request.method == "GET":
        return render_template('add_article.html')

    elif request.method == "POST":
        # print(request.form.get('description'))
        title = request.form['title']
        description = request.form['description']    
        author = request.form['author']

        
        return "SUCCESS"

if __name__ == '__main__': 
    app.run() 

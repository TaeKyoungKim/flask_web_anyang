
from flask import Flask , render_template , request ,redirect
from data import Articles
import pymysql

app = Flask(__name__)
app.debug = True

# database에 접근
db= pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='1234',
                     db='o2',
                     charset='utf8')
# database를 사용하기 위한 cursor를 세팅합니다.
cursor= db.cursor()


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

        sql = f"""INSERT INTO lists(title, description,author) 
        VALUES('{title}', '{description}', '{author}');"""
        # print(sql)
        # SQL query 실행
        cursor.execute(sql)
        
        # 데이터 변화 적용
        db.commit()

        return redirect('/')

@app.route('/<id>/delete')
def del_article(id):
    sql = f"DELETE FROM `o2`.`lists` WHERE (`id` = {int(id)});"
    # print(sql)
    # SQL query 실행
    cursor.execute(sql)
    
    # 데이터 변화 적용
    db.commit()
    return redirect('/')

if __name__ == '__main__': 
    app.run() 

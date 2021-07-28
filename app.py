
from functools import wraps
from flask import Flask , render_template , request ,redirect, session
from data import Articles
import pymysql
from passlib.hash import pbkdf2_sha256

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

def is_loged_in(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        if 'is_loged' in session:
            return func(*args, **kwargs)
        else:
            return redirect('/login')
    return wrap
        

@app.route('/')
@is_loged_in
def main():
    return render_template('index.html')

@app.route('/articles', methods=['GET', 'POST'])
@is_loged_in
def articles():
    # articles = Articles()
    # print(articles)
    sql = f"SELECT * FROM lists"
    # print(sql)
    # SQL query 실행
    cursor.execute(sql)
    articles  = cursor.fetchall()
    # print(articles[0][1])
    # for  i in articles:
    #     print(i[1])
    return render_template('articles.html' , articles =articles )

@app.route('/<id>/article', methods=['GET', 'POST'])
@is_loged_in
def detail(id):
    if request.method == 'GET':
        # articles = Articles()
        # print(articles[int(id)-1])
        sql = f"SELECT * FROM lists WHERE id={int(id)}"
        # print(sql)
        # SQL query 실행
        cursor.execute(sql)
        article  = cursor.fetchone()
        print(article)
        return render_template('detail.html' , article=article)

@app.route('/article/add',methods=['GET', 'POST'] )
@is_loged_in
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
@is_loged_in
def del_article(id):
    sql = f"DELETE FROM `o2`.`lists` WHERE (`id` = {int(id)});"
    # print(sql)
    # SQL query 실행
    cursor.execute(sql)
    
    # 데이터 변화 적용
    db.commit()
    return redirect('/')

@app.route('/<id>/edit', methods=['GET', 'POST'])
@is_loged_in
def edit_article(id):
    if request.method == 'GET':
        sql = f"SELECT * FROM lists WHERE id={int(id)}"
        # print(sql)
        # SQL query 실행
        cursor.execute(sql)
        article  = cursor.fetchone()

        return render_template('edit_article.html', article=article)

    elif request.method =="POST":
        # print(request.form.get('description'))
        title = request.form['title']
        description = request.form['description']    
        author = request.form['author']

        # sql= f"""UPDATE lists SET title='{title}', description='{description}' , author='{author}'
        #  WHERE id = {int(id)} """
        sql= """UPDATE lists SET title='%s', description='%s' , author='%s'
         WHERE id = %d """ % (title,description,author ,int(id))
        # print(sql)
        # SQL query 실행
        cursor.execute(sql)
        
        # 데이터 변화 적용
        db.commit()
        return redirect('/')
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField ,SubmitField
from wtforms.validators import DataRequired, EqualTo

class RegisterForm(FlaskForm):
    id = StringField('아이디', validators=[DataRequired()] )
    name = StringField('Name', validators=[DataRequired()] )
    email = StringField('Emain', validators=[DataRequired()] )
    phone = StringField('Phone Number', validators=[DataRequired()] )
    password = PasswordField('Password', validators=[DataRequired()]) #equalTo("필드네임")
    repassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message="test")])
    submit = SubmitField("가입완료")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'GET':
        return render_template('register.html', form=form)

    elif request.method =='POST':
        if form.validate_on_submit():
            user_id = request.form['id']
            print(user_id)
            name = request.form.get('name')
            email = request.form['email']
            phone = request.form['phone']
            password = pbkdf2_sha256.hash(request.form['password'])
            print(password)
            sql = f"SELECT user_id FROM users WHERE user_id ='{user_id}'"
            cursor.execute(sql)
            user = cursor.fetchone()
            if user != None:
                return render_template('register.html', form=form)
            else:
                sql = f"""INSERT INTO users(user_id, name,email,phone,password) 
                            VALUES('{user_id}', '{name}', '{email}', '{phone}', '{password}');"""
                cursor.execute(sql)
        
                # 데이터 변화 적용
                db.commit()
                return "SUCCESS"
        else:
            return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        user_id = request.form['id']
        password = request.form['password']

        sql =f'SELECT * FROM users WHERE user_id="{user_id}"'
        
        cursor.execute(sql)

        user = cursor.fetchone()
        print(user)
        if user == None:
            return render_template('login.html')
        else:
            user_db_pw = user[5]
            result = pbkdf2_sha256.verify(password, user_db_pw)
            if result:
                session['is_loged'] = True
                session['username'] = user[2]
                return render_template('index.html')
            
            else:
                return render_template('login.html')
                
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__': 
    app.config['SECRET_KEY'] = "secret"
    app.run() 

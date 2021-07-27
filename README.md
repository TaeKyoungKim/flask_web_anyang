![image-20210527112557137](https://user-images.githubusercontent.com/25717861/119756391-729f6d00-bede-11eb-94ba-7ce05968d862.png)





![image-20210527112717645](https://user-images.githubusercontent.com/25717861/119756443-8519a680-bede-11eb-8b9f-cd46ec2e7791.png)



## virtualenv 명령을 통해서 가상환경을 만든다.

virtualenv 설치

```powershell
pip install virtualenv
```



virtualenv 명령을 통해서 userlists 프로젝트 생성

```
virtualenv flask_web
```



activate.bat 명령어를 통해 가상환경으로 들어간다.

```
cd flask_web
Scripts\activate
```





##### flask 라이브러리 설치

```powershell
pip install flask 

```



파이썬 라이브러리 관리는 requirements.txt 를 통해서 관리한다.

requirements.txt  에 설치한 라이브러리를 쓴다.

```powershell
pip freeze > requirements.txt
```



requirements.txt 를 참조해서 라이브러리 설치하는 방법

```
pip install -r requirement.txt
```



서버를 http://localhost:5000 으로 서버를 띄우기 위해 app.py파일을 생성후 다음과 같이 추가한다.

```python
from flask import Flask

app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET' , 'POST'])
def hello_world():
    return 'Hello World!'

    
if __name__ == '__main__':
    app.run(port=5000)
```





![image-20210527144050912](https://user-images.githubusercontent.com/25717861/119772114-a5a32a00-bef9-11eb-9b0f-3f48f7e2c980.png)

위와 같은 결과를 확인할 수 있다.

http://locallhost:5000 GET방식으로 요청이 오면 index.html 파일을 Html Document 문서 데이터로 바꿔서 클라이언트에게 Response 하는 기능을 만든다.



templates/index.html 파일 생성후 다음과 같이 코드를 추가한다.

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>index 페이지</title>
</head>
<body>
    <h1>안녕하세요!!!</h1>
</body>
</html>
```





app.py에 

from flask import Flask , render_template 추가 후

@app.routes('/' ....) 를 다음과 같이 수정한다.



```python
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('index.html')
```



목업 데이터를 data.py 에 다음과 같은 코드를 추가해서 데이터를 만든다.

```python
def Articles():
    articles = [{  'id': 1,  'title':'Article one',  'body':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',  'author':'vasanth',  'create_date':'04-09-2018',  }, 
 {  'id': 2,  'title':'Article two',  'body':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit  in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',  'author':'vasanth nagarajan',  'create_date':'05-09-2018',  },  
{  'id': 3,  'title':'Article three',  'body':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',  'author':'nagarajan vasanth',  'create_date':'04-09-2018',  } ] 
    return articles

# data = Articles()
# print(data)
```



http://localhost:5000 로 request가 들어왔을때 서버가 일정한 데이터 (예) articles)를 실어 보내는 기능

@app.routes('/' ....) 를 다음과 같이 수정한다.

```python
from data import Articles

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    articles  = Articles()
    return render_template('index.html' , articles =articles )
```



index.html 문서를 다음과 같이 수정한다.(jinja2 엔진을 활용한 예)

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>index 페이지</title>
</head>
<body>
    <h1>{{ articles }}</h1>
</body>
</html>
```





Atricles() 에서 articles 의 데이터 모양이 리스트이고 각 구성요서가 딕셔너리로 되어 있다.

index.html 에서 테이블로 랜더링 되도록 한다.



| id   | title | description | author | data |
| ---- | ----- | ----------- | ------ | ---- |
|      |       |             |        |      |
|      |       |             |        |      |

index.html 파일에 다음과 같이 코드를 추가한다.



```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>index 페이지</title>
</head>
<body>
    <table style="width:100%">
        
        <tr>
            <th>id</th>
            <th>title</th>
            <th>description</th>
            <th>author</th>
            <th>date</th>
          </tr>
          {% for article in articles %}

          <tr>
            <td>{{article['id']}}</td>
            <td>{{article['title']}}</td>
            <td>{{article['body']}}</td>
            <td>{{article['author']}}</td>
            <td>{{article['create_date']}}</td>
          </tr>
        {% endfor %}

      </table>
</body>
</html>
```



다음과 같은 화면이 랜더링 된다.

![image-20210726164939821](https://user-images.githubusercontent.com/25717861/126952715-d262f9f7-2fcc-485f-8dd0-12c6f21dcbcb.png)

위와 같은 표를 수정해서 description 보이지 않고  title 클릭시 상세페이지가 보여지는 기능 추가



title 클릭시 http://localhost:5000/id/article 주소로 GET방식으로 요청이 되고 서버는 요청을 받아서 그 아이디에 해당하는 데이터를 RESPONSE 한다.

웹브라우저가가 받아서 웹에 상세 내용을 랜더링한다.



detail.html을 다음과 같이 수정한다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Detail Page</title>
</head>
<body>
    <header>제목 : {{ article['title'] }}</header>
    <h3>작가 : {{ article['author'] }} </h3>
    <span>내용 <hr><br>{{ article['body']}} </span>

    <footer>{{article['create_date'] }}</footer>
</body>
</html>
```





app.py에 다음과 같은 코드 추가

```python
@app.route('/<id>/article', methods=['GET', 'POST'])
def detail(id):
    if request.method == 'GET':
        articles = Articles()
        print(articles[int(id)-1])
        return render_template('detail.html' , article=articles[int(id)-1] )
```



mysql(관계형 데이터베이스) 에 데이터를 CRUD 기능을 이용하여 데이터를 넣고, 편집하고 , 지우고등에 활용을 한다.

DATABASE 생성

```mysql
CREATE DATABASE o2;
```



TABLE 생성

```mysql
CREATE TABLE lists ( id INT AUTO_INCREMENT, title VARCHAR(32) NOT NULL, description LONGTEXT , author VARCHAR(32), create_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP PRIMARY KEY(id) ) ENGINE=INNODB

```





app.py 에 다음과 같은 코드를 추가 한다.

```python
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

        return "SUCCESS"
```





templates/add_article.html 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ADD PAGE</title>
</head>
<body>
    <h1> ADD PAGE </h1>
</body>
</html>
```



POSTMAN 프로그램으로 http://localhost:5000/article/add  POST 방식으로 x-www-url-form 형태로 요청을 보내고 테스트 결과를 확인한다.



![image-20210727142347651](https://user-images.githubusercontent.com/25717861/127100134-c45e21b2-ad86-45a7-b20b-e77433f43b65.png)

myworkbench  프로그램을 통해 데이터가 잘 INSERT  됬는지 확인한다.



templates/add_article.html 다음과 같이 코드를 추가 한다. 

기타 static 폴더에 파일을 추가하고 layouts.html , includes/_navar.html 등의 파일을 추가후 

```html
{% extends "layouts.html" %}
 {% block body %}
 <form action="/article/add" method="POST" >
     <header>제목: </header><input name="title" type="text" placeholder="제목 입력"><br>
     <header>글쓴이 : </header><input name="author" type="text" placeholder="글쓴이 입력"><br>
     <header>내용 : </header>
     <textarea name="description" cols="30" rows="10" placeholder="내용을 입력하세요"></textarea>
     <input type="submit" value="제출">
 </form>

{% endblock %}
```





app.py 파일의 @app.route('/article/add')

이부분의 코드 수정



```python
from flask import Flask , render_template , request ,redirect

@app.route('/article/add',.....)



	....
    
    return redirect('/')
```



삭제 기능을 추가

index. html 파일을 다음과 같이 추가한다.



```html
{% extends "layouts.html" %}

 {% block body %}
    <table class="table table-bordered">
        <thead>
          <tr>
            <th>id</th>
            <th>title</th>
            <th>author</th>
            <th>date</th>
            <th>기타</th>
          </tr>
        </thead>
        <tbody>
          {% for article in articles %}

          <tr>
            <td>{{article['id']}}</td>
            <td><a href="/{{ article['id'] }}/article">{{article['title']}}</a></td>
            <td>{{article['author']}}</td>
            <td>{{article['create_date']}}</td>
            <td>
              <a href="/{{ article['id'] }}/delete">
                <button class="btn btn-danger" onclick="return confirm('정말 삭제하시겠습니까?')">
                  삭제
                </button> 
              </a>
             
              <button class="btn btn-success">편집</button></td>
            
          </tr>
        {% endfor %}
        </tbody>
          

      </table>
      <a href="/article/add"><button class="btn btn-warning">글쓰기</button></a>
    {% endblock %}


```





app.py에 http://localhost:5000/id/delete 로 GET방식으로 요청이 왔을떄 그 id에 해당하는 글이 database 에서 삭제 하는 기능 추가



```python
@app.route('/<id>/delete')
def del_article(id):
    sql = f"DELETE FROM `o2`.`lists` WHERE (`id` = '{int(id)}');"
    # print(sql)
    # SQL query 실행
    cursor.execute(sql)
    
    # 데이터 변화 적용
    db.commit()
    return redirect('/')
```





mysql의 o2 schema의 lists 테이블에 있는 데이터를 조회 해서 articles저장하고 index.html 전달하는 기능 추가하기 위해

app.py를 다음과 같이 수정

```python
...

@app.route('/', methods=['GET', 'POST'])
def hello_world():
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
    return render_template('index.html' , articles =articles )
...
```








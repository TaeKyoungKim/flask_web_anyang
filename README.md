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

from flask import Flask , render_template 추가훈

@app.routes('/' ....) 를 다음과 같이 수정한다.



```python
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('index.html')
```





http://localhost:5000 로 request가 들어왔을때 서버가 일정한 데이터 (예)"메인페이지")를 실어 보내는 기능

@app.routes('/' ....) 를 다음과 같이 수정한다.

```python
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('index.html' , data ="메인페이지" )
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
    <h1>{{ data }}</h1>
</body>
</html>
```




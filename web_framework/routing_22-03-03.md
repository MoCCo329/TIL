## Routing

### 1. 장고 시작하기

urls.py에서 url처리

```python
from articles import views

urlpatterns = [
    path('index/', views.index)
    # index/ url요청이 들어오면, views.py의 index 함수를 불러온다. 경로와 함수명을 꼭 맞출 필요는 없다.
]
```



views.py에서 함수정의

```python
from django.shortcuts import render

def index(request): #함수의 첫 파라미터는 무조건 request로 한다.
    return render(request, 'index.html') # render함수 결과를 반환한다. 두번째 파라미터로 템플릿을 											적는다.
```



index.html에서 표현하기

```html
<h1>Hello world</h1>
```



### 2. git ignore

git을 사용하게 되면 해당 저장소에 있는 폴더의 모든 파일 변경사항이 추적된다. 폴더 중에서 특정 파일, 폴더, 확장자를 git으로 관리하고 싶지 않을때 git ignore를 한다.

.gitignore 파일을 만들게 되면 git이 해당 문서에 적힌 내용(특정 파일, 폴더, 확장자)은 추적하지 않게된다.

https://www.toptal.com/developers/gitignore 에서 간단하게 .gitignore를 만들 수 있다.



### 3. HTML form에서 정보 받아오기

```html
{# throw.html에서 폼 설정 #}

<form action="/catch/" method="get">
  <label for="message">메시지 :</label> # label의 for과 input의 id를 맞추면 짝꿍이 된다.
  <input type="text" id="message" name="message"> # input의 정보가 name으로 전송된다.
  <input type="submit" value="전송하기"> # form 의 action url로 해당 데이터 전송
</form>
```



```python
# views.py

def throw(request):
    render(request, 'throw.html')
    
def catch(request):
    print(request.GET, type(request.GET)) # <QueryDict: {'message': ['오징어게임']}>
    										<class 'django.http.request.QueryDict'>
    message = request.GET.get('message') # request에 GET을 실행시 get으로 정보를 얻을 수 있다.
    context = {
        'message': message
    }
    return render(request, 'catch.html', context)
```

http 리퀘스트가 있을때 장고에서 request 객체를 만들게 되며, 이를 파라미터로 가져왔기 때문에 .GET을 하면 이 정보를 사전형의 데이터로 얻을 수 있게 된다. 다시 여기서 .get('key')를 통해 원하는 정보를 가져올 수 있다. key는 input에서 사용한 name이다.



### 4. variable routing

url에서 

```python
# urls.py

path('blog/<int:id>/', views.blog), #url에서 id라는 데이터를 받는데, 정수로 받는다.
path('blog/<name>/', views.hello),
```



```python
# views.py

def blog(request, id): # 변수명을 파라미터로 받는다.
    context = {
        'id': id
    }
    return render(request, 'blog.html', context)

def hello(request, name):
    context = {
        'name': name
    }
    return render(request, 'hello.html', context)
```



```html
{# blog.html #}

<h1>{{ id }}번째 글입니다.</h1>


{# hello.html #}

<h1>{{ name }}아 안녕?</h1>
```



### 5. 앱별로 urls 관리하기

앱들이 많아지면서 같은 이름을 가진 urls가 생길 수도 있고, 유지 보수가 복잡해 질 수 있다. 이를 막기 위해 앱폴더에서 urls를 각자 관리하고, 프로젝트는 settings에서 각 앱들에 있는 urls를 불러오도록 하여 동작하도록 한다.



```python
from django.urls import include # include를 불러온다.

urlpatterns = [
    path('articles/', include('articles.urls')) # include 함수에 articles/urls 경로를 적는다.
]
```

위와같이 프로젝트 urls에 include로 연동시킨 후 각 앱 폴더에 urls.py를 만들어 path를 관리한다.



url이름이 변경될 수 있기 때문에 url을 변수로 만들어 변수명을 사용하고, 유지보수를 편리하게 할 수도 있다.

```python
app_name = 'articles' # 앱이름도 지정해 놓을 수 있다.

urlpatters = [
    path('throw/', views.catch, name='throw') # throw/의 url을 throw이름으로 저장해놓는다.
]
```

```html
<!-- html에서 앱이름:url이름 으로 사용가능하다. 앱이름이 없으면 url이름만으로도 사용 가능하다 -->
<a href="{% url 'articles:throw' %}">다시 던지기</a>
```
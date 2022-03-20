## CRUD, admin

### 1. HTTP 메시지

- 요청

```python
GET / HTTP/1.1  # GET은 Method, '/'은 Path, HTTP/1.1은 Version of the protocol
Host: developer.mozilla.org  # Headers
Accept-Language: fr
```

Method에는 GET, POST, PATCH, DELETE 등이 있다. 이는 클라이언트가 어떠한 행위를 할지를 의미한다. GET은 서버로부터 그냥 받아오기, POST는 서버에 값을 전송하기이다. HTML에서는 GET, POST 요청만 지원한다.(a태그는 GET만, form태그는 GET과 POST)

Path는 /articles/ 처럼 경로를 의미한다.



- 응답

```python
HTTP/1.1 200 OK
# HTTP/1.1은 Version of the protocol, 200은 Status code, OK는 Status message
```

Status code, Status message 종류는 아래와 같다.

200 OK

3XX Redirect

4XX 클라이언트 - Page not found, Forbidden(csrf_token은 hidden 타입으로 서버에 정보를 보낸다)

5XX 서버 - TemplateDoseNotExist at ...



### 2. admin

- 관리자 사이트에 나올 내용을 지정할 수 있다.

```python
from django.contrib import admin
from .models import Article  # models의 Article객체를 불러온다.

admin.site.register(Article)
```



- admin 아이디 생성

```bash
$ python manage.py createsuperuser
사용자 이름:
이메일 주소:
Password:
Password (again):
```



- 

```python
def __str__(self):
    return f'{self.pk}: {self.title}'


class ArticleAdmin(admin.ModelAdmin):  # admin.ModelAdmin에 있는 list_display를 커스텀
    list_display = ('id', 'title', 'created_at', 'updated_at')
    
admin.site.register(Article, ArticleAdmin)  # 두번째 인자로 위에서 지정한 클래스를 지정
```





### 3 기타

- redirect(f'/articles/{articles.pk}/')와 redirect('articles:detail', article.pk)는 같은의미이다.

- articles = Article.objects.all()[::-1] 하면 자료순서가 뒤집힌다.

  ~.all().order_by('-pk') 하면 pk 내림차순으로 정렬된다. '?'는 랜덤으로 정렬한다.

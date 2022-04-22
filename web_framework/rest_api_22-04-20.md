## Rest API

### 1. HTTP

- HyperText Transfer Protocol의 약자로 웹상에서 컨텐츠를 전송하기 위한 프로토콜(규칙, 약속)이다.
- Stateless, Connectionless의 특성을 가지고 있다. 때문에 쿠키와 세션을 통해 서버 상태를 요청과 연결한다.

- Method, Path, Version of the protocol, Headers를 요청하고 Version of the protocol, Status code, Status message, Headers의 응답을 받는다.

- Method는 자원에 대한 행위를 정의한다. 즉 주어진 리소스에 수행하길 원하는 행동을 나타낸다.

  GET은 조회, POST는 작성, PUT은 수정, DELETE는 삭제

- Status code는 HTTP요청이 성공적으로 완료되었는지 여부를 나타낸다.

  Informational responses(1XX)

  Successful responses(2XX)

  Redirection messages(3XX)

  Client error responses(4XX)

  Server error responses(5XX)



- URI(Uniform Resource Identifier)는 리소스는 식별을 위해 HTTP 전체에서 사용되는 통합 자원 식별자이다. URI의 하위 개념으로 URL과 URL이 있으며 URL은 URII와 같은 의미처럼 사용하기도 한다.
- URL(Uniform Resource Locator)는 자원의 위치를 나타낸다. 과거에는 실제 위치를 나타냈지만, 현재는 추상화된 의미론적 구성을 지닌다.(웹 주소, 링크 라고도 한다)
- URN(Uniform Resource Name)은 자원의 위치에 영향을 받지않는 이름 역할을 한다.



- URI의 구조

  Scheme(protocol) : 브라우저가 사용해야 하는 프로토콜로 http, data, file, ftp 등이 있다.

  Host(Domain name) : 요청을 받는 웹 서버의 이름. IP address를 직접 이용할 수도 있다.

  Port : 웹 서버 상의 리소스에 접근하는데 사용되는 기술적인 문 HTTP 80, HTTPS 443 등이 있다.

  Path : 웹 서버 상의 리소스 경로이다. 초기에는 실제 물리 위치를 나타냈지만, 오늘날은 추상적인 구조로 표현.

  Query(Identifier) : query sting parameters로 웹 서버에 제공되는 추가 매개변수이다. ? 뒤에서 &로 구분되								는 key-value 목록이다.

  Fragment : anchor로 자원 안에서 북마크의 한 종류이다. 해당 문서의 특정 부분만 보여줄 때 사용한다. 서버								에 요청을 보내지는 않으며 브라우저에게 알려주는 요소이다.



### 2. RESTful API

- API(Application Programming Interface)는 프로그래밍 언어가 제공하는 기능을 수행할 수 있게 만든 인터페이스이다.

  CLI는 명령줄, GUI는 그래픽으로 기능을 수행했다면, API는 프로그래밍을 통해 특정한 기능을 수행하는 것이다.(애플리케이션과 프로그래밍으로 소통하는것)

- REST(REpresentational State Transfer)는 API서버를 개발하기 위한 설계 방법론이다. 네트워크 상에서 자원을 정의하고, 자원에 대한 주소를 지정하는 전반적인 방법이다. REST를 따르는 시스템을 RESTful이라 한다.

  자원은 URI로 /  행위는 HTTP Method(GET, HOST, PUT, DELETE)로 / 표현은 JSON으로 한다.

- JSON은 JavaScript의 표기법을 따르는 단순 문자열이다. 가볍고 사람이 읽고 쓰기 쉬우며 기계가 파싱(해석, 분석)하고 만들기에도 쉽다.



### 3. Response

- JsonResponse 객체를 활용한 JSON 데이터 응답 방법들

```python
# 1. 데이터를 직접 JSON형태로 정제해서 주는 방법. JsonResponse 객체는 JSON 데이터로 인코딩하여 보낸다.

from django.http.response import JsonResponse

def article_json_1(request):
    articles = Article.objects.all()
    articles_json = []
    
    for article in articles:
        articles_json.append(
        	{
                'id': article.pk,
                'title': article.title,
                'content': article.content,
                'created_at': article.created_at,
                'updated_at': article.updated_at.                
            }
        )
    return JsonResponser(articles_json, safe=False)  # 딕셔너리 형태가 아니라면 safe=False로


# 응답 형식
[
    {
        'title': title1,
        'content': content1,
        'created_at': created_at1
        'updated_at': updated_at1
    },
    {
        ...
    }
]
```

```python
# 2. 데이터를 serialize 과정을 거쳐 application/json형태로 HttpResponse를 통해 응답한다.

from django.http.response import HttpResponse
from django.core import serializers

def article_json_2(request):
    article = Article.objects.all()
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type='application/json')
# content_type은 데이터의 media type을 클라이언트에게 알려주는 header 정보이다.


# 응답 형식
[
    {
        'model': 'articles.article',
        'pk': 1,
        'fields': {
            'title': title1,
            'content': content1,
            'created_at': created_at1
            'updated_at': updated_at1
        }
    },
    {
        ...
    }
]
```

```python
# 3. Django REST framework(DRF) 라이브러리를 사용해 응답을 한다. djangorestframework를 설치하고, 'rest_framework'를 등록해야 한다.

# serializers.py
from rest_framework import serializers
from .models. import Article

class ArticleSerializer(serializers.ModelSerializer):
    
    class Meat:
        model = Article
        firelds = '__all__'
        

# views.py
from .serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view()  # GET 메서드만 허용
def article_json_3(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)  # 단일객체가 아닐때 many=True
    return Response(serializer.data)


# 응답 형식
HTTP 200 OK
Allow: OPTIONS, GET
Content-Type: application/json
Vary: Accept

[
    {
        'id': 1,
        'title': title1,
        'content': content1,
        '...'
    },
]
```



- Serialization(직렬화) : 데이터 구조나 객체 상태를 저장하고, 나중에 재구성할 수 있는 포맷으로 변환하는 과정. 장고에서 직렬화는 QuerySet 및 Model Instance와 같은 복잡한 데이터를 JSON, XML 등의 유형으로 변환하기 용이한 Python 데이터 타입으로 만들어 준다.
- api_view decorator : default는 GET 메서드만 허용되며 다른 요청에는 405 Method Not Allowed를 표시. DRF에서 필수로 작성해야 view함수가 정상적으로 작동한다.



### 4. Single Model 예시 - articles

- serializers.py

```python
from rest_framework import serializers
from .models import Article

class ArticleListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('id', 'title',)


class ArticleSerializer(serializer.ModelSerializer):  # 모든 필드를 보여주기 위해 나눈다.
    
    class Meta:
        model = Article
        fields = '__all__'
```

- urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('article/', views.article_list),
    path('article/<int:article_pk>', views.article_detail),
]
```

- views.py

```python
from rest_framework import status
from rest_framework.response import Response
from .serializers import ArticleListSerializer, ArticleSerializer
from django.shortcuts import get_list_or_404
from .models import Article

@api_view(['GET', 'POST',])
def article_list(requset):  # 클라이언트가 뷰함수 이름을 참조하여 페이지 제목을 자동 생성한다.
    articles = get_list_or_404(Article)
    
    if request.method == 'GET':
        serializer = ArticleListSerializer(article, many=True)
        retirn Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)  # 첫번째 인자는 instance이다.
        if serializer.is_valid(raise_exception=True):  # 잘못되면 400 에러를 리턴한다.
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT',])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

	elif request.method == 'DELETE':
        article.delete()
        data = {
            'delete': f'데이터 {article_pk}번이 삭제되었습니다.',
        }
       	return Response(data, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializser.data)
```



- Status Code in DRF : DRF에는 status code를 쉽게 사용하도록 status 모듈에서 HTTP status code 집합을 제공한다.

- raise_exception : is_valid() 메서드의 파라미터로 true 인 경우 유효성 검사 실패시 400 오류를 반환한다.





### 5. 1:N Relation 예시 - comments

- models.py

```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DatetimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)                                
    

class Comment(models.Model):
    atricle = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

- serializers.py

```python
from rest_framework import serializers
from .models import Comment

class ArticleListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('id', 'title',)


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)  # 읽기 전용 필드 등록
```

- urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('article/', views.article_list),
    path('article/<int:article_pk>', views.article_detail),
    path('article/<int:article_pk>/comments/', views.comment_create),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
]
```

- views.py

```python
from .serializers import Comment
from .models import Comment

...

@api_view(['GET'])
def comment_list(request):
    comment = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        comment.delete()
        data = {
            'delete': f'댓글 {comment_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=stauts.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)  # request.data로 받지 않는 데이터(article) 넣기
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```



- Read Only Field(읽기 전용 필드) : is_valid를 통과할 때 모든 데이터가 포함되지 않으면 통과되지 않는다. 읽기 전용 필드로 만들면 유효성검사를 통과 가능하고 직렬화 하지 않으며, 반환값에는 해당 필드가 포함되도록 할 수 있다.

- 특정 게시글에 작성된 댓글 목록 출력하기

  Serializer는 기존 필드를 override 하거나 추가 필드를 구성할 수 있다.

  1. PrimaryKeyRelatedField를 이용하는 경우

  ```python
  # serializers.py
  
  class ArticleSerialiser(serializers.ModelSerializer):
      comment_set = serializer.PrimaryKeyRelatedField(many=True, read_only=True)
      # override하는 필드는 Meta에서 read_only를 설정하지 않고, 파라미터로 설정한다.
      
      class Meta:
          model = Article
          fields = '__all__'
  ```

  2. , Nested(중첩) relationships를 이용하는 경우

  ```python
  # serializers.py
  
  class ArticleSerialiser(serializers.ModelSerializer):
      comment_set = CommentSerializer(many=True, read_only=True)
      # 본인을 호출하는 대상의 Serializer를 호출한다. 이 때 가져오는 대상의 필드는 그 대상의 		Serializer 함수에서 설정한다.
      
      class Meta:
          model = Article
          fields = '__all__'
  ```

- 특정 게시글에 작성된 댓글의 개수 구하기

  serializers 필드에서 'source' arguments를 이용해 새로운 필드를 만들 수 있다.

  ```python
  # serializers.py
  
  class ArticleSerialiser(serializers.ModelSerializer):
      comment_set = CommentSerializer(many=True, read_only=True)
      comment_count = serializers.IntegerField(source='comment_set.count', 								read_only=True)
      # comment_set이라는 필드에서 .(dot)을 통해 전체 댓글의 개수를 확인한다. 이 때 .count()는 	built-in Queryset API 중 하나이다.
      
      class Meta:
          model = Article
          fields = '__all__'
  ```

  
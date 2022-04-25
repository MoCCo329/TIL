## Forign Key, Customizing authentication in Django

### 1. Foreign Key란

- 외래 키(외부 키)이며, 관계형 DB에서 한 테이블의 필드 중 다른 테이블의 행을 식별할 수 있는 키이다.
- 참조하는 테이블에서 속성(필드)에 해당하고, 참조되는 테이블의 기본키(Primary Key)를 가리킨다.

- 외래 키의 값이 반드시 부모 테이블의 기본 키일 필요는 없지만 유일한 값이여야 한다.



### 2. Foreign Key를 포함하는 모델 작성

```python
# articles/models.py

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    context = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content
```

- 보통 1:N에서 모델의 이름은 참조되는 모델의 단수형 소문자로 작성한다.

- on_delete : 외래 키가 참조하는 객체가 사라졌을 때 외래키를 가진 객체를 어떻게 처리할 지를 정의한다. 데이터 무결성을 위해 중요한 설정이며 6개의 옵션을 가진다.

  CASCADE : 부모 객체가 삭제 됐을 때 이를 참조하는 객체도 삭제한다.

  PROTEXT

  SET_NULL

  SET_DEFAULT

  SET()

  DO_NOTHING

  RESTRICT

- 데이터 무결성

  1. 개체 무결성(Entity integrity) : 모든 테이블이 PK를 가져야 하며 PK로 선택된 열은 고유해야 한다.

  1. 참조 무결성(Referential integrity) : FK 값이 데이터베이스의 특정 테이블의 PK값을 참조하는 것.
  2. 범위 무결성(Domain integrity) : 정의된 형식에서 관계형 데이터베이스의 모든 컬럼이 선언되도록 규정.



### 3. ORM 이용해 댓글 달아보기

```shell
article = Article.object.create(title='title', content='content')  # 참조될 객체 생성


comment = Comment()
comment.content = 'first comment'  # 이 상태에서 .save()하면 NOT NULL 에러 발생
comment.article_id = article.pk  # comment.article = article 와 같으며 이를 권장
comment.save()


comment.pk
# 1
comment.content
# 'first comment'

comment.article
# <ArticleL: title>
comment.article.pk
# 1
comment.article.content
# 'content'
```



### 4. 역참조

- 1 -> N 방향으로 참조를 할 때는 article.comment 형태로 사용할 수 없고, article.comment_set 처럼 comment_set manager를 사용한다.

```shell
# 참조
comment = Comment.objects.get(pk=1)
# 역참조
article.comment_set.all()
# <QuerySet [<Comment: first comment>, <Comment: second comment>]>

comments = article.comment_set.all()
for comment in comments:
	print(comment.content)
# first comment
# second comment
```



- model_set 이름 바꾸기 (권장되지 않는다.)

```python
class Comment(models.Model):
    article = models.ForignKey(Article, on_delete=models.CASCADE, related_name='comments')

# article.comment_set.all() -> article.comments.all()
```



### 5. 댓글 Create

- CommentForm 작성

```python
# article/forms.py

from .models import Article, Comment

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = '__all__'
```

- urls.py

```python
# articles/urls.py

urlpatterns = [
    path('<int:pk>/comments/', views.comment_create, name='comment_create')
]
```

- views.py

```python
# aritcles/view.py

from .forms import ArticleForm, CommentForm

def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    context = {
        'article': article,
        'comment_form': comment_form
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def comment_create(request, pk):
	if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)  # DB에 저장X, 인스턴스 생성만
            comment.article = article
            comment.save()
	    return redirect('articles:detail', article.pk)
    return redirect('accounts:login')
```

- CommentForm 출력

```html
<form action="{% url 'articles:comment_create' %}" methdo="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
</form>
```

- 이 때 Comment는 내용 필드와 외래키 필드가 있어 외래키 필드도 같이 출력된다. 이를 막기 위해 fields = '\__all\_\_' -> fields = ('content',) 혹은 exclude = ('article',) 로 설정한다.



### 6. 댓글 Read

```python
# aritcles/view.py

@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments
    }
    return render(request, 'articles/detail.html', context)
```

```html
<h4>댓글 목록</h4>
<ul>
  {% for comment in comments %}
    <li>{{ comment.content }}</li>
</ul>
```



### 7. 댓글 Delete

- urls.py

```python
urlpatterns = [
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
]
```

- views.py

```python
# variable routing 으로 comment_pk를 받는 방법

@require_POST
def comments_delete(request, article_pk, comments_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
	    comment.delete()
	return redirect('articles:detail', article_pk)
```

- detail.html

```html
<h4>댓글 목록</h4>
<ul>
  {% for comment in comments %}
    <li>
      {{ comment.content }}
      <form action="{% url 'articles:comment_delete' article.pk comment.pk %}" mehtod="POST">
        {% csrf_token %}
        <input type='submit' value="삭제">
      </form>
    </li>
</ul>
```



### 8. 참고

- 댓글 개수 출력하기

```html
# 1. {{ comments|length }}
# 2. {{ article.comment_set.all|length }}
# 3. {{ comments.count }}
```

- 댓글이 없는 경우 대체 컨텐츠 출력 (DTL의 for-empty 태그 활용)

```html
{% for comment in comments %}
  ...
{% empty %}
  <p>댓글이 없습니다.</p>
{% endfor %}
```



### 9. User model 대체하기

- Django 내장 User 모델이 제공하는 인증 요구사항이 적절하지 않을 수 있기 때문에 이를 커스텀 해야한다.
- AUTH_USER_MODEL : User를 나타내는데 사용하는 모델로 기본은 auth앱의 User모델로 설정되어있다. 프로젝트 중간에 변경하기 힘들기 때문에 첫 migration 전에 꼭 설정해놓아야 한다.

- 대체 방법은 아래와 같다.

1. 기본 User 모델을 구현하는 클래스인 AbstractUser 를 상속받아 새로운 User 모델을 작성 하는것이다. (프로젝트 중간에 진행한다면 db.sqlite3 파일과 migrations 파일을 모두 삭제하고 다시 설정해야한다.)

```python
# accounts/models.py

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```



2. 이후 settings.py의 AUTH_USER_MODEL = 'accounts.User'로 변경해준다.
3. admin사이트에서 사용자 관리창이 없어지기 때문에 admin.py를 재설정해준다. (django authenticatie custom 문서 참고)

```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```



- UserCreationForm과 UserChangeForm은 기존 auth.user 모델을 사용하는 ModelForm이기 때문에 커스텀 User 모델로 대체해야 한다.

```python
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = get_user_model()
    # class Meta(UserCreationForm Meta):  Meta 클래스의 상속을 이용 할 수도 있다
	    # model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('custom_field',)


class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)
```

- get_user_model()은 프로젝트에서 현재 활성화된 사용자 모델을 반환한다. 따라서 User클래스를 직접 참조하는 대신 django.contrib.auth.get_user_model()을 사용해 참조하는것이 유지보수에 바람직하다.



### 10. 1:N 설정

- django가 처음 가동될 때 INSTALLED_APP에서 순차적으로 앱을 import하고, 앱들의 models를 순차적으로 import한다. 따라서 먼저 읽히는 models에서 나중에 읽히는 model을 참조한다면 문제가 발생한다. 그렇기 때문에 models.py에서는 get_user_model() 함수가 아닌 settings.AUTH_USER_MODEL 문자열로 참조하여 문제를 피한다.

```python
# models.py

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```

- 외래 키가 생기면 form에서 외래 키가 선택되지 않도록 설정해 주어야 한다.

```python
# forms.py

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        exclude = ('user',)
```

```python
# views.py

def create(request):
    if request.method == 'POST'
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = form.save(commit=False)
        article.user = request.user  # form에서 user정보를 받지 않기 때문에 업데이트 필요
        article.save()
        ...
```


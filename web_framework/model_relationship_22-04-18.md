## Many to Many Relationship

### 1. 1:N의 한계와 M:N

- 1:N 관계로 정의된 DB에서 M:N 관계가 생성될 경우, 'N' 쪽 객체의 수가 증가시키며 관계를 나타내야 한다.
- 중개 모델(중개 테이블, Associative Table)을 이용해 이를 해결한다. 중개모델은 M:N관계에서 각각 테이블에 대한 외래 키를 가진다.

- django는 ManyToManyField로 중개 모델 없이 다대다 관계를 표현할 수 있다.

```python
from django.db import models

class Doctor(models.Model):
    name = models.TextField()
    

class Patient(models.Model):  # M:N의 경우 필드명을 복수형으로 짓는다.
    doctors = models.ManyToManyField(Doctor)
    name = models.TextField()
    
    
# Patient모델에 ManyToManyField를 작성했지만, 필드가 생기지 않으며 별도의 중개 테이블이 생긴다.
# 반면 Patient 객체에서 doctors 변수명으로 참조가 가능하지만, Doctor 객체에선 역참조를 해야한다.
```



- M:N ORM은 M과 N 양쪽에서 다룰 수 있다.

  ManyToManyField 작성 모델(source model) 객체에서는 상대 변수명과 add, remove 명령어를 사용한다.

  반대로 작성하지 않은 target model의 객체에서는 _set 메니저를 사용하고 add, remove 명령어를 쓴다.

  ```shell
  doctor1 = Doctor.objects.creat(name='justin')
  patient1 = Patient.objects.creat(name='tony')
  
  # 중개 레코드 생성
  patient1.doctors.add(doctor1)
  doctor1.patient_set.all()
  
  # 레코드 확인
  patient1.doctors.all()
  doctor1.patient_set.all()
  
  # 레코드 삭제
  doctor1.patient_set.remove(patient1)
  patient1.doctors.remove(doctor1)
  ```

- 역참조시 related manager (_set매니저)를 바꿀 수 있다. ManyToManyField()의 인자로 related_name을 설정해 주면 설정한 이름으로 참조 가능하다.

  ```python
  class Patient(models.Model):
      doctors = models.ManyToManyField(Doctor, related_name='patients')
      name = models.TextField()
  ```

  

### 2. 중개 테이블 직접 작성하기

- 중개 테이블 작성

```python
class Patient(models.Model):  # source model
    doctors = models.ManyToManyField(Doctor, through='Reservation')  #through 옵션으로 연결
    name = models.TextField()


class Doctor(models.Model):  # target model
    name = models.TextField()


class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)
```

- through 옵션은 중개 테이블을 직접 작성할 때 source model의 ManyToManyField 안에 작성하여 중개 테이블을 연결한다.

- 중개 테이블의 필드 생성 규칙

  source model과 target model이 다른 경우 <model1\>\_id, \<model2\>\_id와 같이 만들어 진다.

  source model과 tagret model이 같은경우 from\_\<model\>\_id, to\_\<model>\_id와 같이 만들어진다.



### 3. like 기능 구현하기

- articles 앱의 Article 테이블과 accounts 앱의 User 테이블의 M:N관계이다.

- User 테이블과 Article 테이블은 1:N관계로 묶여있으므로 related manager 명칭에 충돌이 일어난다.

  때문에 related_name을 필수로 설정 해줘야 한다.

- 큰 QuerySet에서 특정 객체가 존재하는지 확인할 때(views.py에서), in 이 아닌 exist()를 사용하는것이 효율적이다.



- articles/models.py

```python
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    ...
```

- articles/urls.py

```python
urlpatterns = [
    ...
    path('<int:article_pk>/likes/', views.likes, name='likes'),
]
```

- articles/views.py

```python
@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
    
        if request.user in article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
    	return redirect('articles:index')
    return redirect('accounts:login')
```

- articles/index.html

```html
...
<div>
  <form action="{% url 'articles:likes' article.pk %}" method="POST">
    {% csrf_token %}
    {% if user in article.like_users.all %}
      <input type="submit" value="좋아요 취소">
    {% else %}
      <input type="submit" value="좋아요">
    {% endif %}
  </form>
</div>
```

- articles/forms.py

```python
class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        exclude = ('user', 'like_users',)
```



### 4. Profile, Following 구현

- symmetrical : ManyToManyField가 동일한 모델을 가리키는 정의에서만 사용하는 옵션으로 True일 경우 자동으로 대칭되는 레코드가 생성된다. (A -> B 레코드 생성시 A <- B 레코드도 생성)

- with templete tag : 해당 태그 안에서 변수명을 바꾼다.

```html
{% with followers=person.followers.all followers=person.followings.all %}
  ...
{% endwith %}
```



- accounts/models.py

```python
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```

- accounts/urls.py

```python
urlpatterns = [
    path('<username>/', views.profile, name='profile'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]

# variable routing이 문자열인 경우 맨 뒤로 와야한다. 그렇지 않으면 모든 urls에서 호출될 수 있다.
```

- accounts/views.py

```python
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)


@require_POST
def follow(request, user_pk):
    if request.user.is.authenticated:
        person = get_object_or_404(get_user_model(), pk=article_pk)

        if request.user != person:
            if request.user in person.followers.filter(pk=request.user.pk).exist():
                person.followers.remove(request.user)
            else:
                person.followers.add(request.user)
        return redirect('articles:profile', person.username)
    return redirect('accounts:login')
```

- accounts/profile.html

```html
<div>
  팔로워 : {{ person.followers.all|length }} / 팔로우 : {{ person.followings.all|length }}
</div>

<div>
  {% csrf_token %}
  {% if user != person %}
    <form actio="{% url 'accounts:follow' person.pk %}" method="POST">
      {% if user in person.followers.all %}
        <input type="submit" value="언팔로우">
      {% else %}
        <input type="submit" value="팔로우">
      {% endif %}
    <form>
  {% endif %}
</div>
```

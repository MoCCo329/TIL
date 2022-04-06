## Django Form Class

### 1. Django Form이 필요한 이유

- HTML form, input을 통해 사용자로 부터 데이터를 받을 때 유효성을 검증하고, 필요시 입력된 데이터를 검증 결과와 함께 다시 표시해야 한다. Django Form은 이러한 작업을 간편하게 도와주는 Django의 유효성 검사 도구 중 하나이다.

- Django는 Form에 관련된 작업의 다음 세 부분을 처리해 준다.

  1. 렌더링을 위한 데이터 준비 및 재구성

  2. 데이터에 대한 HTML forms 생성

  3. 클라이언트로부터 받은 데이터 수신 및 처리



### 2. Form 사용

- Form 선언하기

```python
# model을 선언하는 것과 유사함을 알 수 있다.
from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length = 10)
    content = forms.CharField()
```

- V, T 에서 사용하기

```python
# articles/view.py
from .forms import ArticleForm

def new(request):
    form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```

```html
<!-- new.html -->

<form action="{% url 'articles:create' %}" method="POST">
  {% csrt_token %}
  {{ form }}
</form>
```



- Form rendering options : \<label> & \<input> 쌍에 대해 3가지 출력 옵션을 줄 수 있다.

  label

  1. as_p() : 각 필드가 단락(\<p> 태그)으로 감싸져서 렌더링 된다
  2. as_ul() : 각 필드가 목록 항목(\<li> 태그)으로 감싸져서 렌더링 된다. (\<ul> 태그는 직접 작성해야 한다.)
  3. as_table() : 각 필드가 테이블(\<tr> 태그) 행으로 감싸져서 렌더링 된다. (\<table> 태그는 직접 작성해야 한다.)

  input

  1. Form fields : input에 대한 유효성 검사 로직을 처리하여 템플릿에서 직접 사용된다.
  2. Widgets : 웹 페이지의 HTML input 요소 렌더링, GET/POST 딕셔너리에서 데이터 추출, widgets은 반드시 Form fields에 할당 된다.

```python
# 위젯 사용
from django import forms

class ArticleForm(forms.Form):
    REGION_A = 'sl'  # 데이터 value값
    REGION_B = 'dj'
    REGION_C = 'gj'
    REGIONS_CHOICES = [
        (REGION_A, '서울'),  # choice태그 출력 내용
        (REGION_B, '대전'),
        (REGION_C, '광주')
    ]
    
    title = forms.CharField(max_length = 10)
    content = forms.CharField(widget=forms.Textarea)
    region = forms.ChoiceField(widget=forms.Select)
```



### 3. Model Form

- 일반적으로 Model에서 정의한 필드를 Form에서 재정의 하는 중복이 생긴다. 따라서 Django는 Model을 통해 Form Class를 만들 수 있는 ModelForm이라는 Helper를 제공한다.

- Meta class는 Model의 정보를 작성하는 곳이다. 

```python
from django import forms
from .models import Article  # 불러와야 한다.

class ArticleForm(forms.ModelForm):
    
    class Meta:
        modle = Article  # 해당 모델
        fields = '__all__'  # 전체 필드를 적지 않아도 된다.
        # exclude = ('title',)  # 전체에서 일정 필드를 제외하기. fields와 동시에 사용 불가하다.
```
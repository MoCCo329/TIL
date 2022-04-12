## Authentication System

### 1. Django Authentication system

- 장고 기본앱중

  django .contrib.auth는 인증 프레임워크의 핵심과 기본 모델을 포함하며

  django.contrib.contenttypes는 사용자가 생성한 모델과 권한을 연결할 수 있게한다.

- 인증(Authentication)은 신원을 확인하는 것이며,

  권한 (Authorization)은 권한을 부여하여 수행 가능한 작업을 결정한다.

- accounts앱 생성하기

  ```bash
  python manage.py startapp accounts
  ```

  app 이름이 반드시 accounts일 필요는 없지만, accounts가 아니면 추가 설정이 필요해 accounts를 권장한다.



### 2. 쿠키와 세션

- HTTP 특징

  비연결 지향(connectionless) : 서버는 요청에 대한 응답 후 연결을 끊음

  무상태(stateless) : 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않는다.

- 쿠키의 개념

  서버가  사용자의 웹 브라우저에 전송하는 데이터 조각으로 사용자의 컴퓨터에 저장되며 동일한 서버에 재 요청 시 저장된 쿠키를 함께 전송한다.

  HTTP 쿠키는 상태가 있는 세션을 만들어 준다.(ex세션관리, 개인화, 트래킹)

- 쿠키의 수명(lifetime)

  Session cookie : 현재 세션이 종료되면 삭제된다.(일부 부라우저는 다시 시작할 때 세션을 복원시킨다.)

  Persistemt cookies : Expires 속성에 지정된 날짜 혹은 Max-Age 속성에 지정된 기간동안 남아있는다.

- 세션(Session)은 사이트와 특정 브라우저 사이의 상태를 유지시키는 것이다. 서버가 클라이언트에 특정 session id를 발급하고, 이 id를 쿠키에 저장. 쿠키는 요청 때마다 함께 전송되며 서버에서 이를 확인해 알맞은 로직을 처리한다.



### 3. 로그인

- AuthentificationForm : 사용자 로그인을 위한 form으로 request를 첫번째 인자로 취한다.

- login(request, user, backend=None) 함수는 view함수에서 사용되며 사용자를 로그인 시켜준다. Django의 session framework를 사용하여 세션에 user의 ID를 저장한다.(== 로그인)
- logout(request) 함수는 반환값이 없으며, session data를 DB에서 완전히 삭제하고 클라이언트 쿠키에서도 sessionid를 삭제한다.

- settings.py의 TEMPLATES OPTIONS에서 자동으로 user가 template에 contect로 넘어가게 해준다. 따라서 template에서 {{ user }}로 바로 사용자명을 쓸 수 있다. 비로그인시 AnonymousUser가 된다.



```python
# views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_requried
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
form django.contrib.auth.forms import AuthenticationsForm  # ModelForm이 아니다.
from django.views.decorators.http import require_http_methods, require_POST


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)  # ModelForm이 아니라 Form의 상속
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context={
        'form': form
    }
    return render(request, 'accounts/login.html', context)


@login_required
@require_POST
def logout(request):
    auth_logout(request)
    return redirect('articles:index')
```

```html
<!-- login.html -->

<form action="{% url 'accounts:login' %}" method='POST'>
  {% csrt_token %}
  {{ form.as_p }}
  <input type='submit'>
</form>
```



- 로그인 사용자에 대한 엑세스 제한 2가지 방법

  is_authenticated : arrtibute이며 로그인 여부에 따라 T/F로 결과를 얻는다. request.user객체로 html에서 로그인 창을 안보이도록 할 수 있다.

  login_required : decorator이며 views.py에서 권한에 따라 엑셋를 제한하여 로그인 사용자만 로그아웃 가능하도록, 로그아웃된 사용자만 로그인창에 접근 가능하도록 할 수 있다.

  로그인이 안돼있으면 'account/login/'으로 redirect하며 여기서 로그인하면 원래 페이지로 접속되도록 한다.

- @login_required 사용시 알아야 할 것들

  로그인이 안되어있으면 로그인 창을 next와 함께 띄운다. 이 때 로그인 폼의 action에 다른 url이 적혀있다면, next가 실행되지 못하고 날라가 버리게 된다. 따라서 url을 비워 동일 url로 새로고침 되도록 하면 next를 request.GET.get('next')를 통해 사용할 수 있게된다.

  redirect로 새로운 페이지를 불러올때 GET method를 이용하기 때문에 @require_POST()와 함께 사용하면 405 에러가 발생하게 된다. 이는 @login_required가 아닌 is_authenticated 속성값을 통해 해결할 수 있다.

  ```python
  @require_POST
  def delete(request, pk):
      if request.user.is_authenticated:
          article = get_object_or_404(Article, pk=pk)
          article.delete()
      return redirect('articles:index')
  ```

  

### 4. 회원가입, 회원탈퇴, 회원정보 수정, 비밀번호 변경

- 회원가입 : UserCreationForm을 이용한다.

```python
from django.contrib.auth.forms import UserCreationForm  # ModelForm이다.

def signup(request):
	if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
```



- 회원탈퇴 : request.user객체의 delete() 메서드를 이용한다.

```python
@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)  # 로그인 세션도 삭제할 수 있다. .delete()를 하면 request객체 정보가 								  사라지므로 위 명령과 순서가 바뀌면 안된다.
    return redirect('articles:index')
```



- 회원정보 수정 : UserChangeForm을 이용하며 일반 사용자를 위해 form을 커스텀 해야한다.

```python
# forms.py

from django.contrib.auth,forms import UserChangeForm
from django.contrib.auth import get_user_model  # user class를 불러온다.

class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name')
```

```python
from .forms import CustomUserChangeForm

@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html')
```



- 비밀번호 변경 : PasswordChangeForm을 사용한다. session도 업데이트해주어야 로그인이 유지된다.

```python
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

@login_required
@require_http_methods(['GET', 'POST'])
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # 세션 업데이트
            return redirect('articles:index')
    else:
		form = PasswordChangeForm(request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/change_password.html', context)
```


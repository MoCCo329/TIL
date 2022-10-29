## 1. html

### 1. html이란

- HTML(Hyper Text Markup Language)이며 hyper text는 참조(하이퍼링크)를 통해 문서에서 다른 문서로 접근, Markup Language는 태그 등을 이용해 문서나 데이터의 구조를 만드는 언어이다.
- W3C vs WHATWG에서 WHATWG(Apple, Google, Microsofit, Mozilla)가 이겨 웹 표준이 되었다.

<br>

### 2. HTML기본 구조

- 요소(element)는 태그(tag)와 내용(content)을 의미하며 태그에 속성(property)와 값(value)를 지정할 수 있다.

- html은 문서의 최상위 요소

- head는 문서 메타데이터 요소로 title(브라우저 상단 타이틀), meta(script 스크립트 요소(JS파일, 코드)), style(css직접 작성), link(외부 리소스 연결 요소(CSS파일, favicon등))등의 내부 태그를 가진다.

- body는 문서 본문 요소

<br>

### 3. DOM(Document Object Model) Tree

텍스트 파일인 HTML 문서를 브라우저에 표현하기 위한 구조이다. 부모-자식 관계, 형제관계(parents children sibling)등으로 구조화 된다. 두칸 띄어쓰기로 계층을 맞춘다.

<br>

### 4. 기본 태그

요소는 태그와 그 사이 내용(content)로 이루어 진다. 시작태크와 종료태그로 컨텐츠를 감싼다. 내용이 없는 태그는 닫는 태그가 없다.(br, hr, img, input, link, meta)

a는 href 속성명을 가지며 가질 수 있는 속성은 태그별로 다르다. 공백은X, 쌍따옴표 사용. 태그와 상관없이 사용 가능한 요소도 있다.(HTML Global Attribute) (id, class, data-*, style, title, tabindex)

img태그는 src, alt 속성을 가지며 alt는 이미지를 설명하는 문장이다.

```html
<head>
  <title>웹브라우저에서 탭 이름</title>
  <meta charset="UTF-8">
</head>
<body>
  <a href="주소", target="_blank", title="간단설명">
    링크표시 글자
  </a>
  <img src="이미지 링크" height="높이" width="너비" alt="alternative text" title="도움말">
  <b></b> <!--굵은 글씨-->
  <string></string> <!--굵은 글씨-->
  <i></i> <!--기울임 글씨-->
  <em></em> <!--기울임 글씨-->
  <br> <!--줄바꿈-->
  <ul>
    <li>목록 표시</li>
  </ul> <!--순서 없는 리스트-->
  <ol>
    <li>목록 표시</li>
  </ol> <!--순서 있는 리스트-->
  <h1>헤드라인1</h1>
  <p>단락구분</p> <!--줄을 띄워 문단으로 만들어 준다-->
  <hr> <!--수평선 생성-->
</body>
```

<br>

### 5. 시맨틱 태그

의미론적 요소를 담은 태그로 기존 영역을 나타내는 div와 같은 태그를 대신해서 사용한다.

```html
<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    <header></header>
    <nav></nav><!--웹페이지의 네비게이션 영역-->
    <article></article><!--본문영역-->
    <section></section><!--이외 영역으로 묶을 때-->
    <footer></footer>      
  </body>
</html>
```

- header : 문서나 섹션의 머릿글을 지정한다.
- footer : 문서나 섹션의 바닥글을 지정한다.
- nav : 네비게이션 내용을 정의한다.
- main : 문서에서 가장 중심이 되는 내용을 지정한다.
- section : 문서 구역을 나눌 때 정의한다.
- article : 본문 내용을 정의한다.
- aside : 페이지 컨텐츠를 제외한 컨텐츠를 정의한다. 링크, 광고, 사이드바 표시 등.



- details : 사용자가 보거나 숨길 수 있는 추가 세부 정보를 정의한다.
- summary : \<details>요소를 위한 눈에 보이는 제목을 정의한다.
- figure : 일러스트레이션, 다이어그램, 사진, 코드 목록 등과 같은 컨텐츠를 지정한다.
- figcaption : \<figure>요소에 대한 캡션을 정의한다.
- address : 웹페이지 저작자의 이름이나 웹페이지, 이메일주소 등 연락처를 넣기 위한 태그이다.
- hn : 제목을 표시할 때 사용하는 테그. 단순히 글자 크기를 키우기 위해서는 지양.
- hgroup : 제목과 부제목을 묶는 용도의 태그이다.
- mark : 형광펜으로 강조표시된 텍스트를 정의한다.
- time : 날짜/시간을 정의한다.

<br>

### 6. table 태그

thead, tbody, tfoot으로 이루어지며 tr로 줄을, th, td로 칸을 지정한다.

```html
<table border="2"<!--두껍게-->>
  <thead>
    <tr> <!--행 묶음-->
      <td>table data1</td><td>table data2</td><td>table data3</td> 
    </tr>
  </thead>
  <tbody>
	<tr>
      <td>table data1</td><td>table data2</td><td>table data3</td>
    </tr>
  </tbody>
  <tfoot>
	<tr>
      <td>table data1</td><td>table data2</td><td>table data3</td>
    </tr>
  </tfoot>
</table>
```

th 기본으로 중앙정렬과 굵은글씨가 적용된다.

td태그 안에 rowspan=""속성을 쓰면 같은행 칸이 합쳐지며, colspan=""을 쓰면 같은열 칸이 합쳐진다. rowspan="2"이면 옆으로 두칸. thead tbody tfoot 는 순서가 바뀌어도 알아서 head-body-foot 순서대로 나온다.

<br>

### 7. form, input 태그

form은 정보를 서버에 제출하기 위한 태그이다.

action은 form을 처리할 url. method는 form을 제출할 때 사용할 HTTP메서드. label의 for 과 input의 id로 연동. checkbox는 다중선택, radio는 단일선택

```html
<form action="URL"><!--action은 전송할 서버 주소-->
  <input type="text" name="id"><!--name은 데이터 이름-->
  <input type="password" name="pwd" value="default value"><!--value는 기본 값-->
  <textarea cols="50" rows="2">dafault value</textarea><!--여러줄을 입력할 수 있는 창-->
  <input type="submit" value="전송">
  <input type="button" value="버튼" onclick="alert('hello world')">
  <input type="reset"><!--정보초기화-->
  <input type="hidden" name="이름" value="값"><!--ui없이 서버에 정보를 전송할때 쓰는 타입-->
</form>
```

submit 타입에서 value는 버튼에 표시되는 내용이다.

button 타입은 단순한 버튼이 생기는 것으로 보통 js같은 언어랑 사용된다.

placeholder 속성은 입력창에 나타나는 글자

autofocus 속성은 자동 커서

required 속성은 필수로 지정

pattern 속성은 입력형식을 제한시킨다. 정규표현식으로 작성한다. [a-zA-z]이면 알파벳 1자를 의미. .은 모든문자 1자 +는 앞형식을 1개이상 가능하다. 마지막에 [0-9]식으로 끝났으면 마지막글자는 숫자로 입력해야한다.

```html
<form action="URL" method="get"><!--URL을 통해 정보를 전달해서 비밀번호가 노출된다-->
  <input type="text" name="id">
  <input type="password" name="pwd">
</form>

<form action="URL" method="post"><!--URL을 통해 정보를 전달하지 않는다-->
  <input type="text" name="id">
  <input type="password" name="pwd">
</form>

<form action="URL" method="post" enctype="multipart/form-data">
  <input type="file"><!--파일을 업로드 하는 타입-->
  <input type="submit">
</form>
```

form의 method를 get으로 할 경우 URL을 통해 input정보가 노출된다. post로 할 경우 URL에 노출되지 않는다.

<br>

### 8. select 태그

```html
<select name="데이터 이름"> <!--선택창 생성-->
  <option value="데이터 값">1번</option>
  <option value="">2번</option>
  <option value="">3번</option>
</select>
```

select의 속성중 multiple은 ctrl키를 눌러 여러키를 선택할 수 있다.(하지만 사용자가 알기 어려움)

```html
검정색 : <input type="radio" name="color" valeu="black">
붉은색 : <input type="radio" name="color" valeu="red" checked>
파란색 : <input type="radio" name="color" valeu="blue">

검정색 : <input type="checkbox" name="color2" valeu="black" checked>
붉은색 : <input type="checkbox" name="color2" valeu="red">
파란색 : <input type="checkbox" name="color2" valeu="blue" checked>

<label for="검정색">검정색 : </label><!--위처럼 그냥 text로 쓰는것 보다 label로 묶는것을 권장-->
<input type="checkbox" id="검정색" name="color2" valeu="black"><!--for,id를 맞추면 연결-->

<label for="검정색">검정색 :
	<input type="checkbox" id="검정색" name="color2" valeu="black">
</label><!--label로 전체를 묶을 수도 있다. checkbox, radio 등도 감싸서 user friendly하게가능-->
```

radio타입 name을 동일하게 지정하면 한가지만 선택이 가능하다.

checkbox는 다중선택이 가능하다.

checked 속성은 자동(기본) 체크.

<br>

### 9. html작성 팁

- html은 의미정보를 담는것이 중요하다. 다른 외관적인 요소는 CSS로 지정하는것이 좋다.

- 검색엔진이 내 사이트의 html을 가져가서 분석하게된다.(SEO)

- title태그에 대표되는 문구를 작성해야한다.(컨텐츠를 명확하게 표현, 페이지별로 다른 title 작성)

- meta태그를 잘 작성하는 것도 중요하다.(위와 동일)

- 페이지 URL 구조를 개선하기.


```html
<a href="주소", target="_blank", title="간단설명">
    링크표시 글자
</a>
```

```html
<!DOCTYPE html>
```

```html
<head>
  <title>웹브라우저에서 탭 이름</title>
  <meta charset="UTF-8">
</head>
<body>
  <ul>
    <li>목록 표시</li>
  </ul> <!--순서 없는 리스트-->
  <ol>
    <li>목록 표시</li>
  </ol> <!--순서 있는 리스트-->
  <string>글씨 두껍게</string>
  <h1>헤드라인1</h1>
  <p>단락구분</p>
  <br> <!--줄바꿈-->
  <img src="이미지 링크" height="높이" width="너비" alt="alternative text" title="도움말">
</body>
```

태그 속성(element, void element)

주석은 ctrl+/ 의 단축키



table

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

td -> th 기본으로 중앙정렬과 굵은글씨가 적용된다.

td태그 안에 rowspan=""속성을 쓰면 같은행 칸이 합쳐지며, colspan=""을 쓰면 같은열 칸이 합쳐진다.

thead tbody tfoot 는 순서가 바뀌어도 알아서 head-body-foot 순서대로 나온다.



form

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

폼은 서버에 데이터를 전송하기 위한 테그

submit 타입에서 value는 버튼에 표시되는 내용이다.

button타입은 단순한 버튼이 생기는 것으로 보통 js같은 언어랑 사용된다.



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

checked 속성은 자동(기본) 체크 



```html
<form action="URL" method="get"><!--URL을 통해 정보를 전달해서 비밀번호가 노출된다-->
  <input type="text" name="id">
  <input type="password" name="pwd">
</form>

<form action="URL" method="post"><!--URL을 통해 정보를 전달하지 않는다-->
  <input type="text" name="id">
  <input type="password" name="pwd">
</form>
```



```html
<form action="URL" method="post" enctype="multipart/form-data">
  <input type="file"><!--파일을 업로드 하는 타입-->
  <input type="submit">
</form>
```



```html
<head>
  <meta charset="utf-8" <!--character set을 utf-8로 하여 문서 인코딩 정보를 지정-->
  <meta name="description" content="html수업"><!--보이지 않는 페이지 정보를 입력-->
  <meta name="keywords" content="html, css, js">
  <meta http-equiv="refresh" content="30"><!--웹페이지가 30초간격 자동으로 새로고침되도록함-->
</head>
```



semantic tag는 구조를 명확하게 하기 위한 태그

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
- article : 본문 내용을 정의한다.
- section : 문서 구역을 나눌 때 정의한다.
- main : 문서에서 가장 중심이 되는 내용을 지정한다.
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



html은 의미정보를 담는것이 중요하다. 다른 외관적인 요소는 CSS로 지정하는것이 좋다.

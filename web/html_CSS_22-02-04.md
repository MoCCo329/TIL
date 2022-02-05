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
  <input type="submit">
</form>
```


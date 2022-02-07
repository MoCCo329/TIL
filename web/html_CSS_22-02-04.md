CSS

선택자를 통해 스타일을 지정할 html 요소 선택

인라인 - style

내부참조 - \<head> 태그 내에 <style\> html내에 적혀있어도 브라우져가 CSS문법으로 읽는다.

외부참조 - 별도 css파일을 만들어 링크탭으로 연결한다.



선택자(selector) 유형

​	기본 선택자

*은 전체 선택자는 태그이름 {} 형태

\* < 요소 < .클래스 < #id

점수가 같으면 css 선언된 순서에 따라 지정. div .baby는 자손선택자로 div 태그 하위 모든 baby 클래스를 가진 것





크기단위

em은 상속의 영향을 받음

rem은 최상위 요소의 사이즈를 기준으로 배수단위를 가진다. em보다 주로 사용한다.

vh

vw



normal flow

margin border padding (contents)

전체, 상하/좌우, 상/좌우/하, 상/우/하/좌

좌우값 auto로 주면 가운데 정렬이 된다.

박스 너비를 지정할 때 기본값은 content-box 넓이가 지정된다. border-box값으로 바꿔서 사용한다(box-sizing: border-box)



-------

a {

​	color:red;

}



style에 입력시 =이 아니라 :이다.

selector, declaration, property, value



일반 태그 선택자 앞에 .을 찍으면 class선택자가 된다. 한 항목에 여러개의 class를 동시에 지정할 수 있으며 띄어쓰기로 나뉜다. (나중순서가 적용됨)

태그 선택자 앞에 #를 적으면 id선택자가 된다. 한 id값은 한 항목에서만 쓰여야 한다.

#a b 라고 선택자를 쓰면 a id안에있는 b태그를 의미하게 된다. #a #b식으로 가독성을 늘릴 수도 있다.

태그 < class < id



화면 전체를 쓰는 태그는 block level element, 컨텐츠의 크기만큼만 테두리를 갖는 것을 inline element라 한다. display:block 혹은 display:inline 등으로 바꿀 수 있다.(기본속성을 바꾸는 것)

테두리와 컨텐츠의 간격은 padding으로, 테두리와 테두리간 간격은 margin, 테두리는 border(border: 1px solid red 혹은 border-width, border-color, border-style로 각각지정)로 지정 가능. width는 넓이, height는 높이

border-bottom, right, top, left



div는 block element. span은 inline element 태그

```html
<head>
  <style>
	#a {
      display:grid;
      grid-template-columns: 150px 1fr;  
    }
  </style>
</head>
<body>
  <div id="a">
    <div>
      ABCD
    </div>
    <div>
      abcd
    </div>
  </div>
</body>

```

ABCD창의 행길이는 150px고정 150px 1fr -> 1fr 1fr로 수정하면 ABCD와 abcd창이 1대1 비율로 유지된다.



```html
@media(min-width:800px) {
  div{
    display:none;
  }
}
```

위같은 미디어쿼리를 사용해서 브라우저 창이 800px 이상일 때 div태그 내용을 안보이게 할 수 있다.



<link rel="stylesheet" href="a.css"\>

를 통해 외부참조를 할 수 있다.



결합자

+

자손결합자 자식결합자>
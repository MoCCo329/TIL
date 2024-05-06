## 2. css

###  1. CSS(Cascading Style Sheets) 기본 문법

```css
a {
  color:red;
}
```

selector(a), declaration(중괄호 안 내용), property(color), value(red)

선택자로 원하는 내용에 속성과 값을 선언한다.

선택자를 통해 스타일을 지정할 html 요소 선택. 세가지 방법이 존재한다.



인라인 - style="property:value; property:value;"

```html
<h1 style="color:blue;margin-left:30px;">
  hello
</h1>
```

내부참조 - \<head> 태그 내에 <style\> 태그안에 적는다. html내에 적혀있어도 브라우저가 CSS문법으로 읽는다.

```html
<head>
  <style>
    body {
      background-color: linen;
    }
    h1 {
      color: maroon;
      margin-left: 40px;
    }
  </style>
</head>
```

외부참조 - 별도 css파일을 만들어 head에 <link rel="stylesheet" href="a.css"\> 를 넣어 외부참조를 할 수 있다.

```html
<head>
  <link rel="stylesheet" type="text/css" href="01_nav_footer.css">
</head>
```

<br>

### 2. 선택자(selector) 유형

- 기본 선택자

일반 태그 선택자 앞에 .을 찍으면 class선택자가 된다. 한 항목에 여러개의 class를 동시에 지정할 수 있으며 띄어쓰기로 나뉜다. 태그 선택자 앞에 #를 적으면 id선택자가 된다. 한 id값은 한 항목에서만 쓰여야 한다. #a b 라고 선택자를 쓰면 a id안에있는 b태그를 의미하게 된다. 선택자간 우선순위는 다음과 같다.

\* < 태그(요소), pseudo-element < .클래스, 속성, pseudo-class < #id < inline < !important(속성뒤에 적는다)

점수가 같으면 css에서 늦게 선언된 것으로 지정. div .baby는 자손선택자로 div 태그 하위 모든 baby 클래스를 가진 것

- 결합자

자손 결합자, 자식 결합자, 일반 형제 결합자, 인접 형제 결합자가 있다.

자손(그냥 띄어쓰기)는 앞선택자 하위의 모든 뒤선택자 요소

자식(>)은 앞선택자 하위의 첫 뒤선택자 요소

일반 형제 결합자 ~는 앞선택자 뒤의 뒤선택자들을 모두 선택

인접 형제 결합자 +는 앞선택자 형제 요소 중 바로 뒤에 위치하는 뒤선택자 요소를 선택(~는 뒤 모두, +는 뒤 하나만)

- 하위 선택자에게 일부 속성을 상속하게 된다. Tex관련 font, color, text-align등은 상속이 되며, box model, position은 상속되지 않는다.

<br>

### 3. 크기단위

- px(픽셀)은 모니터 해상도의 한 화소인 픽셀을 기준으로 한다. 고정적인 단위이다.
- % 백분율 단위는 가변적인 레이아웃에서 자주 사용하며 부모 크기에 따른 크기비율을 갖도록 한다.
- em은 부모의 크기를 1로하여 비율을 지정한다. 상속의 영향을 받는다.
- rem은 최상위 요소의 폰트사이즈를 기준으로 배수단위를 가진다. 최상위 html요소 폰트크기인 16px을 1로하여 비율을 지정한다. 상속의 영향을 받지 않는다.
- vh, vw(100vw 처럼 사용)은 화면에 보이는 크기인 viewport의 비율로 크기를 지정한다.
- vmax, vmin은 viewport의 가로 세로 중 큰 값을 기준으로 할 것인가, 작은 값을 기준으로 할 것인가 차이를 갖는다.

<br>

### 4. 색상 단위

- RGB는 16진수나 함수형 표기법을 사용 #000000, rgb(0, 0, 0)

- HSL은 색상, 채도, 명도를 통해 색을 지정하는 방식 hsl(120, 100%, 0)

- 뒤에 a(alpha)를 붙이면 투명도를 지정한다. rgb(0, 0, 0, 0.5)

<br>

### 5. Display

- 줄 전체를 다 채우는 태그는 block level element, 컨텐츠의 크기만큼만 테두리를 갖는 것을 inline element라 한다. display:block 혹은 display:inline 등으로 바꿀 수 있다.

- inline은 컨텐츠 크기만을 가지며 너비나 높이를 따로 지정할 수 없다.(컨텐츠의 상하여백은 line-height로 지정 가능)

- block은 margin border padding (contents)로 이루어져 있다.

- 테두리와 컨텐츠의 간격은 padding으로, 테두리와 테두리간 간격은 margin, 테두리는 border(border: 1px solid red 혹은 border-width, border-color, border-style로 각각지정)로 지정 가능. width는 넓이, height는 높이

- margin-top:10px; margin-right:20px; 처럼 지정하며 margin과 padding은 shorthand를 통해 다음과 같이 표현 가능하다. margin:10px;(상하좌우), margin:10px 20px;(상하/좌우), margin: 10px 20px 30px(상/좌우/하), margin: 10px 20px 30px 40px(상/우/하/좌) 또 text-align을 이용해 블록안에서 컨텐츠를 어디에 표시할 것인가를 지정할 수 있다.
- 너비를 지정할 때 기본값은 content-box 넓이가 지정된다. border-box값으로 바꿔서 사용한다(box-sizing: border-box)



- block element의 예로는 div, ul, ol, li, p, hr, form 등. inline element의 예로는 span, a, img, input, label 등
- inline-block은 block처럼 크기를 지정할 수 있으며, inline처럼 같은줄에 여러 요소가 올 수 있다.
- display:none은 해당 요소를 화면에 표시하지 않고 공간도 부여하지 않는다. 비슷하게 visibility:hidden은 공간은 차지하나 화면에 표현하지 않는다.

<br>

### 6. Position

- static : 모든 태그의 기본 값으로 일반적인 좌측 상단에 붙는 배치를 가진다. 부모 요소 내에서는 부모 요소의 위치를 기준으로 배치가 된다.
- relative : normal flow를 유지하며 자신의 static 위치를 기준으로 이동한다. 보여지는것은 이동한 위치이지만, 원위치의 공간을 차지한다.
- absolute : normal flow를 벗어나 다른 요소들에 영향을 주지 않는다. 가장 가까이 있는 normal flow 부모/조상 요소를 기준으로 이동한다.
- fixed : normal flow를 벗어나 viewport를 기준으로 이동한다. 즉 화면 한 위치에 고정된다.
- sticky : normal flow를 벗어나 fixed와 비슷하지만, viewport가 아닌 부모 요소 안에서만 고정되어 움직인다.

<br>

### 7. float

- CSS 속성(property) float은 한 요소(element)가 보통 흐름(normal flow)으로부터 빠져 텍스트 및 인라인(inline) 요소가 그 주위를 감싸는 자기 컨테이너의 좌우측을 따라 배치되어야 함을 지정한다.

- block element에서만 사용 가능하다.

- float속성의 값들을 right, left로 넣어 위치 정렬. clear: left 혹은 right, both 를 통해 left나 right로 float된 블럭 아래에 다음 컨텐츠를 붙일 수 있다. clear를 하지 않으면 겹쳐서 보이게 된다.

- float되면 border가 없어지며, 블록이 공간을 차지하지 않는것처럼 되어 겹쳐지게 된다. 하지만 블록이 겹쳐지더라도 내용은 float된 블록의 margin 옆으로 밀려나 보이게 된다.

- float요소들을 부모로 묶고 class="clearfix"(보통의 이름)으로 짓는다.(다른이름도 상관없다)

```html
.clearfix::after {
  content: "";
  display: block;
  clear: both;
}

...

<divvvv class="clearfix">
  <div class="box1 left">box1</div>
</divvvv>
<div class="box2">box2</div>
```

::after에 의해 divvvv태그 맨뒤에 가상요소를 만들고,  내용은 없음(""). clear: both로 인해 float: left나 right 된 요소들 아래에 가상요소가 붙게 된다. 이 처리를 통해 이후 요소들은 겹치지 않게 된다. (자식들이 float 되어있어 divvvv의 높이는 0이다.)



가상 클래스(Pseudo-class)는 요소에 직접적으로 클래스를 부여하지는 않았지만, 요소의 상태에 따라서 클래스를 적용한 것처럼 효과를 다르게 줄 수 있다. (a 태그에 a:hover, a:link 등)

가상 요소(Pseudo-elemets)는 가상의 요소를 만들고 내용을 넣어 출력하겠다는 것이다. (::after, ::before 등)

<br>

### 8. flex

- flex는 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델이다. 부모요소에 display: flex 혹은 inline-flex를 해야 적용 가능하다.

- flex-direction : row 인경우 main axis가 가로이며, cross axis는 세로이다. reverse의 경우 방향이 반대가 된다. (row, row-reverse, column, column-reverse)

- flex-wrap은 축길이를 넘어가는 item들을 다음줄로 할 지, 아님 비율에 맞춰 우겨넣을지 정한다. (wrap, nowrap)

- flex-flow는 flex-direction과 flex-wrap을 동시에 지정 가능하다. (flex-flow: row nowrap 형식)

- justify-content는 축방향으로 아이템을 어떻게 배치 시킬지를 정한다. (flex-start, flex-end, center, space-between, space-around, space-evenly)

- align-contents는 wrap을 통해 줄이 여러줄일 경우, 각 줄을 어떤식으로 배치시킬 것인가를 정한다. (flex-start, flex-end, center, space-between, space-around, space-evenly)

- align-items은 item들을 corse axis에 어떤식으로 위치시킬 것인가를 정한다. (stretch, flex-start, flex-end, center, baseline)

- align-self는 개별 아이템만 align-items를 적용시키는 것이다. 해당 컨테이너가 아니라 개별 아이템에 적용해야 한다. (stretch, flex-start, flex-end, center)

- flex-grow는 남은 영역을 아이템에 분배(flex-grow:1 모든 숫자를 합해 비율로 영역을 부여한다.), order는 순서 배치를 정한다.(order-1, order-2  기본값은 0)

<br>

### 9. 반응형

- grid system은 요소들의 디자인과 배치에 도움을 주는 시스템으로 Column(실제 컨텐츠를 포함하는 부분), Gutter(칼럼과 칼러 사이의 공간), Container(칼럼들을 담고 있는 공간)를 기본요소로 한다.

- grid를 이용한 반응형웹 구현은 아래와 같다.

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



- 미디어 쿼리를 통한 반응형 구현

```html
@media (orientation: landscape) {
	h1 {
		color: green;
	}
} <!-- 가로모드 -->

@media (orientation: portrait) {
	h1 {
		color: red;
	}
} <!-- 세로모드 -->

@media only print {
	* {
		color: black !important;
	}
} <!-- 프린트모드, 이외에도 all, screen, speech -->
```

```html
@media (min-width: 600px) {
	h4 {
		color: red;
}
}
@media (min-width: 700px) {
	h4 {
		color: orange;
}
}
@media (min-width: 800px) {
	h4 {
		color: yellow;
}
} <!--최소 00px 부터 h4의 색을 지정. (max-height: 500px) and (max-width: 500px) 처럼도 가능-->
<!--or역할은 콤마 , 가 해준다. (max-height: 500px) , (max-width: 500px)-->
```

<br>

### 10. bootstrap

- spacing

  margin은 m, padding은 p (border는 border이며 뒤 숫자는 픽셀을 의미하게 된다.)

  top은 t, bottom은 b, left는 s, right는 e, 좌우는 x, 위아래는 y

  숫자는 0~5까지이며 각각 0, 0.25, 0.5, 1, 1.5, 3rem을 의미한다.

  mt-3 같은 식으로 사용한다.

- color

  bg는 background, text는 text

  primary, success, warning, danger, info 등의 색이 있다.

- display

  d-inline, d-block, d-flex, d-grid, d-none 등이 있다.

- position

  position-absolute, position-relative, position-static, position-fixed, position-sticky로 포지션을 지정한다.

  top, bottom, start, end으로 세부 위치를 정한다. 0~100의 값을 가지고 %단위로 작용한다. 이 때 중앙기준으로 정렬되지 않고 top의 경우 위쪽, bottom의 경우 아래쪽, start의 경우 왼쪽, end의 경우 오른쪽을 기준으로 하여 정렬하므로 중앙기준으로 하기 위해선 translate-middle(원래 문법은 transform:translate(-50%,-50%);)이 필요하다.



- bootstrap에서 grid system은 flexbox로 구현된다. container, rows, column으로 컨텐츠를 배치하고 정렬, 12개의 column과 6개의 grid breakpoints(xs, sm, md, lg, xl, xxd)를 가진다.

  xs(576px) < sm(576px) < md(768px) < lg(992px) < xl(1200px) < xxd(1400px)

- class로 w-100을 갖는 div를 중간에 넣어 다음줄로 넘기거나, 다른 row로 묶어 줄을 달리할 수 있다. 칼럼이 12가 넘어가면 저절로 다음줄로 넘어간다.

- offset은 앞쪽을 띄워준다.(마진으로) offset-2를 하면 앞쪽에 2칸 차지하는 빈 공간 생성

- col-12 col-md-6 col-xl-3 같은 식으로 class를 넣어 반응형으로 만들 수 있다.

## 그리드 시스템 / 반응형 웹

### 1. float

- normal flow를 벗어나게 되며 block element에서만 사용 가능하다.

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



### 2. flex

- flex는 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델이다. 부모요소에 display: flex 혹은 inline-flex를 해야 적용 가능하다.

- flex-direction : row 인경우 main axis가 가로이며, cross axis는 세로이다. reverse의 경우 방향이 반대가 된다. (row, row-reverse, column, column-reverse)

- flex-wrap은 축길이를 넘어가는 item들을 다음줄로 할 지, 아님 비율에 맞춰 우겨넣을지 정한다. (wrap, nowrap)

- flex-flow는 flex-direction과 flex-wrap을 동시에 지정 가능하다. (flex-flow: row nowrap 형식)

- justify-content는 축방향으로 아이템을 어떻게 배치 시킬지를 정한다. (flex-start, flex-end, center, space-between, space-around, space-evenly)

- align-contents는 wrap을 통해 줄이 여러줄일 경우, 각 줄을 어떤식으로 배치시킬 것인가를 정한다. (flex-start, flex-end, center, space-between, space-around, space-evenly)

- align-items은 item들을 corse axis에 어떤식으로 위치시킬 것인가를 정한다. (stretch, flex-start, flex-end, center, baseline)

- align-self는 개별 아이템만 align-items를 적용시키는 것이다. 해당 컨테이너가 아니라 개별 아이템에 적용해야 한다. (stretch, flex-start, flex-end, center)

- flex-grow는 남은 영역을 아이템에 분배(flex-grow:1 모든 숫자를 합해 비율로 영역을 부여한다.), order는 순서 배치를 정한다.(order-1, order-2  기본값은 0)



### 3. bootstrap

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



### 4. 반응형

- grid system은 요소들의 디자인과 배치에 도움을 주는 시스템으로 Column(실제 컨텐츠를 포함하는 부분), Gutter(칼럼과 칼러 사이의 공간), Container(칼럼들을 담고 있는 공간)를 기본요소로 한다.

- bootstrap에서 grid system은 flexbox로 구현된다. container, rows, column으로 컨텐츠를 배치하고 정렬, 12개의 column과 6개의 grid breakpoints(xs, sm, md, lg, xl, xxd)를 가진다.

  xs(576px) < sm(576px) < md(768px) < lg(992px) < xl(1200px) < xxd(1400px)

- class로 w-100을 갖는 div를 중간에 넣어 다음줄로 넘기거나, 다른 row로 묶어 줄을 달리할 수 있다. 칼럼이 12가 넘어가면 저절로 다음줄로 넘어간다.

- offset은 앞쪽을 띄워준다.(마진으로) offset-2를 하면 앞쪽에 2칸 차지하는 빈 공간 생성

- col-12 col-md-6 col-xl-3 같은 식으로 class를 넣어 반응형으로 만들 수 있다.



### 5. Grid

- bootstrap을 사용하지 않는 grid와 반응형웹 구현은 아래와 같다.

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
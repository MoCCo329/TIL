float

normal flow를 벗어난다

float속성의 값들을 right left 

겹치더라도 content는 옆으로 밀려나서 보인다.(?)

float요소를 부모로 묶고 .clearfix(보통의 이름)

.clearfix::after {

​	content: "";

​	display: block;

​	clear: both;

}

를 하게 되면 ::after에 의해 맨 뒤에 가상요소 하나가 생기고, clear에 의해 float된 블록의 높이만큼 clearfix의 높이가 생겨 이후요소들과 겹치지 않고 Normal Flow를 가지게 된다.





flex
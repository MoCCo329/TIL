정리 및 보충은 02.05에...





브라우저 표준화 -> 크롬이 최고

hyper text markup language

hyper text는 문서에서 다른 문서로 접근

markup language는 문서나 데이터의 구조를 만드는 것



html > head, body

html은 문서의 최상위 요소

head는 문서 메타데이터 요소

​	<title\> 브라우저 상단 타이틀

​	meta

​	script

​	style

​	link



body는 문서 본문 요소



DOM(Document Object Model) 트리

텍스트 파일인 HTML 문서를 브라우저에 표현하기 위한 구조

부모-자식 관계, 형제관계 parents children sibling

투칸 띄어쓰기로 맞추기



시작태크와 종료태그로 컨텐츠를 감싼다. 내용이 없는 태크는 닫는 태그가 없다.(br, hr, img, input, link, meta)

a는 href 속성명을 가지며 가질 수 있는 속성은 태그별로 다르다. 공백은X, 쌍따옴표 사용. 태그와 상관없이 사용 가능한 요소도 있다.(HTML Global Attribute) (id, class, data-*, style, title, tabindex)

img태그는 src, alt 속성을 가지며 alt는 이미지가 깨질때 설명하는 문장이기도 하다.



시맨틱 태그

의미론적 요소를 담은 태그로 기존 영역을 나타내는 div를 대신해서 



table

tbody>(tr>th*3)*2 식으로 간단하게 만들 수 있다.



thead

tbody

tfoot

caption

으로 이루어지며 tr, th, td로 세부 내용



<form\>은 정보를 서버에 제출하기 위한 영역

action은 form을 처리할 url

method는 form을 제출할 때 사용할 HTTP메서드

enctype는 ..?



label의 for 과 input의 id로 연동

checkbox는 다중선택, radio는 단일선택



alt+b로 웹브라우저로 이동

html autocomplete에 의해 자동완성







CSS

선택자를 통해 스타일을 지정할 html 요소 선택

인라인 - style

내부참조 - \<head> 태그 내에 <style\>

외부참조 - 별도 css파일을 만들어 링크탭으로 연결한다.



선택자(selector) 유형

​	기본 선택자

*은 전체 선택자는 태그이름 {} 형태

\* < 요소 < .클래스 < #id

점수가 같으면 css 선언된 순서에 따라 지정. div .baby는 자손선택자로 div 태크 하위 모든 baby 클래스를 가진 것





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
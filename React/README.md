npx create-react-app하면 실행할때만 create-react-app을 설치하고 지운다. npm은 완전 설치



JSX에서는 className으로 class 설정

JSX에서 style 속성 집어넣을 때 style={ object } 형식으로 지정한다. object는 { color: 'blue', camelCase: '30px' }



/* eslint-disable */ 터미널에 뜨는 문법 에러 메시지 안뜨도록 함



onClick={ 함수 }

js에서 deep copy 하려면 [...arrary]의 spread operator 문법사용

의미없는 div를 빈칸으로 -> fragment문법



컴포넌트 만드는법

1. function 만들고
2. return() 안에 html 담기
3. <함수명\></함수명\> 쓰기



동적인 UI만들기

1. html css로 미리 디자인 완성
2. UI의 현재 상태를 state로 저장
3. state에 따라 UI가 어떻게 보일지 작성. 삼항연산자로 표현



중괄호 안에서 for 반복문 불가. map을 써야한다. 배열안에 태그가 있어도 배열을 벗기고 렌더링한다.



props

< 자식컴포넌트 작명={state이름} \>  : 작명은 보통 state 이름으로 동일하게 한다.

props.작명으로 사용

부모 -> 자식만 가능

대신 string 뿐 아니라 함수 등 모두 전송가능



onClick에 여러 함수를 넣을 수도 있다. 세미콜론으로 구분

react에선 html input 태그 같이 닫는 태그가 없어도 동작하던게 꼭 닫아줘야 동작한다.(?)



onInput, onChange, onMouseOver, onScroll 등 매우 많다.

이벤트함수.target은 이벤트가 실행된 태그를 의미. .target.value는 태그 안의 값



이벤트 버블링으로 하위태그에서 발생한 이벤트는 상위태그에서도 발생한 것이 된다.

event.stopPropagation()은 상위태그로의 이벤트 버블링을 막는 메소드 => js문법이다...



unshift, push, shift, pop, splice(인덱스, 제거할 수, 넣을 값)

arr1.concat(arr2) : arr1 뒤에 arr2 붙이기



CSS에서 url(경로) 를 통해 이미지 지정 가능

HTML에선 style={{ backgroundImage : 'url(경로)' }} , 이미지는 import 해야함

문자열 중간에 변수를 적으려면 'url(' + 변수 + ')'



public 폴더 안 데이터를 쓰려면 /부터 시작. 단 페이지에 세부 path가 있으면 문제가 발생할 수 있다.

src={process.env.PUBLIC_URL + '/logo192.png'}



export 시 default 안하면 export했던 형식으로  import 해야한다.



npm install react-router-dom

index.js에서 컴포넌트를 BrowserRouter 태그로 감싼다.

컴포넌트 js 파일에서 Routes, Route, Link를 import. Link 태그에 to 속성으로 path입력. Routes 태그 안에 Route를 넣고 path속성에 path를, element속성에 표시할 내용을 담는다.



폴더 구조

routes 에 page들 담기



useNavigate는 페이지 이동을 도와주는 함수를 제공하는 훅이다. a태그가 아니라 navigate=useNavigate() 한다음 기존 태그에 onClick 같은 이벤트를 달고 navigate('/detail')처럼 작성 가능하다.

*로 404페이지 띄우기

1은 앞으로 한페이지 (앞으로가기) -1은 뒤로가기



nested routes는 Route안에 Route를 넣어 /path 중첩을 편리하게 하는 것이다. 상위 Route에서 표시하는 컴포넌트들이 같이 표시된다. 상위 컴포넌트에서 하위 컴포넌트가 어디에 표현될 것인가는 상위컴포넌트에서 <Outlet\> 태그로 지정한다.



/:id 처럼 콜론을 이용해 파라미터를 사용 가능하다. 이 파라미터를 가져와 사용하려면 useParams() 훅을 이용한다.



npm install styled-components

import styled 한다음 let Btn = styled.button\`background : yellow; color : black;\` 처럼 작성해 바로 사용

styled-components의 장점은 스타일이 다른 js 파일로 오염되지 않는다. 오염을 막는 다른 한가지 방법은 파일이름을 App.module.css 처럼 중간에 module을 넣는다.

style로 넣어서 로딩시간 단축



React.StrictMode 태그 없애면 콘솔에 두번씩 안뜬다. 이는 디버깅을 위해 한번 미리 실행되기 때문이다.



useEffect()는 html 랜더링 완료 후 동작한다. 때문에 사용자에게 친화적인, 효율적으로 동작하게 할 수 있다.

어려운 연산, 서버에서 가져온 데이터, 타이머(setTimeout(() => {실행할 코드}, 1000)) 장착 등에 이용

useEffect는 두 인자를 받는다. 콜백함수,  dependency. 두번째 인자값이 변할 때마다 함수를 실행한다.  빈 배열로 두면 mount 시에만 실행되며 적지 않으면(default) update시에도 실행된다.

useEffect에 return 값을 넣으면 useEffect 함수 실행 전에 먼저 실행된다.(clean up function) 이전 작업을 지우는 행위를 할 때 주로 사용한다. 예를들면 clearTimeout(이전에지정한타이머), 서버로의 요청을 막을때

또 clean up function은 mount 될 땐 실행이 안되지만 unmount 시에는 실행된다.



npm install axios

axios.get('url')

axios.post('url', { params : 'params' })

Promise.all([ axios.get('url'), axios.get('url') ]).then(() => {})

서버와의 통신은 무조건 문자열만 가능 json은 문자열이다.



axios말고 fetch('url')쓰면 .json()으로 변환해줘야 한다.



css transition: 속성 0.5s; 속성이 변경될때 0.5초에 걸쳐서 변경해준다.



react automatic batching 기능에 의해 근처에 있는 set함수는 한번에 합쳐서 마지막만 재렌더링한다 setTimeout같이 시간차를 조금 두면 해결된다.



Context api를 쓰면 props 전송없이 state 공유가 가능하다. 하지만 성능이 낮아지며(비효율적인 재렌더링), 컴포넌트 재사용이 어려워지는 단점이 있어 잘 사용하진 않는다.

let Context1 = createContext()

<Context1.Provider value={{ val1, val2 }}\>

​	<Detail shoes={val1} \>

</Context.Provider\>

state사용은 const a = useContext(Context1)처럼 불러온다.



npm install react-redux @reduxjs/toolkit

src 폴더안에 store.js 파일 생성 및 기본내용 복붙

index.js에서 import { Provider } from "react-redux" 하고 Provider 태그로 App 태그를 감싼다.

Provider 속성에 store={ 위에서만든 store } 를 한다.



store.js에선

let user = createSlice({

​	name : 'state이름'

​	initialState : '초기값'

})

그리고 내부에 user.reducer

사용은

let a = useSelector((state) => { return state.user }) 해서 사용



state수정은 createSlice안 reducers 에 함수를 작성. return 값으로 변경된다. 파라미터 사용시 뒤에 .payload 붙이기

export let { 함수1, 함수2 }  = user.actions 처럼 .actions로 함수들을 불러와 export 할 수 있다.

let dispatch = useDispatch(), 또 위에서 export한 함수를 불러오고

dispatch(함수1()) 처럼 감싸서 사용한다.



&&, switch, 객체로 if문 쓰는법



local storage에는 key - value 형태로 저장 가능하며 문자열로 한 사이트당 최대 5mb씩 가능하다.

localStorage.setItem('key', 'value') 명령어로 local storage에 저장 가능하다.

.getItem('key')

.removeItem('key')

JSON.stringify(obj)을 통해 배열이나 객체를 JSON으로 바꾸고 저장 가능하다.

JSON.parse(내용)을 통해 다시 배열이나 객체로 이용 가능하다.



redux-persist

react-query



react 개발자 도구(profiler), redux 개발자 도구



const Detail = lazy(() => import('./routes/Detail.js')) 처럼 lazy하게 import할 시 필요할 때 import한다.

대신 해당 컴포넌트를 사용할때 오래걸릴수 있다. 이를위해 Suspense 태그, fallback속성 안에 로딩중에 띄울 UI를 정의할 수 있다. 전체 Routes를 감싸도 된다.



재랜더링 막는 memo, useMemo

memo() 로 감싸면 필요할때만(컴포넌트로의 props 값이 바뀔때만) 재랜더링 한다.

useMemo(() => 함수(). []) 는 랜더링시 1회만 실행해준다. 뒤에 dependency를 적으면 해당 state가 변화할때만 실행한다.



let [isPending, startTransition] = useTransition()

startTransition의 콜백함수로 성능저하가  일어나는 함수를 감싼다. 그러면 다른 작업보다 우선순위가 낮아져서 늦게 처리하게 된다.

isPending은 startTransition 안의 함수가 실행중일때 true로 변한다.



let state = useDeferredValue(state)는 state변동사항이 있을때 늦게 처리해준다.



progressive web app

pwa가 세팅된 react 프로젝트를 생성해야한다.

npx create-react-app 프로젝트명 --template cra-template-pwa

npm run build


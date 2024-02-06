# React

* App.js에 html/css 작성 - 메인페이지(index.html) 화면 구성

* index.js로 App.js ==> index.html 연결

* public folder: static 보관함

## Why React?
#### 선언형 뷰
* 상호작용이 활발한 UI에서 효율적인 데이터 바인딩이 가능
* 코드 예측, 디버그 수월
#### 컴포넌트
* 캡슐화한 요소들을 조합하여 복잡하고 다양한 UI만들기
#### 확장성
* 기존 코드를 다시 작성할 필요없이 React의 새로운 기능 사용
* Node 서버에서 렌더링 가능
* React Native로 모바일 앱 개발

## JSX (Javascript Syntax eXtention)
#### 1. class 태그 주고싶다면?
```javascript
    class (x) 예약어
    className 사용
    <div className = ""> </div>
```
#### 2. onClick
```javascript
    <div onclick=" 함수명 "> 기존js </div>
    <div onClick={ 함수명 }> react </div>

    !onclick이벤트에서 함수를 적을 때 소괄호 빼기!
    함수명() ==> 바로실행
    함수명 ==> 클릭 시 실행
```

## React 기본 사용
#### 1. 왜 App.js에 작성하는 걸까?
리액트의 장점. 데이터 바인딩이 쉬워진다 (react == angular == vue)

> 데이터 바인딩: 
> 서버에서 받아온 데이터를 html에 넣는 것
>   ```javascript
>   ...
>   import logo from './logo.svg';
>   ...
>   let 변수명 = 'Something'
>   function 함수() {
>     return 'Something'
>   }
>
>   document.getElementById().innerHTML = ''
>
>   <div>
>   { 변수명, 함수 }
>   </div>
>
>   <img src = { logo }>
>   //src,id,href등의 속성에도 가능
>
>   <div style = { { color : 'blue', fontSize : '30px' } }>
>   //object형식
>   //속성 font-size: - 연산자로 인식 => fontSize: camelCase로 작성
>   ```
index.html에 보여질 html코드를 app.js에 작성하여 index.js가 연결하여 보여줌

#### return 안에 하나의 html태그만 사용가능
연속된 태그 사용 불가, 태그 하나로 묶어서 사용하

## State
#### 1. state
리액트의 데이터 저장공간
자주 바뀌는 중요한 데이터는 state에 저장해 자동 렌더링이 이루어지도록 한다.

      데이터 저장 방식
      1. 변수에 저장
      2. state에 저장
 
#### state: 변수 대신 쓰는 데이터 저장공간

> 1. { useState }를 상단에 첨부       
> 2. useState(데이터);로 사용
> ```javascript
> import React, { useState } from 'react';
>
> let [데이터, 데이터변경함수] = useState(['','','']);
> //ES6 destructuring: Array, Object에 있는 함수를 변수에 담음
> //문자, 숫자, Array, Object 저장가능
> ```

#### 2. 왜?
웹이 app처럼 동작하게 만들수있음
=> 데이터가 변경될때 state로 만든 데이터는 html이 자동으로 재렌더링이 된다.  
##### * 그냥 변수 사용 시 데이터가 바뛰어도 재렌더링X 새로고침O
- 정렬, 추천 눌렀을 때 등 
- 자주 바뀌는 중요한 데이터는 state에 저장

#### 3. 데이터 변경
데이터 변경 함수를 호출하여 변경
#### state는 일반적인 방법으로 변경 불가 -> 두번째 인자 변경함수 사용
#### 변경함수를 사용해야 재렌더링이 잘 일어남

```javascript
<div onClick={ () => {데이터변경함수( 변경할 데이터 ) } }> react </div>
```

#### Array & Object state 데이터 수정
1. 기존 state의 복사본 생성
2. 복사본에서 수정사항 반영
3. 변경함수()에 복사본 데이터 사용

## Component
HTML을 한 단어로 주여서 쓸 수 있는 React 문법

만드는 기준
`반복 출현하는 HTML덩어리`
`자주 변경되는 HTML UI`
`페이지 구성`

장점 `관리가 편해짐`
    
단점 `state를 쓸 때 복잡` => `상위 component에서 만든 state를 쓰려면 props 문법 이용`

#### 
1.함수 만들고 이름짓기
2. 축약을 원하는 html을 넣고
3. 원하는 곳에서 <함수명/> 사용

#### 유의
1.이름은 대문자로 시작
2. 나란히 사용x return안에 있는 건 태그하나로 묶어야함
    =>의미없는 <div> 쓰기 싫으면 <></> : fragment




#### ❗리액트 대 원칙
immutatable: 원본 데이터를 변경하지 않고 복사본을 만들어 변경사항을 적용시킨다.

#### deep copy
Array, Object는 값 공유(reference data type)가 되기때문에 서로 독립적인 값을 가지도록 복사한다.

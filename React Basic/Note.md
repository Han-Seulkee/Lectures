# React

* App.js에 html/css 작성 - 메인페이지(index.html) 화면 구성

* index.js로 App.js ==> index.html 연결

* public folder: static 보관함

### JSX (Javascript Syntax eXtention)
#### 1. class 태그 주고싶다면?
```javascript
    class (x) 예약어
    className 사용
    <div className = ""> </div>
```
#### 2. onClick
```javascript
    <div onclick=" 함수 "> 기존js </div>
    <div onClick={ 함수 }> react </div>
```

### React 기본 사용
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

### State
#### 1. state
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
데이터변경함수를 호출하여 변경
#### state는 일반적인 방법으로 변경 불가 -> 두번째 인자 변경함수 사용
#### 변경함수를 사용해야 재렌더링이 잘 일어남

```javascript
<div onClick={ () => {데이터변경함수( 변경할 데이터 ) } }> react </div>
```

# React

* App.js에 html/css 작성 - 메인페이지(index.html) 화면 구성

* index.js로 App.js ==> index.html 연결

* public folder: static 보관함


## JSX (Javascript Syntax eXtention)
#### 1. class 태그 주고싶다면?
```javascript
    class (x) 예약어
    className 사용
    <div className = ""> </div>
```
#### 2. 왜 App.js에 작성하는 걸까?
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

wunderbar

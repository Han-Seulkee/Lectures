### [ReactJS로 영화 웹 서비스 만들기](https://nomadcoders.co/react-for-beginners)
React for Begginers
start 2024-02-06 

### Using React
#### make it easy to create component
* Vanilla JS

  add HTML tag -> find tag -> add Event Listener -> function definition

* React

  add element -> describe Event & function in props -> rendering elements

#### React JS & React DOM
`React JS`: make websites interactively

`React DOM`: take React element, turn into HTML

#### JSX
##### "createElement" => not use
createElement([Element], [Property], [Content])

```javascript
  const btn = React.createElement(
  "button",
  { onClick: () => console.log("Hi"),
    style {
      color: "red",
    },
  },
  "Click"
  );

const container = React.createElement("div",null,[btn]);

ReactDOM.render(container, root);
```

##### JSX: almost same as HTML => easy to read & understand  ! but browser can't read jsx

```javascript
  const root = document.getElementById("root");
  const Button = () => (
    <button style={{
      color: "red",
    }} onClick={() => console.log("Hi")}>
    "Click"
    <button/>
  );

  const Container = () => (
    <div>
      <Button />
    </div>
  );

  ReactDOM.render(<Container />, root);
```
###### put elements inside the function, use element as many times as we want

Babel: javascript compiler. transform jsx into javascript 

#### React Rule
First letter of Component SHOULD BE UPPERCASE

### State
#### modify data in react js
checking what was the previous component that was rendered

-> what is the next component is going to be render

-> realizes what is the only different part 

update the only thing that changed

### Props
#### the way that can send data from a parent component to a child component




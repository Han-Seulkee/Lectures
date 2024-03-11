## [ReactJS로 영화 웹 서비스 만들기](https://nomadcoders.co/react-for-beginners)
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

#### JSX: almost same as HTML => easy to read & understand  ! but browser can't read jsx

```javascript
const root = document.getElementById("root");
const Button = () => (
  <button style={{
    color: "red",
    }} onClick={() => console.log("Hi")}
  >
    Click
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

### React Rule
First letter of Component SHOULD BE UPPERCASE

### State
#### modify data in react js
checking what was the previous component that was rendered

-> what is the next component is going to be render

-> realizes what is the only different part 

-> update the only thing that changed

```javascript
const [data, setData] = React.useState("defaultValue");
setData("chage data");
```

### Props
#### props: the way that can send data from a parent component to a child component

```javascript
function Button (props/{text, click}) {        //<---almost using shortcuts. props = { object }
  return (
    <button
      style={{ color: "tomato" }},
      onClick={click}
    >
      {props.text}/{text}
    <button/>
  )
}

function App () {
const [value,setValue] = React.useState("Confirm");
const changeValue = () => setValue("Done");
  return(
    <div>
      <Button text="Confirm" click={changeValue}/>
      <Button text="Cancel" />
    </div>
  );
}
```

#### Memo
announce that don't re-render unchanged props
```javascript
const MemorizedBtn = React.memo(Button);
```

#### PropTypes
Displays a warning when sending the wrong props
```javascript
Button.propTypes = {
  text: PropTypes.string.isRequired,
  click: PropType.func
}
```

### Using CRA
#### simplifies the setup and development of react app
Divide code in deferent files, create CSS files for specific components
create-react-app can help you to access to the development server & automatically refresh

```bat
  npx create-react-app my-project-name
  code my-project-app (open in vscode)
  
  npm start <- run(create) development server

  npm i prop-types
```

### Effects
#### render/run a part of the code only once
### 👼

ReactJS refreshes the thing(component, UI) that changed

 `state change` => `re-render` => `all the code will run again`


### 🤔🤔🤔
#### all the code will run again
1. want to run the code only one time at the start
2. want to run the code on a specific time
3. want to run the code on a specific data in a component changes

#### useEffect
Choose when should the code run

```javascript
useEffect( , )        //1st: function, 2nd: dependencies(what react should watch to update)

const [keyword, setKeyword] = useState("");
const [count, setValue] = useState(0);

//1. watch nothing
useEffect(() => {
  console.log("this code will run only once at the first time");
}, []);

//2. watch one item
useEffect(() => {
  console.log("this code will run when 'keyword' changes");
}, [keyword]);

//3. watch two items
useEffect(() => {
  console.log("this code will run when 'keyword' & 'count' any of them changes");
}, [keyword, count]);
```

#### Cleanup
allows to do something when the component is being destroyed

define a cleanup funtion inside a effect function

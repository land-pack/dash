import React from "react";
import logo from "./logo.svg";
import mylogo from "./mylogo.svg";
import "./App.css";
import CV from "./cv";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={mylogo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
      <body className="App-body">
        <CV />
      </body>
    </div>
  );
}

export default App;

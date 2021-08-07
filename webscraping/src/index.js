import React from "react"
import ReactDOM from "react-dom"
import NavComponent from "./components/nav/NavComponent1"
import { BrowserRouter as Router, Switch, Route } from "react-router-dom"
import home from "./components/page/home"
import about from "./components/page/about"
import pricing from "./components/page/pricing"
import login from "./components/page/login"
import register from "./components/page/register"
import "./main.css"

let root = document.getElementById('root')

ReactDOM.render(
<Router>
    <NavComponent />
    <Switch>
        <Route path="/" exact component={home}/>
        <Route path="/about" component={about}/>
        <Route path="/pricing" component={pricing}/>
        <Route path="/login" component={login}/>
        <Route path="/register" component={register}/>
    </Switch>
</Router>,
root)

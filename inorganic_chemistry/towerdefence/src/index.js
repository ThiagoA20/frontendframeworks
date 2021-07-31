import React from "react"
import ReactDOM from "react-dom"
import PrimeiroComponente from "./components/PrimeiroComponente"
import SegundoComponente from "./components/SegundoComponente"

let root = document.getElementById('root')

ReactDOM.render(
    <div>
        <PrimeiroComponente />
        <SegundoComponente name="Darwin" />
        <SegundoComponente />
        <SegundoComponente name="Nikola Tesla" />
    </div>
, root)
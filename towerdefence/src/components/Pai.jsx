import React from "react"
import Filho from "./Filho"

export default props => {
    return <div>
        <h1>{props.name + " " + props.sobrenome}</h1>
        <ul>
            <Filho name="Albert" sobrenome="Einstein"/>
            <Filho name="Nikola" sobrenome="Tesla"/>
            <Filho name="Isaac" sobrenome="Newton"/>
        </ul>
    </div>
}

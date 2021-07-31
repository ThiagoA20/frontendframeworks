import React from "react"

export default props => {
    if (props.name == undefined) {
       return <h1>Vazio</h1>
    } else {
        return <h1>Olá{" " + props.name}</h1>
    }
}
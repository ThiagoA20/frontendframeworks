import React from "react"

export default function NavElement(props){
    return <h3 style={{
        height: "max-content",
    }}>{props.children}</h3>
}
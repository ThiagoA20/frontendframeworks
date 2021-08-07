import React from "react"
import NavElement from "./NavElement"
import { Link } from "react-router-dom"

export default function Account(){
    return <div style={{
        width: "240px",
        height: "max-content",
        display: "flex",
        flexDirection: "row",
        justifyContent: "space-between"
    }}>
        <Link to="/login" style={{textDecoration: "none", color: "black"}}><NavElement>Log in</NavElement></Link>
        <div style={{
            width: "166px",
            height: "50px",
            backgroundColor: "#2E2F2F",
            lineHeight: "13px",
            textAlign: 'center',
            verticalAlign: "middle",
            borderRadius: "10px",
        }}>
            <Link to="/register" style={{textDecoration: "none"}}>
                <h3 style={{
                    color: "#13E81D",
                    fontSize: "20px",
                }}>Get Started</h3>
            </Link>
        </div>
    </div>
}
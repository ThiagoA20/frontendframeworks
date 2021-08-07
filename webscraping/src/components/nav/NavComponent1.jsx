import React from "react"
import Logo from "../Logo"
import logo_image from "../../media/economy.png"
import NavElement from "../NavElement"
import Account from "../Account"
import { Link } from "react-router-dom"
import useState from 'react'

let img_pmt = {logo: logo_image, w: 55, h: 55, b: 2, br: 220}
let title_pmt = {text: "Finant", fontsz: 45}

export default function NavComponent() {
    return <div style={{
        width: "70%",
        height: "84px",
        marginLeft: "15%",
        marginRight: "15%",
        display: "flex",
        flexDirection: "row",
        justifyContent: "space-between",
        textAlign: "center",
        verticalAlign: "middle",
    }}>
        <Link to="/" style={{textDecoration: "none"}}><Logo direction="h" image={img_pmt} title={title_pmt}/></Link>
        <div style={{
            width: "400px",
            display: "flex",
            flexDirection: "row",
            justifyContent: "space-between"
        }}>
            <Link to="/about" style={{textDecoration: "none", color: "black"}}><NavElement>About us</NavElement></Link>
            <Link to="/pricing" style={{textDecoration: "none", color: "black"}}><NavElement>Services</NavElement></Link>
            <Link to="/pricing" style={{textDecoration: "none", color: "black"}}><NavElement>Pricing</NavElement></Link>
            <Link to="/pricing" style={{textDecoration: "none", color: "black"}}><NavElement>App</NavElement></Link>
        </div>
        <Account />
    </div>
}
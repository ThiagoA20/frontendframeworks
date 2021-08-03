import React from "react"

export default function Sprite({ image, data }) {
    const { y, x } = data
    return <div 
        style={{
        display: "inline-block",
        width: "32px",
        height: "32px",
        backgroundImage: `url(${image})`,
        backgroundRepeat: "no-repeat",
        backgroundPosition: `${x}px ${y}px`
        }}
    />
}

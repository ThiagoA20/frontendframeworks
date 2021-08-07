import React from 'react'

export default function Logo({ direction, image, title }) {
    const { logo, w, h, b, br } = image
    const { text, fontsz } = title
    if (direction == 'v') {
        return <div style={{
            width: "200px",
            height: "max-content",
            display: "flex",
            flexDirection: "column",
            justifyContent: "space-between",
        }}>
            <img src={logo} style={{
                width: `${w}px`,
                height: `${h}px`,
                border: `${b}px solid black`,
                borderRadius: `${br}px`,
            }}></img>
            <h1 style={{
                color: "#13E81D",
                WebkitTextStrokeWidth: "2.5px",
                WebkitTextStrokeColor: "#000",
                fontFamily: "ubuntu",
                fontSize: `${fontsz}px`,
                fontStyle: "italic",
                fontWeight: "500",
            }}>{text}</h1>
        </div>
    } else {
        return <div style={{
            width: "200px",
            height: "max-content",
            display: "flex",
            flexDirection: "row",
            justifyContent: "space-between",
        }}>
            <img src={logo} style={{
                width: `${w}px`,
                height: `${h}px`,
                border: `${b}px solid black`,
                borderRadius: `${br}px`,
            }}></img>
            <h1 style={{
                color: "#13E81D",
                WebkitTextStrokeWidth: "2.5px",
                WebkitTextStrokeColor: "#000",
                fontFamily: "ubuntu",
                fontSize: `${fontsz}px`,
                fontStyle: "italic",
                fontWeight: "bold",
            }}>{text}</h1>
        </div>
    }
}
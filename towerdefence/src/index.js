import React from "react"
import ReactDOM from "react-dom"
import Sprite from "./components/sprites"

let root = document.getElementById('root')

ReactDOM.render(
    <div className="zone-container">
        <Sprite 
        image={"./components/sprites/game_sprites/32/sprite32-2.png"}
        data={{
            x: 0,
            y: 0,
        }}
        />
    </div>
, root)
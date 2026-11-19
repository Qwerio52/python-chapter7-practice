import turtle
import json

track_data = {
    "type": "circle",
    "x": 0,
    "y": 0,
    "radius": 150,
    "color": "#2E86AB",
    "speed": 0
}

def draw_track(engine_data):
    t = turtle.Turtle()
    t.speed(engine_data["speed"])
    t.color(engine_data["color"])
    t.penup()
    t.goto(engine_data["x"], engine_data["y"] - engine_data["radius"])
    t.pendown()
    t.circle(engine_data["radius"])
    turtle.done()

if __name__ == "__main__":
    draw_track(track_data)
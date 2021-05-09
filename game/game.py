import pyglet
import pyglet.gl as pgl

pgl.glEnable(pgl.GL_BLEND)
pgl.glBlendFunc(pgl.GL_SRC_ALPHA, pgl.GL_ONE_MINUS_SRC_ALPHA)

window = pyglet.window.Window()
label = pyglet.text.Label(
    "This is a game",
    font_name="Times New Roman",
    font_size=36,
    x=window.width // 2,
    y=window.height // 2,
    anchor_x="center",
    anchor_y="center",
)
alienBeige = pyglet.sprite.Sprite(pyglet.image.load("../assets/alienBeige.png"))


@window.event
def on_draw():
    window.clear()
    label.draw()
    alienBeige.draw()


pyglet.app.run()

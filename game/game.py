import pyglet
from pyglet.gl import glEnable
from pyglet.gl import glBlendFunc
from pyglet.gl import GL_BLEND
from pyglet.gl import GL_SRC_ALPHA
from pyglet.gl import GL_ONE_MINUS_SRC_ALPHA
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

window = pyglet.window.Window()
label = pyglet.text.Label("This is a game",
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
alienBeige = pyglet.sprite.Sprite(pyglet.image.load('../assets/alienBeige.png'))

@window.event
def on_draw():
    window.clear()
    label.draw()
    glEnable(GL_BLEND)
    alienBeige.draw()

pyglet.app.run()
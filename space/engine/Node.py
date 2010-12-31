from OpenGL.GL import glTranslatef, glRotatef, glScalef, glPushMatrix, glPopMatrix

from Vector2D import Vector2D

class Node(object):
    def __init__(self, world):
        object.__init__(self)
        self.position = Vector2D()
        self.scale    = Vector2D(1.0, 1.0)
        self.rotation = 0.0
        self.world    = world
        self._children = []
        self.move = Vector2D()

    def add(self, child):
        self._children.append(child)

    def remove(self, child):
        self._children.remove(child)

    def update(self, elapsed):
        self.position += self.move
        for child in self._children:
            child.update(elapsed)

    def render(self):
        glTranslatef(self.position.x, self.position.y, 0.0)
        glRotatef(self.rotation, 0.0, 0.0, 1.0)
        glScalef(self.scale.x, self.scale.y, 0.0)

        for child in self._children:
            glPushMatrix()

            child.render()

            glPopMatrix()

        self.draw()

    def draw(self):
        raise NotImplementedError()


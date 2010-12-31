from OpenGL.GL import glLoadIdentity
from Node import Node
from Vector2D import Vector2D

class RootNode(Node):
    def draw(self):
        pass

class World(object):
    def __init__(self):
        object.__init__(self)
        self.__root = RootNode(self)

    def __getroot(self):
        return self.__root
    
    root = property(__getroot)

    def update(self, elapsed):
        self.root.update(elapsed)

    def render(self):
        glLoadIdentity()

        self.root.render()


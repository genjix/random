from Vector2D import Vector2D
from Node import Node

class VerletNode(Node):
    def __init__(self, world):
        Node.__init__(self, world)
        self.last_position = self.position
        self.last_rotation = self.rotation
        self.acceleration = Vector2D()

    def accumulate(self):
        pass

    def constrain(self):
        pass

    def update(self, elapsed):
        self.accumulate()

        old_position = Vector2D(self.position.x, self.position.y)
        self.position += self.position - self.last_position + self.acceleration * elapsed * elapsed
        self.last_position = old_position

        # XXX: not sure if this is correct ...
        old_rotation = self.rotation
        self.rotation += self.rotation - self.last_rotation + elapsed * elapsed
        self.last_rotation = old_rotation

        self.constrain()

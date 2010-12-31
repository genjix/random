import pygame

from OpenGL.GL import (
        glClearColor,
        glDisable,
            GL_DEPTH_TEST, GL_CULL_FACE, GL_LIGHTING, GL_TEXTURE_2D,
        glMatrixMode,
            GL_PROJECTION, GL_MODELVIEW,
        glLoadIdentity,
        glOrtho,
        glClear,
            GL_COLOR_BUFFER_BIT,
)

class GraphicsDevice(object):
    DEFAULT_WIDTH = 800
    DEFAULT_HEIGHT = 600

    def __init__(self, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT):
        object.__init__(self)

        resolution = (width, height)
        flags      = pygame.HWSURFACE | pygame.OPENGL | pygame.DOUBLEBUF
        pygame.display.set_mode(resolution, flags, 0)
        
        glClearColor(0.0, 0.0, 0.0, 1.0)

        glDisable(GL_DEPTH_TEST)
        glDisable(GL_CULL_FACE)
        glDisable(GL_LIGHTING)
        glDisable(GL_TEXTURE_2D)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, width, height, 0, 0, 1)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def clear(self):
        glClear(GL_COLOR_BUFFER_BIT)

    def flip(self):
        pygame.display.flip()


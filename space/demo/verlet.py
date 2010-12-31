#!/usr/bin/env python

import sys, math
import os

# XXX: path hack because I'm too lazy to look up Win32
#      batch file syntax
sys.path += [os.path.join(os.path.dirname(__file__), '..')]

from engine import Vector2D, Node, GraphicsDevice, World, Engine, VerletNode
from random import random
import pygame
from OpenGL.GL import (
        glDisable, glEnable,
            GL_CULL_FACE, GL_DEPTH_TEST, GL_LIGHTING, GL_TEXTURE_2D,
        glMatrixMode,
            GL_PROJECTION, glOrtho,
            GL_MODELVIEW,
        glLoadIdentity,
        glClearColor, glClear,
            GL_COLOR_BUFFER_BIT,
        glBegin, glEnd,
            GL_TRIANGLES, GL_TRIANGLE_FAN,
            glColor3f, glVertex2f, glTexCoord2f
)

APP_NAME = 'lkddsklsdml'
APP_VERSION = '0.01'

class MyNode(VerletNode):
    def __init__(self, mass, world):
        VerletNode.__init__(self, world)
        self.push = Vector2D()
        #self.trumass = mass
        self.mass = mass

    def accumulate(self):
        self.acceleration = self.push
        nlen = len(self.world.root._children)
        i = 0
        while i < nlen:
            c = self.world.root._children[i]
            i += 1
            if c == self:
                continue
            dir = c.position - self.position
            dist = dir.magnitude()
            dir = dir.normalize()
            G = 20000
            proportions = c.mass / self.mass
            if dist < self.mass*30:
                # add mass to ourselves
                # do reaction acc
                self.acceleration += c.acceleration * proportions
                self.acceleration /= 2.0
                self.mass += c.mass
                #self.trumass += c.trumass
                #self.last_position += c.last_position
                #self.last_position /= 2.0
                #self.rotation += c.rotation
                #self.rotation /= 2.0
                #self.last_rotation += c.last_rotation
                #self.last_rotation /= 2.0
                self.world.root._children.remove(c)
                nlen -= 1
            else:
                self.acceleration += dir * G * c.mass * self.mass * proportions / dist
        self.push = Vector2D()
        #accmag = self.acceleration.magnitude()
        #if accmag > 15:
        #    self.acceleration /= (accmag - 15)

    def constrain(self):
        pass
        """if self.position.x > 800.0:
            self.position.x = 800.0
        elif self.position.x < 0.0:
            self.position.x = 0.0

        if self.position.y > 600.0:
            self.position.y = 600.0

            # also stop it dead in its tracks ... 
            self.last_position.x = self.position.x
            self.last_rotation = self.rotation
        elif self.position.y < 0.0:
            self.position.y = 0.0"""

    def draw(self):
        size = self.mass
        if size < 0.2:
            size = 0.2
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(1.0, 0.0, 0.0)
        """glVertex2f(-self.mass, -self.mass)
        glColor3f(0.0, 1.0, 0.0)
        glVertex2f(0.0, self.mass)
        glColor3f(0.0, 0.0, 1.0)
        glVertex2f(self.mass, -self.mass)"""
        glVertex2f(0.0, 0.0)
        glColor3f(0.0, 1.0, 0.0)
        for angle in xrange(0,370,10):
            glVertex2f(math.sin(angle)*size, math.cos(angle)*size)
        glEnd()

def mainloop(device):
    world = World()

    finished = False
    clock = pygame.time.Clock()
    begin_motion = Vector2D(0.0, 0.0)
    end_motion = Vector2D(0.0, 0.0)
    #font = pygame.font.Font(None, 36)
    #text = font.render("Pummel The Chimp, And Win $$$", 1, (10, 10, 10))
    bigbody = True
    move = 6
    
    while not finished:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                finished = True
                break
            elif e.type == pygame.KEYDOWN:
                sc = world.root.scale.x
                if e.key == pygame.K_PAGEDOWN:
                    world.root.scale *= 0.9
                elif e.key == pygame.K_PAGEUP:
                    world.root.scale *= 1.1
                elif e.key == pygame.K_DOWN:
                    world.root.move.y -= move*sc
                elif e.key == pygame.K_UP:
                    world.root.move.y += move*sc
                elif e.key == pygame.K_LEFT:
                    world.root.move.x += move*sc
                elif e.key == pygame.K_RIGHT:
                    world.root.move.x -= move*sc
                elif e.key == pygame.K_SPACE:
                    bigbody = not bigbody
                elif e.key == pygame.K_TAB:
                    move += 2/sc
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_DOWN:
                    world.root.move.y = 0
                elif e.key == pygame.K_UP:
                    world.root.move.y = 0
                elif e.key == pygame.K_LEFT:
                    world.root.move.x = 0
                elif e.key == pygame.K_RIGHT:
                    world.root.move.x = 0
            elif e.type == pygame.MOUSEBUTTONDOWN:
                sc = world.root.scale.x
                begin_motion = (Vector2D(e.pos[0], e.pos[1]) - world.root.position)/sc
            elif e.type == pygame.MOUSEBUTTONUP:
                sc = world.root.scale.x
                end_motion = (Vector2D(e.pos[0], e.pos[1]) - world.root.position)/sc

                # arbitrary constant to give it a little more oomph :)
                motion = (end_motion - begin_motion) * 50

                mass = 1
                if not bigbody:
                    mass = 0.1
                node = MyNode(mass, world)
                node.position = (Vector2D(e.pos[0], e.pos[1]) - world.root.position)/sc
                node.last_position = node.position
                node.scale = Vector2D(40.0, 40.0)
                node.push = motion

                world.root.add(node)

        """for n in world.root._children:
            n.mass = 0
            for c in n.world.root._children:
                if c == n:
                    continue
                dist = (c.position - n.position).magnitude() / 100.0
                n.mass += n.trumass/math.e**dist
            n.mass /= len(world.root._children) + 0.01"""

        device.clear()
        world.update(clock.tick(60) / 1000.0)
        world.render()
        device.flip()
        pygame.time.wait(0)

def main():
    Engine.initialize(APP_NAME, APP_VERSION)

    device = GraphicsDevice()
    mainloop(device)

    Engine.finalize()
    return 0

if __name__ == '__main__':
    main()


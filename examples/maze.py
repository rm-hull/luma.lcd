#!/usr/bin/env python
#
# Maze generator example for RPi-PCD8544
#
# Adapted from:
#    https://github.com/rm-hull/maze/blob/master/src/maze/generator.clj

#import pcd8544.lcd as lcd
#from PIL import Image,ImageDraw
from random import randrange

NORTH=1
WEST=2

class Maze:

    def __init__(self, width, height):
        self.size = width * height
        self.width = width
        self.height = height
        self.generate()

    def __getitem__(self, x, y):
        return self.data[self.offset(x, y)]

    def offset(self, x, y):
        """ Converts [x,y] co-ords into an offset in the maze data """
        return ((y % self.height) * self.width) + (x % self.width)

    def neighbours(self, pos):
        neighbours = []

        if pos > self.width:
            neighbours.append(pos - self.width)

        if pos % self.width > 0:
            neighbours.append(pos - 1)

        if pos % self.width < self.width - 1:
            neighbours.append(pos + 1)

        if pos + self.width < self.size:
            neighbours.append(pos + self.width)

        return neighbours

    def is_wall_between(self, p1, p2):
        """ Checks to see if there is a wall between two (adjacent) points
            in the maze. The return value will indicate the wall type
            (:north, :west,..). If the points aren't adjacent, false is
            returned. """
        if p1 > p2:
            return self.is_wall_between(p2, p1)

        if p2 - p1 == self.width:
            return self.data[p2] & NORTH != 0

        if p2 - p1 == 1:
            return self.data[p2] & WEST != 0

        return false;

    def knockdown_wall(self, p1, p2):
        """ Knocks down the wall between the two given points in the maze.
            Assumes that they are adjacent, otherwise it doesn't make any
            sense (and wont actually make any difference anyway) """
        if p1 > p2:
            return self.knockdown_wall(p2, p1)
        if p2 - p1 == self.width:
            self.data[p2] &= WEST

        if p2 - p1 == 1:
            self.data[p2] &= NORTH

    def generate(self):
        self.data = [ NORTH | WEST ] * self.size
        visited = { 0: True }
        stack = [0]
        not_visited = lambda x: not visited.get(x, False)

        while len(stack) > 0:
            curr = stack[-1]
            n = filter(not_visited, self.neighbours(curr))
            sz = len(n)
            if sz == 0:
                stack.pop()
            else:
                np = n[randrange(sz)]
                self.knockdown_wall(curr, np)
                visited[np] = True
                if sz == 1:
                    stack.pop()
                stack.append(np)

    def to_string(self):
        s = ""
        for y in xrange(self.height):
            for x in range(self.width):
                s += "+"
                if self.data[self.offset(x,y)] & NORTH != 0:
                    s += "---"
                else:
                    s += "   "
            s += "+\n"
            for x in range(self.width):
                if self.data[self.offset(x,y)] & WEST != 0:
                    s += "|"
                else:
                    s += " "
                s += "   "
            s += "|\n"
        s += "+---" * self.width
        s += "+\n"

        return s

if __name__ == "__main__":
    m = Maze(18,20)
    print m.to_string()

from struct import pack
import math

PPF = 800 # Points per frame

class Frame():
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def get_points(self):
        points = []
        lengths = [x.get_length() for x in self.shapes]
        total_length = sum(lengths)
        for i, length in enumerate(lengths):
            point_count = round(length/total_length*PPF)
            points += self.shapes[i].get_points(point_count)
        return points

    def get_pcm(self):
        data = b""
        for x,y in self.get_points():
            x = x - 32768
            y = y - 32768
            data += pack("<hh", y, x)
        return data

class Line():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_length(self):
        return ((self.x1-self.x2)**2+(self.y1-self.y2)**2)**0.5

    def get_points(self, point_count):
        points = []
        dx = (self.x2-self.x1)/point_count
        dy = (self.y2-self.y1)/point_count
        for i in range(point_count):
            x = int(self.x1 + dx * i)
            y = int(self.y1 + dy * i)
            points.append((x,y))
        return points

class Arc():
    def __init__(self, x, y, radius, start, end):
        self.x = x
        self.y = y
        self.radius = radius
        self.start = start
        self.end = end

    def _get_arc_size(self):
        return self.end-self.start

    def get_length(self):
        return 2 * math.pi * self.radius * (abs(self._get_arc_size()) / 360)

    def get_points(self, point_count):
        points = []
        d_angle = self._get_arc_size() / point_count
        for i in range(point_count):
            angle = self.start + d_angle * i
            x = int(self.x + self.radius * math.cos(math.radians(angle)))
            y = int(self.y + self.radius * math.sin(math.radians(angle)))
            points.append((x, y))
        return points

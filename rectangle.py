from pyscopelib import *
from sys import stdout
from fps import FPS

fps = FPS(60)

rect = Rectangle(0, 0, 65535, 65535)

while True:
    f = Frame()
    f.add_shape(rect)
    stdout.buffer.write(f.get_pcm())
    fps.sleep()

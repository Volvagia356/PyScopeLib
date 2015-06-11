from pyscopelib import *
from sys import stdout
from fps import FPS

fps = FPS(60)

f = Frame()

f.add_shape(Line(0, 65535, 32768, 0))
f.add_shape(Line(32768, 0, 65535, 65535))
f.add_shape(Line(65535, 65535, 0, 65535))

while True:
    stdout.buffer.write(f.get_pcm())
    fps.sleep()

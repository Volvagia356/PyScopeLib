from pyscopelib import *
from sys import stdout
from fps import FPS

fps = FPS(60)

deg_per_frame = 8
arc = Arc(32768, 32768, 16384, 0, 0)

while True:
    f = Frame()
    f.add_shape(arc)
    stdout.buffer.write(f.get_pcm())
    if arc.start >= 360:
        arc.start = 0
        arc.end = 0
    elif arc.end >= 360:
        arc.start += deg_per_frame
    elif arc.start <= 0:
        arc.end += deg_per_frame
    fps.sleep()

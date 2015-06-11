from pyscopelib import *
from sys import stdout
from fps import FPS

fps = FPS(60)

f = Frame()

f.add_shape(Line(28160, 21760, 10240, 25600))
f.add_shape(Line(19968, 24064, 19968, 43519))
f.add_shape(Line(8704, 31744, 30720, 31744))

f.add_shape(Line(37119, 23039, 53759, 23039))
f.add_shape(Line(53759, 23039, 53759, 31488))
f.add_shape(Line(53759, 31488, 37119, 31488))
f.add_shape(Line(37119, 31488, 37119, 23039))
f.add_shape(Line(37119, 25600, 53759, 25600))
f.add_shape(Line(45567, 31488, 45567, 43519))
f.add_shape(Line(34559, 37119, 56319, 37119))

while True:
    stdout.buffer.write(f.get_pcm())
    fps.sleep()

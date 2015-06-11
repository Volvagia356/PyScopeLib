from time import time, sleep

class FPS():
    
    def __init__(self, fps):
        self.fps = fps
        self.frame_time = 1/fps
        self.last_time = None

    def sleep(self):
        if self.last_time:
            time_elapsed = time() - self.last_time
            if time_elapsed < self.frame_time:
                sleep_time = self.frame_time - time_elapsed
                sleep(sleep_time)
        self.last_time = time()

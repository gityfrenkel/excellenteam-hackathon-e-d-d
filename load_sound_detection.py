import sounddevice as sd
import numpy as np

duration = 100  # seconds

volume = 0
def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata) * 10
    volume = (int(volume_norm))
    print(volume)

def a():
    with sd.Stream(callback=print_sound):
        sd.sleep(duration * 5)
    return volume


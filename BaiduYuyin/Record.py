#!/usr/bin/env python
#encoding=utf-8

import pyaudio
import wave
import datetime
import sys
sys.path.append("..")
import setting

CHUNK = setting.CHUNK
CHANNELS = setting.CHANNELS
RATE = setting.RATE
RECORD_SECONDS = setting.RECORD_SECONDS
WAVE_OUTPUT_FILENAME = "Temp/output.wav"

FORMAT = pyaudio.paInt16
p = pyaudio.PyAudio()
def record():
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    print("* recording")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("* done recording")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
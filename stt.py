from vosk import KaldiRecognizer, Model, SetLogLevel
from sounddevice import RawInputStream
from queue import Queue
from json import loads

SetLogLevel(-1)
model = Model("path to your model")                   # here we assign a language model for speech recognition
q = Queue()


def q_callback(indata, frames, time, status):
    q.put(bytes(indata))                                        # creates the data to be read


def kozak_listen(callback):
    with RawInputStream(samplerate=48000, blocksize=8000, device=1, dtype='int16',
                        channels=1, callback=q_callback, latency="low"):
        rec = KaldiRecognizer(model, 48000)
        while True:
            data = q.get()
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                callback(loads(rec.Result())["text"])                # returns results to callback function


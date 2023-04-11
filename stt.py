from vosk import KaldiRecognizer, Model, SetLogLevel
from torch.hub import download_url_to_file
from sounddevice import RawInputStream
from queue import Queue
from json import loads
from os.path import isfile, splitext
from zipfile import ZipFile

SetLogLevel(-1)                                                                 
q = Queue()

model_check = "vosk-model-uk-v3\\vosk-model-uk-v3\\am\\final.mdl"
model_file_zip = "vosk-model-uk-v3.zip"

if not isfile(model_check):
    download_url_to_file('https://alphacephei.com/vosk/models/vosk-model-uk-v3.zip', model_file_zip)
    
    with ZipFile(model_file_zip, "r") as f:
        f.extractall(splitext(model_file_zip)[0])
        
model = Model("vosk-model-uk-v3\\vosk-model-uk-v3")


def q_callback(indata, frames, time, status):
    q.put(bytes(indata))


def kozak_listen(callback):
    with RawInputStream(samplerate=48000, blocksize=8000, device=1, dtype='int16',
                        channels=1, callback=q_callback, latency="low"):
        rec = KaldiRecognizer(model, 48000)
        while True:
            data = q.get()
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                    callback(loads(rec.Result())["text"])


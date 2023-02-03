from torch import device, set_num_threads
from torch.hub import download_url_to_file
from torch.package import PackageImporter
from sounddevice import play, stop
from time import sleep
from os import path

language = 'ua'
model_id = 'v3_ua'                          # determination of the necessary parameters
device = device('cpu')
set_num_threads(8)

local_file = "ua_voice_pt"

if not path.isfile(local_file):         # check whether voice model is already installed, and if not, then it will be
    download_url_to_file('https://models.silero.ai/models/tts/ua/v3_ua.pt', local_file)                   # installed

model = PackageImporter(local_file).load_pickle("tts_models", "model")

model.to(device)

sample_rate = 48000
speaker = 'mykyta'
example_text = "ай"


def kozak_speak(what):
    audio = model.apply_tts(text=what,
                            speaker=speaker,                         # speaker function
                            sample_rate=sample_rate)

    play(audio, sample_rate)
    sleep((len(audio) / sample_rate) + 0.5)
    stop()

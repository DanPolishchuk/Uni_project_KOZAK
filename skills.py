from string import capwords
from telegram_credentials import client
from tts import kozak_speak
from requests import get
from bs4 import BeautifulSoup as bs
from re import sub
from random import choice
from os import system, startfile
from datetime import datetime
from starting import jokes_db, apps
from num2words import num2words
from webbrowser import open

############################################ all curent assistent functions ###########################################


def wiki(endpoint):
    kozak_speak("Почекай будь ласка, я перевіряю інформацію, якщо я не відповім то інформацію я не знайшов")
    url = "".join(["https://uk.wikipedia.org/wiki/" + capwords(endpoint)])    # creates final endpoint
    req = get(url)
    soup = bs(req.text, "html.parser")
    results = soup.find("div", id="mw-content-text").find_all("p", limit=3)   # getting info from wikipedia
    for i in results:
        text = sub("\(МФА.+\)|́", "", i.get_text())                            # replaces unwanted elements
        if text.startswith(f'{endpoint.split()[0].capitalize()} '):
            kozak_speak(text)


async def send_message(whom, what):
    await client.send_message(whom, what)  # sends a message to assigned user or group


def jokes():
    kozak_speak("Добре, тоді слухай..")
    kozak_speak(choice(jokes_db))                                            # takes a random joke to be represented


def musics():
    kozak_speak("Насолоджуйся друже...")
    system('C:\\Users\\danpl\\Music\\Playlists\\Music.wpl')                # turns on music if there are some installed


def current_time():
    hour = num2words(datetime.now().hour, lang="uk")
    minutes = num2words(datetime.now().minute, lang="uk")         # defines current time and translates numbers to text
    kozak_speak(f"Зараз {hour} годин, {minutes} ")


def open_smt(what):
    if what in apps["app"].keys():
        kozak_speak("Гаразд, зараз все буде...")
        startfile(apps["app"][what])
    elif what in apps["website"].keys():                          # opens wanted app or tool
        kozak_speak("Гаразд, зараз все буде...")
        open(apps["website"][what])
    else:
        kozak_speak("Є два варіанти, або я не можу це зробити або ти не правильно сказав команду, хахахахаха.....")


def weather_now():
    kozak_speak("Секундочку, дай гляну...")
    url = "https://www.gismeteo.ua/ua/weather-ludwigshafen-am-rhein-2669/now/"
    req = get(url, headers={
                            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/51.0.2704.103 Safari/537.36"
                            })   # uses random client to avoid connection abort
    soup = bs(req.text, "html.parser")
    temp = soup.find("span", class_="unit_temperature_c").get_text()     # getting current weather
    final_temp = num2words(temp, lang="uk")
    if "+" in temp:
        kozak_speak(f"У твоєму місті зараз плюс {final_temp}...")
    if "-" in temp:
        kozak_speak(f"У твоєму місті зараз мінус {final_temp}...")

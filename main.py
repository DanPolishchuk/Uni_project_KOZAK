from skills import wiki, send_message, jokes, musics, current_time, open_smt, weather_now
from urllib.request import urlopen
from urllib3 import disable_warnings
from telethon.errors.rpcerrorlist import InputUserDeactivatedError
from telegram_credentials import client
from stt import kozak_listen
from tts import kozak_speak
from starting import end, joke, open_something, msg_how, msg, time, music, wikipedia, start, question1, \
                     question2, weather

####################################### Preparation functions ########################################################

disable_warnings()
contacts = {}
names = []


async def get_contacts():
    async for contact in client.iter_dialogs():         # getting dialog information from connected Telegram account
        contacts[contact.title] = contact.id             # for further usage


def list_of_names():
    for i in contacts.keys():                           # creating a list, that contains names of all chats
        names.append(i)


def connect():
    try:
        urlopen('http://google.com')                    # check internet connection
        return True
    except:
        return False

######################################### Execution begins here #######################################################


def kozak(voice: str):
    try:
        print(voice)
        if voice.startswith(start):
            kozak_speak("Здоровенькі були..Чим зможу бути корисним?")

        if voice.startswith(msg):
            if connect():                               # checks internet connection to avoid connection error
                kozak_speak("Як, кому, та що мені відправити? Але говори чітко бо я не зможу "
                            "зрозуміти кому відправити")
            else:
                kozak_speak("Схоже ти не підключенний до інтернету, без нього повідомлення не відправиться")

        if voice.startswith(msg_how):
            for x in msg_how:
                voice = voice.replace(x, "").strip()
                for name in names:
                    voice = voice.capitalize()
                    if voice.startswith(str(name)):
                        contact = contacts[name]
                        voice = voice.replace(name, "").strip()
                        send_message(contact, voice)
                        with client:
                            client.loop.run_until_complete(send_message(contact, voice))
                        kozak_speak("Виконав, що далі?")

        if voice.startswith(wikipedia):
            if connect():                                  # checks internet connection to avoid connection error
                for x in wikipedia:
                    voice = voice.replace(x, "").strip()
                wiki(voice)
            else:
                kozak_speak("Схоже ти не підключенний до інтернету, без нього я не можу шукати інформацію, вибач")

        if voice.startswith(joke):
            jokes()

        if voice.startswith(music):
            musics()

        if voice.startswith(time):
            current_time()

        if voice.startswith(open_something):
            for x in open_something:
                voice = voice.replace(x, "").strip()
            open_smt(voice)

        if voice.startswith(question1):
            kozak_speak("Я кіберкозак, мене створив Даня Поліщук, у мій вільний від служіння йому час я полюбляю "
                        "взламувати російські сайти та банки, і переводити кошти на ЗеСеУ...")

        if voice.startswith(question2):
            kozak_speak("Мої можливості обмеженні лише уявою мого творця, наразі я можу відсилати повідомлення в "
                        "телеграмі, отримувати інформацію з вікіпедії, росказувати анекдоти, відкривати дуякі "
                        "програми, вмикати музику, дізнаватись погоду та повідомляти котра година..")

        if voice.startswith(end):
            kozak_speak("Як скажеш, розбудиш мене якщо ще знадоблюсь, бувай..")
            exit()

        if voice.startswith(weather):
            weather_now()

    except ValueError:
        kozak_speak("Підсядь ближче бо не чую")

    except TypeError:
        kozak_speak("Повтори для мене, бо я глухий")

    except KeyError:
        kozak_speak("Або ти щось не те сказав або я не зрозумів, а ну ж бо, повтори")

    except RuntimeWarning:
        print("")

    except InputUserDeactivatedError:
        print("")


if __name__ == "__main__":                        # application start point
    if connect():                                 # checks internet connection to avoid connection error
        with client:
            client.loop.run_until_complete(get_contacts())
        list_of_names()
    print(names)
    print(contacts)
    kozak_speak("Козак готовий...")
    kozak_listen(kozak)

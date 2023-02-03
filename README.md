KOZAK

It is a voice assistant, now available only on Ukrainian language, later I will add English version as well.

Steps to set up this application:

1. Run "pip install -r requirements.txt" command

2. You would need to visit www.my.telegram.org website, create there an account and retrieve API ID and API hash, 
after that, paste them into telegram_credentials file.

3. You have to follow this link https://alphacephei.com/vosk/models, and download Ukrainian language module, 
now 4 different sizes are available, speed and quality of application depends on which one you will choose.
After you have downloaded a model, you will need to unpack a file, and add it to the same directory where all files of application are located, 
and update stt.py file, to match the language model name.

4. During the first application start, you will need to provide your phone number, associated with your telegram account, 
and text code sent to your account after typing your phone number. That is only mandatory during first run.

5. The main features are sending messages via telegram using only your voice, obtaining info from Wikipedia based on your query, 
but there are some another possibilities as well, feel free to explore skills.py, starting.py and main.py, 
there you will find out all stuff that KOZAK can execute, have a fun

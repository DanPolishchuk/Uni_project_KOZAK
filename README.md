# Uni_project_KOZAK
It`s a voice assistant, now available only on ukrainian language, later i will add english version as well.

Steps to set up this application:

1. You would need to visit www.my.telegram.org website, create there an account and retrieve api id and api hash, 
after that paste them into telegram_credentials file.

2. You have to follow this link https://alphacephei.com/vosk/models , and download ukrainian language module, 
now 4 different sizes are available,speed and quolity of application depends on which one you will choose.
After you`ve downloaded a model, you will need unpack a file, and add it to the same directory where all files of application are located, 
and update stt.py file,to match the language model name.

3. During first application start, you will need to provide your phone number, associated with your telegram account, 
and text code sent to your account after typing your phone number. That`s it, it`s only mandatory during first run.

4. The main feautures are sending messages via telegram using only your voice, obtaining info from wikipedia based on your query, 
but there are some another possibilities as well, feel free to explore skills.py, starting.py and main.py, 
there you will find out all stuff that KOZAK can execute, have a fun

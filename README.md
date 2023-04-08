KOZAK

It is a voice assistant, now available only on Ukrainian language, later I will add English version as well.

Steps to set up this application:

1. Run "pip install -r requirements.txt" command

2. You would need to visit www.my.telegram.org website, create there an account and retrieve API ID and API hash, 
after that, paste them into telegram_credentials file.

3. During the first application start, you will need to provide your phone number, associated with your telegram account, 
and text code sent to your account after typing your phone number. That is only mandatory during first run.

4. The main features are sending messages via telegram using only your voice, obtaining info from Wikipedia based on your query, 
but there are some another possibilities as well, feel free to explore skills.py, starting.py and main.py, 
there you will find out all stuff that KOZAK can execute, have a fun

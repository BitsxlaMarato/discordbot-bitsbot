# BitsBot
Discord bot assistant for BitsxLaMarató2020 online edition

## Set Up
First of all copy the enviroment:
```
cp .env.template .env
```

Open the enviroment file, and set up the discord and dropbox tokens:
```
vim .env
```

Create a python enviroment with virtualenv:
```
virtualenv env --python=python3
source env/bin/activate
```

Install de requirements:
```
pip install -r requirements.txt
```

Enjoy the bot and add it to a server:
```
python bot.py
```

Enter a random channel and start spamming [COMMAND_PREFIX]biene !!

## Deploy
In order to deploy to heroku, you must connect it to an heroku app and then activate the free dynos and then set up your enviroment variables.
For more info check this awesome [Tutorial](https://dev.to/p014ri5/making-and-deploying-discord-bot-with-python-4hep) 

## List of commands
List of all the commands with the COMMAND_PREFIX

### Random commands
Can only be sent on MEMES_CHANNEL, RANDOM_CHANNEL and ORGANIZER_CHANNEL, have a 10 second cooldown in order to stop spam.
```
parrot
dog
cat
biene
ping
joke
parJoke
proJoke
```

### Hacker commands
Commands in order to help hackers join their team
```
help
login [email]
createTeam [teamName]
addToTeam [@user]
```

### Admin commands
Commands to make the organization easier
```
info [@user]
email [@user]
clearYesImSure
loginEmails
```

## Author
Made with :heart:

Special thanks to [LoBot](https://github.com/LleidaHack/hackeps-2020-discordbot)

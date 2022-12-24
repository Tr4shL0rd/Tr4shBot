# Discord Bot

This is a Discord bot built using the Discord Python library. It can respond to various commands and provide information such as dog and cat facts, greetings, and weather information.

## Table of Contents

- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [OpenWeatherMap api key](#openweathermap-api-key)
- [Todo](#todo)
- [Known Glitches](#known-glitches)
- [Credits](#credits)

## Requirements

* [Python](www.python.org) 3.9 or higher
* [Discord account](www.discord.com) account and [Discord bot token](https://discord.com/developers/applications)
* [OpenWeatherMap](#openweathermap-api-key) api key

## Setup

    Clone this repository: git clone https://github.com/Tr4shL0rd/Tr4shBot
    Navigate to the project directory: cd discord-bot
    Create a virtual environment and activate it: python3 -m venv venv and source venv/bin/activate
    Install the required packages: pip install -r requirements.txt
    Create a .env file in the project directory and add your Discord bot token: echo TOKEN=your-bot-token > .env
    Run the bot: python bot.py

## Usage

The bot can respond to the following commands:

    !ping: The bot will respond with "pong"
    Greetings (e.g. "!hello", "!hi", "!hey"): The bot will respond with a greeting and the name of the person who sent the message
    !dogfact or !dog-fact: The bot will provide a random dog fact
    !catfact or !cat-fact: The bot will provide a random cat fact
    !weather [city]: The bot will provide weather information for the specified city. If no city is provided, the default city is "Esbjerg".

### OpenWeatherMap api key
    Go to the OpenWeatherMap website and click on the "Sign Up" button in the top right corner.
    Fill out the registration form and click on the "Sign Up" button.
    After completing the registration, you will be redirected to the dashboard.
    In the dashboard, click on the "API keys" tab.
    Click on the "Generate" button to generate a new API key.
    Copy the generated API key and save it in a secure location. You will use this key to authenticate your API requests.

## Todo 

* [ ] Add better commenting for the code
* [ ] Host the bot on a raspberry pi
* [ ] Restructure the project 
* [ ] refactor code to use on_raw_message_\*() instead of on_message_\*()

## Known Glitches



## Credits

* [Discord Python library](https://discordpy.readthedocs.io/en/stable/)
* [GeoPy library](https://geopy.readthedocs.io/en/stable/)
* [openweathermap API](https://openweathermap.org/)
* [kinduff's dog API](https://dogapi.dog/)
* [meowfacts API](https://github.com/wh-iterabb-it/meowfacts)
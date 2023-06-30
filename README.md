# Discord Selfbot for Light Control

This Discord selfbot written in Python allows you to control your lights through Discord. It integrates with the Philips Hue lighting system and enables you to change the colors of your lights by simply interacting with the selfbot.

## Prerequisites

Before running this selfbot, ensure you have the following prerequisites:

- Python 3.7 or higher installed
- `discord.py` library (install using `pip install discord.py`)
- `phue` library (install using `pip install phue`)
- A Philips Hue lighting system set up in your home network

## How It Works

Replace '192.168.0.2' with the IP address of your Hue bridge.
This selfbot listens for a specific command in Discord and responds by displaying a message with color options as reactions. When a user reacts to the message with a color emoji, the selfbot communicates with the Philips Hue bridge and changes the color of the lights accordingly.



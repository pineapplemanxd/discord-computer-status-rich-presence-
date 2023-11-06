# Discord Rich Presence with System Information

This Python script allows you to display real-time system information, such as CPU and RAM usage, on your Discord profile through Discord Rich Presence. It uses the `psutil` library to gather system information and the `pypresence` library to communicate with Discord.

## Prerequisites

1. **Python**:
   - Make sure you have Python installed on your system. You can download and install Python from the [official Python website](https://www.python.org/downloads/).

2. **Discord Developer Application**:
   - Create a Discord Developer Application and set up a bot.
   - You can do this by visiting the [Discord Developer Portal](https://discord.com/developers/applications).
   - Copy the `client_id` of your bot, which you'll use in the script.

3. **Python Libraries**:
   - Install the necessary Python libraries if you haven't already. You can install them using pip:
   
   ```shell
   pip install psutil pypresence

## Script Configuration
Before running the script, you need to configure it by following these steps:
1. Open the script file in a code editor.
2. Replace 'xxxxxxxxxxxxxxxxxxx' in the client_id variable with your Discord bot's client ID.

## Running the Script
Once you've configured the script, you can run it to display your system information as a rich presence on your Discord profile:
1. Open a terminal or command prompt
2. Navigate to the directory where you saved the script.
3. Run the script using the following command:
   ```shell
   python computer_Stats.py
   
4.The script will start and display real-time information about your system's CPU and RAM usage in your Discord profile's rich presence.



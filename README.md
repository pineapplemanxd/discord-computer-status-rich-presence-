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
   
 4.The script will start and display real-time information about your system's CPU and RAM usage in your Discord profile's 
 rich presence.
## Customization

You can customize the script to display additional information or modify the update frequency. The following variables in the script can be adjusted:
- 'details': This is the text that appears below your Discord username. You can modify this to display any system information you like.
- 'state': This is the second line of text in your rich presence. You can customize it to display different system metrics or information.
- 'time.sleep(15)': This line controls the update frequency of the rich presence. By default, it updates every 15 seconds. You can change this value to update more or less frequently, but be mindful of rate limits imposed by Discord.

## Stopping the Script
To stop the script and remove the rich presence from your Discord profile, simply terminate the script by pressing Ctrl+C in the terminal where it's running.

That's it! You've successfully set up and used this Python script to display system information in a Discord rich presence. Customize it to suit your preferences and enjoy showing off your system stats to your friends on Discord.



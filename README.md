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

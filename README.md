


# ChatGPT-Turbo SMS

ChatGPT-Turbo SMS is a Flask application that allows users to send SMS text messages to ChatGPT-Turbo using Twilio and receive instant responses. This application can be run locally or hosted on services like DigitalOcean to stay active 24/7 using [tmux](https://github.com/tmux/tmux/wiki). The application uses [Flask](https://flask.palletsprojects.com/), [Twilio](https://www.twilio.com/), [OpenAI](https://openai.com/), and [ngrok](https://ngrok.com/) python libraries.

## Video Demonstration

A video demonstration of the ChatGPT-Turbo SMS application, hosted on DigitalOcean and utilizing tmux to keep the session open after closing the console, is shown below.

https://user-images.githubusercontent.com/63890666/225838063-f71c5a9b-fe22-4882-ab70-b3c20e26ba11.mp4


## Features

-   Send text messages to ChatGPT-Turbo and receive instant responses
-   Utilizes Twilio API for SMS handling and OpenAI API for processing user queries
-   Supports local deployment and also easily deployable on DigitalOcean using tmux for persistent sessions
-   Utilizes ngrok for easy access to the application
-   Can easily change system role by replacing the content 'You are a helpful assistant.' to anything else in line 25 in app.py
 > `{"role": "system", "content": "You are a helpful assistant."}`

## Prerequisites

-   Python 3.6 or later
-   Twilio account with an SMS-enabled phone number
-   OpenAI API key
-   ngrok

## Installation

1.  Clone the repository:
    
    	`git clone https://github.com/Kaludii/ChatGPT-Turbo-SMS.git
    
    	cd ChatGPT-Turbo-SMS` 
    
2.  Create and activate a virtual environment:
    
    	`python3 -m venv venv
    
    	source venv/bin/activate` 
    
3.  Install the required packages:
    
    `pip install -r requirements.txt` 
    
4.  Create a `.env` file in the project root directory and copy your Twilio Account SID, Auth Token, and OpenAI API Key:
    

	    `TWILIO_ACCOUNT_SID=your_twilio_account_sid
    
	    TWILIO_AUTH_TOKEN=your_twilio_auth_token
    
	    OPENAI_API_KEY=your_openai_api_key`

Replace `your_twilio_account_sid`, `your_twilio_auth_token`, and `your_openai_api_key` with the corresponding values from your Twilio and OpenAI accounts.

## Usage

### Running the application locally

1.  Start the Flask app:
    
    `python app.py` 
    
2.  Go to the following [website](https://dashboard.ngrok.com/get-started/setup), sign up for ngrok and connect your authtoken to your account.

3.  In a separate terminal, start ngrok:
    
    `ngrok http 5000` 
    
4.  Configure your Twilio phone number's messaging webhook with the generated ngrok URL followed by `/sms`. For example, if your ngrok URL is `https://abcd1234.ngrok.io`, set the webhook to `https://abcd1234.ngrok.io/sms`.
	
   > Add the webhook URL to the following two Twilio pages, [Phone Numbers > Manage > Active Numbers](https://console.twilio.com/us1/develop/phone-numbers/manage/incoming?frameUrl=/console/phone-numbers/incoming/), and [Conversations > Manage > Global Webhooks](https://console.twilio.com/us1/develop/conversations/manage/webhooks?frameUrl=/console/conversations/configuration/webhooks?x-target-region=us1). Make sure both are with HTTP POST and for the second link make sure "onMessageAdded" is selected in the Post-webhooks section. Example pictures:

![image](https://user-images.githubusercontent.com/63890666/225955417-c6c8f306-9f77-4497-bdd8-b8c7b382e6f6.png)
    
5.  Send an SMS to your Twilio phone number. ChatGPT-Turbo will process the message and you'll receive an immediate response.
    

### Hosting the application on DigitalOcean

To host the application on DigitalOcean like in the video example shown above, follow these steps:

1.  Create a DigitalOcean account if you don't have one: [https://www.digitalocean.com/](https://www.digitalocean.com/)
    
2.  Create a new droplet (virtual machine) by clicking "Create" and then "Droplets." Choose an appropriate plan, region, and operating system (e.g., Ubuntu 20.04 LTS) for your droplet. (I used the cheapest $4 dollar plan and it works perfectly, you don't need any more than that)
    
3.  Use an SSH client (e.g., PuTTY on Windows or `ssh` on macOS/Linux) to connect to your droplet using its IP address, username `root`, and the provided password.
    
4.  Update your system packages and install necessary dependencies:
    
	    `sudo apt-get update
    
	    sudo apt-get upgrade
    
	    sudo apt-get install python3-pip python3-venv` 
    
5.  Clone the Flask application repository or transfer the Flask application files to the droplet using `scp` or an SFTP client, and also configure the `.env` file as described in hosting locally section.
    
6.  Navigate to the Flask application directory and create a virtual environment:
    
    `python3 -m venv venv` 
    
7.  Activate the virtual environment and install the Flask application's dependencies:
    
	    `source venv/bin/activate
    
	    pip install -r requirements.txt` 
    
8.  Set the Flask environment variables:
    
	    `export FLASK_APP=app.py
    
	    export FLASK_ENV=production` 
    
9.  Run the Flask application using the `flask run` command:
    
    `flask run` 
    
    This will start the Flask application on the default port 5000.
    
10.  In another terminal (SSH) session, install ngrok on your DigitalOcean droplet and connect your authtoken to your account using [this](https://dashboard.ngrok.com/get-started/setup) website:
    
    `wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
    
    sudo apt-get install unzip
    
    unzip ngrok-stable-linux-amd64.zip` 
    
11.  Run ngrok to create a tunnel to the Flask application:
    
    `./ngrok http 5000`
    
12.  Copy the webhook URL from the ngrok window followed by `/sms` and add it to the two Twlio sections, similar to 3A from the running locally section.

### Hosting the application on DigitalOcean (Using tmux to keep session active after console is closed)

1.  Deploy a new Droplet on DigitalOcean.

2.  Install the required dependencies on the Droplet.

3.  Clone the repository and configure the `.env` file as described in hosting locally section.

4.  Start a new `tmux` session:

`tmux new -s chatgpt-turbo-sms` 

5.  Run the application within the `tmux` session:

`python app.py` 

6.  In a separate terminal, start a new `tmux` session:
    
    `tmux new -s chatgpt-turbo-sms-ngrok` 

7.  Install ngrok on your DigitalOcean droplet and connect your authtoken to your account using [this](https://dashboard.ngrok.com/get-started/setup) website:
    
	    `wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
    
	    sudo apt-get install unzip
    
	    unzip ngrok-stable-linux-amd64.zip` 

8.  Start ngrok:

    `start ngrok` 

9.  Copy the webhook URL from the ngrok window followed by `/sms` and add it to the two Twlio sections, similar to 3A from the running locally section.

10.  Detach from the `tmux` session by pressing `Ctrl-b` followed by `d`.

The application will continue running even after you close your console. To reattach to the `tmux` session, use:

`tmux attach -t chatgpt-turbo-sms`, and `tmux attach -t chatgpt-turbo-ngrok`


## About the Developer

This app was developed by [Kaludii](https://github.com/Kaludii) using the the different libraries linked above. Kaludii is an AI enthusiast who is passionate about developing and applying large learning models to solve real-world problems quickly and stress-free.

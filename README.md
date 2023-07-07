# Psyccess

## Description
  Before twitter went private, I had a scrappper for mining tweets and saving them on sqlite database. Now I have decided to opensource the code. Feel free to use or modify.

## Build Setup

```
# I used linux but you can use windows

# Install linux dependencies 
$ apt update && apt install -y python3, python3-pip, python3-venv, unzip

# Get webdriver
$ cd /tmp && /
    wget https://chromedriver.storage.googleapis.com/80.0.3987.16/chromedriver_linux64.zip && /
    unzip chromedriver_linux64.zip && /
    sudo mv chromedriver /usr/bin/chromedriver

# Navigate to your home folder
$ cd ~

# Create virtual environment
$ python3 venv psyccess

# Change to environment you created above
$ source psyccess/bin/activate

# Clone the project
# git clone https://github.com/framasha/psyccess.git

# Navigate to project folder
$ cd psyccess

# Install dependencies
$ pip install requirements.txt

# Run
$ python mine_tweets.py
```

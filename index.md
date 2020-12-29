# Welcome to Block!
Block is a program to easily block out distracting websites.

### Requirements
Python 3.7 +

### Installation

Installation can be done using `pip`
```
python -m pip install https://github.com/anand2312/block/archive/0.1.0.tar.gz
```

#### Note: Run all Block commands as administrator. 
###### On Linux
On Linux, running commands with admin permissions is as simple as adding `sudo` before the command
```
sudo python -m block
```
###### On Windows
This isn't as easy on Windows.
You will have to run either Command Prompt or Powershell **as administrator.**
- Use `Win + X`, which brings up a popup menu with many options. Pick `Powershell (Administrator)`
- Search for `Command Prompt`/`cmd` in your search bar > Right click and `Run as administrator`.
\
From here on, it will be assumed that you are running commands as administrator, and it won't be explicitly stated in the examples.

### Setup

Before you block any websites, you need to setup Block.
To do so, open a command line window, and run the following command:
```
python -m block setup
```
This will begin an interactive setup session.

### Usage

##### Starting Block
Starting Block is as simple as running 
```
python -m block start
```
This will begin an interactive sesssion, which will ask you to enter:
- The websites to be blocked. You have to enter a space separated list of websites. For example, to block *youtube* and *instagram*, you would enter
```
www.youtube.com www.instagram.com
```
- The amount of time that these sites have to be blocked for:
The time has to be entered like:
For keeping sites blocked for 5 hours, you would enter `5h`
For keeping sites blocked for 3 days, you would enter `3d`.
The smallest supported unit of time currently is _hours_.

##### Stopping Block
You can stop blocking sites by running
```
python -m block stop
```
This will raise an error if the time you'd specified while starting hasn't elapsed yet.
\
**Note: Block does NOT automatically unblock sites after the time you specified has elapsed. It merely lets you to stop blocking by yourself.
That is, if you try stopping blocking before the time is up, Block will raise an error, but after the time is up, you have to run `block stop` to gain back access to the sites.**

##### Editing time period
In case you accidentally set the blocking time incorrectly, you can edit this by doing 
```
python -m block edit
```
Note that this new time is set from the time you're running the edit command.
For example;
If you used the `edit` command, and edited the time to be `3h`. Now you have to wait 3 hours more to stop it.
This obviously means that if you want to immedietely stop the blocking, you have to run `edit` and enter `0h` as the time.

### Support or Contact

Contact me on Discord: Ares#7286
Make an issue on [Github](https://github.com/anand2312/block)

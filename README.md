## Snkrs Tracker

Simple script to track Nike Snkrs to scrap website and search for specific surprise sneaker releases using keywords and emails your if it finds anything

### Requirements

 - Python 3.0 and above
 - virtualenvwrapper or virtualenv

### Installing

Create a virtualenv to reference later for cron job usage and for maintaining the packages that get will get installed   

If you are using virtualenvwrapper  
  `mkvirtualenv --python=python3 snkrsTracker`

To install packages required   
  `pip install -r requirements`


### Usage  

To use the script call from within your virtualenv  
  `./watcher.py --keywords keyword1 keyword2 ... --email bob@gmail.com --password secretpass --listserve joe@gmail.com bob@gmail.com`

This should probably only run on machines you maintain just to make sure you password is safe and all

You can run this either on your own periodically or setup a cron job on your machine or aws to do it there

Point to your virtualenv for the python executable to make sure it has the packages your need

In my case  
  `~/virtualenvs/snkrsTracker/bin/python3.7 ./watcher.py --keywords keyword1 keyword2 ... --email bob@gmail.com --password secretpass --listserve joe@gmail.com bob@gmail.com`

And just call that within your cron job and should email you if it finds match to your keywords

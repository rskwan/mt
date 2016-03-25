# MT

[![Requirements Status](https://requires.io/github/rskwan/mt/requirements.svg?branch=master)](https://requires.io/github/rskwan/mt/requirements/?branch=master)

## What does "MT" mean?

Math Tournament. Milk Tea. (Or whatever you want it to be.)

## Setup

MT requires Python 3 and MySQL.

### Installing Python Dependencies

Make sure you have Python 3, pip, and virtualenv (plus virtualenvwrapper) installed.
[The Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/) has
some good sections on how to install Python and virtualenvwrapper.

```
mkvirtualenv --python=`which python3` your_env_name  # 'mt' is a good name
pip3 install -r requirements/local.txt               # or requirements/production.txt
```

### Setting up MySQL

Installing and setting up MySQL can be a pain, so be careful.
For Mac OS X, [here's a guide to setting up (and tearing down) an installation.](https://coderwall.com/p/os6woq/uninstall-all-those-broken-versions-of-mysql-and-re-install-it-with-brew-on-mac-mavericks)

### Environment Variables

Set these environment variables. (With virtualenv, you probably want to
put these in `your_env_name/bin/postactivate`.)

```
export DJANGO_SETTINGS_MODULE='mt.settings.local'          # or production
export MT_SECRET_KEY='milk_tea'                            # randomly generated string
export MT_MYSQL_URL='mysql://USER:PASSWORD@HOST:PORT/NAME'
export HOST_NAME='mt.com'                                  # only needed in production
```

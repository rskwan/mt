# MT

[![Requirements Status](https://requires.io/github/rskwan/mt/requirements.svg?branch=master)](https://requires.io/github/rskwan/mt/requirements/?branch=master)
[![Build Status](https://travis-ci.org/rskwan/mt.svg?branch=master)](https://travis-ci.org/rskwan/mt)
[![codecov.io](https://codecov.io/github/rskwan/mt/coverage.svg?branch=master)](https://codecov.io/github/rskwan/mt?branch=master)

## What does "MT" mean?

Math Tournament. Milk Tea. Empty. (Or whatever you want it to be.)

## Setup

MT requires Python 3.4+, Django 1.8+, and MySQL.

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

Once/if you have an existing MySQL installation, you might need to run any
or all of the following commands in a `mysql` console.

```
create user 'username'@localhost identified by 'pass';
grant all privileges on mt.* to 'username'@localhost;
grant all privileges on test_mt.* to 'username'@localhost;
```

### Environment Variables

Set these environment variables. (With virtualenv, you probably want to
put these in `your_env_name/bin/postactivate`.)

```
export DJANGO_SETTINGS_MODULE='mt.settings.local'          # or production
export MT_SECRET_KEY='milk_tea'                            # randomly generated string
export MT_MYSQL_URL='mysql://USER:PASSWORD@HOST:PORT/NAME'
export MT_ADMIN_PATH='hello'                               # admin is at /hello/ instead of /admin/
export MT_HOST_NAME='mt.com'                               # only needed in production
```

### Migrations and Your User Account

In order to do anything, you (presumably the webmaster) should set up
the database and a user account. Run `python manage.py migrate` to apply
migrations to your db, then run `python manage.py createsuperuser` to
make a superuser account.

At this point, if you're running locally, you should be able to able
to start the server with `python manage.py runserver` and log into
the admin site at `localhost:8000/MT_ADMIN_PATH/`.

## Testing

To run the test suite, `cd` into `mt` and run `py.test`.
If you want an HTML coverage report, add the option `--cov-report html`,
which will generate a folder `coverage_html_report`.

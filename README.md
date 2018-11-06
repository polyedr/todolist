# To-do lists demo project

To-do lists demo project. Users are not allowed to the admin pages. User can see only his own posts in to-do list. Filters are included. No theming, for example of theming, you can find the latest front end project ready here, https://github.com/polyedr/dpfiles

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
You can use this application to make your own to-do list.

### Prerequisites

What things you need to install the software and how to install them

PostgreSQL
Python 3.4+

### Installing

You can create virtual environment first from the requirements.txt file. 
After that, if necessary, you can check SQLite version of the project demo_project_sqlite.tar.gz

User accounts:
* Superuser
* admin
* adminadmin

* User
* info@poly-edr.ru
* info
* @/./+/-/_

## Deployment

1. Create PostgreSQL user and database
2. Restore PostgreSQL database from dump, https://www.postgresql.org/docs/current/backup-dump.html
3. Copy project files to server. Set up allowed hosts in settings.py
4. Deploy with NGINX and Gunicorn or UWSGI
5. Check that you have Debug = False in settings.py

## Built With

* [Python](https://www.python.org/) - Programming language
* [Django](https://www.djangoproject.com/) - The Web framework for perfectionists with deadlines

## Authors

* **Ivan Ishchukov** - *web development* - http://poly-edr.com/

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## Acknowledgments

* Thanks for all Django authors
 

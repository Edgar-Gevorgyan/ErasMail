ErasMail
===========

ErasMail is a free and open source tool that allows you to clean up your email boxes. The goal of ErasMail is to contribute to the reduction of digital pollution and more particularly of the pollution generated by emails. 

Most of the cleaning tools are limited to unsubscribing and deleting newsletters, not to mention the fact that they sell their users' data. Erasmail offers much more features and does not keep/sell any data. 

ErasMail uses IMAP which makes it compatible with all email providers.

![](erasmail.gif)

## Features
- Estimation of the pollution generated by your emails
- Detection, unsubscription and deletion of newsletters
- Detection of the most polluting threads, possible duplicated attachments and possibility to delete attachments or threads
- Possibility to filter emails   
  - the oldest 
  - the largest 
  - the useless (welcome emails, confirmation emails, social, ...)
  - the most polluting
  - the folder
- Detailed statistics on your email box
- Advanced gamification system (badges, ranking, success)

## Licence
Code released under Apache License 2.0

## Development 

### Requirements : 
* Install docker and docker-compose
* Set an environment file called .env.dev with :
  * SECRET KEY : django secret key
  * DJANGO_ALLOWED_HOSTS : **localhost**
  * SQL_DATABASE : the postgres database name
  * SQL_USER : postgres username
  * SQL_PASSWORD : postgres database password
  * SQL_HOST : **db** (mandatory)
  * SQL_PORT : **5432**
  * DATABASE : **postgres**
### Run :
>docker-compose up -d --build


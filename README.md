# groja.com

This repo contains the code for groja.com .

For the Requirements used to create this, see the README-Requirements.md file in this directory.

## MasterPlan

After reading a lot about marketing and the new Google Analytics, etc., I've decided to define this site's purpose as follows:

## Lead-generation -> Possible combo site

As learned in the Google Analytics (GA) "Getting Started" class, we can define this site as having two purposes:

1. The Groja project's lead Generation site
2. The Groja project's e-commerce site

The idea is to find people who are willing to purchase a Spiritual Portrait of themself, and later,
to begin to automate the sales process to the extent that we can.

### (1) First and foremost: Lead-generation site

As a lead-generation site, this site has the following purposes:

* Drive traffic to groja.com our parallel lead generation and e-commerce site
* Gather email addresses for an occasional emails containing special offers

To begin with, this is the site's primary purpose, to be implemented:

* On the Home page
* Possibly in the aside area on other pages

### (2) Later (maybe): E-Commerce site

As an E-commerce site, this site has the following purposes:

* Coordinating the billing for and purchase of Spiritual Portraits
* Possibly allow selling of printed portraits, or groupings of portraits, or ???

To begin with, this is a secondary purpose to be implemented on the Your Portraits page.

## 2017-02-10 Migration to Flask

In light of these decisions, I've decided to:

* Move the gallery to seeourminds.com .
* Replace the static site with one that uses Flask.

### Proof of concept:

We tested this out already - twice! For details see:

- https://github.com/tomwhartung/always_learning_python/tree/master/6-flask_templates_exp
- https://github.com/tomwhartung/always_learning_python/tree/master/7-flask_bootstrap_exp

**There's a lot of information there, that we will not repeat here!**

These are very very similar.  It's pretty much a matter of whether we include bootstrap manually or use flask_bootstrap.

We are going with the second (7-flask_bootstrap_exp) version.

### Process overview

Following is an overview of the process used.

1. Remove old and copy new files
2. Install flask and flask-bootstrap
3. Test on localhost
3.1 hello.py
3.2 groja.py
4. Update apache config and test
5. Deploy to backup host (barbara)
6. Deploy to production host (ava)

### Details

Following are some details with respect to this adventure.

#### Step (1) Remove old and copy new files

Use git rm -fr and git add --all .

#### Step (2) Installation

Test installation of flask:

```
python3
>>> import flask
```

Hopefully there's no error, else see references above (in the always_learning_python repo).

**We are doing super-basic stuff at this time, so do not worry about versions.**

If flask-bootstrap is not installed globally, here's how to fix that:

As root:

```
(sudo su -)
pip3 install flask-bootstrap
```

#### Step (3) Running hello.py and groja.py locally

```
gogg              # /var/www/groja.com/htdocs/groja.com
cd Site
python3 hello.py  # http://127.0.0.1:5000/
```

Ensure that works before proceeding.

```
python3 groja.py  # http://127.0.0.1:5000/
```

Commit changes to github (if that hasn't been done already).

#### Step (4) Update apache config, restart apache, and test

We need to run it through wsgi, so model the new file after 050-seeourminds.com.conf .

References for updating the apache .conf file:

- http://flask.pocoo.org/docs/0.12/deploying/mod_wsgi/#creating-a-wsgi-file
- http://www.jakowicz.com/flask-apache-wsgi/

As root:

```
(sudo su -)
cd /etc/apache2/sites-available
rd 020-groja.com.conf           # ensure current version is checked in
vi 020-groja.com.conf
service apache2 stop
service apache2 start
```

Test:

- http://jane.groja.com/

#### Step (5) Deploy to barbara

##### 5.1 Verify installation of flask and flask_bootstrap

We are just starting out so it's ok to install the current default version(s) globally.

We can worry about virtual environments when it comes to upgrading.

As tomh:
```
python3
>>> import flask
>>> import flask_bootstrap

```

As root (if necessary):
```
pip3 install flask-bootstrap
```

Root permissions are needed to install it in /usr/bin .

##### 5.2 Update apache config

Copy and paste, and verify it looks good.

##### 5.3 Pull code

Decided to preserve the old static in a new repo, groja.com-static , for easy possible future reference.

##### 5.4 Restart apache

```
sudo service apache2 restart
```

##### 5.5 Test

- http://barbara.groja.com/

#### Step (6) Deploy to ava

This is essentially the same process used on barbara.  For details, see above for the process used on that host.

##### 6.1 Verify installation of flask and flask_bootstrap

As tomh:
```
python3
>>> import flask
>>> import flask_bootstrap

```

Install as root if necessary.

##### 6.2 Update apache config

Copy and paste, and verify it looks good.

##### 6.3 Pull code

```
gp   # my super-cool alias for git pull, cos I run it rather frequently :-)
```

##### 6.4 Restart apache

```
sudo service apache2 restart
```

##### 6.5 Test

- http://ava.groja.com/


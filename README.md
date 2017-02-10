# groja.com

Code for groja.com .

## MasterPlan

After reading a lot about marketing and the new Google Analytics, etc., I've decided to define this site's purpose as follows:

## Combo site

As learned in the Google Analytics (GA) "Getting Started" class, we can define this site as having two purposes:

1. The Groja project's lead Generation site
2. The Groja project's e-commerce site

The idea is to find people who are willing to purchase a Spiritual Portrait of themself, and later,
to begin to automate the sales process to the extent that we can.

### Lead-generation site

As a lead-generation site, this site has the following purposes:

* Drive traffic to groja.com our parallel lead generation and e-commerce site
* Gather email addresses for an occasional emails containing special offers

To begin with, this is the site's primary purpose, to be implemented:

* On the Home page
* Possibly in the aside area on other pages

### E-Commerce site

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

#### Step (4) Update apache config

We need to run it through wsgi, so model the new file after 050-seeourminds.com.conf .

As root:

```
(sudo su -)
cd /etc/apache2/sites-available
rd 020-groja.com.conf           # ensure current version is checked in
vi 020-groja.com.conf
```

Test:

- http://jane.groja.com/


#### Step (5) Deploy to barbara

#### Step (6) Deploy to ava



## Requirements

### Pages

These are the pages (menu options):

* Home Page: landing page to gather leads
* About: information about the idea, etc.
* Books and Sites: lists of and links to background information
* Your Portrait: information about how to get your portrait, and how much it will cost
* Link to seeourminds.com home page as right-most option in the menu

This is the bulk of the project: routes (urls) and views, so Flask is ideal.

### Navigation and urls

KISS is how we want to play it, through and through.

Following is a list of the pages for the site, and the route or routes of each:

* Home page: `home` or `''`
* About: `about`
* Books and Sites: `booksandsites`
* Your portrait: `yourportrait`

### Page Layouts

KISS is the key here.  All pages shall contain "minimal main navigation" and content **ONLY**.

The term "minimal main navigation" refers to links in the heading for the following pages:

* Home
* Galleries
* Your Portrait
* About

If it's easy, ensure the selected option in this menu is disabled.

### Data

Lists of images along with their descriptions shall be stored in JSON format.

### Devices

Following is a list of goals with respect to mobile phones and other devices:

* Keep layouts as simple as possible.
* Use minimal media queries.
* Probably want to use bootstrap to build columns of images
* No need for device detection at this time.

#### Bonus Extra Credit!

Have "minimal main navigation: shrink into a hambuger menu icon on small screen sizes.


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

## Updates

In light of these decisions, I've decided to move the gallery to seeourminds.com .

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


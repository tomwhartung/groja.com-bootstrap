# groja.com

These are the requirements for groja.com .

Almost all of these requirements have been fulfilled, so we keep them in a separate file.

For other information, see the main README.md file in this directory.

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

Have "minimal main navigation" that shrinks into a hambuger menu icon on small screen sizes.


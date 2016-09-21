# groja.com

Code for groja.com .

### MasterPlan

Be mindful that the MasterPlan is to do the same thing or something very similar using:

* HTML5, CSS, and JavaScript,
* Python and Django, and
* Node.js and React,

then compare the process, results, and ease of scalability.

So be on the lookout for opportunities to share non-react-dependent JavaScript, HTML, or CSS between the two!

## static_image_gallery - goals

The main goal at this time is get a django site running on my server, no matter how simplistic, asap.

## Requirements

### Pages

The Static Image Gallery shall contain the following pages, with content as described.

* Home Page: static; briefly describe what the site is about and include a self-portrait
* List of Galleries: (possibly) driven by JSON data
* Set of GRoJA Images: driven by JSON data
* Single Image Display - Popup: contains the image, its title and description and navigation/close button only
* About: static; more information, and links to other sites and a Contact Me page

This is the bulk of the project: routes (urls) and views.

### Navigation and urls

KISS is how we want to play it, through and through.

Following is a list of the pages for the site, and the route or routes of each:

* Home page: `home` or `''`
* Galleries: `galleries`
  * Friends: `galleries/gallery.html?gallery=friends`
  * Generics: `galleries/gallery.html?gallery=generics`
  * TV Shows: `galleries/gallery.html?gallery=tvshows`
  * Politicians: `galleries/gallery.html?gallery=politicians`
* About: `about`
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


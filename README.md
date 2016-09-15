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

Keep in mind that the main goal is get a django site running on my server, no matter how simplistic, asap.

1. Learn how to get views.py and urls.py to work together
2. Have something minimal to host at groja.com
3. Lay the mental groundwork for building something that uses models or PIP or both

## Requirements

### Pages

The Static Image Gallery shall contain the following pages, with content as described.

* Home Page: static; briefly describe what the site is about and include a self-portrait
* List of Galleries: driven by JSON data
* Set of GRoJA Images: driven by JSON data
* Single Image Page: contains the image, its title and description (and navigation) only
* About: static; more information, and links to other sites and a Contact Me page

This is the bulk of the project: routes (urls) and views.

### Navigation and urls

KISS is how we want to play it, through and through.

* Home page: `home`
* Generics: `generics`
* Celebrities: `celebrities`
  * Politicians: `celebrities/politicians`
  * TV Shows: `celebrities/tv_shows`
  * Historical: `celebrities/historical`
* About: `about`

### Page Layouts

KISS is the key here.  All pages shall contain:

* navigation and
* content

ONLY.

### Data

Lists of images shall be stored in JSON format.

### Devices

* Keep layouts as simple as possible.
* Use minimal media queries.
* Probably want to use bootstrap to build columns of images
* No need for device detection at this time.

#### Bonus Extra Credit!

Have navigation shrink into a hambuger menu icon on small screen sizes.

### Design

Most of the site's design is determined by django.

* Single project: `static_image_gallery`
* Single app: `groja_gallery`

Views: TBD.


/**
 * ****************************************
 *  Data and functions used by the gallery
 * ****************************************
 *
 * We could keep this in the global js directory, but
 *   I think it's fine keeping it here, at least for now.
 *
 * That is, I do not forsee other pages using any of this, but
 *   if it turns out to be useful to one or more of them,
 *     by all means move it to the global js dir.
 *
 */

gallery = {};

/**
 ************************************
 * Gallery data
 ************************************
 */
gallery.name = {
   'sixteen_types':
      "Sixteen Types",
   'friends':
      "Friends and Family",
   'tv_shows':
      "TV Shows",
   'politicians':
      "Politicians"
}

gallery.description = {
   'sixteen_types':
      "This gallery contains images of ... Sixteen Types ... and so on.",
   'friends':
      "This gallery contains images of ... Friends and Family ... and so on.",
   'tv_shows':
      "This gallery contains images of ... TV Shows ... and so on.",
   'politicians':
      "This gallery contains images of ... Politicians ... and so on."
}

/**
 ************************************
 * Gallery functions
 ************************************
 */

/**
 * All we want is a simple way to get the
 * value of the "gallery" query variable so we know which gallery to display.
 *
 * This method, which is just one of many found (there are several on stack overflow),
 * is quite simple (many use regexes).  Yay for that!
 * Yet it is also quite  possibly fairly inefficient - especially if we are looking for
 * the values of multiple query variables.
 *
 * If we need to do this in more than one place or for more than one query variable,
 * we should definitely move/merge this with a global JS file and probably look at
 * using a different method (e.g., one that processes all query variables, putting
 * them in an associative array, so we only have to do all that once).
 *
 * Reference:
 *    https://css-tricks.com/snippets/javascript/get-url-variables/
 */
gallery.getQueryVariable = function (variable) {
       var query = window.location.search.substring(1);
       var vars = query.split("&");
       for (var i=0;i<vars.length;i++) {
               var pair = vars[i].split("=");
               if(pair[0] == variable){return pair[1];}
       }
       return(false);
}

/**
 * Once we have the gallery to show, we can set its name and the description.
 */
gallery.populateNameAndDescription = function() {
   $('#name-of-gallery').text( this.name[this.galleryToShow] );
   $('#description-of-gallery').text( this.description[this.galleryToShow] );
   //
   // For debugging
   //
   console.log( 'populateNameAndDescription - this.pathToImages: ' + this.pathToImages )
   $('#gallery-to-show').text( this.galleryToShow );
   $('#json-file-name').text( this.jsonFileName );
   $('#path-to-images').text( this.pathToImages );
}

/**
 * Callback from getJSON call that processes the JSON we get
 */
gallery.populateGallery = function( images ) {
   //
   // call this "proof of concept"
   //
   console.log( 'populateGallery - gallery.pathToImages: ' + gallery.pathToImages )
   var full_path_to_image;
   full_path_to_image = gallery.pathToImages + images[0].image_file_name;  // "this." does not work in callbacks
   console.log( 'images.length = ' + images.length );
   $('#number-of-images').text( images.length );
   $('#image-zero-id').text( images[0].id );
   $('#image-zero-image-name').text( images[0].image_name );
   $('#image-zero-four-letter-type').text( images[0].four_letter_type );
   $('#image-zero-image-file-name').text( images[0].image_file_name );
   $('#image-zero-full-path-to-image').text( full_path_to_image );
   //
   // our first image is a static image
   //
   full_path_to_image = gallery.pathToImages + images[1].image_file_name;  // "this." does not work in callbacks
   $('#static-image-img').attr( "src", full_path_to_image );
   $('#static-image-figcaption').text( images[1].image_name );
   $('#static-image-frontpage-blurb').text( images[1].frontpage_blurb );
}

/**
 ********************************************
 * Code to assemble the data needed and
 * call the functions in the proper sequence
 ********************************************
 *
 * Get the name of the gallery to show from the query variable (in the url)
 */
gallery.galleryToShow = gallery.getQueryVariable( 'gallery' );
gallery.jsonFileName = 'json/' + gallery.galleryToShow + '.json';
gallery.pathToImages = '../../images/galleries/' + gallery.galleryToShow + '/';

/*
 * (1) Fill in the name and description of the gallery.
 * (2) Get the corresponding json file containing the data for the gallery to show,
 *     setting a callback function to populate the gallery with each image and its data.
 */
gallery.populateNameAndDescription();

$.getJSON( gallery.jsonFileName, gallery.populateGallery );



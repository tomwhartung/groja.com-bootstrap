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
   $('#gallery-to-show').text( this.galleryToShow );
   $('#json-file-name').text( this.jsonFileName );
}

/**
 * Get the json file for the gallery to show,
 * setting a callback to populate the gallery with
 * each image and its corresponding data.
 */
gallery.getJsonAndPopulateGallery = function() {
   $.getJSON( this.jsonFileName, gallery.populateGallery );
}

/**
 * Callback from getJSON call that processes the JSON we get
 */
gallery.populateGallery = function( images ) {

   console.log( 'images.length = ' + images.length );
   $('#number-of-images').text( images.length );
   $('#image-zero-id').text( images[0].id );
   $('#image-zero-image-name').text( images[0].image_name );
   $('#image-zero-four-letter-type').text( images[0].four_letter_type );
}

gallery.galleryToShow = gallery.getQueryVariable( 'gallery' );
gallery.jsonFileName = 'json/' + gallery.galleryToShow + '.json';

gallery.populateNameAndDescription();
gallery.getJsonAndPopulateGallery();



/**
 * At least at first, all we want is a simple way to get the
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

gallery = {};

gallery.getQueryVariable = function (variable) {
       var query = window.location.search.substring(1);
       var vars = query.split("&");
       for (var i=0;i<vars.length;i++) {
               var pair = vars[i].split("=");
               if(pair[0] == variable){return pair[1];}
       }
       return(false);
}

gallery.galleryToShow = gallery.getQueryVariable( 'gallery' );

$('#gallery-to-show').text( gallery.galleryToShow );

console.log( 'gallery.galleryToShow = ' + gallery.galleryToShow );

// console.log( 'gallery.genericImages.length = ' + gallery.genericImages.length );



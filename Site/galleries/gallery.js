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
   $('#name-of-gallery').text( this.name[this.gallery_to_show] );
   $('#description-of-gallery').text( this.description[this.gallery_to_show] );
}

/**
 * Callback from getJSON call that processes the JSON we get
 */
gallery.populateGallery = function( image_json ) {
   //
   // For debugging - remove when page works ok for all galleries
   //
   $('#gallery-to-show').text( gallery.gallery_to_show );
   $('#json-file-name').text( gallery.json_file_name );
   $('#number-of-images').text( image_json.image_list.length );
   $('#path-to-images').text( gallery.path_to_images );

   var full_path_to_image;
   //
   // our first image is a static image - remove when everything is working
   //
   full_path_to_image = gallery.path_to_images + image_json.image_list[1].image_file_name;  // "this." does not work in callbacks
   $('#static-image-img').attr( "src", full_path_to_image );
   $('#static-image-figcaption').text( image_json.image_list[1].image_name );
   $('#static-image-frontpage-blurb').text( image_json.image_list[1].frontpage_blurb );
   //
   // Compile the handlebars template
   // Add the full path to the image to the image data
   // After every "columns" images, set "add_row_separator" to a truesy value and add it to the image data
   // Give the handlebars template the resultant image data to get the html
   // Add the html to the document in the appropriate place
   //
   var num_columns = 4;
   var handlebars_html = $("#gallery-image-template").html();
   var handlebars_template = Handlebars.compile( handlebars_html );
   console.log( 'image_json.image_list.length: ' + image_json.image_list.length );
   for( var data_sub = 0; data_sub < image_json.image_list.length; data_sub++ ) {
      image_json.image_list[data_sub].full_path_to_image = gallery.path_to_images +
         image_json.image_list[data_sub].image_file_name;
      if( (data_sub % num_columns) == 0 && data_sub != 0 ) {
         image_json.image_list[data_sub].add_row_separator = true;
      } else {
         image_json.image_list[data_sub].add_row_separator = false;
      }
      console.log( 'image_json.image_list[data_sub].add_row_separator: ' + image_json.image_list[data_sub].add_row_separator );
      console.log( 'image_json.image_list[data_sub].full_path_to_image: ' + image_json.image_list[data_sub].full_path_to_image );
   }
   var gallery_html = handlebars_template( image_json );
   $('#all-gallery-images').html( gallery_html );
}

/**
 ********************************************
 * Code to assemble the data needed and
 * call the functions in the proper sequence
 ********************************************
 *
 * Get the name of the gallery to show from the query variable (in the url)
 */
gallery.gallery_to_show = gallery.getQueryVariable( 'gallery' );
gallery.json_file_name = 'json/' + gallery.gallery_to_show + '.json';
gallery.path_to_images = '../../images/galleries/' + gallery.gallery_to_show + '/';

/*
 * (1) Fill in the name and description of the gallery.
 * (2) Get the corresponding json file containing the data for the gallery to show,
 *     setting a callback function to populate the gallery with each image and its data.
 */
gallery.populateNameAndDescription();

$.getJSON( gallery.json_file_name, gallery.populateGallery );



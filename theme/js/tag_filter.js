(function ($) {
    // custom css expression for a case-insensitive contains()
    jQuery.expr[':'].Contains = function(a,i,m){
        return (a.textContent || a.innerText || "").toUpperCase().indexOf(m[3].toUpperCase())>=0;
    };

    function listFilter() {

        $('.filterinput')
        .change( function () {
            var filter = $(this).val();
            if(filter) {
                // this finds all links in a list that contain the input,
                // and hide the ones not containing the input while showing the ones that do
                $('.list-of-tags').find("a:not(:Contains(" + filter + "))").parent().hide();
                $('.list-of-tags').find("a:Contains(" + filter + ")").parent().show();
            } else {
                $('.list-of-tags').find("span").show();
            }
            return false;
        })
        .keyup( function () {
            // fire the above change event after every letter
            $(this).change();
        });
    }

    //ondomready
    $(function () {
        listFilter($());
    });
}(jQuery));
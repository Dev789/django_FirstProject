(function ($) {

    'use strict';

    $('.alert[data-auto-dismiss]').each(function (index, element) {
        var $element = $(element),
            timeout = $element.data('auto-dismiss') || 3000;

        setTimeout(function () {
            $element.alert('close');
        }, timeout);
    });

})(jQuery);
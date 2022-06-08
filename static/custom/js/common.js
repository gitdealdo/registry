$(function() {
    $('[rel="tooltip"]').tooltip();
    $('[data-toggle="popover"]').popover()

    // $('#navbarMain').addClass('c-nav');
});

// $.extend(FormSerializer.patterns, {
//     validate: /^[a-z][a-z0-9_-]*(?:\[(?:\d*|[a-z0-9_-]+)\])*$/i,
//     key: /[a-z0-9_-]+|(?=\[\])/gi,
//     named: /^[a-z0-9_-]+$/i
// });

// $('.btn-action').on('click', event => {
// event.preventDefault();
// const btn = event.target;
// console.log($(btn).attr('id'));
// $.get("{% url 'control:persona_list_ajax' %}", data, function(r, status) {
//     process(r, '#list');
// });
// });
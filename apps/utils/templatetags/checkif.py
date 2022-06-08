from django import template

register = template.Library()


@register.filter
def has_url(image=None):
    if image:
        return image.url
    # return 'http://via.placeholder.com/640x360'
    return '/static/img/default.png'


@register.filter
def first_active(index):
    if index == 0:
        return 'active'
    return ''


@register.filter
def is_equal(var, args):
    """
    Use: 
    {% if item.id|is_equal:q %}active{% endif %}
    """
    return str(var) == args

# def is_in(var, args):
#     if args is None:
#         return False
#     arg_list = [arg.strip() for arg in args.split(',')]
#     return var in arg_list

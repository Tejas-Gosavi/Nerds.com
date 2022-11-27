from django import template

register = template.Library()

# create simple tag
@register.simple_tag()
def paginatedURL(request_qd, page):     # getting request QueryDict and page number
    
    # by default request QueryDict is immutable (not changeable)
    # so creating same mutable QueryDict by copying current QueryDict
    qd = request_qd.copy()

    # if new QueryDict has pages key
    if qd.__contains__('pages'):
        
        # then set it with new page, if we don't do this then pages will be appended every time. see below for ex.
        # title__icontains=&brand=2&comic_type=&price__gte=&price__lte=&pages=2&pages=3
        qd.__setitem__('pages', page)

    # if new QueryDict has not pages key
    else:

        # then add it in new QueryDict
        qd.appendlist('pages', page)

    # return new QueryDict in query string format
    return qd.urlencode(safe=None)

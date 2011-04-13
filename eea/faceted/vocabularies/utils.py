#
# Util sort method
#
def compare(a, b):
    """ Compare lower values """
    if not isinstance(a, unicode):
        a = a.decode('utf-8')
    if not isinstance(b, unicode):
        b = b.decode('utf-8')
    return cmp(a.lower(), b.lower())

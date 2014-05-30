import urllib

d=dict([tuple(line.split(",",1)) for line in file('photos.txt')])


def photoprinter():
    image = urllib.URLopener()
    for i,n in d.iteritems():
        image.retrieve(i, n)
        print i, n


photoprinter()

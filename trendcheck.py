from pyquery import PyQuery as pq
import argparse
import re


def testAnalyticsTags(link):
    """ Check that the Webtrends image is present on the page """
    page = pq(url=link)
    # regular expression for Webtrends tags
    dcsid = re.search('[dcs]{3}[a-z,0-9_]{27}', str(page))
    tag = page('img#DCSIMG')
    tagsrc = tag.attr('src')
    tagsrctype = type(tagsrc)

    print "\n-- Checking URL: %s" % link.rstrip('\n')

    if tagsrctype is not str or dcsid == None:
        print " * Img Tag Src Type: %s" % tagsrctype
        print " * Dcsid: %s " % dcsid
        print " * Error: Link has no Webtrends tag"
        raise Exception("Webtrends tag not found")
    else:
        print " * Tag Link: %s " % tagsrc
        print " * Tag: %s " % dcsid.group()
        print " * Pass!"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script to check for Webtrends tags")
    parser.add_argument('--file', action="store",
        dest='file', help='filename', type=str)
    parser.add_argument('--url', action="store", type=str,
        dest='url', help="url")
    results = parser.parse_args()
    if (type(results.file) != str) and (type(results.url == str)):
        testAnalyticsTags(results.url)
    elif (type(results.file) == str):
        openFile = open(results.file, "r")
        urls = openFile.readlines()
        openFile.close()
        for url in urls:
            testAnalyticsTags(url)
    else:
        print "Please enter a valid filename or URL"

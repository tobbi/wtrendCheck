from pyquery import PyQuery as pq
import argparse
import re


def testAnalyticsTags(url):
    """ Check that webtrends image is present on page"""
    page = pq(url)
    ##regular expression for webtrends tags
    dcsid = re.search('[dcs]{3}[a-z,0-9_]{27}', str(page))
    tag = page('img#DCSIMG')
    if tag.attr('src') != str or dcsid == ' ':
        print "Error: " + url + " has no Webtrends tag"
        raise Exception("Webtrend Tag not found")
    else:
        print "Url: " + url
        print "Tag Link: " + tag.attr('src')
        print "Tag:" + dcsid.group()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script to check for webtrends tags")
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
        print "Enter a valid  filename or url"

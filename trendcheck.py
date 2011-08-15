from pyquery import PyQuery as pq
import argparse
import re


def testAnalyticsTags(url):
    """ Check that the Webtrends image is present on the page """
    page = pq(url)
    # regular expression for Webtrends tags
    dcsid = re.search('[dcs]{3}[a-z,0-9_]{27}', str(page))
    tag = page('img#DCSIMG')
    print type(tag.attr('src'))
    if tag.attr('src') != str and dcsid == None:
        print "Error: " + url + " has no Webtrends tag"
        raise Exception("Webtrends tag not found")
    else:
        print "URL: " + url
        print "Tag Link: " + tag.attr('src')
        print "Tag:" + dcsid.group()

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

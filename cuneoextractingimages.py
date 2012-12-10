__author__ = "Christina Cuneo"
__date__ = 12/10 
'''extracts images from an HTML file and saves them'''
import os
import time
import urllib2
import urllib
import re
import sys

class Extract:

    CACHE_DIR = "webcache"

    def __init__(self):
        if not os.path.exists(self.CACHE_DIR):
            os.mkdir(self.CACHE_DIR)
    
    def getImageURLs(self, url):
    '''This looks through the HTML for image tags'''
    #This is basically copied from the class webspider code
        # Visit url
        try:
            url_object = urllib2.urlopen(url)
            page_text = url_object.read()
        except:
            print url, "is broekn"
            return []
        # Find image tags
        links = re.findall("img src=\"([^\"]+)\"", page_text)
        absolute_links = []
        for link in links:
            if link[:4] != "http":
                absolute_links.append(url + "/" + link)
            else:
                absolute_links.append(link)

        return absolute_links



    def getExt(self, url):
    '''this will find the file extension of the saved image'''
        extenson=""
        extension=re.findall("[\.][a-z]{3}", url) #RegEx for a file extension
        url = url.replace(".", " ")
        url = url.replace("http://", "")       
        url = url.replace("/", " ")
        url = url.replace("~", "")
        return extension[-1] #the last one should be the image FE, list swill also have .com and whatnot


	
	
	

    def createName(self, url):
	ext = self.getExt(url)
	end = url.find(ext)
	cutURL = url [:end]
	start = url.rfind("/")+1
	name = cutURL[start:]
	return name
    
    def saveImages(self, imageFolder, url):
	   	images = self.getImagesURLs(self, url)
	   	os.makedir(imageFolder)
	   	for image in images:
		   urllib2.urlretrieve(image, imageFolder)

   	


if __name__ == "__main__":

    grabber = Extract()
    images = Extract.getImageURLs(grabber, sys.argv[1])
    saveLoc = sys.argv[2]
    os.makedirs(saveLoc)
    for image in images:
    	filename=grabber.createName(image)+grabber.getExt(image)
	location = saveLoc + "/"+ filename
	urllib.urlretrieve(image, location)


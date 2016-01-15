from bs4 import BeautifulSoup
import urllib2
import difflib

TCGA_URL = 'https://tcga-data.nci.nih.gov/tcgafiles/ftp_auth/distro_ftpusers/anonymous/tumor/brca/bcr/nationwidechildrens.org/diagnostic_images/slide_images/'

page = urllib2.urlopen(TCGA_URL).read()
soup = BeautifulSoup(page)
#print(soup.prettify())

IMAGES = {}
UNIQUECOUNT = 0
DUPLICATECOUNT = 0
for link in soup.findAll('a', href=True):
    url = link['href']

    #print link.contents
    if(url[-1] == '/' and link.contents[0][0] == 'n' ):
        par = link.parent
        #print par.contents
        #Fetch this page
        subpage = urllib2.urlopen(TCGA_URL + url)
        soup2 = BeautifulSoup(subpage)

        for imgLink in soup2.findAll('a', href=True):
            imgurl = imgLink['href']
            if(imgurl.endswith('.svs')):
                if("DX1" in imgurl):
                    parentOfImg = imgLink.parent
                    imgID = imgurl[0:12]

                    downloadUrl =  TCGA_URL + url + imgurl
                    #print(downloadUrl)
                    #print imgID

                    if(IMAGES.has_key(imgID)):
                        #f print url + " " + IMAGES[imgID] + " "+ imgurl
                        #print IMAGES[imgID]
                        #print imgurl
                        if(IMAGES[imgID] == imgurl):
                            DUPLICATECOUNT+=1
                            #print(DUPLICATECOUNT)
                            #else:
                            #print(IMAGES[imgID], imgurl)
                            #print(difflib.ndiff(IMAGES[imgID], imgurl))

                    else:
                        #print "Nope"
                        UNIQUECOUNT+=1
                        print(UNIQUECOUNT)
                        IMAGES[imgID] =  imgurl

                    #print parentOfImg
                    #print ".."
                    #print("")
                    #print imgurl


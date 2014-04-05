import urllib, re, sys

def dlProgress(count, blockSize, totalSize):
      percent = int(count*blockSize*100/totalSize)
      sys.stdout.write("[" + "#"*(percent/10) + " "*(10 - (percent/10)) + "] %2d%%" % percent)
      sys.stdout.write("\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b")
      sys.stdout.flush()

def parse_page(url):
	image_regex = r"http:\/\/www\.facets\.la\/(fullview|thumbnail)\/._(.*)_(.*)\.jpg"
	
	stream = urllib.urlopen(url)
	response = stream.read()
	
	for x in re.findall(image_regex, response, re.MULTILINE):
		url = "http://www.facets.la/wallpaper/W_" + x[1] + "_" + x[2] + ".jpg"
		sys.stdout.write("Downloading " + x[1] + "_" + x[2] + "... ")    
		urllib.urlretrieve (url, x[1] + "_" + x[2]+".jpg", reporthook=dlProgress)
		print "\n"
	### Pagination support, incase you want to modify the program to not only get the wallpapers, but the fullviews on the main page.
		#print "\nMoving to next page...\n"
		#parse_page(re.findall(r'<div id="search-box-next"><a href="(http:\/\/www.facets.la\/offset\/[0-9]+\/)">', response, re.MULTILINE))
	###
parse_page("http://www.facets.la/wallpapers/")

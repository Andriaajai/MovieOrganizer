try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
from urllib.request import Request, urlopen 
import json
import os
import time

def remove_prefix(text, prefix):
	return text[len(prefix):] if text.startswith(prefix) else text 
# to search 

def findDetails(name):
	p=name.find("-")
	name=name[p+1:]
	p=name.find(")")
	name=name[:p+1]
	print("name :",name)
	result=[j for j in search(name, tld="co.in", num=10, stop=1, pause=2)]
	
	imdblink="NULL"
	for k in result:
		if "https://www.imdb.com/title/" in  k:
			imdblink=k
			break
	r=remove_prefix(imdblink,"https://www.imdb.com/title/")
	# r=imdblink.lstrip("https://www.imdb.com/title/");
	r=r.rstrip("/")
	print("IMDB ID: ",r)
	searchl="http://www.omdbapi.com/?apikey=a5401634&i="+r

	html = urlopen(searchl)
	data= json.load(html)
      #return data
	#print(data["Title"],data["imdbRating"])
	print(data)

files_path = [os.path.abspath(x) for x in os.listdir()]
files =[x for x in os.listdir()]
for i in files:
	# print("File : ",i)
	findDetails(i)
	time.sleep(1)







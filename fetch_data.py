import urllib2

request = urllib2.Request("https://www.theguardian.com/books/2016/dec/22/jk-rowling-reveals-shes-working-on-two-new-novels-harry-potter-robert-galbraith")
response = urllib2.urlopen(request)
# html = response.read()



from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(response)

# string = ""
data = []

table = soup.findAll('div', {"class":"content__article-body from-content-api js-article__body"})
for x in table:
	xTable = x.find_all('p')
	for p_tag in xTable:
		#print p_tag.text,p_tag.next_sibling
		# data.append(p_tag.text+p_tag.next_sibling)
		# string += p_tag.text
		# string += '\n\n'
		data.append(p_tag.text)

string = ""
for story in data:
	string += story.encode('ascii','ignore')
	string += "\n\n"

print string
		
f = open("story.txt", "w")
f.write(string)
f.close()


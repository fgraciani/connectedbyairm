# Created 8/10/2020
from bs4 import BeautifulSoup
import os

def create_html():
  # Create Index
  # Create page per class
  
  airm_pages_directory = "docs/advanced-viewer/1.0.0/LM"
  # creates docs/advanced-viewer/1.0.0/LM directory
  path = airm_pages_directory
  try:
      os.mkdir(path)
  except OSError:
      print ("Creation of the directory %s failed" % path)
  else:
      print ("Successfully created the directory %s " % path)
  import airm
  airm = airm.Airm()
  airm_logical_classes = airm.logical_classes.to_dict('records')

  #Create index page
  #creates soup for index using concept-list-template.html
  html = open("data/html/templates/airm-concept-list-template.html").read()
  soup = BeautifulSoup(html, "lxml") 

  #For each entry
    #create table entry
  for record in airm_logical_classes:
    tr = soup.new_tag("tr")

    td_ic_name = soup.new_tag("td")
    url = "LM/"+record["name"]+".html"
    text = record["name"]
    print(text)
    new_link = soup.new_tag("a")
    new_link['href'] = url
    new_link['target'] = "_blank"
    new_link.string = text
    td_ic_name.insert(1,new_link)
    tr.insert(1,td_ic_name)
    
    td = soup.new_tag("td")
    td.string = "-"
    tr.insert(2,td)

    if record["definition"] != "":
      td_def = soup.new_tag("td")
      td_def.string = str(record["definition"])
      tr.insert(3,td_def)

    td = soup.new_tag("td")
    td.string = "-"
    tr.insert(4,td)
    
    soup.find('tbody').insert(1,tr)

  f= open("docs/advanced-viewer/1.0.0/logical-model.html","w+")
  f.write(soup.prettify())
  f.close() 
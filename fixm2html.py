# Created 25/9/2020
from bs4 import BeautifulSoup
import os


def create_html():
  # Create Index
  # Create page per class
  
  mapping_pages_directory = "docs/developers/amxm-2.0.0-to-airm-1.0.0"
  # creates developers/amxm-2.0.0-to-airm-1.0.0 directory
  path = mapping_pages_directory
  try:
      os.mkdir(path)
  except OSError:
      print ("Creation of the directory %s failed" % path)
  else:
      print ("Successfully created the directory %s " % path)
  import fixm
  fixm = fixm.Fixm()
  fixm_mapping_dict = fixm.fixm_mapping_dataframe.to_dict('records')

  #Create index page
  #creates soup for data/html/templates/concept-list-template.html using fixm_mapping_template.html
  html = open("data/html/templates/concept-list-template.html").read()
  soup = BeautifulSoup(html, "lxml") 

  #For each entry
    #create table entry
  for record in fixm_mapping_dict:
    tr = soup.new_tag("tr")

    td_ic_name = soup.new_tag("td")
    url = "amxm-2.0.0-to-airm-1.0.0/"+record["Information Concept"]+".html"
    text = record["Information Concept"]
    new_link = soup.new_tag("a")
    new_link['href'] = url
    new_link['target'] = "_blank"
    new_link.string = text
    td_ic_name.insert(1,new_link)
    tr.insert(1,td_ic_name)

    if record["Data Concept"] != "":
      td_dc_name = soup.new_tag("td")
      td_dc_name.string = record["Data Concept"]

      url = "amxm-2.0.0-to-airm-1.0.0/"+record["Information Concept"]+".html"+"#"+record["Data Concept"]
      text = record["Data Concept"]
      print(text)
      new_link = soup.new_tag("a")
      new_link['href'] = url
      new_link['target'] = "_blank"
      new_link.string = text
      td_ic_name.insert(1,new_link)
      tr.insert(2,td_dc_name)

    if record["Definition"] != "":
      td_def = soup.new_tag("td")
      td_def.string = str(record["Definition"])
      tr.insert(3,td_def)

    td_type = soup.new_tag("td")
    td_type.string = record["Type"]
    tr.insert(4,td_type)
    
    soup.find('tbody').insert(1,tr)

  f= open("docs/developers/amxm-2.0.0-to-airm-1.0.0.html","w+")
  f.write(soup.prettify())
  f.close() 
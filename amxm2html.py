from bs4 import BeautifulSoup
import os

def create_html():
  mapping_pages_directory = "docs/developers/amxm-2.0.0-to-airm-1.0.0"
  # creates docs/developers/amxm-2.0.0-to-airm-1.0.0 directory
  path = mapping_pages_directory
  try:
      os.mkdir(path)
  except OSError:
      print ("Creation of the directory %s failed" % path)
  else:
      print ("Successfully created the directory %s " % path)
  
  import amxm
  amxm = amxm.Amxm()
  amxm_mapping_dict = amxm.amxm_mapping_dataframe.to_dict('records')
  amxm_enum_mapping_dict = amxm.amxm_mapping_enum_dataframe.to_dict('records')

  #Create index page
  #creates soup for developers/amxm-2.2.0-to-airm-1.0.0.html using amxm_mapping_template.html
  html = open("data/html/templates/AMXM-list-template.html").read()
  soup = BeautifulSoup(html, "lxml") 

  #For each entry
    #create table entry
  for record in amxm_mapping_dict:
    tr = soup.new_tag("tr")
    print(record)
    print("\n")

    td_ic_name = soup.new_tag("td")
    if str(record["Information Concept"]) != "missing data" and str(record["Information Concept"]) != "":
      if str(record["Data Concept"]) == "missing data" or str(record["Data Concept"]) == "":
        url = "amxm-2.0.0-to-airm-1.0.0/"+record["Information Concept"]+".html"
        text = record["Information Concept"]
        #print(text)
        new_link = soup.new_tag("a")
        new_link['href'] = url
        new_link['target'] = "_blank"
        new_link.string = text
        td_ic_name.insert(1,new_link)
      else:
        td_ic_name.string = record["Information Concept"]
    else:
      td_ic_name.string = "-"
    tr.insert(0,td_ic_name)

    td_dc_name = soup.new_tag("td")
    if str(record["Data Concept"]) != "missing data" and str(record["Data Concept"]) != "":
      url = "amxm-2.0.0-to-airm-1.0.0/"+record["Information Concept"]+".html"+"#"+record["Data Concept"]
      text = record["Data Concept"]
      #print(text)
      new_link = soup.new_tag("a")
      new_link['href'] = url
      new_link['target'] = "_blank"
      new_link.string = text
      td_dc_name.insert(1,new_link)
    else:
      td_dc_name.string = "-"
    tr.insert(1,td_dc_name)

    td_def = soup.new_tag("td")
    if str(record["Concept Definition"]) != "missing data":
      definition = str(record["Concept Definition"])
      td_def.string = definition.replace("Definition: ","")
    else:
      td_def.string = "-"
    tr.insert(2,td_def)

    #td_dc_type = soup.new_tag("td")
    #if str(record["Data Concept's Basic Type"]) != "missing data":
    #  parts = str(record["Data Concept's Basic Type"]).split(":")
    #  clean_type = parts[-1]
    #  url = "amxm-2.0.0-to-airm-1.0.0/"+clean_type+".html"
    #  text = clean_type
    #  print(text)
    #  new_link = soup.new_tag("a")
    #  new_link['href'] = url
    #  new_link['target'] = "_blank"
    #  new_link.string = text
    #  td_dc_type.insert(1,new_link)
    #else:
    #  td_dc_type = soup.new_tag("td")
    #  td_dc_type.string = "-"
    #tr.insert(3,td_dc_type)
    
    soup.find('tbody').insert(1,tr)
  
  for record in amxm_enum_mapping_dict:
    tr = soup.new_tag("tr")
    print(record)
    print("\n")

    td_ic_name = soup.new_tag("td")
    if str(record["Information Concept"]) != "missing data" and str(record["Information Concept"]) != "":
      if str(record["Data Concept"]) == "missing data" or str(record["Data Concept"]) == "":
        url = "amxm-2.0.0-to-airm-1.0.0/"+record["Information Concept"]+".html"
        text = record["Information Concept"]
        #print(text)
        new_link = soup.new_tag("a")
        new_link['href'] = url
        new_link['target'] = "_blank"
        new_link.string = text
        td_ic_name.insert(1,new_link)
      else:
        td_ic_name.string = record["Information Concept"]
    else:
      td_ic_name.string = "-"
    tr.insert(0,td_ic_name)

    td_dc_name = soup.new_tag("td")
    if str(record["Data Concept"]) != "missing data" and str(record["Data Concept"]) != "":
      url = "amxm-2.0.0-to-airm-1.0.0/"+record["Information Concept"]+".html"+"#"+record["Data Concept"]
      text = record["Data Concept"]
      #print(text)
      new_link = soup.new_tag("a")
      new_link['href'] = url
      new_link['target'] = "_blank"
      new_link.string = text
      td_dc_name.insert(1,new_link)
    else:
      td_dc_name.string = "-"
    tr.insert(1,td_dc_name)

    td_def = soup.new_tag("td")
    if str(record["Concept Definition"]) != "missing data":
      td_def.string = str(record["Concept Definition"])
    else:
      td_def.string = "-"
    tr.insert(2,td_def)

#    td_dc_type = soup.new_tag("td")
#    if str(record["Data Concept's Basic Type"]) != "missing data":
#      parts = str(record["Data Concept's Basic Type"]).split(":")
#      clean_type = parts[-1]
#      url = "amxm-2.0.0-to-airm-1.0.0/"+clean_type+".html"
#      text = clean_type
#      #print(text)
#      new_link = soup.new_tag("a")
#      new_link['href'] = url
#      new_link['target'] = "_blank"
#      new_link.string = text
#      td_dc_type.insert(1,new_link)
#    else:
#      td_dc_type = soup.new_tag("td")
#      td_dc_type.string = "-"
#    tr.insert(3,td_dc_type)
    
    soup.find('tbody').insert(1,tr) 

  f= open("docs/developers/amxm-2.0.0-to-airm-1.0.0.html","w+")
  f.write(soup.prettify())
  f.close() 


  


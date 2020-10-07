# Created 25/9/2020
from bs4 import BeautifulSoup
import os


def create_html():
  # Create Index
  # Create page per class
  
  mapping_pages_directory = "docs/developers/fixm-4.2.0-to-airm-1.0.0"
  # creates developers/docs/developers/fixm-4.2.0-to-airm-1.0.0 directory
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
  #creates soup for index using concept-list-template.html
  html = open("data/html/templates/concept-list-template.html").read()
  soup = BeautifulSoup(html, "lxml") 

  #For each entry
    #create table entry
  for record in fixm_mapping_dict:
    tr = soup.new_tag("tr")

    td_ic_name = soup.new_tag("td")
    url = "fixm-4.2.0-to-airm-1.0.0/"+record["Information Concept"]+".html"
    text = record["Information Concept"]
    print(text)
    new_link = soup.new_tag("a")
    new_link['href'] = url
    new_link['target'] = "_blank"
    new_link.string = text
    td_ic_name.insert(1,new_link)
    tr.insert(1,td_ic_name)

    if record["Data Concept"] != "":
      td_dc_name = soup.new_tag("td")
      url = "fixm-4.2.0-to-airm-1.0.0/"+record["Information Concept"]+".html"+"#"+record["Data Concept"]
      text = record["Data Concept"]
      print(text)
      new_link = soup.new_tag("a")
      new_link['href'] = url
      new_link['target'] = "_blank"
      new_link.string = text
      td_dc_name.insert(1,new_link)
      tr.insert(2,td_dc_name)

    if record["Definition"] != "":
      td_def = soup.new_tag("td")
      td_def.string = str(record["Definition"])
      tr.insert(3,td_def)

    td_type = soup.new_tag("td")
    td_type.string = record["Type"]
    tr.insert(4,td_type)
    
    soup.find('tbody').insert(1,tr)

  f= open("docs/developers/fixm-4.2.0-to-airm-1.0.0.html","w+")
  f.write(soup.prettify())
  f.close() 

def print_create_html_pages():
  import fixm
  fixm = fixm.Fixm()
  fixm_info_concepts_dict = fixm.get_information_concepts()

  for info_concept in fixm_info_concepts_dict:
    print(info_concept['Information Concept'])
    traces = fixm.get_traces_by_info_concept(info_concept['Information Concept'])
    for trace in traces:
      print('\t'+trace['Data Concept'])
      print('\t\tSemantic Corresponce:')
      sem_correspondences = str(trace['Semantic Correspondence']).split('\n')
      for line in sem_correspondences:
        print('\t\t\t'+line)
      print('\t\tAdditional Traces:')
      add_correspondences = str(trace['Additional Traces']).split('\n')
      for line in add_correspondences:
        print('\t\t\t'+line)

def create_html_pages():
  import fixm
  fixm = fixm.Fixm()
  fixm_info_concepts_dict = fixm.get_information_concepts()

  for info_concept in fixm_info_concepts_dict:
    print(info_concept['Information Concept'])
    #creates soup for concept page using concept-template.html
    html = open("data/html/templates/concept-template.html").read()
    soup = BeautifulSoup(html, "lxml") 
    
    #span = soup.new_tag("span")
    #span.string = str(info_concept['Information Concept'])
    #soup.find(id="BC_INFO_CONCEPT_NAME").insert(0,span)

    soup.find(text="FIXM_CLASS_NAME_BC").replace_with(str(info_concept['Information Concept']))

    h2 = soup.new_tag("h2")
    h2.string = str(info_concept['Information Concept'])
    soup.find(id="INFO_CONCEPT_NAME").insert(0,h2)
    
    traces = fixm.get_traces_by_info_concept(info_concept['Information Concept'])
    for trace in traces:
      print('\t'+trace['Data Concept'])
      
      tr = soup.new_tag("tr")

      if trace["Data Concept"] != "":
        td_dc_name = soup.new_tag("td")
        url = "#"+trace["Data Concept"]
        text = trace["Data Concept"]
        new_link = soup.new_tag("a")
        new_link['href'] = url
        new_link.string = text
        td_dc_name.insert(1,new_link)
        tr.insert(1,td_dc_name)
      
      if trace["Definition"] != "":
        td_def = soup.new_tag("td")
        td_def.string = str(trace["Definition"])
        tr.insert(2,td_def)

      soup.find(id="DATA_CONCEPTS_LIST").insert(1,tr)


      print('\t\tSemantic Corresponce:')
      sem_correspondences = str(trace['Semantic Correspondence']).split('\n')
      for line in sem_correspondences:
        print('\t\t\t'+line)
      print('\t\tAdditional Traces:')
      add_correspondences = str(trace['Additional Traces']).split('\n')
      for line in add_correspondences:
        print('\t\t\t'+line)
    
    f= open("docs/developers/fixm-4.2.0-to-airm-1.0.0/"+str(info_concept['Information Concept'])+".html","w+")
    f.write(soup.prettify())
    f.close()
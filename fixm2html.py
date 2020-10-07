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
    #soup.find(id="BC_INFO_CONCEPT_NAME").insert(0,span)span = soup.new_tag("span")
    #span.string = str(info_concept['Information Concept'])

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
      
      if trace["Type"] != "":
        td_def = soup.new_tag("td")
        td_def.string = str(trace["Type"])
        tr.insert(3,td_def)
      
      soup.find(id="DATA_CONCEPTS_LIST").insert(1,tr)

    for trace in traces:
      property_div = soup.new_tag("div")
      property_div["style"] = "border: 0.5px solid #b2b2b2;border-radius: 4px;box-shadow: 2px 2px #b2b2b2;padding: 15px;padding-bottom: 0px;"

      h3 = soup.new_tag("h3")
      h3.string = str(trace["Data Concept"])
      property_div.insert(1,h3)
      
      p = soup.new_tag("p")
      p.string = str(trace["Definition"])
      br = soup.new_tag("br")
      p.insert(2,br)
      property_div.insert(2,p)
      
      p = soup.new_tag("p")
      p.string = "Type:&nbsp;"
      span = soup.new_tag("span")
      span.string = str(trace['Type'])
      p.insert(2,span)
      property_div.insert(3,p)

      h4 = soup.new_tag("h4")
      h4.string = "Semantic Correspondence"
      h4['style'] = "margin-top: 40px;"
      property_div.insert(4,h4)

      sc_div = soup.new_tag("div")
      sc_div["class"] = "table-responsive"
      sc_table = soup.new_tag("table")
      sc_table["class"] = "table"
      sc_thead = soup.new_tag("thead")
      tr = soup.new_tag("tr")
      th = soup.new_tag("th")
      th.string = "AIRM Concept"
      tr.insert(1,th)
      th = soup.new_tag("th")
      th.string = "Definition"
      tr.insert(2,th)
      sc_thead.insert(1,tr)
      sc_table.insert(1,sc_thead)
      tbody = soup.new_tag("tbody")
      #for each insert row
      print('\t\tSemantic Corresponce:')
      sem_correspondences = str(trace['Semantic Correspondence']).split('\n')
      for line in sem_correspondences:
        print('\t\t\t'+line)
        tr = soup.new_tag("tr")
        td = soup.new_tag("td")
        td.string = "dddddddddddddddddddAIRM Concept"
        tr.insert(1,td)
        td = soup.new_tag("td")
        td.string = "ddddddddddd ddddddddd dddddddd ddddDefinition"
        tr.insert(2,td)
        tbody.insert(1,tr)

      sc_table.insert(2,tbody)
      sc_div.insert(1,sc_table)
      property_div.insert(5,sc_div)

      h5 = soup.new_tag("h5")
      h5.string = "Additional Traces"
      property_div.insert(6,h5)

      add_div = soup.new_tag("div")
      add_div["class"] = "table-responsive"
      add_table = soup.new_tag("table")
      add_table["class"] = "table"
      add_thead = soup.new_tag("thead")
      tr = soup.new_tag("tr")
      th = soup.new_tag("th")
      th.string = "AIRM Concept"
      tr.insert(1,th)
      th = soup.new_tag("th")
      th.string = "Definition"
      tr.insert(2,th)
      add_thead.insert(1,tr)
      add_table.insert(1,add_thead)
      tbody = soup.new_tag("tbody")
      #for each insert row
      print('\t\tAdditional Traces:')
      add_correspondences = str(trace['Additional Traces']).split('\n')
      for line in add_correspondences:
        print('\t\t\t'+line)
        tr = soup.new_tag("tr")
        td = soup.new_tag("td")
        td.string = "dddddddddddddddddddAIRM Concept"
        tr.insert(1,td)
        td = soup.new_tag("td")
        td.string = "ddddddddddd ddddddddd dddddddd ddddDefinition"
        tr.insert(2,td)
        tbody.insert(1,tr)

      add_table.insert(2,tbody)
      add_div.insert(1,add_table)
      property_div.insert(7,add_div)

      h5 = soup.new_tag("h5")
      h5.string = "Rationale"
      property_div.insert(8,h5)

      p = soup.new_tag("p")
      p.string = trace["Rationale"]
      property_div.insert(9,h4)

      h4 = soup.new_tag("h4")
      h4.string = "Notes"
      property_div.insert(10,h4)

      p = soup.new_tag("p")
      p.string = trace["Rationale"]
      property_div.insert(11,h4)

      soup.find(id="DATA_CONCEPTS_DETAIL").insert(1,property_div)

    f= open("docs/developers/fixm-4.2.0-to-airm-1.0.0/"+str(info_concept['Information Concept'])+".html","w+")
    f.write(soup.prettify())
    f.close()
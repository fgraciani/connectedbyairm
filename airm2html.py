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
  airm_logical_properties = airm.logical_properties.to_dict('records')

  #Create index page
  #creates soup for index using concept-list-template.html
  html = open("data/html/templates/airm-concept-list-template.html").read()
  soup = BeautifulSoup(html, "lxml") 

  #For each entry
    #create table entry
  for record in airm_logical_classes:
    tr = soup.new_tag("tr")

    td_ic_name = soup.new_tag("td")
    td_ic_name["data-order"] = record["name"]
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

  for record in airm_logical_properties:
    tr = soup.new_tag("tr")
    
    td = soup.new_tag("td")
    td["data-order"] = record["parent"]
    td.string = record["parent"]
    tr.insert(1,td)

    td_ic_name = soup.new_tag("td")
    td_ic_name["data-order"] = record["name"]
    url = "LM/"+record["parent"]+".html#"+record["name"]
    text = record["name"]
    print(text)
    new_link = soup.new_tag("a")
    new_link['href'] = url
    new_link['target'] = "_blank"
    new_link.string = text
    td_ic_name.insert(1,new_link)
    tr.insert(2,td_ic_name)

    if record["definition"] != "":
      td_def = soup.new_tag("td")
      td_def.string = str(record["definition"])
      tr.insert(3,td_def)

    td = soup.new_tag("td")
    td.string = record["type"]
    tr.insert(4,td)
    
    soup.find('tbody').insert(1,tr)
  f= open("docs/advanced-viewer/1.0.0/logical-model.html","w+")
  f.write(soup.prettify())
  f.close() 

def create_html_pages():
  import airm
  my_airm = airm.Airm()
  airm_logical_classes = my_airm.logical_classes.to_dict('records')

  for info_concept in airm_logical_classes:
    if info_concept['name']!="missing data":
      print(info_concept['name'])
      #creates soup for concept page using concept-template.html
      html = open("data/html/templates/airm-concept-template.html").read()
      soup = BeautifulSoup(html, "lxml") 
      
      #span = soup.new_tag("span")
      #span.string = str(info_concept['Information Concept'])
      #soup.find(id="BC_INFO_CONCEPT_NAME").insert(0,span)span = soup.new_tag("span")
      #span.string = str(info_concept['Information Concept'])
      #soup.find(text="CONCEPT_NAME_HERE").replace_with(str(info_concept['name']))
      soup.title.string = str(info_concept['name'])+" - Logical Model | AIRM.aero"

      soup.find(text="FIXM_CLASS_NAME_BC").replace_with(str(info_concept['name']))

      h2 = soup.new_tag("h2")
      h2.string = str(info_concept['name'])
      soup.find(id="INFO_CONCEPT_NAME").insert(0,h2)
      code = soup.new_tag("code")
      code.string = info_concept['urn']
      code["class"] = "text-secondary"
      soup.find(id="INFO_CONCEPT_NAME").insert(1,code)
      
      soup.find(text="FIXM_CLASS_DEFINITION").replace_with(str(info_concept['definition']))

      traces = airm.get_properties_by_parent(my_airm, info_concept['name'])
      if traces != None:
        for trace in traces:
          print('\t'+trace['name'])
          
          tr = soup.new_tag("tr")

          if trace["name"] != "":
            td_dc_name = soup.new_tag("td")
            url = "#"+trace["name"]
            text = trace["name"]
            new_link = soup.new_tag("a")
            new_link['href'] = url
            new_link.string = text
            td_dc_name.insert(1,new_link)
            tr.insert(1,td_dc_name)
          
          if trace["definition"] != "":
            td_def = soup.new_tag("td")
            td_def.string = str(trace["definition"])
            tr.insert(2,td_def)
          
          if trace["type"] != "":
            td_dc_type = soup.new_tag("td")
            url = trace["type"]+".html"
            text = trace["type"]
            new_link = soup.new_tag("a")
            new_link['href'] = url
            new_link.string = text
            td_dc_type.insert(1,new_link)
            tr.insert(3,td_dc_type)
          
          soup.find(id="DATA_CONCEPTS_LIST").insert(1,tr)

        for trace in traces:
          property_div = soup.new_tag("div")
          property_div["style"] = "border: 0.5px solid #b2b2b2;border-radius: 4px;box-shadow: 2px 2px #b2b2b2;padding: 15px;padding-bottom: 0px; margin-bottom: 30px"

          h3 = soup.new_tag("h3")
          h3.string = str(trace["name"])
          h3["id"] = str(trace["name"])
          h3["data-toggle"] = "tooltip"
          h3["data-placement"] = "right"
          h3["title"] = trace["urn"]
          property_div.insert(0,h3)

          code = soup.new_tag("code")
          identifier = trace['urn']
          code.string = identifier
          code["class"] = "text-secondary"
          property_div.insert(1,code)
          
          p = soup.new_tag("p")
          p.string = str(trace["definition"])
          br = soup.new_tag("br")
          p.insert(2,br)
          property_div.insert(2,p)
          
          p = soup.new_tag("p")
          p.string = "type: "
          span = soup.new_tag("span")
          url = trace["type"]+".html"
          text = trace["type"]
          new_link = soup.new_tag("a")
          new_link['href'] = url
          new_link.string = text
          span.insert(1,new_link)
          p.insert(2,span)
          property_div.insert(3,p)

          connections = airm.get_connections_by_urn(my_airm, trace['urn'])
          if connections != None:
            p = soup.new_tag("p")
            button = soup.new_tag("button")
            button["class"] = "btn btn-light"
            button["type"] = "button"
            button["data-toggle"] = "collapse"
            button["data-target"] = "#"+str(trace["name"])+"collapse"
            button["aria-expanded"] = "false"
            button["aria-controls"] = "collapseExample"
            button.string = "Show presence in mappings"
            p.insert(1,button)
            property_div.insert(4,p)

            sc_div = soup.new_tag("div")
            sc_div["class"] = "table-responsive collapse"
            sc_div["id"] = str(trace["name"])+"collapse"
            sc_table = soup.new_tag("table")
            sc_table["class"] = "table"
            sc_thead = soup.new_tag("thead")
            tr = soup.new_tag("tr")
            th = soup.new_tag("th")
            th.string = "Model"
            tr.insert(1,th)
            th = soup.new_tag("th")
            th.string = "Concept"
            tr.insert(2,th)
            sc_thead.insert(1,tr)
            sc_table.insert(1,sc_thead)
            tbody = soup.new_tag("tbody")
            #for each insert row
            #print('\t\tPresence in Mappings:')
          
            for entry in connections:
              #print('\t\t\t'+line)
              tr = soup.new_tag("tr")
              if entry["model_name"] == "FIXM 4.2.0":
                td = soup.new_tag("td")
                url = "../../../developers/fixm-4.2.0-to-airm-1.0.0.html"
                text = "FIXM 4.2.0"
                a = soup.new_tag("a")
                a['href'] = url
                a['target'] = "_blank"
                a.string = text
                td.insert(1,a)
                tr.insert(1,td)
                td = soup.new_tag("td")
                parts = str(entry["concept_id"]).split(":")
                url = "../../../developers/fixm-4.2.0-to-airm-1.0.0/"+parts[1]+".html#"+entry["concept_name"]
                text = entry["concept_name"]
                a = soup.new_tag("a")
                a['href'] = url
                a['target'] = "_blank"
                a["data-toggle"] = "tooltip"
                a["data-placement"] = "left"
                a["title"] = entry["concept_id"]
                a.string = text
                td.insert(1,a)
                tr.insert(2,td)
              tbody.insert(1,tr)

            sc_table.insert(2,tbody)
            sc_div.insert(1,sc_table)
            property_div.insert(5,sc_div)

          soup.find(id="DATA_CONCEPTS_DETAIL").insert(1,property_div)

      f= open("docs/advanced-viewer/1.0.0/LM/"+str(info_concept['name'])+".html","w+")
      f.write(soup.prettify())
      f.close()
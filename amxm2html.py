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
        td_ic_name["data-order"] = record["Information Concept"]
      else:
        td_ic_name.string = record["Information Concept"]
        td_ic_name["data-order"] = record["Information Concept"]
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
      td_dc_name["data-order"] = record["Data Concept"]
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
        td_ic_name["data-order"] = record["Information Concept"]
      else:
        td_ic_name.string = record["Information Concept"]
        td_ic_name["data-order"] = record["Information Concept"]
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
      td_dc_name["data-order"] = record["Data Concept"]
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

def create_url(urn):
  issue_url=""
  url=""
  if isinstance(urn, str):
    if urn.startswith("changeRequest"):
      url="https://ext.eurocontrol.int/swim_confluence/display/SWIM/SWIM-INFO-014+Forms+of+semantic+correspondence"
    elif urn=="outOfScope":
      url="https://ext.eurocontrol.int/swim_confluence/display/SWIM/SWIM-INFO-015+Out-of-scope+or+no+correspondence"
    elif urn.startswith("noSemanticCorrespondence"):
      url=issue_url
    elif urn.startswith("urn"):
      components = urn.split(":")
      last_component = components[-1]
      components = last_component.split("@")
      entity = components[0]
      prop = ""
      if len(components) == 2:
        prop = components[1]
      url="../../viewer/1.0.0/logical-model/"+entity+"#"+prop
  return url

def create_name(urn):
  name=""
  if isinstance(urn, str):
    if urn.startswith("changeRequest"):
      name="AIRM Change Request"
    elif urn=="outOfScope":
      name="Out of Scope"
    elif urn.startswith("noSemanticCorrespondence"):
      name="No Semantic Correspondence"
    elif urn.startswith("urn"):
      components = urn.split(":")
      last_component = components[-1]
      name = last_component
  return name

def create_html_pages():
  import amxm
  import airm
  amxm = amxm.Amxm()
  airm = airm.Airm()
  amxm_info_concepts_dict = amxm.get_information_concepts()

  for info_concept in amxm_info_concepts_dict:
    if info_concept['Information Concept']!="missing data":
      print(info_concept['Information Concept'])
      #creates soup for concept page using concept-template.html
      html = open("data/html/templates/AMXM-concept-template.html").read()
      soup = BeautifulSoup(html, "lxml") 
      
      #span = soup.new_tag("span")
      #span.string = str(info_concept['Information Concept'])
      #soup.find(id="BC_INFO_CONCEPT_NAME").insert(0,span)span = soup.new_tag("span")
      #span.string = str(info_concept['Information Concept'])
      soup.title.string = str(info_concept['Information Concept'])+" - AMXM 2.0.0 to AIRM 1.0.0 | AIRM.aero"
  
      soup.find(text="FIXM_CLASS_NAME_BC").replace_with(str(info_concept['Information Concept']))

      definition = str(info_concept["Concept Definition"])
      definition = definition.replace("Definition: ","")
      soup.find(text="FIXM_CLASS_DEFINITION").replace_with(definition)

      h2 = soup.new_tag("h2")
      h2.string = str(info_concept['Information Concept'])
      soup.find(id="INFO_CONCEPT_NAME").insert(0,h2)
      code = soup.new_tag("code")
      datac_identifier = info_concept['Concept Identifier']
      
      code.string = datac_identifier
      code["class"] = "text-secondary"
      soup.find(id="INFO_CONCEPT_NAME").insert(1,code)
      
      traces = amxm.get_traces_by_info_concept(info_concept['Information Concept'])
      for trace in traces:
        if trace['Data Concept'] != "missing data":
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
          
          if trace["Concept Definition"] != "":
            td_def = soup.new_tag("td")
            definition = str(trace["Concept Definition"])
            definition = definition.replace("Definition: ","")
            td_def.string = definition
            tr.insert(2,td_def)
                  
          soup.find(id="DATA_CONCEPTS_LIST").insert(1,tr)

      for trace in traces:
        if trace['Data Concept'] != "missing data":

          property_div = soup.new_tag("div")
          property_div["style"] = "border: 0.5px solid #b2b2b2;border-radius: 4px;box-shadow: 2px 2px #b2b2b2;padding: 15px;padding-bottom: 0px; margin-bottom: 30px"

          h3 = soup.new_tag("h3")
          h3.string = str(trace["Data Concept"])
          h3["id"] = str(trace["Data Concept"])
          h3["style"] = "padding-top: 120px; margin-top: -120px;"
          property_div.insert(0,h3)

          code = soup.new_tag("code")
          identifier = trace['Concept Identifier']
          code.string = identifier
          code["class"] = "text-secondary"
          property_div.insert(1,code)
          
          p = soup.new_tag("p")
          definition = str(trace["Concept Definition"])
          definition = definition.replace("Definition: ","")
          p.string = definition
          br = soup.new_tag("br")
          p.insert(2,br)
          property_div.insert(2,p)
          
          sc_h5 = soup.new_tag("h5")
          sc_h5.string = "Semantic Correspondence"
          sc_h5['style'] = "margin-top: 40px;"
          property_div.insert(3,sc_h5)

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
          if str(trace['AIRM Concept Identifier']) == "missing data":
              tr = soup.new_tag("tr")
              td = soup.new_tag("td")
              line = str(trace['Special Case'])
              url = create_url(line)
              text = create_name(line)
              a = soup.new_tag("a")
              a['href'] = url
              a['target'] = "_blank"
              a.string = text
              
              a["data-toggle"] = "tooltip"
              a["data-placement"] = "right"
              a["title"] = line

              td.insert(1,a)
              tr.insert(1,td)
              td = soup.new_tag("td")
              airm_entry = airm.load_and_find_urn(line)
              td.string = airm_entry["definition"]
              tr.insert(2,td)
              tbody.insert(1,tr)
          else:
            sem_correspondences = str(trace['AIRM Concept Identifier']).split('\n')
            for line in sem_correspondences:
              print('\t\t\t'+line)
              tr = soup.new_tag("tr")
              td = soup.new_tag("td")
              
              url = create_url(line)
              text = create_name(line)
              a = soup.new_tag("a")
              a['href'] = url
              a['target'] = "_blank"
              a.string = text
              
              a["data-toggle"] = "tooltip"
              a["data-placement"] = "right"
              a["title"] = line

              td.insert(1,a)
              tr.insert(1,td)
              td = soup.new_tag("td")
              airm_entry = airm.load_and_find_urn(line)
              td.string = airm_entry["definition"]
              tr.insert(2,td)
              tbody.insert(1,tr)

          sc_table.insert(2,tbody)
          sc_div.insert(1,sc_table)
          property_div.insert(4,sc_div)

          
          

          
          
          if str(trace["Rationale"]) != "missing data":
            h5 = soup.new_tag("h5")
            h5.string = "Rationale"
            property_div.insert(5,h5)

            p = soup.new_tag("p")
            p.string = str(trace["Rationale"])
            print('Rationale:'+str(trace["Rationale"]))
            property_div.insert(6,p)
          
          if str(trace["Remarks"]) != "missing data":
            notes_h5 = soup.new_tag("h5")
            notes_h5.string = "Remarks"
            property_div.insert(7,notes_h5)

            p = soup.new_tag("p")
            p.string = str(trace["Remarks"])
            print('Remarks:'+str(trace["Remarks"]))
            property_div.insert(8,p)

          top_link_p = soup.new_tag("p")
          new_link = soup.new_tag("a")
          new_link['href'] = "#top"
          new_icon = soup.new_tag("i")
          new_icon['class'] = "fa fa-arrow-circle-up"
          new_icon["data-toggle"] = "tooltip"
          new_icon["data-placement"] = "left"
          new_icon["title"] = "Top of page"
          new_link.insert(1,new_icon)
          top_link_p.insert(1,new_link)
          top_link_p['class'] =   "text-right"
          property_div.insert(9,top_link_p)

          soup.find(id="DATA_CONCEPTS_DETAIL").insert(1,property_div)

      f= open("docs/developers/amxm-2.0.0-to-airm-1.0.0/"+str(info_concept['Information Concept'])+".html","w+")
      f.write(soup.prettify())
      f.close()


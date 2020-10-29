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
  soup.title.string = "FIXM 4.2.0 to AIRM 1.0.0 | AIRM.aero"

  #For each entry
    #create table entry
  for record in fixm_mapping_dict:
    tr = soup.new_tag("tr")

    td_ic_name = soup.new_tag("td")
    td_ic_name.string = str(record["Information Concept"])
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

    if record["Type"] != "":
      td_dc_type = soup.new_tag("td")
      parts = str(record["Type"]).split(":")
      clean_type = parts[-1]
      #url = "fixm-4.2.0-to-airm-1.0.0/"+clean_type+".html"
      #text = clean_type
      print(text)
      td_dc_type.string = clean_type
      #new_link = soup.new_tag("a")
      #new_link['href'] = url
      #new_link['target'] = "_blank"
      #new_link.string = text
      #td_dc_type.insert(1,new_link)
      tr.insert(4,td_dc_type)
    
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

def create_url(urn):
  issue_url="http://fixm.aero"
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
      url="../../advanced-viewer/1.0.0/LM/"+entity+"#"+prop
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
  import fixm
  import airm
  fixm = fixm.Fixm()
  airm = airm.Airm()
  fixm_info_concepts_dict = fixm.get_information_concepts()

  for info_concept in fixm_info_concepts_dict:
    if info_concept['Information Concept']!="missing data":
      print(info_concept['Information Concept'])
      #creates soup for concept page using concept-template.html
      html = open("data/html/templates/concept-template.html").read()
      soup = BeautifulSoup(html, "lxml") 
      
      #span = soup.new_tag("span")
      #span.string = str(info_concept['Information Concept'])
      #soup.find(id="BC_INFO_CONCEPT_NAME").insert(0,span)span = soup.new_tag("span")
      #span.string = str(info_concept['Information Concept'])
      soup.title.string = str(info_concept['Information Concept'])+" - FIXM 4.2.0 to AIRM 1.0.0 | AIRM.aero"
  
      soup.find(text="FIXM_CLASS_NAME_BC").replace_with(str(info_concept['Information Concept']))

      h2 = soup.new_tag("h2")
      h2.string = str(info_concept['Information Concept'])
      soup.find(id="INFO_CONCEPT_NAME").insert(0,h2)
      code = soup.new_tag("code")
      datac_identifier = info_concept['Identifier']
      parts = datac_identifier.split(":")
      identifier = parts[0]+":"+parts[1]
      code.string = identifier
      code["class"] = "text-secondary"
      soup.find(id="INFO_CONCEPT_NAME").insert(1,code)
      
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
          td_type = soup.new_tag("td")
          if trace["Type"] != "enum value":
            parts = str(trace["Type"]).split(":")
            clean_type = parts[-1]
            url = clean_type+".html"
            text = clean_type
            print(text)
            new_link = soup.new_tag("a")
            new_link['href'] = url
            new_link['target'] = "_blank"
            new_link.string = text
            td_type.insert(1,new_link)
          else:
            td_type.string = str(trace["Type"])
          tr.insert(3,td_type)
        
        soup.find(id="DATA_CONCEPTS_LIST").insert(1,tr)

      for trace in traces:
        property_div = soup.new_tag("div")
        property_div["style"] = "border: 0.5px solid #b2b2b2;border-radius: 4px;box-shadow: 2px 2px #b2b2b2;padding: 15px;padding-bottom: 0px; margin-bottom: 30px"

        h3 = soup.new_tag("h3")
        h3.string = str(trace["Data Concept"])
        h3["id"] = str(trace["Data Concept"])
        property_div.insert(0,h3)

        code = soup.new_tag("code")
        identifier = trace['Identifier']
        code.string = identifier
        code["class"] = "text-secondary"
        property_div.insert(1,code)
        
        p = soup.new_tag("p")
        p.string = str(trace["Definition"])
        br = soup.new_tag("br")
        p.insert(2,br)
        property_div.insert(2,p)
        
        p = soup.new_tag("p")
        p.string = "Type: "
        span = soup.new_tag("span")
        if trace["Type"] != "enum value":
            parts = str(trace["Type"]).split(":")
            clean_type = parts[-1]
            url = clean_type+".html"
            text = clean_type
            print(text)
            new_link = soup.new_tag("a")
            new_link['href'] = url
            new_link['target'] = "_blank"
            new_link.string = text
            span.insert(1,new_link)
        else:
            span.string = str(trace["Type"])
        p.insert(2,span)
        property_div.insert(3,p)

        sc_h5 = soup.new_tag("h5")
        sc_h5.string = "Semantic Correspondence"
        sc_h5['style'] = "margin-top: 40px;"
        property_div.insert(4,sc_h5)

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
        property_div.insert(5,sc_div)

        add_correspondences = str(trace['Additional Traces']).split('\n')
        if len(add_correspondences) > 0:
          if add_correspondences[0] != "missing data":

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
        
            for line in add_correspondences:
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

            add_table.insert(2,tbody)
            add_div.insert(1,add_table)
            property_div.insert(7,add_div)
        
        if str(trace["Rationale"]) != "missing data":
          h5 = soup.new_tag("h5")
          h5.string = "Rationale"
          property_div.insert(8,h5)

          p = soup.new_tag("p")
          p.string = str(trace["Rationale"])
          print('Rationale:'+str(trace["Rationale"]))
          property_div.insert(9,p)
        
        if str(trace["Notes"]) != "missing data":
          notes_h5 = soup.new_tag("h5")
          notes_h5.string = "Notes"
          property_div.insert(10,notes_h5)

          p = soup.new_tag("p")
          p.string = str(trace["Notes"])
          print('NOTES:'+str(trace["Notes"]))
          property_div.insert(11,p)
        
        top_link_p = soup.new_tag("p")
        new_link = soup.new_tag("a")
        new_link['href'] = "#top"
        new_icon = soup.new_tag("i")
        new_icon['class'] = "fa fa-arrow-circle-up"
        new_link.insert(1,new_icon)
        top_link_p.insert(1,new_link)
        top_link_p['class'] =   "text-right"
        property_div.insert(12,top_link_p)

        soup.find(id="DATA_CONCEPTS_DETAIL").insert(1,property_div)

      f= open("docs/developers/fixm-4.2.0-to-airm-1.0.0/"+str(info_concept['Information Concept'])+".html","w+")
      f.write(soup.prettify())
      f.close()
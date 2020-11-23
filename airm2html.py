# Created 8/10/2020
from bs4 import BeautifulSoup
import os

def create_index_logical_global():
  import airm100
  airm = airm100.Airm()
  airm_logical = airm.logical_concepts.to_dict('records')
  html = open("data/html/templates/viewer/1.0.0/logical-model-template.html").read()
  soup = BeautifulSoup(html, "lxml")
  for record in airm_logical:
    if record["supplement"] == "\t\t\t" or record["supplement"] == "\t":
      tr = soup.new_tag("tr")
      td_ic_name = soup.new_tag("td")
      td_ic_name["data-order"] = record["class name"]
      if record["stereotype"] != "missing data": #The record is a class
        filename = str(record['class name'])+".html"
        filename = filename.replace("/", "-")
        filename = filename.replace("*", "-")
        filename = filename.replace(" ", "")
        filename = filename.replace("\t", "")
        filename = filename.replace("\n", "")
        url = "logical-model/"+filename
        text = record["class name"]
        print(text)
        new_link = soup.new_tag("a")
        new_link['href'] = url
        new_link['target'] = "_blank"
        new_link.string = text
        td_ic_name.insert(1,new_link)
        tr.insert(1,td_ic_name)
      else: #The record is a property
        td_ic_name.string = record["class name"]
        tr.insert(1,td_ic_name)
      
      td_dc_name = soup.new_tag("td")
      td_dc_name["data-order"] = str(record["property name"])
      if record["stereotype"] == "missing data": #The record is a property
        filename = str(record['class name'])+".html#"+str(record['property name'])
        filename = filename.replace("/", "-")
        filename = filename.replace("*", "-")
        filename = filename.replace(" ", "")
        filename = filename.replace("\t", "")
        filename = filename.replace("\n", "")
        url = "logical-model/"+filename
        text = str(record["property name"])
        print(text)
        new_link = soup.new_tag("a")
        new_link['href'] = url
        new_link['target'] = "_blank"
        new_link.string = text
        td_dc_name.insert(1,new_link)
        tr.insert(2,td_dc_name)
      else: #The record is a class
        td_dc_name.string = "-"
        tr.insert(2,td_dc_name)

      if record["definition"] != "":
        td_def = soup.new_tag("td")
        td_def.string = str(record["definition"])
        tr.insert(3,td_def)
      
      if record["type"] != "missing data":
        td_def = soup.new_tag("td")
        td_def.string = str(record["type"])
        tr.insert(4,td_def)
      else:
        td_def = soup.new_tag("td")
        td_def.string = "-"
        tr.insert(4,td_def)
      
      soup.find('tbody').insert(1,tr)
  
  f= open("docs/viewer/1.0.0/logical-model.html","w+")
  f.write(soup.prettify())
  f.close() 

def create_index_logical_supp():
  import airm100
  airm = airm100.Airm()
  airm_logical = airm.logical_concepts.to_dict('records')
  html = open("data/html/templates/viewer/1.0.0/logical-model-with-supplements-template.html").read()
  soup = BeautifulSoup(html, "lxml")
  for record in airm_logical:
    path = "logical-model/"
    tr = soup.new_tag("tr")

    td_supplement = soup.new_tag("td")
    if record["supplement"] == "\t\t\tEuropean Supplement" or record["supplement"] == "\tEuropean Supplement":
      span_supplement = soup.new_tag("spam")
      span_supplement['class'] = "badge badge-secondary"
      span_supplement.string = "European Supplement"
      td_supplement.insert(1,span_supplement)
      path = "logical-model/european-supplement/"
    tr.insert(1,td_supplement)

    td_ic_name = soup.new_tag("td")
    td_ic_name["data-order"] = record["class name"]
    if record["stereotype"] != "missing data": #The record is a class
      filename = str(record['class name'])+".html"
      filename = filename.replace("/", "-")
      filename = filename.replace("*", "-")
      filename = filename.replace(" ", "")
      filename = filename.replace("\t", "")
      filename = filename.replace("\n", "")
      url = path+filename
      text = record["class name"]
      print(text)
      new_link = soup.new_tag("a")
      new_link['href'] = url
      new_link['target'] = "_blank"
      new_link.string = text
      td_ic_name.insert(1,new_link)
      tr.insert(2,td_ic_name)
    else: #The record is a property
      td_ic_name.string = record["class name"]
      tr.insert(2,td_ic_name)
    
    td_dc_name = soup.new_tag("td")
    td_dc_name["data-order"] = str(record["property name"])
    if record["stereotype"] == "missing data": #The record is a property
      filename = str(record['class name'])+".html#"+str(record['property name'])
      filename = filename.replace("/", "-")
      filename = filename.replace("*", "-")
      filename = filename.replace(" ", "")
      filename = filename.replace("\t", "")
      filename = filename.replace("\n", "")
      url = path+filename
      text = str(record["property name"])
      print(text)
      new_link = soup.new_tag("a")
      new_link['href'] = url
      new_link['target'] = "_blank"
      new_link.string = text
      td_dc_name.insert(1,new_link)
      tr.insert(3,td_dc_name)
    else: #The record is a class
      td_dc_name.string = "-"
      tr.insert(3,td_dc_name)

    if record["definition"] != "":
      td_def = soup.new_tag("td")
      td_def.string = str(record["definition"])
      tr.insert(4,td_def)
    
    if record["type"] != "missing data":
      td_def = soup.new_tag("td")
      td_def.string = str(record["type"])
      tr.insert(5,td_def)
    else:
      td_def = soup.new_tag("td")
      td_def.string = "-"
      tr.insert(5,td_def)
    
    soup.find('tbody').insert(1,tr)
  
  f= open("docs/viewer/1.0.0/logical-model-with-supplements.html","w+")
  f.write(soup.prettify())
  f.close() 

def create_pages_logical_concepts():
  import airm100
  airm = airm100.Airm()
  airm_logical = airm.logical_concepts.to_dict('records')
  scope = ""

  for record in airm_logical:
    
    if record["supplement"] == "\t\t\t":
      html = open("data/html/templates/viewer/1.0.0/logical-model/logical-model-concept-template.html").read()
      directory = "docs/viewer/1.0.0/logical-model/"
      scope = "global"

    elif record["supplement"] == "\t\t\tEuropean Supplement":
      html = open("data/html/templates/viewer/1.0.0/logical-model/european-supplement/logical-model-concept-template.html").read()
      directory = "docs/viewer/1.0.0/logical-model/european-supplement/"
      scope = "European Supplement"

    if record["stereotype"] != "missing data":
      print(record['class name'])
      soup = BeautifulSoup(html, "lxml") 

      soup.title.string = str(record['class name'])+" - Logical Model | AIRM.aero"
      soup.find(text="FIXM_CLASS_NAME_BC").replace_with(str(record['class name']))

      h2 = soup.new_tag("h2")
      h2.string = str(record['class name'])

      span_supplement = soup.new_tag("spam")
      if record["supplement"] == "\t\t\tEuropean Supplement":
        span_supplement['class'] = "badge badge-secondary"
        span_supplement.string = "European Supplement"
      h2.insert(1,span_supplement)

      soup.find(id="INFO_CONCEPT_NAME").insert(0,h2)
      code = soup.new_tag("code")
      code.string = record['urn']
      code["class"] = "text-secondary"
      soup.find(id="INFO_CONCEPT_NAME").insert(1,code)
      soup.find(text="FIXM_CLASS_DEFINITION").replace_with(str(record['definition']))
      
      p = soup.new_tag("p")
      insert_index = 1
      if record["source"] != "missing data":
        b = soup.new_tag("b")
        b.string = "Source: "
        p.insert(insert_index,b)
        insert_index = insert_index+1

        span = soup.new_tag("span")
        span.string = record["source"]
        p.insert(insert_index,span)
        insert_index = insert_index+1

        br = soup.new_tag("br")
        p.insert(insert_index,br)
        insert_index = insert_index+1

      if record["synonyms"] != "missing data":
        b = soup.new_tag("b")
        b.string = "Synonyms: "
        p.insert(insert_index,b)
        insert_index = insert_index+1

        span = soup.new_tag("span")
        span.string = record["synonyms"]
        p.insert(insert_index,span)
        insert_index = insert_index+1

        br = soup.new_tag("br")
        p.insert(insert_index,br)
        insert_index = insert_index+1

      if record["abbreviation"] != "missing data":
        b = soup.new_tag("b")
        b.string = "Abbreviations: "
        p.insert(insert_index,b)
        insert_index = insert_index+1

        span = soup.new_tag("span")
        span.string = record["abbreviation"]
        p.insert(insert_index,span)
        insert_index = insert_index+1

        br = soup.new_tag("br")
        p.insert(insert_index,br)
        insert_index = insert_index+1
      
      if record["parent"] != "missing data":
        b = soup.new_tag("b")
        b.string = "Parent concept: "
        p.insert(insert_index,b)
        insert_index = insert_index+1

        filename = str(record["parent"])+".html"
        filename = filename.replace("/", "-")
        filename = filename.replace("*", "-")
        filename = filename.replace(" ", "")
        filename = filename.replace("\t", "")
        filename = filename.replace("\n", "")
        if scope == "global":
          url = filename
        elif scope == "European Supplement":
          url = "european-supplement/"+filename
        text = record["parent"]
        print(text)
        new_link = soup.new_tag("a")
        new_link['href'] = url
        new_link.string = text
        p.insert(insert_index,new_link)
        insert_index = insert_index+1

        br = soup.new_tag("br")
        p.insert(insert_index,br)
        insert_index = insert_index+1
      
      # Insert properties
      results = airm.get_logical_properties_by_class(str(record['class name']), scope)
      if results != None:
        print("RESULTS for " + str(record['class name'])+ "SCOPE: "+scope)
        print(results)
        hr = soup.new_tag("hr")
        p.insert(insert_index,hr)
        insert_index = insert_index+1

        b = soup.new_tag("b")
        b.string = "Properties: "
        p.insert(insert_index,b)
        insert_index = insert_index+1

        br = soup.new_tag("br")
        p.insert(insert_index,br)
        insert_index = insert_index+1

        for result in results:
          print('\t'+str(result['property name']))

          tr = soup.new_tag("tr")

          if result["property name"] != "":
            td_dc_name = soup.new_tag("td")
            url = "#"+result["property name"]
            text = result["property name"]
            new_link = soup.new_tag("a")
            new_link['href'] = url
            new_link.string = text
            td_dc_name.insert(1,new_link)
            tr.insert(1,td_dc_name)
          
          if result["definition"] != "":
            td_def = soup.new_tag("td")
            td_def.string = str(result["definition"])
            tr.insert(2,td_def)
          
          if result["type"] != "":
            td_dc_type = soup.new_tag("td")
            filename = str(result['type'])+".html"
            filename = filename.replace("/", "-")
            filename = filename.replace("*", "-")
            filename = filename.replace(" ", "")
            filename = filename.replace("\t", "")
            filename = filename.replace("\n", "")
            if scope == "global":
              url = filename
            elif scope == "European Supplement":
              url = "european-supplement/"+filename
            text = result["type"]
            new_link = soup.new_tag("a")
            new_link['href'] = url
            new_link.string = text
            td_dc_type.insert(1,new_link)
            tr.insert(3,td_dc_type)
          
          soup.find(id="DATA_CONCEPTS_LIST").insert(1,tr)
        for trace in results:
          property_div = soup.new_tag("div")
          property_div["style"] = "border: 0.5px solid #b2b2b2;border-radius: 4px;box-shadow: 2px 2px #b2b2b2;padding: 15px;padding-bottom: 0px; margin-bottom: 30px"

          h3 = soup.new_tag("h3")
          h3.string = str(trace["property name"])
          h3["id"] = str(trace["property name"])
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
          filename = str(trace['type'])+".html"
          filename = filename.replace("/", "-")
          filename = filename.replace("*", "-")
          filename = filename.replace(" ", "")
          filename = filename.replace("\t", "")
          filename = filename.replace("\n", "")
          if scope == "global":
            url = filename
          elif scope == "European Supplement":
            url = "european-supplement/"+filename
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
            button.string = "Show presence in semantic correspondences"
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
              elif entry["model_name"] == "AMXM 2.0.0":
                td = soup.new_tag("td")
                url = "../../../developers/amxm-2.0.0-to-airm-1.0.0.html"
                text = "AMXM 2.0.0"
                a = soup.new_tag("a")
                a['href'] = url
                a['target'] = "_blank"
                a.string = text
                td.insert(1,a)
                tr.insert(1,td)
                td = soup.new_tag("td")
                if "." in str(entry["concept_id"]):
                  parts = str(entry["concept_id"]).split(".")
                  url = "../../../developers/amxm-2.0.0-to-airm-1.0.0/"+parts[-2]+".html#"+entry["concept_name"]
                else:
                  url = "../../../developers/amxm-2.0.0-to-airm-1.0.0/"+entry["concept_name"]+".html#"
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
              elif entry["model_name"] == "AIXM 5.1.1":
                td = soup.new_tag("td")
                url = "../../../developers/aixm-5.1.1-to-airm-1.0.0.html"
                text = "AIXM 5.1.1"
                a = soup.new_tag("a")
                a['href'] = url
                a['target'] = "_blank"
                a.string = text
                td.insert(1,a)
                tr.insert(1,td)
                td = soup.new_tag("td")
                if "." in str(entry["concept_id"]):
                  parts = str(entry["concept_id"]).split(".")
                  url = "../../../developers/aixm-5.1.1-to-airm-1.0.0/"+parts[-2]+".html#"+str(entry["concept_name"])
                else:
                  url = "../../../developers/aixm-5.1.1-to-airm-1.0.0/"+str(entry["concept_name"])+".html#"
                text = str(entry["concept_name"])
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
          property_div.insert(6,top_link_p)

          soup.find(id="DATA_CONCEPTS_DETAIL").insert(1,property_div)
          
          

      

      soup.find(id="INFO_CONCEPT_OTHER").insert(insert_index,p)

      filename = str(record['class name'])+".html"
      filename = filename.replace("/", "-")
      filename = filename.replace("*", "-")
      filename = filename.replace(" ", "")
      filename = filename.replace("\t", "")
      filename = filename.replace("\n", "")
      f= open(directory + filename,"w+")
      f.write(soup.prettify())
      f.close()

def create_index_cp_global():
  import airm100
  airm = airm100.Airm()
  airm_concepts = airm.conceptual_concepts.to_dict('records')
  html = open("data/html/templates/viewer/1.0.0/conceptual-model-template.html").read()
  soup = BeautifulSoup(html, "lxml")
  for record in airm_concepts:
    if record["supplement"] == "\t\t\t":
      if record["stereotype"] != "missing data":
        tr = soup.new_tag("tr")

        td_ic_name = soup.new_tag("td")
        td_ic_name["data-order"] = record["class name"]
        filename = str(record['class name'])+".html"
        filename = filename.replace("/", "-")
        filename = filename.replace("*", "-")
        filename = filename.replace(" ", "")
        filename = filename.replace("\t", "")
        filename = filename.replace("\n", "")
        url = "conceptual-model/"+filename
        text = record["class name"]
        print(text)
        new_link = soup.new_tag("a")
        new_link['href'] = url
        new_link['target'] = "_blank"
        new_link.string = text
        td_ic_name.insert(1,new_link)
        tr.insert(1,td_ic_name)
        
        if record["definition"] != "":
          td_def = soup.new_tag("td")
          td_def.string = str(record["definition"])
          tr.insert(2,td_def)
      
        soup.find('tbody').insert(1,tr)
  
  f= open("docs/viewer/1.0.0/conceptual-model.html","w+")
  f.write(soup.prettify())
  f.close() 

def create_index_cp_supp():
  import airm100
  airm = airm100.Airm()
  airm_concepts = airm.conceptual_concepts.to_dict('records')
  html = open("data/html/templates/viewer/1.0.0/conceptual-model-with-supplements-template.html").read()
  soup = BeautifulSoup(html, "lxml")
  for record in airm_concepts:
    if record["supplement"] == "\t\t\t":
      if record["stereotype"] != "missing data":
        tr = soup.new_tag("tr")
        td_supplement = soup.new_tag("td")
        tr.insert(1,td_supplement)

        td_ic_name = soup.new_tag("td")
        td_ic_name["data-order"] = record["class name"]
        filename = str(record['class name'])+".html"
        filename = filename.replace("/", "-")
        filename = filename.replace("*", "-")
        filename = filename.replace(" ", "")
        filename = filename.replace("\t", "")
        filename = filename.replace("\n", "")
        url = "conceptual-model/"+filename
        text = record["class name"]
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
      
        soup.find('tbody').insert(1,tr)
    elif record["supplement"] == "\t\t\tEuropean Supplement":
      if record["stereotype"] != "missing data":
        tr = soup.new_tag("tr")
        td_supplement = soup.new_tag("td")
        span_supplement = soup.new_tag("spam")
        span_supplement['class'] = "badge badge-secondary"
        span_supplement.string = "European Supplement"
        td_supplement.insert(1,span_supplement)
        tr.insert(1,td_supplement)
        
        td_ic_name = soup.new_tag("td")
        td_ic_name["data-order"] = record["class name"]
        filename = str(record['class name'])+".html"
        filename = filename.replace("/", "-")
        filename = filename.replace("*", "-")
        filename = filename.replace(" ", "")
        filename = filename.replace("\t", "")
        filename = filename.replace("\n", "")
        url = "conceptual-model/european-supplement/"+filename
        text = record["class name"]
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
      
        soup.find('tbody').insert(1,tr)

  f= open("docs/viewer/1.0.0/conceptual-model-with-supplements.html","w+")
  f.write(soup.prettify())
  f.close() 

def create_pages_cp_concepts():
  import airm100
  airm = airm100.Airm()
  airm_conceps = airm.conceptual_concepts.to_dict('records')
  scope = ""

  for record in airm_conceps:
    
    if record["supplement"] == "\t\t\t":
      html = open("data/html/templates/viewer/1.0.0/conceptual-model/conceptual-model-concept-template.html").read()
      directory = "docs/viewer/1.0.0/conceptual-model/"
      scope = "global"

    elif record["supplement"] == "\t\t\tEuropean Supplement":
      html = open("data/html/templates/viewer/1.0.0/conceptual-model/european-supplement/conceptual-model-concept-template.html").read()
      directory = "docs/viewer/1.0.0/conceptual-model/european-supplement/"
      scope = "European Supplement"

    if record["stereotype"] != "missing data":
      print(record['class name'])
      soup = BeautifulSoup(html, "lxml") 

      soup.title.string = str(record['class name'])+" - Conceptual Model | AIRM.aero"
      soup.find(text="CONCEPT_NAME_BC").replace_with(str(record['class name']))

      h2 = soup.new_tag("h2")
      h2.string = str(record['class name'])

      span_supplement = soup.new_tag("spam")
      if record["supplement"] == "\t\t\tEuropean Supplement":
        span_supplement['class'] = "badge badge-secondary"
        span_supplement.string = "European Supplement"
      h2.insert(1,span_supplement)

      soup.find(id="INFO_CONCEPT_NAME").insert(0,h2)
      code = soup.new_tag("code")
      code.string = record['urn']
      code["class"] = "text-secondary"
      soup.find(id="INFO_CONCEPT_NAME").insert(1,code)
      soup.find(text="CONCEPT_DEFINITION").replace_with(str(record['definition']))
      
      p = soup.new_tag("p")
      insert_index = 1
      if record["source"] != "missing data":
        b = soup.new_tag("b")
        b.string = "Source: "
        p.insert(insert_index,b)
        insert_index = insert_index+1

        span = soup.new_tag("span")
        span.string = record["source"]
        p.insert(insert_index,span)
        insert_index = insert_index+1

        br = soup.new_tag("br")
        p.insert(insert_index,br)
        insert_index = insert_index+1

      if record["synonyms"] != "missing data":
        b = soup.new_tag("b")
        b.string = "Synonyms: "
        p.insert(insert_index,b)
        insert_index = insert_index+1

        span = soup.new_tag("span")
        span.string = record["synonyms"]
        p.insert(insert_index,span)
        insert_index = insert_index+1

        br = soup.new_tag("br")
        p.insert(insert_index,br)
        insert_index = insert_index+1

      if record["abbreviation"] != "missing data":
        b = soup.new_tag("b")
        b.string = "Abbreviations: "
        p.insert(insert_index,b)
        insert_index = insert_index+1

        span = soup.new_tag("span")
        span.string = record["abbreviation"]
        p.insert(insert_index,span)
        insert_index = insert_index+1

        br = soup.new_tag("br")
        p.insert(insert_index,br)
        insert_index = insert_index+1
      
      # Insert related concepts
      results = airm.get_concept_properties_by_parent(str(record['class name']), scope)
      if results != None:
        print("RESULTS for " + str(record['class name'])+ "SCOPE: "+scope)
        print(results)
        hr = soup.new_tag("hr")
        p.insert(insert_index,hr)
        insert_index = insert_index+1

        b = soup.new_tag("b")
        b.string = "Related: "
        p.insert(insert_index,b)
        insert_index = insert_index+1

        br = soup.new_tag("br")
        p.insert(insert_index,br)
        insert_index = insert_index+1

        for result in results:
          print('\t'+result['property name'])
          
          span = soup.new_tag("span")
          span.string = result["property name"]
          p.insert(insert_index,span)
          insert_index = insert_index+1

          filename = str(result['type'])+".html"
          filename = filename.replace("/", "-")
          filename = filename.replace("*", "-")
          filename = filename.replace(" ", "")
          filename = filename.replace("\t", "")
          filename = filename.replace("\n", "")
          if scope == "global":
            url = filename
          elif scope == "European Supplement":
            url = "european-supplement/"+filename
          text = result["type"]
          print(text)
          new_link = soup.new_tag("a")
          new_link['href'] = url
          new_link.string = text
          p.insert(insert_index,new_link)
          insert_index = insert_index+1

          br = soup.new_tag("br")
          p.insert(insert_index,br)
          insert_index = insert_index+1

      

      soup.find(id="DATA_CONCEPTS_DETAIL").insert(insert_index,p)

      filename = str(record['class name'])+".html"
      filename = filename.replace("/", "-")
      filename = filename.replace("*", "-")
      filename = filename.replace(" ", "")
      filename = filename.replace("\t", "")
      filename = filename.replace("\n", "")
      f= open(directory + filename,"w+")
      f.write(soup.prettify())
      f.close()

def create_index_cx_terms_global():
  # Create Index
  airm_cx_pages_directory = "docs/viewer/1.0.0/contextual-model"
  path = airm_cx_pages_directory
  try:
      os.mkdir(path)
  except OSError:
      print ("Creation of the directory %s failed" % path)
  else:
      print ("Successfully created the directory %s " % path)
  import airm100
  airm = airm100.Airm()
  airm_terms = airm.contextual_terms.to_dict('records')
  html = open("data/html/templates/viewer/1.0.0/contextual-model-terms-template.html").read()
  soup = BeautifulSoup(html, "lxml")
  for record in airm_terms:
    if record["supplement"] == "\t\t\t":
      tr = soup.new_tag("tr")

      td_ic_name = soup.new_tag("td")
      td_ic_name["data-order"] = record["class name"]
      filename = str(record['class name'])+".html"
      filename = filename.replace("/", "-")
      filename = filename.replace("*", "-")
      filename = filename.replace(" ", "")
      filename = filename.replace("\t", "")
      filename = filename.replace("\n", "")
      url = "contextual-model/"+filename
      text = record["class name"]
      print(text)
      new_link = soup.new_tag("a")
      new_link['href'] = url
      new_link['target'] = "_blank"
      new_link.string = text
      td_ic_name.insert(1,new_link)
      tr.insert(1,td_ic_name)
      
      if record["definition"] != "":
        td_def = soup.new_tag("td")
        td_def.string = str(record["definition"])
        tr.insert(2,td_def)
     
      soup.find('tbody').insert(1,tr)
  
  f= open("docs/viewer/1.0.0/contextual-model-terms.html","w+")
  f.write(soup.prettify())
  f.close() 

def create_index_cx_terms_supp():
  import airm100
  airm = airm100.Airm()
  airm_terms = airm.contextual_terms.to_dict('records')
  html = open("data/html/templates/viewer/1.0.0/contextual-model-terms-with-supplements-template.html").read()
  soup = BeautifulSoup(html, "lxml")
  for record in airm_terms:
    if record["supplement"] == "\t\t\t":
      tr = soup.new_tag("tr")
      td_supplement = soup.new_tag("td")
      tr.insert(1,td_supplement)

      td_ic_name = soup.new_tag("td")
      td_ic_name["data-order"] = record["class name"]
      filename = str(record['class name'])+".html"
      filename = filename.replace("/", "-")
      filename = filename.replace("*", "-")
      filename = filename.replace(" ", "")
      filename = filename.replace("\t", "")
      filename = filename.replace("\n", "")
      url = "contextual-model/"+filename
      text = record["class name"]
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
     
      soup.find('tbody').insert(1,tr)
    elif record["supplement"] == "\t\t\tEuropean Supplement":
      tr = soup.new_tag("tr")
      td_supplement = soup.new_tag("td")
      span_supplement = soup.new_tag("spam")
      span_supplement['class'] = "badge badge-secondary"
      span_supplement.string = "European Supplement"
      td_supplement.insert(1,span_supplement)
      tr.insert(1,td_supplement)
      
      td_ic_name = soup.new_tag("td")
      td_ic_name["data-order"] = record["class name"]
      filename = str(record['class name'])+".html"
      filename = filename.replace("/", "-")
      filename = filename.replace("*", "-")
      filename = filename.replace(" ", "")
      filename = filename.replace("\t", "")
      filename = filename.replace("\n", "")
      url = "contextual-model/european-supplement/"+filename
      text = record["class name"]
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
     
      soup.find('tbody').insert(1,tr)

  f= open("docs/viewer/1.0.0/contextual-model-terms-with-supplements.html","w+")
  f.write(soup.prettify())
  f.close() 

def create_pages_cx_terms():
  import airm100
  airm = airm100.Airm()
  airm_terms = airm.contextual_terms.to_dict('records')

  for record in airm_terms:
    
    if record["supplement"] == "\t\t\t":
      html = open("data/html/templates/viewer/1.0.0/contextual-model/contextual-model-term-template.html").read()
      directory = "docs/viewer/1.0.0/contextual-model/"

    elif record["supplement"] == "\t\t\tEuropean Supplement":
      html = open("data/html/templates/viewer/1.0.0/contextual-model/european-supplement/contextual-model-term-template.html").read()
      directory = "docs/viewer/1.0.0/contextual-model/european-supplement/"
          
    print(record['class name'])
    soup = BeautifulSoup(html, "lxml") 

    soup.title.string = str(record['class name'])+" - Contextual Model | AIRM.aero"
    soup.find(text="CONCEPT_NAME_BC").replace_with(str(record['class name']))

    h2 = soup.new_tag("h2")
    h2.string = str(record['class name'])

    span_supplement = soup.new_tag("spam")
    if record["supplement"] == "\t\t\tEuropean Supplement":
      span_supplement['class'] = "badge badge-secondary"
      span_supplement.string = "European Supplement"
    h2.insert(1,span_supplement)

    soup.find(id="INFO_CONCEPT_NAME").insert(0,h2)
    code = soup.new_tag("code")
    code.string = record['urn']
    code["class"] = "text-secondary"
    soup.find(id="INFO_CONCEPT_NAME").insert(1,code)
    soup.find(text="CONCEPT_DEFINITION").replace_with(str(record['definition']))
    
    p = soup.new_tag("p")
    insert_index = 1
    if record["source"] != "missing data":
      b = soup.new_tag("b")
      b.string = "Source: "
      p.insert(insert_index,b)
      insert_index = insert_index+1

      span = soup.new_tag("span")
      span.string = record["source"]
      p.insert(insert_index,span)
      insert_index = insert_index+1

      br = soup.new_tag("br")
      p.insert(insert_index,br)
      insert_index = insert_index+1

    if record["synonyms"] != "missing data":
      b = soup.new_tag("b")
      b.string = "Synonyms: "
      p.insert(insert_index,b)
      insert_index = insert_index+1

      span = soup.new_tag("span")
      span.string = record["synonyms"]
      p.insert(insert_index,span)
      insert_index = insert_index+1

      br = soup.new_tag("br")
      p.insert(insert_index,br)
      insert_index = insert_index+1

    if record["abbreviation"] != "missing data":
      b = soup.new_tag("b")
      b.string = "Abbreviations: "
      p.insert(insert_index,b)
      insert_index = insert_index+1

      span = soup.new_tag("span")
      span.string = record["abbreviation"]
      p.insert(insert_index,span)
      insert_index = insert_index+1

      br = soup.new_tag("br")
      p.insert(insert_index,br)
      insert_index = insert_index+1

    soup.find(id="DATA_CONCEPTS_DETAIL").insert(insert_index,p)

    filename = str(record['class name'])+".html"
    filename = filename.replace("/", "-")
    filename = filename.replace("*", "-")
    filename = filename.replace(" ", "")
    filename = filename.replace("\t", "")
    filename = filename.replace("\n", "")
    f= open(directory + filename,"w+")
    f.write(soup.prettify())
    f.close()

def create_index_cx_abbs_global():
  # Create Index
  airm_cx_pages_directory = "docs/viewer/1.0.0/contextual-model"
  path = airm_cx_pages_directory
  try:
      os.mkdir(path)
  except OSError:
      print ("Creation of the directory %s failed" % path)
  else:
      print ("Successfully created the directory %s " % path)
  import airm100
  airm = airm100.Airm()
  airm_abbs = airm.contextual_abbreviations.to_dict('records')
  html = open("data/html/templates/viewer/1.0.0/contextual-model-abbreviations-template.html").read()
  soup = BeautifulSoup(html, "lxml")
  for record in airm_abbs:
    if record["supplement"] == "\t\t\t":
      tr = soup.new_tag("tr")

      td_ic_name = soup.new_tag("td")
      td_ic_name["data-order"] = record["class name"]
      filename = str(record['class name'])+".html"
      filename = filename.replace("/", "-")
      filename = filename.replace("*", "-")
      filename = filename.replace(" ", "")
      filename = filename.replace("\t", "")
      filename = filename.replace("\n", "")
      url = "contextual-model/"+ filename
      text = record["class name"]
      print(text)
      new_link = soup.new_tag("a")
      new_link['href'] = url
      new_link['target'] = "_blank"
      new_link.string = text
      td_ic_name.insert(1,new_link)
      tr.insert(1,td_ic_name)
      
      if record["definition"] != "":
        td_def = soup.new_tag("td")
        td_def.string = str(record["definition"])
        tr.insert(2,td_def)
     
      soup.find('tbody').insert(1,tr)
  
  f= open("docs/viewer/1.0.0/contextual-model-abbreviations.html","w+")
  f.write(soup.prettify())
  f.close() 

def create_index_cx_abbs_supp():
  import airm100
  airm = airm100.Airm()
  airm_abbs = airm.contextual_abbreviations.to_dict('records')
  html = open("data/html/templates/viewer/1.0.0/contextual-model-abbreviations-with-supplements-template.html").read()
  soup = BeautifulSoup(html, "lxml")
  for record in airm_abbs:
    if record["supplement"] == "\t\t\t":
      tr = soup.new_tag("tr")
      td_supplement = soup.new_tag("td")
      tr.insert(1,td_supplement)

      td_ic_name = soup.new_tag("td")
      td_ic_name["data-order"] = record["class name"]
      filename = str(record['class name'])+".html"
      filename = filename.replace("/", "-")
      filename = filename.replace("*", "-")
      filename = filename.replace(" ", "")
      filename = filename.replace("\t", "")
      filename = filename.replace("\n", "")
      url = "contextual-model/"+filename
      text = record["class name"]
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
     
      soup.find('tbody').insert(1,tr)
    elif record["supplement"] == "\t\t\tEuropean Supplement":
      tr = soup.new_tag("tr")
      td_supplement = soup.new_tag("td")
      span_supplement = soup.new_tag("spam")
      span_supplement['class'] = "badge badge-secondary"
      span_supplement.string = "European Supplement"
      td_supplement.insert(1,span_supplement)
      tr.insert(1,td_supplement)
      
      td_ic_name = soup.new_tag("td")
      td_ic_name["data-order"] = record["class name"]
      filename = str(record['class name'])+".html"
      filename = filename.replace("/", "-")
      filename = filename.replace("*", "-")
      filename = filename.replace(" ", "")
      filename = filename.replace("\t", "")
      filename = filename.replace("\n", "")
      url = "contextual-model/european-supplement/"+filename
      text = record["class name"]
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
     
      soup.find('tbody').insert(1,tr)

  f= open("docs/viewer/1.0.0/contextual-model-abbreviations-with-supplements.html","w+")
  f.write(soup.prettify())
  f.close() 

def create_pages_cx_abbs():
  import airm100
  airm = airm100.Airm()
  airm_abbs = airm.contextual_abbreviations.to_dict('records')

  for record in airm_abbs:
    
    if record["supplement"] == "\t\t\t":
      html = open("data/html/templates/viewer/1.0.0/contextual-model/contextual-model-abbreviation-template.html").read()
      directory = "docs/viewer/1.0.0/contextual-model/"

    elif record["supplement"] == "\t\t\tEuropean Supplement":
      html = open("data/html/templates/viewer/1.0.0/contextual-model/european-supplement/contextual-model-abbreviation-template.html").read()
      directory = "docs/viewer/1.0.0/contextual-model/european-supplement/"
          
    print(record['class name'])
    soup = BeautifulSoup(html, "lxml") 

    soup.title.string = str(record['class name'])+" - Contextual Model | AIRM.aero"
    soup.find(text="CONCEPT_NAME_BC").replace_with(str(record['class name']))

    h2 = soup.new_tag("h2")
    h2.string = str(record['class name'])

    span_supplement = soup.new_tag("spam")
    if record["supplement"] == "\t\t\tEuropean Supplement":
      span_supplement['class'] = "badge badge-secondary"
      span_supplement.string = "European Supplement"
    h2.insert(1,span_supplement)

    soup.find(id="INFO_CONCEPT_NAME").insert(0,h2)
    code = soup.new_tag("code")
    code.string = record['urn']
    code["class"] = "text-secondary"
    soup.find(id="INFO_CONCEPT_NAME").insert(1,code)
    soup.find(text="CONCEPT_DEFINITION").replace_with(str(record['definition']))
    
    p = soup.new_tag("p")
    p.string = "Source: "
    span = soup.new_tag("span")
    span.string = record["source"]
    p.insert(2,span)
    soup.find(id="DATA_CONCEPTS_DETAIL").insert(1,p)
    filename = str(record['class name'])+".html"
    filename = filename.replace("/", "-")
    filename = filename.replace("*", "-")
    filename = filename.replace(" ", "")
    filename = filename.replace("\t", "")
    filename = filename.replace("\n", "")
    f= open(directory + filename,"w+")
    f.write(soup.prettify())
    f.close()


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
            button.string = "Show presence in semantic correspondences"
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
              elif entry["model_name"] == "AMXM 2.0.0":
                td = soup.new_tag("td")
                url = "../../../developers/amxm-2.0.0-to-airm-1.0.0.html"
                text = "AMXM 2.0.0"
                a = soup.new_tag("a")
                a['href'] = url
                a['target'] = "_blank"
                a.string = text
                td.insert(1,a)
                tr.insert(1,td)
                td = soup.new_tag("td")
                if "." in str(entry["concept_id"]):
                  parts = str(entry["concept_id"]).split(".")
                  url = "../../../developers/amxm-2.0.0-to-airm-1.0.0/"+parts[-2]+".html#"+entry["concept_name"]
                else:
                  url = "../../../developers/amxm-2.0.0-to-airm-1.0.0/"+entry["concept_name"]+".html#"
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
              elif entry["model_name"] == "AIXM 5.1.1":
                td = soup.new_tag("td")
                url = "../../../developers/aixm-5.1.1-to-airm-1.0.0.html"
                text = "AIXM 5.1.1"
                a = soup.new_tag("a")
                a['href'] = url
                a['target'] = "_blank"
                a.string = text
                td.insert(1,a)
                tr.insert(1,td)
                td = soup.new_tag("td")
                if "." in str(entry["concept_id"]):
                  parts = str(entry["concept_id"]).split(".")
                  url = "../../../developers/aixm-5.1.1-to-airm-1.0.0/"+parts[-2]+".html#"+str(entry["concept_name"])
                else:
                  url = "../../../developers/aixm-5.1.1-to-airm-1.0.0/"+str(entry["concept_name"])+".html#"
                text = str(entry["concept_name"])
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
          property_div.insert(6,top_link_p)

          soup.find(id="DATA_CONCEPTS_DETAIL").insert(1,property_div)

      f= open("docs/advanced-viewer/1.0.0/LM/"+str(info_concept['name'])+".html","w+")
      f.write(soup.prettify())
      f.close()
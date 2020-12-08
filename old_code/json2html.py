from bs4 import BeautifulSoup
import os
import json
import lxml

def create_html():
  import airm
  airm = airm.Airm()
  #configuration
  json_mapping_file = "data/json/fixm-mapping.json" #assets/js/fixm-mapping-test.json OR assets/js/fixm-mapping.json
  mapping_pages_directory = "data/html/export/developers/fixm-4.2.0-to-airm-1.0.0"

  # creates developers/fixm-4.2.0-to-airm-1.0.0.html using developers/template.html
  html = open("data/html/templates/template.html").read()
  soup = BeautifulSoup(html, "lxml")

  f= open("data/html/export/developers/fixm-4.2.0-to-airm-1.0.0.html","w+")
  f.write(soup.prettify())
  f.close() 

  # creates assets/js/mapping-table.js injecting the contents of assets/js/fixm-mapping.json as values and using assets/js/mapping-table-template.js
  with open(json_mapping_file) as json_file:
    with open('data/html/templates/mapping-table-template.js') as fin, open('data/html/export/assets/js/mapping-table.js', 'w') as fout:
        for line in fin:
            if '        var values = [] ;' in line:
                line = '        var values = '+ json_file.read()  +' ;\n'
            fout.write(line)

  # creates developers/fixm-4.2.0-to-airm-1.0.0 directory
  path = mapping_pages_directory
  try:
      os.mkdir(path)
  except OSError:
      print ("Creation of the directory %s failed" % path)
  else:
      print ("Successfully created the directory %s " % path)

  # loads assets/js/fixm-mapping.json as a dictionary
  with open(json_mapping_file) as json_file:
    json_contents = json_file.read()
  mapping_list = json.loads(json_contents)

  # creates one page per concept in the mapping
  html = open("data/html/templates/concept-template.html").read()
  for trace in mapping_list:
    #print(trace['Concept'])
      
    components = str(trace['Id']).split(":")
    container_concept = components[1]
    #TO-DO replace shortnames in id with full namespaces
    full_id = str(trace['Id'])

    # creates developers/fixm-4.2.0-to-airm-1.0.0/CONCEPT NAME.html using developers/concept-template.html
    soup = BeautifulSoup(html, "lxml") 
    # container concept for breadcrumb
    soup.find(text="CONTAINER CONCEPT HERE").replace_with(container_concept)
    # name for heading
    soup.find(text="CONTAINER@CONCEPT NAME HERE").replace_with(trace['Concept'])
    # ID for sub heading
    soup.find(text="FULL ID HERE").replace_with(full_id)  
    # definition 
    soup.find(text="DEFINITION HERE").replace_with(str(trace['Definition']))
    # type 
    soup.find(text="TYPE HERE").replace_with(str(trace['Type']))
    # rationale 
    soup.find(text="RATIONALE HERE").replace_with(str(trace['Rationale']))
    # notes 
    soup.find(text="NOTES HERE").replace_with(str(trace['Notes']))

    # semantic correspondence name and url 
    new_link = BeautifulSoup('<a href="'+trace['url']+'">'+trace['Correspondence']+'</a>', "lxml")
    row = soup.find(text="AIRM CONCEPT HERE").parent
    row.clear()
    row.append(new_link.a)

    # AIRM concept definition 
    entry = airm.load_and_find_urn(trace['urn'])
    soup.find(text="AIRM CONCEPT DEFINITION HERE").replace_with(entry["definition"])
        
    # semantic correspondence url 
    new_link = BeautifulSoup('<a href="'+trace['addurl']+'">'+trace['Additional']+'</a>', "lxml")
    addrow = soup.find(text="AIRM ADDITIONAL CONCEPT HERE").parent
    addrow.clear()
    addrow.append(new_link.a)

    

    #page_content = BeautifulSoup("<div>"+container_concept+"</div>")
    #soup.find(text="CONTAINER CONCEPT HERE").replace_with(page_content)
    
    filename = trace['Concept']
    filename = filename.replace("@",".")
    f= open(mapping_pages_directory+"/"+ filename +".html","w+")
    
    f.write(soup.prettify())
    f.close() 

  #DONE
  print(str(airm.not_found_counter)+" AIRM URNs were not found")
  print("Done")
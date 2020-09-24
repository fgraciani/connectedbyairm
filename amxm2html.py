from bs4 import BeautifulSoup
import os
import xlsx2json
import json
import lxml

def create_html():
  mapping_pages_directory = "data/html/export/developers/amxm-2.0.0-to-airm-1.0.0"
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

  import aixm
  aixm = aixm.Aixm()

  import amxm
  amxm = amxm.Amxm()
  amxm_mapping_dict = amxm.amxm_mapping_dataframe.to_dict('records')

  #Create index page
  #creates soup for developers/amxm-2.2.0-to-airm-1.0.0.html using amxm_mapping_template.html
  html = open("data/html/templates/amxm_mapping_template.html").read()
  soup = BeautifulSoup(html, "lxml") 

  #For each entry
    #create table entry
  for record in amxm_mapping_dict:
    tr = soup.new_tag("tr")

    td_ic_name = soup.new_tag("td")
    td_ic_name.string = record["Information Concept"]
    tr.insert(1,td_ic_name)

    td_dc_name = soup.new_tag("td")
    td_dc_name.string = record["Data Concept"]
    tr.insert(2,td_dc_name)

    td_def = soup.new_tag("td")
    td_def.string = record["Concept Definition"]
    tr.insert(3,td_def)

    airm_concept = soup.new_tag("td")
    
    text = xlsx2json.create_name(record["AIRM Concept Identifier"])
    if text == "":
      airm_concept.string = record["Special cases \n(CR, OutOfScope, Not Established)"] 
      tr.insert(4,airm_concept)
      fixm_concept = soup.new_tag("p")
      fixm_concept.string = 'n.a.'
      fixm_concepts = soup.new_tag("td")
      fixm_concepts.insert(1,fixm_concept)
      tr.insert(5,fixm_concepts)
      aixm_concept = soup.new_tag("p")
      aixm_concept.string = 'n.a.'
      aixm_concepts = soup.new_tag("td")
      aixm_concepts.insert(1,aixm_concept)
      tr.insert(6,aixm_concepts)
    else:
      url = xlsx2json.create_url(record["AIRM Concept Identifier"])
      new_link = soup.new_tag("a")
      new_link['href'] = url
      new_link['target'] = "_blank"
      new_link.string = text
      airm_concept.insert(1,new_link)
      tr.insert(4,airm_concept)

      fixm_concepts = soup.new_tag("td")
      results = fixm.get_from_fixm_mapping(record["AIRM Concept Identifier"])
      if results is not None:
        for result in results:
          fixm_concept = soup.new_tag("p")
          url=fixm.create_url(result["Identifier"])
          new_link = soup.new_tag("a")
          new_link['href'] = url
          new_link['target'] = "_blank"
          new_link.string = result["Identifier"]
          fixm_concept.insert(1,new_link)
          fixm_concepts.insert(1,fixm_concept)
      else:
        fixm_concept = soup.new_tag("p")
        fixm_concept.string = 'n.a.'
        fixm_concepts.insert(1,fixm_concept)
      tr.insert(5,fixm_concepts)
      
      aixm_concepts = soup.new_tag("td")
      results = aixm.get_from_aixm_mapping(record["AIRM Concept Identifier"])
      if results is not None:
        for result in results:
          aixm_concept = soup.new_tag("p")
          aixm_concept.string = result["Concept Identifier"]
          aixm_concepts.insert(1,aixm_concept)
      else:
        aixm_concept = soup.new_tag("p")
        aixm_concept.string = 'n.a.'
        aixm_concepts.insert(1,aixm_concept)
      tr.insert(6,aixm_concepts)

    #print(tr)
    soup.find('tbody').insert(1,tr)

  f= open("data/html/export/developers/amxm-2.0.0-to-airm-1.0.0.html","w+")
  f.write(soup.prettify())
  f.close() 

  

def old_create_html():
  import airm
  airm = airm.Airm()
  #configuration
  json_mapping_file = "data/json/fixm-mapping.json" #assets/js/fixm-mapping-test.json OR assets/js/fixm-mapping.json
  

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
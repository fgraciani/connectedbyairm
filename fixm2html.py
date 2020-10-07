# Created 25/9/2020




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
  #creates soup for docs/developers/amxm-2.0.0-to-airm-1.0.0.html using fixm_mapping_template.html
  html = open("data/html/templates/concept-list-template.html").read()
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
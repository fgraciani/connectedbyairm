import fixm

fixm = fixm.Fixm()

fixm_mapping_dict = fixm.fixm_mapping_dataframe.to_dict('records')

empty_info_concept_counter = 0
overlap_aixm_counter = 0
overlap_amxm_counter = 0

def process_data_concept(record):
  import aixm
  import amxm
  
  aixm = aixm.Aixm()
  amxm = amxm.Amxm()
  
  if isinstance(record['Semantic Correspondence'], str):
    urn = record['Semantic Correspondence']
    urn = urn.strip()
    if aixm.is_in_aixm_mapping(urn):
      global overlap_aixm_counter 
      overlap_aixm_counter += 1
    
    if amxm.is_in_amxm_mapping(urn):
      global overlap_amxm_counter 
      overlap_amxm_counter += 1


def create_report():
  for record in fixm_mapping_dict:
    if isinstance(record['Information Concept'], str):
      if isinstance(record['Data Concept'], str):
        process_data_concept(record)
      else:
        process_data_concept(record)
    else:
      global empty_info_concept_counter
      empty_info_concept_counter += 1

def report():
  create_report()
  print("Report:")
  print("Overlap AIXM counter:"+str(overlap_aixm_counter))
  print("Overlap AMXM counter:"+str(overlap_amxm_counter))
import pandas as pd

amxm_dataframe = pd.read_excel (r'data/xlsx/AMXM_Semantic_Correspondence_Report.xlsx', sheet_name='semantic_corresponence') #it would be nice to align sheet names

amxm_mapping_dict = amxm_dataframe.to_dict('records')

empty_info_concept_counter = 0
overlap_aixm_counter = 0
overlap_fixm_counter = 0

def process_data_concept(record):
  import aixm
  import fixm
  
  aixm = aixm.Aixm()
  fixm = fixm.Fixm()
  
  if isinstance(record['AIRM Concept Identifier'], str):
    urn = record['AIRM Concept Identifier']
    urn = urn.strip()
    if aixm.is_in_aixm_mapping(urn):
      global overlap_aixm_counter 
      overlap_aixm_counter += 1
    
    if fixm.is_in_fixm_mapping(urn):
      global overlap_fixm_counter 
      overlap_fixm_counter += 1


def create_report():
  for record in amxm_mapping_dict:
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
  print("Overlap FIXM counter:"+str(overlap_fixm_counter))
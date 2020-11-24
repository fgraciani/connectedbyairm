import pandas as pd

class Aixm_adr:
  aixm_adr_mapping_dataframe = pd.read_excel (r'data/xlsx/ADR_23.5.0_Semantic_Correspondence_Report.xlsx', sheet_name='semantic_correspondence') #it would be nice to align sheet names

  def __init__(self):
    self.aixm_adr_mapping_dataframe.fillna("missing data", inplace = True)
    self.aixm_adr_mapping_dataframe.columns = ["Information Concept","Data Concept","Basic Type", "Concept Identifier", "Concept Definition", "AIRM Concept Identifier", "Special Case", "CR Number",  "Rationale", "Level of semantic correspondence", "Remarks"]

  def is_in_amxm_adr_mapping(self, airm_urn):
    results = self.get_from_amxm_mapping(airm_urn) 
    
    if results is None:
      return False
    else:
      print(airm_urn)
      return True

  def get_from_amxm_adr_mapping(self, airm_urn):
    #print("Searching for " + airm_urn)
    amxm_df = self.aixm_adr_mapping_dataframe.copy()
    
    filter = amxm_df["AIRM Concept Identifier"]==airm_urn
    amxm_df.sort_values("AIRM Concept Identifier", inplace = True)
    amxm_df.where(filter, inplace = True) 
    df_results = amxm_df.dropna(how='all')  
    
    if df_results.empty:
      return None
    else:
      results_dict = df_results.to_dict('records')
      return results_dict

  def get_information_concepts(self):
    results_dict = []
    amxm_df = self.aixm_adr_mapping_dataframe.copy()
    amxm_df = amxm_df.drop_duplicates(subset='Information Concept', keep="last")
    amxm_df = amxm_df.drop(["Data Concept", "Basic Type"], axis=1)
    amxm_dict = amxm_df.to_dict('records')
    for entry in amxm_dict:
      info_concept = str(entry["Information Concept"])
      concept_def = str(entry["Concept Definition"])
      concept_id = str(entry["Concept Identifier"])
      results_dict.append({"Information Concept": info_concept, "Concept Definition": concept_def, "Concept Identifier": concept_id,
      "AIRM Concept Identifier": str(entry["AIRM Concept Identifier"]), "Semantic Correspondence": str(entry["Special Case"]), "Rationale": str(entry["Rationale"]), "Level of semantic correspondence": str(entry["Level of semantic correspondence"]), "Remarks": str(entry["Remarks"])})
    
    return results_dict

  def get_traces_by_info_concept(self, info_concept):
      amxm_df = self.aixm_adr_mapping_dataframe.copy()
      
      filter = amxm_df["Information Concept"]==info_concept
      amxm_df.sort_values("Information Concept", inplace = True)
      amxm_df.where(filter, inplace = True) 
      df_results = amxm_df.dropna(how='all')      

      if df_results.empty:
        return None
        
      else:
        results_dict = df_results.to_dict('records')
        return results_dict
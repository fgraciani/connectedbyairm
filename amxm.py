import pandas as pd

class Amxm:
  amxm_mapping_dataframe = pd.read_excel (r'data/xlsx/AMXM_Semantic_Correspondence_Report.xlsx', sheet_name='semantic_corresponence') #it would be nice to align sheet names
  #classes = pd.Dataframe() #TO DO load in init
  #properties = pd.Dataframe() #TO DO load in init
     
  def __init__(self):
    self.amxm_mapping_dataframe["AIRM Concept Identifier"] = self.amxm_mapping_dataframe["AIRM Concept Identifier"].str.strip()
    self.amxm_mapping_dataframe.fillna("missing data", inplace = True)
    #self.classes.fillna("missing data", inplace = True)
    #self.properties.fillna("missing data", inplace = True)

  def is_in_amxm_mapping(self, airm_urn):
    results = self.get_from_amxm_mapping(airm_urn) 
    
    if results is None:
      return False
    else:
      print(airm_urn)
      return True

  def get_from_amxm_mapping(self, airm_urn):
    #print("Searching for " + airm_urn)
    amxm_df = self.amxm_mapping_dataframe.copy()
    
    filter = amxm_df["AIRM Concept Identifier"]==airm_urn
    amxm_df.sort_values("AIRM Concept Identifier", inplace = True)
    amxm_df.where(filter, inplace = True) 
    df_results = amxm_df.dropna(how='all')  
    
    if df_results.empty:
      return None
    else:
      results_dict = df_results.to_dict('records')
      return results_dict
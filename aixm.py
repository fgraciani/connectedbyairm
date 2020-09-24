import pandas as pd

class Aixm:
  aixm_mapping_dataframe = pd.read_excel (r'data/xlsx/AIXM_Semantic_Correspondence_Report.xlsx', sheet_name='semantic correspondences')
  #classes = pd.Dataframe() #TO DO load in init
  #properties = pd.Dataframe() #TO DO load in init
     
  def __init__(self):
    self.aixm_mapping_dataframe.fillna("missing data", inplace = True)
    #self.classes.fillna("missing data", inplace = True)
    #self.properties.fillna("missing data", inplace = True)

  def is_in_aixm_mapping(self, airm_urn):
    results = self.get_from_aixm_mapping(airm_urn) 
    
    if results is None:
      return False
    else:
      #print(airm_urn)
      return True

  def get_from_aixm_mapping(self, airm_urn):
    #print("Searching for " + airm_urn)
    aixm_df = self.aixm_mapping_dataframe.copy()
    
    filter = aixm_df["AIRM Concept Identifier"]==airm_urn
    aixm_df.sort_values("AIRM Concept Identifier", inplace = True)
    aixm_df.where(filter, inplace = True) 
    df_results = aixm_df.dropna(how='all')  
    
    if df_results.empty:
      return None
    else:
      results_dict = df_results.to_dict('records')
      return results_dict
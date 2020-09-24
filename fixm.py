import pandas as pd

class Fixm:
  fixm_mapping_dataframe = pd.read_excel (r'data/xlsx/mapping FIXM 4.2.0.xlsx', sheet_name='semantic correspondences')
  #classes = pd.Dataframe() #TO DO load in init
  #properties = pd.Dataframe() #TO DO load in init
     
  def __init__(self):
    self.fixm_mapping_dataframe.fillna("missing data", inplace = True)
    #self.classes.fillna("missing data", inplace = True)
    #self.properties.fillna("missing data", inplace = True)
  
  def create_url(self, id):
    url=""
    if isinstance(id, str):
        components = id.split(":")
        entity = components[-2]+"."+components[-1]
        url="fixm-4.2.0-to-airm-1.0.0/"+entity+".html"
    return url

  def is_in_fixm_mapping(self, airm_urn):
    results = self.get_from_fixm_mapping(airm_urn)
    if results is None:
      return False
    else:
      print(airm_urn)
      return True

  def get_from_fixm_mapping(self, airm_urn):
    #print("Searching for " + airm_urn)
    fixm_df = self.fixm_mapping_dataframe.copy()
    
    filter = fixm_df["Semantic Correspondence"]==airm_urn
    fixm_df.sort_values("Semantic Correspondence", inplace = True)
    fixm_df.where(filter, inplace = True) 
    df_results = fixm_df.dropna(how='all')      

    if df_results.empty:
      return None
    else:
      results_dict = df_results.to_dict('records')
      return results_dict
    
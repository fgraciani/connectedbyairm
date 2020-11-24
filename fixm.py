import pandas as pd

class Fixm:
  fixm_mapping_dataframe = pd.read_excel (r'data/xlsx/mapping FIXM 4.2.0.xlsx', sheet_name='semantic correspondences')
  fixm_definitions_dataframe = pd.read_excel (r'data/xlsx/FIXM classes.xlsx', sheet_name='FIXM Core 4.2.0')
  #classes = pd.Dataframe() #TO DO load in init
  #properties = pd.Dataframe() #TO DO load in init
     
  def __init__(self):
    self.fixm_mapping_dataframe.fillna("missing data", inplace = True)
    self.fixm_definitions_dataframe.fillna("missing data", inplace = True)
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
  
  def get_fixm_class_definition(self, fixm_class):
    fixm_df = self.fixm_definitions_dataframe.copy()
    
    filter = fixm_df["Information Concept"]==fixm_class
    fixm_df.sort_values("Information Concept", inplace = True)
    fixm_df.where(filter, inplace = True) 
    df_results = fixm_df.dropna(how='all')   
    definition = ""   
    print("*******FOUND DEFINITION FOR:"+fixm_class)
    print(df_results)
    
    if df_results.empty:
      return definition
    else:
      results_dict = df_results.to_dict('records')
      definition = ""
      for record in results_dict:
        if record['Information Concept'] == fixm_class:
          definition = record['Definition']
          print(definition)
      return definition

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
  
  def get_information_concepts(self):
    fixm_df = self.fixm_mapping_dataframe.copy()
    fixm_df = fixm_df.drop_duplicates(subset='Information Concept', keep="last")
    fixm_df = fixm_df.drop(["Data Concept", "Definition", "Type", "Semantic Correspondence", "Additional Traces", "Rationale", "Notes"], axis=1)
    
    if fixm_df.empty:
      return None
    else:
      results_dict = fixm_df.to_dict('records')
      return results_dict
  
  def get_traces_by_info_concept(self, info_concept):
    fixm_df = self.fixm_mapping_dataframe.copy()
    
    filter = fixm_df["Information Concept"]==info_concept
    fixm_df.sort_values("Information Concept", inplace = True)
    fixm_df.where(filter, inplace = True) 
    df_results = fixm_df.dropna(how='all')      

    if df_results.empty:
      return None
    else:
      results_dict = df_results.to_dict('records')
      return results_dict
    
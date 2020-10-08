import pandas as pd

class Airm:
  contextual_classes = pd.read_excel (r'data/xlsx/AIRM 1.0.0.xlsx', sheet_name='Contextual Classes')
  conceptual_classes = pd.read_excel (r'data/xlsx/AIRM 1.0.0.xlsx', sheet_name='Conceptual Classes')
  logical_classes = pd.read_excel (r'data/xlsx/AIRM 1.0.0.xlsx', sheet_name='Logical Classes')
  contextual_properties = pd.read_excel (r'data/xlsx/AIRM 1.0.0.xlsx', sheet_name='Contextual Properties')
  conceptual_properties = pd.read_excel (r'data/xlsx/AIRM 1.0.0.xlsx', sheet_name='Conceptual Properties')
  logical_properties = pd.read_excel (r'data/xlsx/AIRM 1.0.0.xlsx', sheet_name='Logical Properties')
  not_found_counter = 0
   
  def __init__(self):
    self.contextual_classes.fillna("missing data", inplace = True)
    self.conceptual_classes.fillna("missing data", inplace = True)
    self.logical_classes.fillna("missing data", inplace = True)
    self.contextual_properties.fillna("missing data", inplace = True)
    self.conceptual_properties.fillna("missing data", inplace = True)
    self.logical_properties.fillna("missing data", inplace = True)

  def valid_urn(urn): #TO DO: adapt regex to urn grammar
    import re
    regex = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return re.match(regex, urn)

  def load_and_find_urn(self, urn):
    print("Searching for: "+urn) #REMOVE WHEN WORKING
    name = "invalid urn"
    definition = "invalid urn"
    
    if "urn:" in urn:#if valid_urn(urn):
      if "ContextualModel" in urn:
        if "@" in urn:
          dataframe = self.contextual_properties.copy()
        else:
          dataframe = self.contextual_classes.copy()
      elif "ConceptualModel" in urn:
        if "@" in urn:
          dataframe = self.conceptual_properties.copy()
        else:
          dataframe = self.conceptual_classes.copy()
      elif "Logical" in urn:
        if "@" in urn:
          dataframe = self.logical_properties.copy()
        else:
          dataframe = self.logical_classes.copy()
      

      #Search block:
      filter = dataframe["urn"]==urn
      dataframe.sort_values("urn", inplace = True)
      dataframe.where(filter, inplace = True) 
      results = dataframe.dropna(how='all')   
      
      print("Results: ")#REMOVE WHEN WORKING
      print(results)#REMOVE WHEN WORKING

      if results.empty:
        self.not_found_counter += 1
        name = "not found"
        definition = "not found"
      
      else:
        name = results["name"].iloc[0]
        definition = results["definition"].iloc[0]

    entry = {
      "name": name,
      "definition": definition
    }
    
    return entry

def get_properties_by_parent(self,info_concept):
    properties_df = self.logical_properties.copy()
    
    filter = properties_df["parent"]==info_concept
    properties_df.sort_values("parent", inplace = True)
    properties_df.where(filter, inplace = True) 
    df_results = properties_df.dropna(how='all')      

    if df_results.empty:
      return None
    else:
      results_dict = df_results.to_dict('records')
      return results_dict
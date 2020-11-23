import pandas as pd

class Airm:
  contextual_abbreviations = pd.read_excel (r'data/xlsx/airm-1.0.0/cx_abbr.xlsx', sheet_name='cx_abbr')
  contextual_terms = pd.read_excel (r'data/xlsx/airm-1.0.0/cx_terms.xlsx', sheet_name='cx_terms')
  not_found_counter = 0
  conceptual_concepts = pd.read_excel (r'data/xlsx/airm-1.0.0/cp_all.xlsx', sheet_name='cp_all')
  logical_concepts = pd.read_excel (r'data/xlsx/airm-1.0.0/logical_all.xlsx', sheet_name='logical_all')
  
  df_connected_index = pd.read_excel (r'data/xlsx/connected_index.xlsx', sheet_name='connceted_index')
   
  def __init__(self):
    print("init")

    self.contextual_abbreviations.fillna("missing data", inplace = True)
    self.contextual_terms.fillna("missing data", inplace = True)
    self.conceptual_concepts.fillna("missing data", inplace = True)
    self.logical_concepts.fillna("missing data", inplace = True)
    
    self.df_connected_index.fillna("missing data", inplace = True)
    
    print("missing data applied")

    self.contextual_abbreviations.columns = ["supplement","stereotype","class name","property name", "type", "definition", "synonyms", "abbreviation", "urn",  "parent", "source"]
    self.contextual_terms.columns = ["supplement","stereotype","class name","property name", "type", "definition", "synonyms", "abbreviation", "urn",  "parent", "source"]
    self.conceptual_concepts.columns = ["supplement","stereotype","class name","property name", "type", "definition", "synonyms", "abbreviation", "urn",  "parent", "source"]
    self.logical_concepts.columns = ["supplement","stereotype","class name","property name", "type", "definition", "synonyms", "abbreviation", "urn",  "parent", "source"]

    print("new collumn names")

  def get_connections_by_urn(self,urn):
    connections_df = self.df_connected_index.copy()
    
    filter = connections_df["airm_urn"]==urn
    connections_df.sort_values("airm_urn", inplace = True)
    connections_df.where(filter, inplace = True) 
    df_results = connections_df.dropna(how='all')      

    if df_results.empty:
      return None
    else:
      results_dict = df_results.to_dict('records')
      return results_dict


  def get_logical_properties_by_class(self, class_name, scope):
    logical_df = self.logical_concepts.copy()

    filter = logical_df["class name"] == class_name
    logical_df.sort_values("class name", inplace = True)
    logical_df.where(filter, inplace = True) 
    df_results01 = logical_df.copy()    

    if scope == "global":
      scope_filter = "\t"
    elif scope == "European Supplement":
      scope_filter = "\tEuropean Supplement"
    
    df_results01.fillna("missing data", inplace = True)
    filter = df_results01["stereotype"]=="missing data"
    df_results01.sort_values("stereotype", inplace = True)
    df_results01.where(filter, inplace = True)
    df_results02 = df_results01.copy()

    filter = df_results02["supplement"]==scope_filter
    df_results02.sort_values("supplement", inplace = True)
    df_results02.where(filter, inplace = True) 
    df_results03 = df_results02.dropna(how='all') 

    if df_results03.empty:
      return None
    else:
      results_dict = df_results03.to_dict('records')
      return results_dict

  def get_concept_properties_by_parent(self, parent, scope):
    
    concepts_df = self.conceptual_concepts.copy()
    
    filter = concepts_df["class name"]==parent
    concepts_df.sort_values("class name", inplace = True)
    concepts_df.where(filter, inplace = True) 
    df_results01 = concepts_df.copy()    

    if scope == "global":
      scope_filter = "\t"
    elif scope == "European Supplement":
      scope_filter = "\tEuropean Supplement"
    
    df_results01.fillna("missing data", inplace = True)
    filter = df_results01["stereotype"]=="missing data"
    df_results01.sort_values("stereotype", inplace = True)
    df_results01.where(filter, inplace = True)
    df_results02 = df_results01.copy()

    filter = df_results02["supplement"]==scope_filter
    df_results02.sort_values("supplement", inplace = True)
    df_results02.where(filter, inplace = True) 
    df_results03 = df_results02.dropna(how='all') 

    if df_results03.empty:
      return None
    else:
      results_dict = df_results03.to_dict('records')
      return results_dict
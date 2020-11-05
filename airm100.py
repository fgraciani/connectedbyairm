import pandas as pd

class Airm:
  contextual_abbreviations = pd.read_excel (r'data/xlsx/airm-1.0.0/cx_abbr.xlsx', sheet_name='cx_abbr')
  not_found_counter = 0
   
  def __init__(self):
    self.contextual_abbreviations.fillna("missing data", inplace = True)

    self.contextual_abbreviations.columns = ["supplement","stereotype","class name","property name", "type", "definition", "synonyms", "abbreviation", "urn",  "parent", "source"]
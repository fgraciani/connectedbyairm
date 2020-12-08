import pandas as pd
import json

df = pd.read_excel (r'data/xlsx/mapping FIXM 4.2.0.xlsx', sheet_name='semantic correspondences')
issue_url="http://fixm.aero"

mapping = df.to_dict('records')

data = {}
data['mapping'] = []

def create_url(urn):
  url=""
  if isinstance(urn, str):
    if urn.startswith("changeRequest"):
      url="https://ext.eurocontrol.int/swim_confluence/display/SWIM/SWIM-INFO-014+Forms+of+semantic+correspondence"
    elif urn=="outOfScope":
      url="https://ext.eurocontrol.int/swim_confluence/display/SWIM/SWIM-INFO-015+Out-of-scope+or+no+correspondence"
    elif urn.startswith("noSemanticCorrespondence"):
      url=issue_url
    elif urn.startswith("urn"):
      components = urn.split(":")
      last_component = components[-1]
      components = last_component.split("@")
      entity = components[0]
      url="http://airm.aero/viewer/1.0.0/includes-supplements/logical-model.html#"+entity
  return url

def create_name(urn):
  name=""
  if isinstance(urn, str):
    if urn.startswith("changeRequest"):
      name="AIRM Change Request"
    elif urn=="outOfScope":
      name="Out of Scope"
    elif urn.startswith("noSemanticCorrespondence"):
      name="No Semantic Correspondence"
    elif urn.startswith("urn"):
      components = urn.split(":")
      last_component = components[-1]
      name = last_component
  return name

def process_multiple(urn):
  components = ["",""]
  if isinstance(urn, str):
    components = urn.split("\n")

  return components

for record in mapping:
  additionals = process_multiple(record['Additional Traces'])
  if len(additionals)<2:
    additionals.append("")
  
  if isinstance(record['Data Concept'], str):
    data['mapping'].append({
      'Concept': record['Information Concept']+'@'+record['Data Concept'],
      'html': 'fixm-4.2.0-to-airm-1.0.0/'+record['Information Concept']+'.'+record['Data Concept']+'.html',
      'Id': record['Identifier'],
      'Definition': record['Definition'],
      'Type': record['Type'],
      'Rationale': record['Rationale'],
      'Notes': record['Notes'],
      'Correspondence': create_name(record['Semantic Correspondence']),
      'urn': record['Semantic Correspondence'],
      'url': create_url(record['Semantic Correspondence']),
      'Additional': create_name(additionals[0]),
      'addurn': additionals[0],
      'addurl': create_url(additionals[0]),
      'Additional2': additionals[1],
      'addurl2': create_url(additionals[1])
})

def transform():
  
  with open('data/json/fixm-mapping.json', 'w') as outfile:
    json.dump(data['mapping'], outfile, indent=4)

  print("Done")
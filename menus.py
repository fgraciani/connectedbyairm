import xlsx2json
import json2html
import amxm2html
import my_zip
import airm
import airm_importer
import amxm_overlap_comparator as compare
import fixm_overlap_comparator as compare_fixm

def main(): #See https://github.com/Mckinsey666/bullet for improvements
  choice ='0'
  while choice =='0':
      print('\n')
      print("Menu: ")
      print("1: Generate excel file from AIRM xmi")
      print("2: Find AIRM element by URN")
      print("3: Generate JSON file from excel mapping")
      print("4: Create html pages from FIXM JSON file")
      print("5: Create zip file from html/export...")
      print("6: Compare AMXM other XMs")
      print("7: Compare FIXM other XMs")
      print("8: Create html pages from AMXM mapping")

      choice = input ("Please make a choice: ")

      if choice == "1":
          print('\n')
          print("Generating excel file from AIRM xmi...")
          dataframes=airm_importer.import_xmi("data/xml/airm")
          main()
      elif choice == "2":
          #dataframes=airm.import_xmi("data/xml/airm")
          urn = input("provide a URN (type exit to go back to the menu)>")
          while urn!="exit":
            print(airm.load_and_find_urn(urn))
            urn = input("provide a URN (type exit to go back to the menu)>")
          main()
      elif choice == "3":
          print('\n')
          print("Generating JSON file from excel mapping...")
          xlsx2json.transform()
          main()
      elif choice == "4":
          print('\n')
          print("Creating html pages from JSON file...")
          json2html.create_html()
          main()
      elif choice == "5":
          print('\n')
          name = input ("How would you like to name the .zip file? (Do not use .zip as part of the name): ")
          print("Creating zip file from html/export...")
          my_zip.compress("data/html/export",name)
          main()   
      elif choice == "6":
          print('\n')
          compare.report()
          main()     
      elif choice == "7":
          print('\n')
          compare_fixm.report()
          main()     
      elif choice == "8":
          print('\n')
          print("Creating html pages from JSON file...")
          amxm2html.create_html()
          main()       
      else:
          print("I don't understand your choice.")
          main()
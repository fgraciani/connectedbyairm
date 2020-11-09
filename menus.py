import xlsx2json
import json2html
import amxm2html
import fixm2html
import airm2html
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
      print("8: Create index from AMXM mapping")
      print("9: Create html index from FIXM mapping")
      print("10: Create html pages from FIXM mapping")
      print("11: Create html index for AIRM Advanced Viewer")
      print("12: Create html pages for AIRM Advanced Viewer")
      print("13: Create xml with connected index for Advanced Viewer")
      print("14: Create html pages from AMXM mapping")
      print("15: Create index from AIXM mapping")
      print("16: Create pages from AIXM mapping")
      print("17: VIEWER - CX - ABBREVIATIONS - Create index")
      print("18: VIEWER - CX - ABBREVIATIONS - Create pages")
      print("19: VIEWER - CX - TERMS - Create index")
      print("20: VIEWER - CX - TERMS - Create pages")

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
          print("Creating html index from xls file...")
          amxm2html.create_html()
          main()        
      elif choice == "9":
          print('\n')
          print("Creating html pages from xls file...")
          fixm2html.create_html()
          main()   
      elif choice == "10":
          print('\n')
          print("Creating html pages from xls file...")
          fixm2html.create_html_pages()
          main()       
      elif choice == "11":
          print('\n')
          print("Creating html pages from xls file...")
          airm2html.create_html()
          main()        
      elif choice == "12":
          print('\n')
          print("Creating html pages from xls file...")
          airm2html.create_html_pages()
          main()          
      elif choice == "13":
          print('\n')
          print("Creating conncected index...")
          airm.create_connected_index()
          main()  
      elif choice == "14":
          print('\n')
          print("Creating html pages...")
          amxm2html.create_html_pages()
          main()  
      elif choice == "15":
          print('\n')
          print("Creating html pages from xls file...")
          import aixm2html
          aixm2html.create_html()
          print("Done")
          main()  
      elif choice == "16":
          print('\n')
          print("Creating html pages from xls file...")
          import aixm2html
          aixm2html.create_html_pages()
          print("Done")
          main()      
      elif choice == "17":
          print('\n')
          print("VIEWER - CX - ABBREVIATIONS (Global) Creating index from xls file...")
          import airm2html
          airm2html.create_index_cx_abbs_global()
          print("Done")
          print("VIEWER - CX - ABBREVIATIONS (Supps) Creating index from xls file...")
          airm2html.create_index_cx_abbs_supp()
          print("Done")
          main()        
      elif choice == "18":
          print('\n')
          print("VIEWER - CX - ABBREVIATIONS Creating pages from xls file...")
          import airm2html
          airm2html.create_pages_cx_abbs()
          print("Done")
          main()          
      elif choice == "19":
          print('\n')
          print("VIEWER - CX - TERMS Creating index from xls file...")
          import airm2html
          airm2html.create_index_cx_terms_global()
          print("Done")
          print("VIEWER - CX - TERMS (Supps) Creating index from xls file...")
          airm2html.create_index_cx_terms_supp()
          print("Done")
          main()          
      elif choice == "20":
          print('\n')
          print("VIEWER - CX - TERMS Creating pages from xls file...")
          import airm2html
          airm2html.create_pages_cx_terms()
          print("Done")
          main()     
      else:
          print("I don't understand your choice.")
          main()
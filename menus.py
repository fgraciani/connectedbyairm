def main(): #See https://github.com/Mckinsey666/bullet for improvements
  choice ='0'
  while choice =='0':
      print('\n')
      print("Menu: ")
      print('\n')
      print("1: Create index from AMXM mapping")
      print("2: Create html pages from AMXM mapping")
      print('\n')
      print("3: Create html index from FIXM mapping")
      print("4: Create html pages from FIXM mapping")
      print('\n')
      print("5: Create index from AIXM mapping")
      print("6: Create pages from AIXM mapping")
      print('\n')
      print("7: Create index from AIXM ADR mapping")
      print("8: Create pages from AIXM ADR mapping")
      print('\n')
      print("9: Create connected graph for AIRM Viewer")
      print('\n')
      print("10: VIEWER - CX - ABBREVIATIONS - Create index")
      print("11: VIEWER - CX - ABBREVIATIONS - Create pages")
      print("12: VIEWER - CX - TERMS - Create index")
      print("13: VIEWER - CX - TERMS - Create pages")
      print('\n')
      print("14: VIEWER - CP - Create index")
      print("15: VIEWER - CP - Create pages")
      print('\n')
      print("16: VIEWER - LOGICAL - Create index")
      print("17: VIEWER - LOGICAL - Create pages")
      print('\n')
      choice = input ("Please make a choice: ")
      print('\n')

      if choice == "1":
          print('\n')
          print("Creating html index from .xls file...")
          import amxm2html
          amxm2html.create_html()
          main()    

      elif choice == "2":
          print('\n')
          print("Creating html pages from .xls file...")
          import amxm2html
          amxm2html.create_html_pages()
          main()   

      elif choice == "3":
          print('\n')
          print("Creating html pages from .xls file...")
          import fixm2html
          fixm2html.create_html()
          main()   

      elif choice == "4":
          print('\n')
          print("Creating html pages from .xls file...")
          import fixm2html
          fixm2html.create_html_pages()
          main()    

      elif choice == "5":
          print('\n')
          print("Creating html pages from .xls file...")
          import aixm2html
          aixm2html.create_html()
          print("Done")
          main()  

      elif choice == "6":
          print('\n')
          print("Creating html pages from .xls file...")
          import aixm2html
          aixm2html.create_html_pages()
          print("Done")
          main()   

      elif choice == "7":
          print('\n')
          print("Creating html pages from .xls file...")
          import aixm_adr2html
          aixm_adr2html.create_html()
          print("Done")
          main()  

      elif choice == "8":
          print('\n')
          print("Creating html pages from .xls file...")
          import aixm_adr2html
          aixm_adr2html.create_html_pages()
          print("Done")
          main() 

      elif choice == "9":
          print('\n')
          print("Creating conncected index...")
          import airm
          airm.create_connected_index()
          main()  
      
          
      elif choice == "10":
          print('\n')
          print("VIEWER - CX - ABBREVIATIONS (Global) Creating index from .xls file...")
          import airm2html
          airm2html.create_index_cx_abbs_global()
          print("Done")
          print("VIEWER - CX - ABBREVIATIONS (Supps) Creating index from .xls file...")
          airm2html.create_index_cx_abbs_supp()
          print("Done")
          main()      

      elif choice == "11":
          print('\n')
          print("VIEWER - CX - ABBREVIATIONS Creating pages from .xls file...")
          import airm2html
          airm2html.create_pages_cx_abbs()
          print("Done")
          main()  

      elif choice == "12":
          print('\n')
          print("VIEWER - CX - TERMS Creating index from .xls file...")
          import airm2html
          airm2html.create_index_cx_terms_global()
          print("Done")
          print("VIEWER - CX - TERMS (Supps) Creating index from .xls file...")
          airm2html.create_index_cx_terms_supp()
          print("Done")
          main()    

      elif choice == "13":
          print('\n')
          print("VIEWER - CX - TERMS Creating pages from .xls file...")
          import airm2html
          airm2html.create_pages_cx_terms()
          print("Done")
          main()  

      elif choice == "14":
          print('\n')
          print("VIEWER - CP Creating index from .xls file...")
          import airm2html
          airm2html.create_index_cp_global()
          print("Done")
          print("VIEWER - CP (Supps) Creating index from .xls file...")
          airm2html.create_index_cp_supp()
          print("Done")
          main()    

      elif choice == "15":
          print('\n')
          print("VIEWER - CP Creating pages from .xls file...")
          import airm2html
          airm2html.create_pages_cp_concepts()
          print("Done")
          main()      

      elif choice == "16":
          print('\n')
          print("VIEWER - LOGICAL Creating index from .xls file...")
          import airm2html
          airm2html.create_index_logical_global()
          print("Done")
          print("VIEWER - LOGICAL (Supps) Creating index from .xls file...")
          airm2html.create_index_logical_supp()
          print("Done")
          main()       

      elif choice == "17":
          print('\n')
          print("VIEWER - LOGICAL Creating pages from .xls file...")
          import airm2html
          airm2html.create_pages_logical_concepts()
          print("Done")
          main()

      else:
          print("I don't understand your choice.")
          main()


          
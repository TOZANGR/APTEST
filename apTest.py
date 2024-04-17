from tkinter import *
import overpy
api = overpy.Overpass()
root = Tk()
root.title("App")
root.geometry('510x200')
lbl = Label(root, text = "Please enter a housenumber")
lbl.grid()
txt = Entry(root, width=10)
txt.grid(column =1, row =0)
lbl1 = Label(root, text = "Please enter an area(city, state, country, province, ect)")
lbl1.grid()
txt1 = Entry(root, width=10)
txt1.grid(column =1, row =1)
results = Label(root, text= "results: ")
results.grid(column=0, row=3)
def clicked():
   value = txt.get()
   area = txt1.get()
   result = api.query("""
   area[name = """ + area + """]->.a;
  (
  node["addr:housenumber" = """ + value + """](area.a);
  way["addr:housenumber" = """ + value + """](area.a);
  relation["addr:housenumber" = """ + value + """](area.a);
  );
  out center;
   """)
   coords  = []
   coords += [node.tags
          for node in result.nodes]
   coords += [way.tags
          for way in result.ways]
   coords += [relation.tags
          for relation in result.relations]
   addr = []
   final = ''
   for i in coords:
      if i.get("addr:housenumber"):
         final += i.get('addr:housenumber')
         final += ' ' 
         print(i)
         if i.get("addr:street"):
              final += i.get('addr:street') 
              final += ' '
              if i.get("addr:city"):
                     final += ' '
                     final += i.get('addr:city') 
                     if i.get("addr:postcode"):
                            final += ' '
                            final += i.get('addr:postcode')   
                            if i.get("addr:state"):
                                   final += ' '
                                   final += i.get('addr:state')
                            if i.get("addr:country"):
                                 final += ' '
                                 final += i.get('addr:country')
      print(final, '\n')
      addr.append(final)
      final = ''
   j = 0
   x = 0
   global root
   root.destroy()
   root1 = Tk()
   for i in range(len(addr)):
        x += 1
        addressLabel = Label(root1, text=addr[i])
        addressLabel.grid(column=j, row=(x + 4))
        root1.geometry(str(300 * (j + 1)) + 'x' + str(25 * i))
        if x > 44:
             j += 1
             x = 0
   root1.mainloop()           
btn = Button(root, text = "Enter" ,
            fg = "red", command=clicked)
btn.grid(column=2, row=1)
root.mainloop()
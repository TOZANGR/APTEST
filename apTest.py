from tkinter import *
import overpy
api = overpy.Overpass()
root = Tk()
root.title("Bingus")
root.geometry('350x200')
lbl = Label(root, text = "Please enter")
lbl.grid()
txt = Entry(root, width=10)
txt.grid(column =1, row =0)
def clicked():
   value = txt.get()
   result = api.query("""
   area[name = "Portland"]->.a;
  (
  node["addr:housenumber" = """ + value + """](area.a);
  way["addr:housenumber" = """ + value + """](area.a);
  relation["addr:housenumber" = """ + value + """](area.a);
  );
  out center;
   """)
   coords  = []
   coords += [node.lat
          for node in result.nodes]
   coords += [way.id
          for way in result.ways]
   coords += [relation.id
          for relation in result.relations]
   print(coords)
btn = Button(root, text = "Click me" ,
            fg = "red", command=clicked)
btn.grid(column=2, row=0)
root.mainloop()
      
import PIL 
from PIL import Image
from tkinter import Tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import Label

# creating an instane as 

win = Tk()
win.geometry("400x400")
win.configure(bg='black')
def openFiles():
  imagelist =[]
  newimagelist =[]
  finallist = []
  file_path =  filedialog.askopenfilenames()
  for files in file_path:
   imagelist.append(PIL.Image.open(files))
  for images in imagelist: 
      newimagelist.append(images.convert('RGB'))
  for  img in newimagelist:
    finallist.append(img.resize((img.size),PIL.Image.ANTIALIAS))




  save_path = filedialog.asksaveasfilename()
  new1 = newimagelist[0]  
  new1.save(save_path+r"_compressed.pdf",save_all = True,append_images=finallist)
  print("*****")

labels = Label(win, text="Select the Button to Open the File", font=('Aerial 11'))
labels.pack(pady=30)

ttk.Button(win, text="Select a File", command=openFiles).pack()
win.mainloop()
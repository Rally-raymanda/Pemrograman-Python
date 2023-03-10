import tkinter as tk 
from functools import partial

def pertambahan (labelHasil, bil1, bil2):
    b1 = int(bil1.get()) 
    b2 = int(bil2.get())
    hasil = b1 + b2
    labelHasil.config(text=hasil)
    return

root = tk.Tk()
root.geometry('400x200+500+200')
root.option_add('*font', ('Verdana', 10, 'normal'))
root.title('Aritmatika')

labelBilangan1 = tk.Label(root, text="Masukkan Bilangan 1")
labelBilangan1.grid(row=0, column=0, padx=(10,20))

labelBilangan2 = tk.Label(root, text="Masukkan Bilangan 2")
labelBilangan2.grid(row=1, column=0, padx=(10,20))

bilangan1 = tk.StringVar()
bilangan2 = tk.StringVar()

inputBilangan1 = tk.Entry(root, textvariable=bilangan1) 
inputBilangan1.grid(row=0, column=1)

inputBilangan2 = tk.Entry(root, textvariable=bilangan2) 
inputBilangan2.grid(row=1, column=1)

labelHasil = tk.Label(root)
labelHasil.grid(row=2, column=1)

pertambahan = partial(pertambahan, labelHasil, bilangan1, bilangan2)

tombolTambah = tk.Button(root, text="Tambah", command=pertambahan) 
tombolTambah.grid(row=2, column=0, sticky="WE", padx=(10,20), pady=(5,0)) 
tombolTambah.configure(bg="#000", fg="#FFF")

root.mainloop()

from tkinter import *
from dao.UsuarioDao import UsuarioDao
from config.Config import Config
from config.Database import Database

config = Config()
database = Database(config.config)
dao = UsuarioDao(database.conn)

main = Tk()
main.title("Meu formulário")
main.geometry("800x600")

row = Frame(main)
row.pack(side=TOP, fill=X, padx=5, pady=5)

lbl = Label(row, text="Id:", anchor='w')
lbl.pack(side=LEFT)

txt = Entry(row)
txt.pack(side=LEFT, expand=YES, fill=X, padx=5)

def apagarUsuario():
    id = int(txt.get())

    dao.apagarUsuario1(id)

btn = Button(main, text="Apagar", command=apagarUsuario)
btn.pack(side=LEFT, padx=5, pady=5)

btn = Button(main, text="Fechar", command=main.destroy)
btn.pack(side=RIGHT, padx=5, pady=5)

main.mainloop()

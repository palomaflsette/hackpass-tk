from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import json


root = Tk()

dic = {"opHack": {},
       "dataNasc": "",
       "PrimeirosNumCpf": "",
       "numCel": "",
       "numTel": "",
       "cep": "",
       "rg": "",
       "numDigPass": "",
       "numApto": "",
       "velocExec": "",
       "dadosImp": []}

class App():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.elementos_frame_1()
        self.elementos_frame_2()
        #self.browseFiles()
        root.mainloop()
        
        
    def tela(self):
        self.root.title("Hackpass")
        self.root.configure(background='#10161C')
        self.root.geometry("820x620")
        self.root.resizable(True, True)
        self.root.maxsize(width=1200, height=700)
        self.root.minsize(width=400, height= 220)
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg='#012C36',
                             highlightbackground='#04404E', highlightthickness=2)
        self.frame_1.place(relx=0.02 , rely=0.02, relwidth=0.96, relheight=0.46)
        
    def browseFiles(self):
        self.filename = filedialog.askopenfilename(initialdir="/",
                                                title="Select a File",
                                                filetypes=(("Text files",
                                                            "*.txt*"),
                                                            ("all files",
                                                            "*.*")))
        label_file_explorer = Label(self.frame_1,
                                            text="File Explorer",
                                            width=35, height=1,
                                            fg="#FFFFFF", bg='#0E647B')
        label_file_explorer.place(relx=0.70, rely=0.62)
        # Change label contents
        self.label_file_explorer.configure(text=self.filename,
                                        fg="#FFFFFF", bg='#0E647B')
        self.label_file_explorer.place(relx=0.80, rely=0.62)


    def elementos_frame_1(self):
        #### Botões 
        self.bt1 = Button(self.frame_1, text='Executar', command=self.submit_entry_value)
        self.bt1.place(relx=0.35, rely=0.85, 
                      relwidth=0.10, relheight=0.12)
        self.bt2 = Button(self.frame_1, text='Salvar dados', command=self.file_save)
        self.bt2.place(relx=0.55, rely=0.85, 
                      relwidth=0.13, relheight=0.12)
        # def browseFiles():
        #     filename = filedialog.askopenfilename(initialdir="/",
        #                                             title="Select a File",
        #                                             filetypes=(("Text files",
        #                                                         "*.txt*"),
        #                                                         ("all files",
        #                                                         "*.*")))
        #     label_file_explorer = Label(self.frame_1,
        #                                      text="File Explorer",
        #                                      width=35, height=1,
        #                                      fg="#FFFFFF", bg='#0E647B')
        #     label_file_explorer.place(relx=0.70, rely=0.62)
        #     # Change label contents
        #     label_file_explorer.configure(text=filename,
        #                                     fg="#FFFFFF", bg='#0E647B')
        #     label_file_explorer.place(relx=0.69, rely=0.62)
        self.bt3 = Button(self.frame_1, text='Importar', command=self.browseFiles)
        self.bt3.place(relx=0.6, rely=0.62,
                       relwidth=0.08, relheight=0.085)
        
        #### Checkboxes
        self.check_dic = Checkbutton(
            self.frame_1, text='Dict',
            variable=self.var_checkbutton_dic , onvalue=1, offvalue=0, 
            command=self.display_input_cb,
            bg='#012C36', fg='#7F8C8D')
        self.check_fb = Checkbutton(
            self.frame_1, text='BF', variable=self.var_checkbutton_fb, 
            onvalue=1, offvalue=0, command=self.display_input_cb, 
            bg='#012C36', fg='#7F8C8D')
        self.check_dic.place(relx=0.55, rely=0.02,
                             relwidth=0.10, relheight=0.15)
        self.check_fb.place(relx=0.4, rely=0.02,
                            relwidth=0.10, relheight=0.15)    
        
        ### Labels 
        self.lb_codigo = Label(
            self.frame_1, text='Data de nascimento:', bg='#012C36', fg='#FFFFFF')
        self.lb_codigo.place(relx=0.01, rely=0.2)
        self.lb_codigo = Label(
            self.frame_1, text='Três 1os. díg. CPF:', bg='#012C36', fg='#FFFFFF')
        self.lb_codigo.place(relx=0.01, rely=0.3)
        self.lb_codigo = Label(
            self.frame_1, text='Número cel.:', bg='#012C36', fg='#FFFFFF')
        self.lb_codigo.place(relx=0.01, rely=0.4)
        self.lb_codigo = Label(
            self.frame_1, text='Número tel.::', bg='#012C36', fg='#FFFFFF')
        self.lb_codigo.place(relx=0.01, rely=0.5)
        self.lb_codigo = Label(
            self.frame_1, text='CEP.:', bg='#012C36', fg='#FFFFFF')
        self.lb_codigo.place(relx=0.01, rely=0.6)
        self.lb_codigo = Label(
            self.frame_1, text='Número do RG:', bg='#012C36', fg='#FFFFFF')
        self.lb_codigo.place(relx=0.01, rely=0.7)
        self.lb_codigo = Label(
            self.frame_1, text='Nº de dígitos da senha:', bg='#012C36', fg='#FFFFFF')
        self.lb_codigo.place(relx=0.6, rely=0.3)
        self.lb_codigo = Label(
            self.frame_1, text='Número apto.:', bg='#012C36', fg='#FFFFFF')
        self.lb_codigo.place(relx=0.6, rely=0.4)
        self.lb_codigo = Label(
            self.frame_1, text='Velocidade exec.:', bg='#012C36', fg='#FFFFFF')
        self.lb_codigo.place(relx=0.6, rely=0.5)
        
        self.label_file_explorer = Label(self.frame_1,
                                    text="File Explorer",
                                    width=35, height=1,
                                    fg="#FFFFFF", bg='#0E647B')
        self.label_file_explorer.place(relx=0.70, rely=0.62)
        
        ### Entries
        self.data_nasc = Entry(self.frame_1)
        self.data_nasc.place(relx=0.2, rely=0.2)
        self.data_nasc.bind("<Return>", 
                            self.submit_entry_value)
        self.tres_num_cpf = Entry(self.frame_1)
        self.tres_num_cpf.place(relx=0.2, rely=0.3)
        self.tres_num_cpf.bind("<Return>",
                            self.submit_entry_value)
        self.num_cel = Entry(self.frame_1)
        self.num_cel.place(relx=0.2, rely=0.4)
        self.num_cel.bind("<Return>",
                            self.submit_entry_value)
        self.num_tel = Entry(self.frame_1)
        self.num_tel.place(relx=0.2, rely=0.5)
        self.num_tel.bind("<Return>",
                            self.submit_entry_value)
        self.cep = Entry(self.frame_1)
        self.cep.place(relx=0.2, rely=0.6)
        self.cep.bind("<Return>",
                            self.submit_entry_value)
        self.rg = Entry(self.frame_1)
        self.rg.place(relx=0.2, rely=0.7)
        self.rg.bind("<Return>",
                            self.submit_entry_value)
        self.num_alg_entry = Entry(self.frame_1)
        self.num_alg_entry.place(relx=0.81, rely=0.3, width=25)
        self.num_alg_entry.bind("<Return>",
                            self.submit_entry_value)
        self.num_apto = Entry(self.frame_1)
        self.num_apto.place(relx=0.81, rely=0.4, width=25)
        self.num_apto.bind("<Return>",
                            self.submit_entry_value)
        self.veloc = Entry(self.frame_1)
        self.veloc.place(relx=0.81, rely=0.5, width=25)
        self.veloc.bind("<Return>",
                        self.submit_entry_value)
        
        #label - explorador de arquivos
        # label_file_explorer = Label(self.frame_1,
        #                             text="File Explorer",
        #                             width=35, height=1,
        #                             fg="#FFFFFF", bg='#0E647B')
        # label_file_explorer.place(relx=0.70, rely=0.62)
    var_checkbutton_fb = IntVar()
    var_checkbutton_dic = IntVar()
    def display_input_cb(self):
        dic['opHack'] = {'BruteForce': self.var_checkbutton_fb.get(),
                         'Dic': self.var_checkbutton_dic.get()}
        
    def file_save(self):
        f = filedialog.asksaveasfile(mode='w', defaultextension=".json")
        if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
            return
        text2save = str(self.txtBox.get(1.0, END))  # starts from `1.0`, not `0.0`
        f.write(text2save)
        f.close()
    
        
    def submit_entry_value(self):
        self.getEntry1 = self.data_nasc.get()
        self.getEntry2 = self.tres_num_cpf.get()
        self.getEntry3 = self.num_cel.get()
        self.getEntry4 = self.num_tel.get()
        self.getEntry5 = self.cep.get()
        self.getEntry6 = self.rg.get()
        self.getEntry7 = self.num_alg_entry.get()
        self.getEntry8 = self.num_apto.get()
        self.getEntry9 = self.veloc.get()
        self.getEntry10 = self.veloc.get()
        lista_ent_val = [{}, self.getEntry1, self.getEntry2, 
                         self.getEntry3, self.getEntry4,
                         self.getEntry5, self.getEntry6, 
                         self.getEntry7, self.getEntry8, 
                         self.getEntry9, ['senha1', 'senha2']]
        
        
        for i, (k, v) in enumerate(dic.items()):
            if type(dic[k]) is list and type(lista_ent_val[i]) is list:
                for el in lista_ent_val[i]:
                    dic[k].append(el)
            else:
                if type(dic[k]) is str and type(lista_ent_val[i]) is str:
                    dic[k] = lista_ent_val[i]
                
        self.txtBox.insert(INSERT, json.dumps(dic, indent=4))
        
    def elementos_frame_2(self):
        ### TextBox
        self.txtBox = Text(self.root , bd=4, bg='#000000', fg='#FFFFFF',
                            highlightbackground='#04404E', highlightthickness=2)
        self.txtBox.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
    
App()
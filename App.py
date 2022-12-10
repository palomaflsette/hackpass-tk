from tkinter import *
from tkinter import ttk
import re
from random import randint
import tkinter.scrolledtext as scrolledtext
from tkinter import filedialog
import json
import serial 
from time import sleep
from tqdm import tqdm


root = Tk()

global filename
filename = False

# dic = {"opHack": {},
#        "dataNasc": "",
#        "PrimeirosNumCpf": "",
#        "numCel": "",
#        "numTel": "",
#        "cep": "",
#        "rg": "",
#        "numDigPass": "",
#        "numApto": "",
#        "velocExec": "",
#        "dadosImp": []}

global dic
dic = {}

global serialcomm
serialcomm = serial.Serial('COM4', 9600)
serialcomm.timeout = 1

global lista_dados_exp
lista_dados_exp = []
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
        global filename 
        filename = filedialog.askopenfilename(initialdir="/",
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
        self.label_file_explorer.configure(text=filename,
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

    var_checkbutton_fb = IntVar()
    var_checkbutton_dic = IntVar()
    def display_input_cb(self):
        global dic
        dic['opHack'] = {'BruteForce': self.var_checkbutton_fb.get(),
                         'Dic': self.var_checkbutton_dic.get()}
        
    def file_save(self):
        global dic
        global lista_dados_exp
        a = self.data_nasc.get()
        b = self.tres_num_cpf.get()
        c = self.num_cel.get()
        d = self.num_tel.get()
        e = self.cep.get()
        f = self.rg.get()
        g = self.num_alg_entry.get()
        h = self.num_apto.get()
        i = self.veloc.get()
        dic["dataNasc"] = a
        dic["PrimeirosNumCpf"] = b
        dic["numCel"] = c
        dic["numTel"] = d
        dic["cep"] = e
        dic["rg"] = f
        dic["numDigPass"] = g
        dic["numApto"] = h
        dic["velocExec"] = i
        global filename
        if filename is not False:
            with open(filename, 'r') as file:
                for line in file:
                    lista_dados_exp.append(line.replace('\n', ''))
        dic["dadosExportados"] = lista_dados_exp
        files = [('JSON File', '*.json')]
        filepos = filedialog.asksaveasfile(filetypes=files, defaultextension=json, initialfile='IOTEDU')
        json.dump(dic, filepos, indent=4)
    

        
    def submit_entry_value(self):
        global dic
        global serialcomm
        self.getEntry1 = self.data_nasc.get()
        self.getEntry2 = self.tres_num_cpf.get()
        self.getEntry3 = self.num_cel.get()
        self.getEntry4 = self.num_tel.get()
        self.getEntry5 = self.cep.get()
        self.getEntry6 = self.rg.get()
        self.getEntry7 = self.num_alg_entry.get()
        self.getEntry8 = self.num_apto.get()
        self.getEntry9 = self.veloc.get()
        dic["dataNasc"] = self.getEntry1
        dic["PrimeirosNumCpf"] = self.getEntry2
        dic["numCel"] = self.getEntry3
        dic["numTel"] = self.getEntry4
        dic["cep"] = self.getEntry5
        dic["rg"] = self.getEntry6
        dic["numDigPass"] = self.getEntry7
        dic["numApto"] = self.getEntry8
        dic["velocExec"] = self.getEntry9
        global filename
        if filename is not False:
            with open(filename, 'r') as file:
                for line in file:
                    lista_dados_exp.append(line.replace('\n', ''))
        dic["dadosExportados"] = lista_dados_exp
        
        entradas = ''
        not_digit = []
        digit = []
        lista = list(dic.values())
        for value in lista:
            if type(value) is str:
                if not value.isdigit() and value != '':
                    not_digit.append(value)
                else:
                    # TRATANDO DOS VALORES QUE SÃO PURAMENTE DIGITOS
                    entradas = entradas + value+','
            # TRATANDO DOS DADOS NO DICIONÁRIO QUE NÃO SÃO STRING
            elif type(value) is list:
                temp = value
                for v in temp:
                    entradas = entradas + v+','

        for value in not_digit:
            digit.append(re.sub('[^0-9]', ',', value))
        for value in digit:
            entradas = entradas + value+','

        entradas = entradas.replace(',,', ',')
        entradas = entradas[:-1]
                # for i, (k, v) in enumerate(dic.items()):
        #     if type(dic[k]) is list and type(lista_ent_val[i]) is list:
        #         for el in lista_ent_val[i]:
        #             dic[k].append(el)
        #     else:
        #         if type(dic[k]) is str and type(lista_ent_val[i]) is str:
        #             dic[k] = lista_ent_val[i]
        
        self.txtBox.insert(INSERT, "Enviando opara o Arduino...\n\n\n")
        serialcomm.write(entradas.encode())
        for i in range(5):
            self.progress_bar['value'] += 20
            # get the value
            # update value
            self.root.update_idletasks()
            sleep(1)
        self.lb.config(text='∞ ' + serialcomm.readline().decode('ascii'), font=('Cascadia Code', 8))
        #self.txtBox.insert(INSERT, serialcomm.readline().decode('ascii'))
    
    def elementos_frame_2(self):
        ### Tex
        self.txtBox = scrolledtext.ScrolledText(self.root, undo=True, bd=4, bg='#000000', fg='#FFFFFF',
                                                highlightbackground='#04404E', highlightthickness=2)
        self.txtBox['font'] = ('consolas', '12')
        self.txtBox.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.25)
        self.lb = Label(self.root, fg="#FFFFFF", bg='#0E647B', bd=10,
                        highlightbackground='#04404E', highlightthickness=2)
        self.lb.place(relx=0.02, rely=0.77, relwidth=0.96, relheight=0.2)
        self.progress_bar = ttk.Progressbar(
            self.root, orient=HORIZONTAL, length=400, mode='determinate')
        self.progress_bar.place(relx=0.02, rely=0.93, relwidth=0.96)
App()
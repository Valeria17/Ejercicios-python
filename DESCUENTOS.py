from tkinter import *
import tkMessageBox
import math
from ttk import Combobox

Wind = Tk()

wind.wm_title("Descuento de unidades")
wind.minsize(width=300, height=200)

lblART = Label(wind, text="Cantidad de unidades").grid(row=0)
txtART = Entry(wind, width=6)
txtART.grid(row=0,column=1)

lblVA = Label(wind, text="Valor de la unidad").grid(row=1)
txtVA = Entry(wind, width=9)
txtVA.grid(row=1,column=1)

lblCRD = Label(wind,text="Tiene tarjeta de afiliacion?").grid(row=2)


cmbCRD=Combobox(wind,width=3)
cmbCRD['values'] = ('Si','No')
cmbCRD.grid(row=2, column=1)



cmbREF = Combobox(wind)
cmbREF["values"]=("Ref. Igual", "Ref.Dift")
cmbREF.grid(row=3, column=1)




def descuento():

     if re.match("^[0-9]+$",txtVA.get()):
        va = int(txtVA.get())


        art=float(txtART.get())
        va=float(txtVA.get())

        if art>=3 and \
               cmbREF.current()>=0 and \
               cmbCRD.current()>=1:
                    vf = va-(va*0.30)
        else:

                if art>=3 and \
                   cmbREF.current()>=0 and \
                   cmbCRD.current()>=0:
                        vf = va-(va*0.10)

        if art >= 3:
            vt=va*0.1

        if art>1 or art<3:
            vt=va*1

        if art >= 3 and cmbCRD.current()==0:
            vt=va*0.3

        if art >= 3 and cmbCRD.current()==1:
            vt=va*1

        if art==1 and cmbCRD.current()==0:
                vt=va*0.15

        else:
            if ard==1 and cmbCDR.current()==1:
                vt =va*0.05

        vf=va-vt

        if vf == 0:
            vf=va

        txtEND.configure(state="normal")
        txtEND.delete(0,END)
        txtEND.insert(0,str(vf))
        txtEND.configure(state="readonly")

     else:
        tkMessageBox.showerror("Error leyendo datos","El dato debe ser entero")



botCalcular = Button(wind, text="Calcular descuento",command=descuento).grid(row=4, column=0)

txtEND = Entry(wind, width=10)
txtEND.grid(row=4, column=1)
txtEND.configure(state="readonly")

wind.mainloop()
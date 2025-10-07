from tkinter import *
import matplotlib.pyplot as plt
from PIL import ImageTk,Image


def interpolacion(c, x, curva):
    if curva == 41:
        intervar = Curvas.Curva41()
        interx = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5]
    elif curva == 42:
        intervar = Curvas.Curva42()
        interx = [0.1, 0.2, 0.3, 0.4, 0.5]
    elif curva == 43:
        intervar = Curvas.Curva43()
        interx = [0.1, 0.2, 0.3, 0.4, 0.5]
    elif curva == 44:
        intervar = Curvas.Curva44()
        interx = [0.1, 0.2, 0.3, 0.4, 0.5]
    elif curva == 45:
        intervar = Curvas.Curva45()
        interx = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
    for i in range(len(interx)):
        if interx[i] <= x <= interx[i + 1]:
            x0 = interx[i]
            x1 = interx[i + 1]
            y0 = intervar.seleccionar_curva(x0, c)
            y1 = intervar.seleccionar_curva(x1, c)
            break
    y = y0 + ((y1 - y0) / (x1 - x0)) * (x - x0)
    return y


class Tabla:

    def __init__(self):
        self.colortabla = "sienna4"
        self.separaciony = 5
        self.separacionx = 5

    def mostrar_tabla(self, ventana, cadena,colorfondo,colorcontexto,unidades):
        tablasFrame = Frame(ventana)
        entradas = Label(tablasFrame,text ="Entrada de datos:",font=("Arial", 20, "bold"),bg = colorfondo,fg = "white")
        entradas.pack()
        tablasFrame.config(bg=colorfondo)
        tabla1 = Frame(tablasFrame)
        tabla1.config(bg=self.colortabla)
        self.entrylista = []
        for i in range(len(cadena)):
            self.l1 = Label(tabla1, text=cadena[i], font=("Arial", 12, "bold"), bg=self.colortabla)
            self.l1.grid(row=i, column=0, pady = self.separaciony)
            self.entrylista.append(Entry(tabla1, font=("Arial", 12, "bold")))
            self.entrylista[i].grid(row=i, column=1, pady = self.separaciony)
            self.l0 = Label(tabla1, text=unidades[i], font=("Arial", 12, "bold"), bg=self.colortabla)
            self.l0.grid(row=i, column=2, padx = self.separacionx)
        tabla1.pack(padx=40)
        self.enclis = ["Fo =", "(1)/(Kr) =", "Kr =", "SKr =", "(Fo)/(SKr) =", "No =", "(N)/(No) =", "No' =", "(N)/(No') =",
                       "(1)/(kt) =", "(Sp)/(S) =",
                       "Sp =", "PD =", "W =", "Wrf =", "(Wrf)/(SKr) =", "(F1)/(Skr) =", "(F2)/(Skr) =", "(2T)/(S^2Kr) =",
                       "(F3)/(SKr) =", "PPRL =", "MPRL =", "PT =", "PRHP =", "CBE ="]
        botcal = Button(tablasFrame, text="Calcular", bg=colorcontexto, command=self.calculos)
        botcal.pack()
        tablasFrame.pack(side = LEFT)


    def calculos(self):
        ventanares = Tk()
        label = Label(ventanares,text ="Resultados:",font=("Arial", 20, "bold"),bg = "sienna4",fg = "white")
        label.pack()
        tabla2 = Frame(ventanares)
        tabla2.config(bg=self.colortabla)
        self.entlist = []
        self.reslist = []
        for i in range(10):
            #self.l0 = Label(tabla2, text=(str(i + 1) + ".-"), font=("Arial", 12, "bold"), bg=self.colortabla)
            #self.l0.grid(row=i, column=0)
            self.l1 = Label(tabla2, text=self.enclis[i], font=("Arial", 12, "bold"), bg=self.colortabla)
            self.l1.grid(row=i, column=1)
            self.entlist.append(Entry(tabla2, font=("Arial", 12, "bold")))
            self.entlist[i].grid(row=i, column=2)
        tabla2.pack(side=LEFT,  padx = 80,pady = 80)
        tabla3 = Frame(ventanares)
        tabla3.config(bg=self.colortabla)
        for i in range(10):
            #self.l0 = Label(tabla3, text=(str(i + 5) + ".-"), font=("Arial", 12, "bold"), bg=self.colortabla)
            #self.l0.grid(row=i, column=2)
            self.l1 = Label(tabla3, text=self.enclis[i + 10], font=("Arial", 12, "bold"), bg=self.colortabla)
            self.l1.grid(row=i, column=0)
            self.entlist.append(Entry(tabla3, font=("Arial", 12, "bold")))
            self.entlist[i + 10].grid(row=i, column=1)
        tabla3.pack(side=LEFT,  padx = 80,pady = 80)
        tabla4 = Frame(ventanares)
        tabla4.config(bg=self.colortabla)
        for i in range(5):
            #self.l0 = Label(tabla3, text=(str(i + 5) + ".-"), font=("Arial", 12, "bold"), bg=self.colortabla)
            #self.l0.grid(row=i, column=2)
            self.l1 = Label(tabla4, text=self.enclis[i + 20], font=("Arial", 12, "bold"), bg=self.colortabla)
            self.l1.grid(row=i, column=0)
            self.entlist.append(Entry(tabla4, font=("Arial", 12, "bold")))
            self.entlist[i + 20].grid(row=i, column=1)
        tabla4.pack(side=LEFT, padx = 80,pady = 80)

        ventanares.config(bg = self.colortabla)
        self.reslist.clear()
        H = float(self.entrylista[0].get()) * 1.00002
        L = float(self.entrylista[1].get()) * 1.00002
        Di = float(self.entrylista[2].get()) * 1.00002
        N = float(self.entrylista[3].get()) * 1.00002
        S = float(self.entrylista[4].get()) * 1.00002
        G = float(self.entrylista[5].get()) * 1.00002
        Wr = float(self.entrylista[6].get()) * 1.00002
        Er = float(self.entrylista[7].get()) * 10**(-6)
        Fc = float(self.entrylista[8].get()) * 1.00002
        Et = float(self.entrylista[9].get()) * 10**(-6)
        Ta = 1

        '''H = 4500
        L = 5000
        Di = 1.5
        N = 16
        S = 54
        D = 1.5
        G = 0.9
        Va = 0
        Wr = 1.833
        Er = 0.804 * 10 ** -6
        Fc = 1.082
        Et = 0.307 * 10 ** -6
        Ta = 0.997'''
        self.valorround = 10

        Fo = round(0.34 * (G * Di ** 2) * H, self.valorround)
        self.reslist.append(Fo)
        _Kr = round(Er * L, self.valorround)
        self.reslist.append(_Kr)
        Kr = round(1 / _Kr, self.valorround)
        self.reslist.append(Kr)
        SKr = round(S / (_Kr), self.valorround)
        self.reslist.append(SKr)
        Fo_SKr = round(Fo / SKr, self.valorround)
        self.reslist.append(Fo_SKr)
        No = round(245000 / L, self.valorround)
        self.reslist.append(No)
        N_No = round(N / No, self.valorround)
        self.reslist.append(N_No)
        Nop = round(Fc * No, self.valorround)
        self.reslist.append(Nop)
        N_Nop = round(N / Nop, self.valorround)
        self.reslist.append(N_Nop)
        _Kt = round(Et * L, self.valorround)
        self.reslist.append(_Kt)
        Sp_S = round(interpolacion(N_Nop, Fo_SKr, 41), self.valorround)
        self.reslist.append(Sp_S)
        Sp = round((Sp_S * S) - (Fo * _Kt), self.valorround)
        self.reslist.append(Sp)
        PD = round(0.1166 * Sp * N * (Di ** 2), self.valorround)
        self.reslist.append(PD)
        W = round(Wr * L, self.valorround)
        self.reslist.append(W)
        Wrf = round(W * (1 - 0.128 * G), self.valorround)
        self.reslist.append(Wrf)
        Wrf_SKr = round(Wrf / SKr, self.valorround)
        self.reslist.append(Wrf_SKr)
        F1_SKr = round(interpolacion(N_No,Fo_SKr,42),self.valorround)
        self.reslist.append(F1_SKr)
        F2_SKr = round(interpolacion(N_No,Fo_SKr,43),self.valorround)
        self.reslist.append(F2_SKr)
        T2_S2Kr = round(interpolacion(N_No,Fo_SKr,44),self.valorround)
        self.reslist.append(T2_S2Kr)
        F3_SSKr = round(interpolacion(N_No,Fo_SKr,45),self.valorround)
        self.reslist.append(F3_SSKr)
        PPRL =round(Wrf + (F1_SKr)*SKr,self.valorround)
        self.reslist.append(PPRL)
        MPRL = round(Wrf -(F2_SKr) * SKr, self.valorround)
        self.reslist.append(MPRL)
        PT = round(T2_S2Kr*SKr*(S/2)*Ta, self.valorround)
        self.reslist.append(PT)
        PRHP = round(F3_SSKr*SKr*S*N*2.53*10**(-6), self.valorround)
        self.reslist.append(PRHP)
        CBE = round(1.06*(Wrf+(1/2)*(Fo)), self.valorround)
        self.reslist.append(CBE)

        for i in range(len(self.reslist)):
            self.entlist[i].delete(0, END)
            self.entlist[i].insert(0, self.reslist[i])
        ventanares.mainloop()


class Curvas:
    class Curva41:

        def seleccionar_curva(self, curva, x):
            if curva == 0.05:
                if 0 <= x < 0.275:
                    y = 7.3081*x**3 - 0.1101*x**2 - 0.0002*x + 0.9503
                elif 0.275 <= x < 0.4:
                    y = -6826.7 * x ** 5 + 8533.3 * x ** 4 - 3594.7 * x ** 3 + 464.27 * x ** 2 + 45.589 * x - 9.866
                elif 0.4 <= x <= 0.6:
                    y = -14 * x ** 3 + 19.1 * x ** 2 - 5.87 * x + 1.33
                else:
                    y = 1
            elif curva == 0.1:
                if 0 <= x < 0.275:
                    y = -1896.6*x**5 + 1287.2*x**4 - 289.49*x**3 + 25.904*x**2 - 0.5571*x + 0.9003
                elif 0.275 <= x < 0.35:
                    y = 277.33 * x ** 3 - 260 * x ** 2 + 80.087 * x - 7.066
                elif 0.35 <= x < 0.6:
                    y = 53.333 * x ** 4 - 124 * x ** 3 + 104.47 * x ** 2 - 35.36 * x + 5.1
                else:
                    y = 1
            elif curva == 0.2:
                if 0 <= x < 0.05:
                    y = 0.1 * x + 0.805
                elif 0.05 <= x < 0.1:
                    y = 0.3 * x + 0.795
                elif 0.1 <= x < 0.15:
                    y = 0.5 * x + 0.775
                elif 0.15 <= x < 0.2:
                    y = 0.6 * x + 0.76
                elif 0.2 <= x < 0.25:
                    y = 1 * x + 0.68
                elif 0.25 <= x < 0.275:
                    y = -0.52 * x + 1.06
                elif 0.275 <= x < 0.3:
                    y = -1.08 * x + 1.214
                elif 0.3 <= x < 0.325:
                    y = -0.08 * x + 0.914
                elif 0.325 <= x < 0.35:
                    y = 1.48 * x + 0.407
                elif 0.35 <= x < 0.4:
                    y = 2.1 * x + 0.19
                elif 0.4 <= x <= 0.6:
                    y = 2.45 * x + 0.05
                else:
                    y = 1
            elif curva == 0.3:
                if 0 <= x < 0.05:
                    y = 0.2 * x + 0.7
                elif 0.05 <= x < 0.1:
                    y = 0.3 * x + 0.695
                elif 0.1 <= x < 0.15:
                    y = 0.5 * x + 0.675
                elif 0.15 <= x < 0.2:
                    y = 1 * x + 0.6
                elif 0.2 <= x < 0.225:
                    y = 0.8 * x + 0.64
                elif 0.225 <= x < 0.25:
                    y = -0.8 * x + 1
                elif 0.25 <= x < 0.275:
                    y = -1.2 * x + 1.1
                elif 0.275 <= x < 0.3:
                    y = 0.4 * x + 0.66
                elif 0.3 <= x < 0.35:
                    y = 2 * x + 0.18
                elif 0.35 <= x < 0.4:
                    y = 2 * x + 0.18
                elif 0.4 <= x <= 0.6:
                    y = 2.25 * x + 0.08
                else:
                    y = 1
            elif curva == 0.4:
                if 0 <= x < 0.05:
                    y = 0.3 * x + 0.6
                elif 0.05 <= x < 0.1:
                    y = 0.3 * x + 0.6
                elif 0.1 <= x < 0.15:
                    y = 0.5 * x + 0.58
                elif 0.15 <= x < 0.2:
                    y = 0.8 * x + 0.535
                elif 0.2 <= x < 0.25:
                    y = -0.4 * x + 0.775
                elif 0.25 <= x < 0.275:
                    y = 0.6 * x + 0.525
                elif 0.275 <= x < 0.3:
                    y = 1.2 * x + 0.36
                elif 0.3 <= x < 0.35:
                    y = 1.9 * x + 0.15
                elif 0.35 <= x < 0.4:
                    y = 2 * x + 0.115
                elif 0.4 <= x < 0.5:
                    y = 2.05 * x + 0.095
                elif 0.5 <= x <= 0.6:
                    y = 2.35 * x - 0.055
                else:
                    y = 1
            elif curva == 0.5:
                if 0 <= x < 0.05:
                    y = 0.2 * x + 0.5
                elif 0.05 <= x < 0.1:
                    y = 0.4 * x + 0.49
                elif 0.1 <= x < 0.15:
                    y = 0.6 * x + 0.47
                elif 0.15 <= x < 0.2:
                    y = 0.54 * x + 0.479
                elif 0.2 <= x < 0.225:
                    y = -0.68 * x + 0.723
                elif 0.225 <= x < 0.25:
                    y = 0.4 * x + 0.48
                elif 0.25 <= x < 0.325:
                    y = 1.73 * x + 0.148
                elif 0.325 <= x < 0.55:
                    y = 1.91 * x + 0.089
                elif 0.55 <= x < 0.6:
                    y = 2.2 * x - 0.07

            return y

        def sacar_matriz(self, curva):
            self.listax = []
            self.listay = []
            i = 0
            self.temp = Curvas.Curva41()
            while i <= 0.6:
                self.listax.append(i)
                self.listay.append(self.temp.seleccionar_curva(curva, i))
                i = i + 0.001

    class Curva42:

        def seleccionar_curva(self, curva, x):
            if curva == 0.1:
                if 0 <= x < 0.05:
                    y = 0.36 * x + 0.1
                elif 0.05 <= x < 0.1:
                    y = 0.58 * x + 0.089
                elif 0.1 <= x < 0.15:
                    y = 0.68 * x + 0.079
                elif 0.15 <= x < 0.2:
                    y = 0.78 * x + 0.064
                elif 0.2 <= x < 0.25:
                    y = 0.82 * x + 0.056
                elif 0.25 <= x < 0.3:
                    y = 0.88 * x + 0.041
                elif 0.3 <= x < 0.35:
                    y = 1.04 * x - 0.007
                elif 0.35 <= x < 0.4:
                    y = 1.1 * x - 0.028
                elif 0.4 <= x < 0.45:
                    y = 1.66 * x - 0.252
                elif 0.45 <= x < 0.5:
                    y = 2.46 * x - 0.612
                elif 0.5 <= x <= 0.55:
                    y = 2.84 * x - 0.802
                else:
                    y = 1

            elif curva == 0.2:
                if 0 <= x < 0.05:
                    y = 0.5 * x + 0.2
                elif 0.05 <= x < 0.1:
                    y = 0.6 * x + 0.195
                elif 0.1 <= x < 0.15:
                    y = 0.74 * x + 0.181
                elif 0.15 <= x < 0.2:
                    y = 0.74 * x + 0.181
                elif 0.2 <= x < 0.25:
                    y = 0.78 * x + 0.173
                elif 0.25 <= x < 0.3:
                    y = 0.84 * x + 0.158
                elif 0.3 <= x < 0.35:
                    y = 0.9 * x + 0.14
                elif 0.35 <= x < 0.4:
                    y = 1 * x + 0.105
                elif 0.4 <= x < 0.45:
                    y = 1.38 * x - 0.047
                elif 0.45 <= x < 0.5:
                    y = 2.2 * x - 0.416
                elif 0.5 <= x <= 0.55:
                    y = 3.08 * x - 0.856
                else:
                    y = 1

            elif curva == 0.3:
                if 0 <= x < 0.05:
                    y = 0.54 * x + 0.3
                elif 0.05 <= x < 0.1:
                    y = 0.6 * x + 0.297
                elif 0.1 <= x < 0.15:
                    y = 0.62 * x + 0.295
                elif 0.15 <= x < 0.2:
                    y = 0.7 * x + 0.283
                elif 0.2 <= x < 0.25:
                    y = 0.7 * x + 0.283
                elif 0.25 <= x < 0.3:
                    y = 0.88 * x + 0.238
                elif 0.3 <= x < 0.35:
                    y = 0.96 * x + 0.214
                elif 0.35 <= x < 0.4:
                    y = 1.12 * x + 0.158
                elif 0.4 <= x < 0.45:
                    y = 1.48 * x + 0.014
                elif 0.45 <= x < 0.5:
                    y = 1.9 * x - 0.175
                elif 0.5 <= x <= 0.55:
                    y = 3.04 * x - 0.745
                else:
                    y = 1

            elif curva == 0.4:
                if 0 <= x < 0.05:
                    y = 0.5 * x + 0.4
                elif 0.05 <= x < 0.1:
                    y = 0.58 * x + 0.396
                elif 0.1 <= x < 0.15:
                    y = 0.62 * x + 0.392
                elif 0.15 <= x < 0.2:
                    y = 0.64 * x + 0.389
                elif 0.2 <= x < 0.25:
                    y = 0.66 * x + 0.385
                elif 0.25 <= x < 0.3:
                    y = 0.7 * x + 0.375
                elif 0.3 <= x < 0.35:
                    y = 1.02 * x + 0.279
                elif 0.35 <= x < 0.375:
                    y = 1.36 * x + 0.16
                elif 0.375 <= x < 0.4:
                    y = 1 * x + 0.295
                elif 0.4 <= x < 0.425:
                    y = 1.2 * x + 0.215
                elif 0.425 <= x < 0.45:
                    y = 1 * x + 0.3
                elif 0.45 <= x < 0.5:
                    y = 1.7 * x - 0.015
                elif 0.5 <= x <= 0.55:
                    y = 2.7 * x - 0.515
                else:
                    y = 1

            elif curva == 0.5:
                if 0 <= x < 0.05:
                    y = 0.68 * x + 0.5
                elif 0.05 <= x < 0.1:
                    y = 0.62 * x + 0.503
                elif 0.1 <= x < 0.15:
                    y = 0.54 * x + 0.511
                elif 0.15 <= x < 0.2:
                    y = 0.62 * x + 0.499
                elif 0.2 <= x < 0.25:
                    y = 0.6 * x + 0.503
                elif 0.25 <= x < 0.3:
                    y = 0.62 * x + 0.498
                elif 0.3 <= x < 0.325:
                    y = 0.28 * x + 0.6
                elif 0.325 <= x < 0.35:
                    y = 0.36 * x + 0.574
                elif 0.35 <= x < 0.375:
                    y = 1.92 * x + 0.028
                elif 0.375 <= x < 0.385:
                    y = 2.2 * x - 0.077
                elif 0.385 <= x < 0.4:
                    y = 1.33 * x + 0.258
                elif 0.4 <= x < 0.425:
                    y = 0.72 * x + 0.502
                elif 0.425 <= x < 0.45:
                    y = 0.96 * x + 0.4
                elif 0.45 <= x < 0.5:
                    y = 1.4 * x + 0.202
                elif 0.5 <= x <= 0.55:
                    y = 2.12 * x - 0.158
                else:
                    y = 1
            else:
                y = 1000
            return y

        def sacar_matriz(self, curva):
            self.listax = []
            self.listay = []
            i = 0
            self.temp = Curvas.Curva42()
            while i <= 0.55:
                self.listax.append(i)
                self.listay.append(self.temp.seleccionar_curva(curva, i))
                i = i + 0.001

    class Curva43:

        def seleccionar_curva(self, curva, x):
            if curva == 0.1:
                if 0 <= x < 0.05:
                    y = 0.22 * x + 0
                elif 0.05 <= x < 0.1:
                    y = 0.36 * x - 0.007
                elif 0.1 <= x < 0.15:
                    y = 0.52 * x - 0.023
                elif 0.15 <= x < 0.2:
                    y = 0.68 * x - 0.047
                elif 0.2 <= x < 0.25:
                    y = 0.76 * x - 0.063
                elif 0.25 <= x < 0.3:
                    y = 0.96 * x - 0.113
                elif 0.3 <= x < 0.325:
                    y = 1.16 * x - 0.173
                elif 0.325 <= x < 0.35:
                    y = 1.04 * x - 0.134
                elif 0.35 <= x < 0.4:
                    y = 0.86 * x - 0.071
                elif 0.4 <= x < 0.45:
                    y = 0.58 * x + 0.041
                elif 0.45 <= x < 0.475:
                    y = 0.8 * x - 0.058
                elif 0.475 <= x < 0.5:
                    y = 1 * x - 0.153
                elif 0.5 <= x < 0.525:
                    y = 1.4 * x - 0.353
                elif 0.525 <= x < 0.55:
                    y = 2 * x - 0.668
                else:
                    y = 1
            elif curva == 0.2:
                if 0 <= x < 0.05:
                    y = 0.3 * x + 0
                elif 0.05 <= x < 0.1:
                    y = 0.46 * x - 0.008
                elif 0.1 <= x < 0.15:
                    y = 0.64 * x - 0.026
                elif 0.15 <= x < 0.2:
                    y = 0.86 * x - 0.059
                elif 0.2 <= x < 0.225:
                    y = 0.96 * x - 0.079
                elif 0.225 <= x < 0.25:
                    y = 0.72 * x - 0.025
                elif 0.25 <= x < 0.3:
                    y = 0.72 * x - 0.025
                elif 0.3 <= x < 0.35:
                    y = 0.74 * x - 0.031
                elif 0.35 <= x < 0.4:
                    y = 0.8 * x - 0.052
                elif 0.4 <= x < 0.45:
                    y = 0.94 * x - 0.108
                elif 0.45 <= x < 0.5:
                    y = 1.02 * x - 0.144
                elif 0.5 <= x < 0.525:
                    y = 1.28 * x - 0.274
                elif 0.525 <= x < 0.55:
                    y = 1.84 * x - 0.568
                else:
                    y = 1
            elif curva == 0.3:
                if 0 <= x < 0.05:
                    y = 0.38 * x + 0
                elif 0.05 <= x < 0.1:
                    y = 0.52 * x - 0.007
                elif 0.1 <= x < 0.15:
                    y = 0.7 * x - 0.025
                elif 0.15 <= x < 0.2:
                    y = 0.92 * x - 0.058
                elif 0.2 <= x < 0.225:
                    y = 0.84 * x - 0.042
                elif 0.225 <= x < 0.25:
                    y = 0.76 * x - 0.024
                elif 0.25 <= x < 0.3:
                    y = 0.72 * x - 0.014
                elif 0.3 <= x < 0.35:
                    y = 0.8 * x - 0.038
                elif 0.35 <= x < 0.4:
                    y = 0.68 * x + 0.004
                elif 0.4 <= x < 0.425:
                    y = 0.52 * x + 0.068
                elif 0.425 <= x < 0.45:
                    y = 0.68 * x + 0
                elif 0.45 <= x < 0.475:
                    y = 1 * x - 0.144
                elif 0.475 <= x < 0.5:
                    y = 1.36 * x - 0.315
                elif 0.5 <= x < 0.525:
                    y = 1.36 * x - 0.315
                elif 0.525 <= x < 0.55:
                    y = 1.32 * x - 0.294
                else:
                    y = 1

            elif curva == 0.4:
                if 0 <= x < 0.05:
                    y = 0.32 * x + 0
                elif 0.05 <= x < 0.075:
                    y = 0.4 * x - 0.004
                elif 0.075 <= x < 0.1:
                    y = 0.52 * x - 0.013
                elif 0.1 <= x < 0.125:
                    y = 0.64 * x - 0.025
                elif 0.125 <= x < 0.15:
                    y = 0.76 * x - 0.04
                elif 0.15 <= x < 0.175:
                    y = 0.88 * x - 0.058
                elif 0.175 <= x < 0.2:
                    y = 0.96 * x - 0.072
                elif 0.2 <= x < 0.225:
                    y = 0.92 * x - 0.064
                elif 0.225 <= x < 0.25:
                    y = 0.76 * x - 0.028
                elif 0.25 <= x < 0.3:
                    y = 0.76 * x - 0.028
                elif 0.3 <= x < 0.325:
                    y = 0.72 * x - 0.016
                elif 0.325 <= x < 0.35:
                    y = 0.72 * x - 0.016
                elif 0.35 <= x < 0.375:
                    y = 0.68 * x - 0.002
                elif 0.375 <= x < 0.4:
                    y = 0.6 * x + 0.028
                elif 0.4 <= x < 0.425:
                    y = 0.84 * x - 0.068
                elif 0.425 <= x < 0.45:
                    y = 0.8 * x - 0.051
                elif 0.45 <= x < 0.475:
                    y = 0.76 * x - 0.033
                elif 0.475 <= x < 0.5:
                    y = 0.88 * x - 0.09
                elif 0.5 <= x < 0.525:
                    y = 0.92 * x - 0.11
                elif 0.525 <= x < 0.55:
                    y = 1.52 * x - 0.425
                else:
                    y = 1
            elif curva == 0.5:
                if 0 <= x < 0.025:
                    y = 0.48 * x + 0
                elif 0.025 <= x < 0.05:
                    y = 0.44 * x + 0.001
                elif 0.05 <= x < 0.075:
                    y = 0.52 * x - 0.003
                elif 0.075 <= x < 0.1:
                    y = 0.56 * x - 0.006
                elif 0.1 <= x < 0.125:
                    y = 0.64 * x - 0.014
                elif 0.125 <= x < 0.15:
                    y = 0.68 * x - 0.019
                elif 0.15 <= x < 0.175:
                    y = 0.76 * x - 0.031
                elif 0.175 <= x < 0.2:
                    y = 0.76 * x - 0.031
                elif 0.2 <= x < 0.225:
                    y = 0.76 * x - 0.031
                elif 0.225 <= x < 0.25:
                    y = 0.72 * x - 0.022
                elif 0.25 <= x < 0.275:
                    y = 0.76 * x - 0.032
                elif 0.275 <= x < 0.3:
                    y = 0.76 * x - 0.032
                elif 0.3 <= x < 0.325:
                    y = 0.88 * x - 0.068
                elif 0.325 <= x < 0.35:
                    y = 0.72 * x - 0.016
                elif 0.35 <= x < 0.375:
                    y = 0.64 * x + 0.012
                elif 0.375 <= x < 0.385:
                    y = 0.7 * x - 0.011
                elif 0.385 <= x < 0.4:
                    y = 0.4 * x + 0.105
                elif 0.4 <= x < 0.425:
                    y = 0.36 * x + 0.121
                elif 0.425 <= x < 0.45:
                    y = 0.6 * x + 0.019
                elif 0.45 <= x < 0.475:
                    y = 0.88 * x - 0.107
                elif 0.475 <= x < 0.5:
                    y = 1.12 * x - 0.221
                elif 0.5 <= x < 0.525:
                    y = 1.04 * x - 0.181
                elif 0.525 <= x < 0.55:
                    y = 0.8 * x - 0.055
                else:
                    y = 1
            else:
                y = 1000
            return y

        def sacar_matriz(self, curva):
            self.listax = []
            self.listay = []
            i = 0
            self.temp = Curvas.Curva43()
            while i <= 0.55:
                self.listax.append(i)
                self.listay.append(self.temp.seleccionar_curva(curva, i))
                i = i + 0.001

    class Curva44:

        def seleccionar_curva(self, curva, x):
            if curva == 0.1:
                if 0 <= x < 0.05:
                    y = 0.2 * x + 0.09
                elif 0.05 <= x < 0.1:
                    y = 0.28 * x + 0.086
                elif 0.1 <= x < 0.15:
                    y = 0.52 * x + 0.062
                elif 0.15 <= x < 0.2:
                    y = 0.7 * x + 0.035
                elif 0.2 <= x < 0.25:
                    y = 0.9 * x - 0.005
                elif 0.25 <= x < 0.3:
                    y = 0.86 * x + 0.005
                elif 0.3 <= x < 0.35:
                    y = 0.84 * x + 0.011
                elif 0.35 <= x < 0.4:
                    y = 0.9 * x - 0.01
                elif 0.4 <= x < 0.45:
                    y = 0.96 * x - 0.034
                elif 0.45 <= x < 0.5:
                    y = 0.98 * x - 0.043
                elif 0.5 <= x < 0.55:
                    y = 0.98 * x - 0.043
                elif 0.55 <= x <= 0.6:
                    y = 1.04 * x - 0.076
            elif curva == 0.2:
                if 0 <= x < 0.05:
                    y = 0.42 * x + 0.139
                elif 0.05 <= x < 0.1:
                    y = 0.54 * x + 0.133
                elif 0.1 <= x < 0.15:
                    y = 0.66 * x + 0.121
                elif 0.15 <= x < 0.2:
                    y = 0.76 * x + 0.106
                elif 0.2 <= x < 0.25:
                    y = 0.8 * x + 0.098
                elif 0.25 <= x < 0.3:
                    y = 0.8 * x + 0.098
                elif 0.3 <= x < 0.35:
                    y = 0.84 * x + 0.086
                elif 0.35 <= x < 0.4:
                    y = 0.84 * x + 0.086
                elif 0.4 <= x < 0.45:
                    y = 0.82 * x + 0.094
                elif 0.45 <= x < 0.5:
                    y = 0.84 * x + 0.085
                elif 0.5 <= x < 0.55:
                    y = 0.9 * x + 0.055
                elif 0.55 <= x <= 0.6:
                    y = 0.9 * x + 0.055
            elif curva == 0.3:
                if 0 <= x < 0.05:
                    y = 0.5 * x + 0.189
                elif 0.05 <= x < 0.1:
                    y = 0.52 * x + 0.188
                elif 0.1 <= x < 0.15:
                    y = 0.6 * x + 0.18
                elif 0.15 <= x < 0.2:
                    y = 0.6 * x + 0.18
                elif 0.2 <= x < 0.25:
                    y = 0.66 * x + 0.168
                elif 0.25 <= x < 0.3:
                    y = 0.74 * x + 0.148
                elif 0.3 <= x < 0.35:
                    y = 0.78 * x + 0.136
                elif 0.35 <= x < 0.4:
                    y = 0.8 * x + 0.129
                elif 0.4 <= x < 0.45:
                    y = 0.8 * x + 0.129
                elif 0.45 <= x < 0.5:
                    y = 0.84 * x + 0.111
                elif 0.5 <= x < 0.55:
                    y = 0.98 * x + 0.041
                elif 0.55 <= x <= 0.6:
                    y = 1.1 * x - 0.025
            elif curva == 0.4:
                if 0 <= x < 0.05:
                    y = 0.66 * x + 0.22
                elif 0.05 <= x < 0.1:
                    y = 0.6 * x + 0.223
                elif 0.1 <= x < 0.15:
                    y = 0.54 * x + 0.229
                elif 0.15 <= x < 0.2:
                    y = 0.46 * x + 0.241
                elif 0.2 <= x < 0.25:
                    y = 0.38 * x + 0.257
                elif 0.25 <= x < 0.3:
                    y = 0.4 * x + 0.252
                elif 0.3 <= x < 0.35:
                    y = 0.82 * x + 0.126
                elif 0.35 <= x < 0.4:
                    y = 1.14 * x + 0.014
                elif 0.4 <= x < 0.45:
                    y = 0.72 * x + 0.182
                elif 0.45 <= x < 0.5:
                    y = 0.94 * x + 0.083
                elif 0.5 <= x < 0.55:
                    y = 1.3 * x - 0.097
                elif 0.55 <= x <= 0.6:
                    y = 1.12 * x + 0.002
            elif curva == 0.5:
                if 0 <= x < 0.05:
                    y = 0.56 * x + 0.248
                elif 0.05 <= x < 0.1:
                    y = 0.48 * x + 0.252
                elif 0.1 <= x < 0.15:
                    y = 0.42 * x + 0.258
                elif 0.15 <= x < 0.2:
                    y = 0.38 * x + 0.264
                elif 0.2 <= x < 0.25:
                    y = 0.32 * x + 0.276
                elif 0.25 <= x < 0.275:
                    y = 0.32 * x + 0.276
                elif 0.275 <= x < 0.3:
                    y = 0.52 * x + 0.221
                elif 0.3 <= x < 0.35:
                    y = 0.86 * x + 0.119
                elif 0.35 <= x < 0.365:
                    y = 2.33 * x - 0.396
                elif 0.365 <= x < 0.385:
                    y = 1.4 * x - 0.056
                elif 0.385 <= x < 0.4:
                    y = 0.87 * x + 0.148
                elif 0.4 <= x < 0.4125:
                    y = 0.88 * x + 0.144
                elif 0.4125 <= x < 0.425:
                    y = 0.4 * x + 0.342
                elif 0.425 <= x < 0.45:
                    y = 0.24 * x + 0.41
                elif 0.45 <= x < 0.475:
                    y = 0.52 * x + 0.284
                elif 0.475 <= x < 0.5:
                    y = 1.16 * x - 0.02
                elif 0.5 <= x < 0.55:
                    y = 1.3 * x - 0.09
                elif 0.55 <= x <= 0.6:
                    y = 1.18 * x - 0.024
            else:
                y = 1000
            return y

        def sacar_matriz(self, curva):
            self.listax = []
            self.listay = []
            i = 0
            self.temp = Curvas.Curva44()
            while i <= 0.6:
                self.listax.append(i)
                self.listay.append(self.temp.seleccionar_curva(curva, i))
                i = i + 0.001

    class Curva45:

        def seleccionar_curva(self, curva, x):
            if curva == 0.1:
                if 0 <= x < 0.05:
                    y = 0.16 * x + 0.09
                elif 0.05 <= x < 0.1:
                    y = 0.24 * x + 0.086
                elif 0.1 <= x < 0.15:
                    y = 0.34 * x + 0.076
                elif 0.15 <= x < 0.2:
                    y = 0.36 * x + 0.073
                elif 0.2 <= x < 0.25:
                    y = 0.42 * x + 0.061
                elif 0.25 <= x < 0.3:
                    y = 0.48 * x + 0.046
                elif 0.3 <= x < 0.325:
                    y = 0.52 * x + 0.034
                elif 0.325 <= x < 0.35:
                    y = 0.6 * x + 0.008
                elif 0.35 <= x < 0.4:
                    y = 0.68 * x - 0.02
                elif 0.4 <= x < 0.45:
                    y = 0.9 * x - 0.108
                elif 0.45 <= x < 0.475:
                    y = 1 * x - 0.153
                elif 0.475 <= x < 0.5:
                    y = 1 * x - 0.153
                elif 0.5 <= x < 0.525:
                    y = 1.16 * x - 0.233
                elif 0.525 <= x < 0.55:
                    y = 1.24 * x - 0.275
                else:
                    y = 1
            elif curva == 0.2:
                if 0 <= x < 0.05:
                    y = 0.18 * x + 0.159
                elif 0.05 <= x < 0.1:
                    y = 0.22 * x + 0.157
                elif 0.1 <= x < 0.15:
                    y = 0.3 * x + 0.149
                elif 0.15 <= x < 0.2:
                    y = 0.36 * x + 0.14
                elif 0.2 <= x < 0.225:
                    y = 0.44 * x + 0.124
                elif 0.225 <= x < 0.25:
                    y = 0.4 * x + 0.133
                elif 0.25 <= x < 0.3:
                    y = 0.54 * x + 0.098
                elif 0.3 <= x < 0.35:
                    y = 0.62 * x + 0.074
                elif 0.35 <= x < 0.4:
                    y = 0.84 * x - 0.003
                elif 0.4 <= x < 0.45:
                    y = 1 * x - 0.067
                elif 0.45 <= x < 0.5:
                    y = 1.22 * x - 0.166
                elif 0.5 <= x < 0.525:
                    y = 1.36 * x - 0.236
                elif 0.525 <= x < 0.55:
                    y = 1.44 * x - 0.278
                else:
                    y = 1
            elif curva == 0.3:
                if 0 <= x < 0.05:
                    y = 0.22 * x + 0.21
                elif 0.05 <= x < 0.1:
                    y = 0.22 * x + 0.21
                elif 0.1 <= x < 0.15:
                    y = 0.24 * x + 0.208
                elif 0.15 <= x < 0.2:
                    y = 0.32 * x + 0.196
                elif 0.2 <= x < 0.225:
                    y = 0.32 * x + 0.196
                elif 0.225 <= x < 0.25:
                    y = 0.48 * x + 0.16
                elif 0.25 <= x < 0.3:
                    y = 0.46 * x + 0.165
                elif 0.3 <= x < 0.35:
                    y = 0.78 * x + 0.069
                elif 0.35 <= x < 0.4:
                    y = 1.16 * x - 0.064
                elif 0.4 <= x < 0.425:
                    y = 1.32 * x - 0.128
                elif 0.425 <= x < 0.45:
                    y = 1.48 * x - 0.196
                elif 0.45 <= x < 0.475:
                    y = 1.52 * x - 0.214
                elif 0.475 <= x < 0.5:
                    y = 1.56 * x - 0.233
                elif 0.5 <= x < 0.525:
                    y = 1.6 * x - 0.253
                elif 0.525 <= x < 0.55:
                    y = 1.6 * x - 0.253
                else:
                    y = 1
            elif curva == 0.4:
                if 0 <= x < 0.05:
                    y = 0.18 * x + 0.24
                elif 0.05 <= x < 0.075:
                    y = 0.2 * x + 0.239
                elif 0.075 <= x < 0.1:
                    y = 0.24 * x + 0.236
                elif 0.1 <= x < 0.125:
                    y = 0.24 * x + 0.236
                elif 0.125 <= x < 0.15:
                    y = 0.24 * x + 0.236
                elif 0.15 <= x < 0.175:
                    y = 0.36 * x + 0.218
                elif 0.175 <= x < 0.2:
                    y = 0.28 * x + 0.232
                elif 0.2 <= x < 0.225:
                    y = 0.4 * x + 0.208
                elif 0.225 <= x < 0.25:
                    y = 0.48 * x + 0.19
                elif 0.25 <= x < 0.275:
                    y = 0.52 * x + 0.18
                elif 0.275 <= x < 0.3:
                    y = 0.72 * x + 0.125
                elif 0.3 <= x < 0.325:
                    y = 1.04 * x + 0.029
                elif 0.325 <= x < 0.35:
                    y = 1.2 * x - 0.023
                elif 0.35 <= x < 0.375:
                    y = 1.36 * x - 0.079
                elif 0.375 <= x < 0.4:
                    y = 1.44 * x - 0.109
                elif 0.4 <= x < 0.425:
                    y = 1.48 * x - 0.125
                elif 0.425 <= x < 0.45:
                    y = 1.56 * x - 0.159
                elif 0.45 <= x < 0.475:
                    y = 1.6 * x - 0.177
                elif 0.475 <= x < 0.5:
                    y = 1.64 * x - 0.196
                elif 0.5 <= x < 0.525:
                    y = 1.64 * x - 0.196
                elif 0.525 <= x < 0.55:
                    y = 1.68 * x - 0.217
                else:
                    y = 1
            elif curva == 0.5:
                if 0 <= x < 0.025:
                    y = 0.16 * x + 0.25
                elif 0.025 <= x < 0.05:
                    y = 0.24 * x + 0.248
                elif 0.05 <= x < 0.075:
                    y = 0.16 * x + 0.252
                elif 0.075 <= x < 0.1:
                    y = 0.28 * x + 0.243
                elif 0.1 <= x < 0.125:
                    y = 0.24 * x + 0.247
                elif 0.125 <= x < 0.15:
                    y = 0.28 * x + 0.242
                elif 0.15 <= x < 0.175:
                    y = 0.28 * x + 0.242
                elif 0.175 <= x < 0.2:
                    y = 0.36 * x + 0.228
                elif 0.2 <= x < 0.225:
                    y = 0.44 * x + 0.212
                elif 0.225 <= x < 0.25:
                    y = 0.52 * x + 0.194
                elif 0.25 <= x < 0.275:
                    y = 0.64 * x + 0.164
                elif 0.275 <= x < 0.3:
                    y = 0.88 * x + 0.098
                elif 0.3 <= x < 0.325:
                    y = 1.2 * x + 0.002
                elif 0.325 <= x < 0.35:
                    y = 1.4 * x - 0.063
                elif 0.35 <= x < 0.375:
                    y = 1.56 * x - 0.119
                elif 0.375 <= x < 0.385:
                    y = 1.6 * x - 0.134
                elif 0.385 <= x < 0.4:
                    y = 1.6 * x - 0.134
                elif 0.4 <= x < 0.425:
                    y = 1.64 * x - 0.15
                elif 0.425 <= x < 0.45:
                    y = 1.6 * x - 0.133
                elif 0.45 <= x < 0.475:
                    y = 1.56 * x - 0.115
                elif 0.475 <= x < 0.5:
                    y = 1.48 * x - 0.077
                elif 0.5 <= x < 0.525:
                    y = 1.56 * x - 0.117
                elif 0.525 <= x < 0.55:
                    y = 1.52 * x - 0.096
                else:
                    y = 1
            elif curva == 0.6:
                if 0 <= x < 0.05:
                    y = 0.18 * x + 0.24
                elif 0.05 <= x < 0.075:
                    y = 0.2 * x + 0.239
                elif 0.075 <= x < 0.1:
                    y = 0.24 * x + 0.236
                elif 0.1 <= x < 0.125:
                    y = 0.24 * x + 0.236
                elif 0.125 <= x < 0.15:
                    y = 0.24 * x + 0.236
                elif 0.15 <= x < 0.175:
                    y = 0.36 * x + 0.218
                elif 0.175 <= x < 0.2:
                    y = 0.28 * x + 0.232
                elif 0.2 <= x < 0.225:
                    y = 0.68 * x + 0.152
                elif 0.225 <= x < 0.25:
                    y = 0.76 * x + 0.134
                elif 0.25 <= x < 0.3:
                    y = 1.12 * x + 0.044
                elif 0.3 <= x < 0.35:
                    y = 1.4 * x - 0.04
                elif 0.35 <= x < 0.4:
                    y = 1.5 * x - 0.075
                elif 0.4 <= x < 0.5:
                    y = 1.65 * x - 0.135
                elif 0.5 <= x < 0.55:
                    y = 1.64 * x - 0.13
                else:
                    y = 1
            else:
                y = 1000
            return y

        def sacar_matriz(self, curva):
            self.listax = []
            self.listay = []
            i = 0
            self.temp = Curvas.Curva45()
            while i <= 0.55:
                self.listax.append(i)
                self.listay.append(self.temp.seleccionar_curva(curva, i))
                i = i + 0.001


class Ventana:

    def __init__(self):
        self.colorfondo = "sienna4"
        self.colorcontexto = "yellow"
        self.ventana = Tk()
        self.ventana.state("zoomed")
        self.encabezado = Frame(self.ventana)
        self.encabezado.config(bg=self.colorfondo,highlightbackground="black", highlightthickness=2)
        self.ipn = Image.open("ipn.png")
        self.ipn = self.ipn.resize((75,124),Image.ANTIALIAS)
        self.myipn = ImageTk.PhotoImage(self.ipn)
        self.ipnlab = Label(self.encabezado, image=self.myipn)
        self.ipnlab.config(bg=self.colorfondo)
        self.ipnlab.pack(side=LEFT, anchor="n")
        self.esia = Image.open("esia.png")
        self.esia = self.esia.resize((75,124),Image.ANTIALIAS)
        self.myesia = ImageTk.PhotoImage(self.esia)
        self.esialab = Label(self.encabezado, image=self.myesia)
        self.esialab.config(bg=self.colorfondo)
        self.esialab.pack(side=RIGHT, anchor="n")
        self.ventana.config(bg=self.colorfondo)
        self.materia = Label(self.encabezado,text="SAP", fg="white", font=("srial", 24, "bold"),
                             bg=self.colorfondo)
        self.nombres = ["Martínez Arce Kevin Adair", "Ojeda Moreno Carlos Daniel", "Lorenzo Muñoz Sergio"]
        #self.materia.pack(side=TOP)
        for i in range(len(self.nombres)):
            self.nombrelab = Label(self.encabezado,text=self.nombres[i], fg="white", font=("srial", 16, "bold"), bg=self.colorfondo)
            self.nombrelab.pack(side=TOP,pady = 8)
        self.encabezado.pack(side=LEFT,padx = 180)
        self.mostrar_tablas()


    def mostrar_tablas(self):
        variables = ["H =", "L =", "Di =", "N =", "S =", "G =", "Wr =", "Er =", "Fc =", "Et ="]
        unidades = ["ft", "ft","in", "SPM", "in","adim","(lb)/(ft)","(*10^-6)*(in)*(lb/ft)","adim","(*10^-6)*(in)*(lb/ft)"]
        tablavariables = Tabla()
        tablavariables.mostrar_tabla(self.ventana, variables,self.colorfondo,self.colorcontexto,unidades)


class Plots:

    def plot_curva4_1(self):
        fig, ax = plt.subplots()
        p = Curvas.Curva41()
        p.sacar_matriz(0.05)
        ax.plot(p.listax, p.listay)
        p.sacar_matriz(0.1)
        ax.plot(p.listax, p.listay)
        p.sacar_matriz(0.2)
        ax.plot(p.listax, p.listay)
        p.sacar_matriz(0.3)
        ax.plot(p.listax, p.listay)
        p.sacar_matriz(0.4)
        ax.plot(p.listax, p.listay)
        p.sacar_matriz(0.5)
        ax.plot(p.listax, p.listay)
        plt.ylim(0, 1.7)
        plt.xlim(0, 0.7)
        plt.show()

    def plot_curva4_2(self):
        fig, ax = plt.subplots()
        p = Curvas.Curva42()
        p.sacar_matriz(0.1)
        ax.plot(p.listax, p.listay)
        p.sacar_matriz(0.2)
        ax.plot(p.listax, p.listay)
        p.sacar_matriz(0.3)
        ax.plot(p.listax, p.listay)
        p.sacar_matriz(0.4)
        ax.plot(p.listax, p.listay)
        p.sacar_matriz(0.5)
        ax.plot(p.listax, p.listay)
        plt.ylim(0, 1.2)
        plt.xlim(0, 0.65)
        plt.show()

    def plot_curva4_3(self):
        fig, ax = plt.subplots()
        p = Curvas.Curva43()
        p.sacar_matriz(0.1)
        ax.plot(p.listax, p.listay)
        p.sacar_matriz(0.2)
        ax.plot(p.listax, p.listay)
        p.sacar_matriz(0.3)
        ax.plot(p.listax, p.listay)
        p.sacar_matriz(0.4)
        ax.plot(p.listax, p.listay)
        p.sacar_matriz(0.5)
        ax.plot(p.listax, p.listay)
        plt.ylim(0, 0.5)
        plt.xlim(0, 0.7)
        plt.show()

    def plot_curva4_4(self):
        fig, ax = plt.subplots()
        p = Curvas.Curva44()
        p.sacar_matriz(0.1)
        ax.plot(p.listax, p.listay)
        p.sacar_matriz(0.2)
        ax.plot(p.listax, p.listay)
        p.sacar_matriz(0.3)
        ax.plot(p.listax, p.listay)
        p.sacar_matriz(0.4)
        ax.plot(p.listax, p.listay)
        p.sacar_matriz(0.5)
        ax.plot(p.listax, p.listay)
        plt.ylim(0, 0.7)
        plt.xlim(0, 0.7)
        plt.show()

    def plot_curva4_5(self):
        fig, ax = plt.subplots()
        p = Curvas.Curva45()
        p.sacar_matriz(0.1)
        ax.plot(p.listax, p.listay)
        p.sacar_matriz(0.2)
        ax.plot(p.listax, p.listay)
        p.sacar_matriz(0.3)
        ax.plot(p.listax, p.listay)
        p.sacar_matriz(0.4)
        ax.plot(p.listax, p.listay)
        p.sacar_matriz(0.5)
        ax.plot(p.listax, p.listay)
        p.sacar_matriz(0.6)
        ax.plot(p.listax, p.listay)
        plt.ylim(0, 0.85)
        plt.xlim(0, 0.7)
        plt.show()


if __name__ == "__main__":
    principal = Ventana()
    principal.ventana.mainloop()

import tkinter as tk
class input(object):
    def __init__(self,Titre, demande):
        self.Titre = Titre
        self.demande = demande
    
    def message(self):
        window = tk.Tk()
        window.title(self.Titre)
        window.geometry("1000x100")
        htLabel = tk.Label(window, text=self.demande)
        htLabel.pack() 
        ht = tk.DoubleVar()
        ht.set(ht)
        saisieHT = tk.Entry(window, textvariable=ht, width = 15)
        saisieHT.pack()
        bouton1 = tk.Button(window, text="Ok", width = 10, command=window.destroy)
        bouton1.pack()
        window.mainloop()
        return ht
    
    def messagemult(self,demande0,demande1,demande2,demande3,demande4,demande5,demande6,demande7,demande8,demande9,demande10):
        window = tk.Tk()
        window.title(self.Titre)
        window.geometry("1200x500")
        ht0Label = tk.Label(window, text=demande0)
        ht0Label.pack() 
        ht0 = tk.DoubleVar()
        ht0.set(ht0)
        saisieHT0 = tk.Entry(window, textvariable=ht0, width = 15)
        saisieHT0.pack()
        ht1Label = tk.Label(window, text=demande1)
        ht1Label.pack() 
        ht1 = tk.DoubleVar()
        ht1.set(ht1)
        saisieHT1 = tk.Entry(window, textvariable=ht1, width = 15)
        saisieHT1.pack()
        ht2Label = tk.Label(window, text=demande2)
        ht2Label.pack() 
        ht2 = tk.DoubleVar()
        ht2.set(ht2)
        saisieHT2 = tk.Entry(window, textvariable=ht2, width = 15)
        saisieHT2.pack()
        ht3Label = tk.Label(window, text=demande3)
        ht3Label.pack() 
        ht3 = tk.DoubleVar()
        ht3.set(ht3)
        saisieHT3 = tk.Entry(window, textvariable=ht3, width = 15)
        saisieHT3.pack()
        ht4Label = tk.Label(window, text=demande4)
        ht4Label.pack() 
        ht4 = tk.DoubleVar()
        ht4.set(ht4)
        saisieHT4 = tk.Entry(window, textvariable=ht4, width = 15)
        saisieHT4.pack()
        ht5Label = tk.Label(window, text=demande5)
        ht5Label.pack() 
        ht5 = tk.DoubleVar()
        ht5.set(ht5)
        saisieHT5 = tk.Entry(window, textvariable=ht5, width = 15)
        saisieHT5.pack()
        ht6Label = tk.Label(window, text=demande6)
        ht6Label.pack() 
        ht6 = tk.DoubleVar()
        ht6.set(ht6)
        saisieHT6 = tk.Entry(window, textvariable=ht6, width = 15)
        saisieHT6.pack()
        ht7Label = tk.Label(window, text=demande7)
        ht7Label.pack() 
        ht7 = tk.IntVar()
        ht7.set(ht7)
        saisieHT7 = tk.Entry(window, textvariable=ht7, width = 15)
        saisieHT7.pack()
        ht8Label = tk.Label(window, text=demande8)
        ht8Label.pack() 
        ht8 = tk.DoubleVar()
        ht8.set(ht8)
        saisieHT8 = tk.Entry(window, textvariable=ht8, width = 15)
        saisieHT8.pack()
        ht9Label = tk.Label(window, text=demande9)
        ht9Label.pack() 
        ht9 = tk.IntVar()
        ht9.set(ht9)
        saisieHT9 = tk.Entry(window, textvariable=ht9, width = 15)
        saisieHT9.pack()
        ht10Label = tk.Label(window, text=demande10)
        ht10Label.pack() 
        ht10 = tk.IntVar()
        ht10.set(ht10)
        saisieHT10 = tk.Entry(window, textvariable=ht10, width = 15)
        saisieHT10.pack()
        bouton1 = tk.Button(window, text="Ok", width = 10, command=window.destroy)
        bouton1.pack()
        window.mainloop()
        return ht0,ht1,ht2,ht3,ht4,ht5,ht6,ht7,ht8,ht9,ht10
        
    def mespot(self,demande0,demande1,demande2,demande3,demande4):
        window = tk.Tk()
        window.title(self.Titre)
        window.geometry("800x400")
        ht0Label = tk.Label(window, text=demande0)
        ht0Label.pack() 
        ht0 = tk.DoubleVar()
        ht0.set(ht0)
        saisieHT0 = tk.Entry(window, textvariable=ht0, width = 15)
        saisieHT0.pack()
        ht1Label = tk.Label(window, text=demande1)
        ht1Label.pack() 
        ht1 = tk.DoubleVar()
        ht1.set(ht1)
        saisieHT1 = tk.Entry(window, textvariable=ht1, width = 15)
        saisieHT1.pack()
        ht2Label = tk.Label(window, text=demande2)
        ht2Label.pack() 
        ht2 = tk.DoubleVar()
        ht2.set(ht2)
        saisieHT2 = tk.Entry(window, textvariable=ht2, width = 15)
        saisieHT2.pack()
        ht3Label = tk.Label(window, text=demande3)
        ht3Label.pack() 
        ht3 = tk.DoubleVar()
        ht3.set(ht3)
        saisieHT3 = tk.Entry(window, textvariable=ht3, width = 15)
        saisieHT3.pack()
        ht4Label = tk.Label(window, text=demande4)
        ht4Label.pack() 
        ht4 = tk.DoubleVar()
        ht4.set(ht4)
        saisieHT4 = tk.Entry(window, textvariable=ht4, width = 15)
        saisieHT4.pack()
        bouton1 = tk.Button(window, text="Ok", width = 10, command=window.destroy)
        bouton1.pack()
        window.mainloop()
        return ht0,ht1,ht2,ht3,ht4
    def mesconst(self,demande0,demande1,demande2,demande3):
        window = tk.Tk()
        window.title(self.Titre)
        window.geometry("800x400")
        ht0Label = tk.Label(window, text=demande0)
        ht0Label.pack() 
        ht0 = tk.DoubleVar()
        ht0.set(ht0)
        saisieHT0 = tk.Entry(window, textvariable=ht0, width = 15)
        saisieHT0.pack()
        ht1Label = tk.Label(window, text=demande1)
        ht1Label.pack() 
        ht1 = tk.DoubleVar()
        ht1.set(ht1)
        saisieHT1 = tk.Entry(window, textvariable=ht1, width = 15)
        saisieHT1.pack()
        ht2Label = tk.Label(window, text=demande2)
        ht2Label.pack() 
        ht2 = tk.DoubleVar()
        ht2.set(ht2)
        saisieHT2 = tk.Entry(window, textvariable=ht2, width = 15)
        saisieHT2.pack()
        ht3Label = tk.Label(window, text=demande3)
        ht3Label.pack() 
        ht3 = tk.DoubleVar()
        ht3.set(ht3)
        saisieHT3 = tk.Entry(window, textvariable=ht3, width = 15)
        saisieHT3.pack()
        bouton1 = tk.Button(window, text="Ok", width = 10, command=window.destroy)
        bouton1.pack()
        window.mainloop()
        return ht0,ht1,ht2,ht3
    def mestdh(self,demande0,demande1,demande2,demande3):
            window = tk.Tk()
            window.title(self.Titre)
            window.geometry("800x400")
            ht0Label = tk.Label(window, text=demande0)
            ht0Label.pack() 
            ht0 = tk.DoubleVar()
            ht0.set(ht0)
            saisieHT0 = tk.Entry(window, textvariable=ht0, width = 15)
            saisieHT0.pack()
            ht1Label = tk.Label(window, text=demande1)
            ht1Label.pack() 
            ht1 = tk.DoubleVar()
            ht1.set(ht1)
            saisieHT1 = tk.Entry(window, textvariable=ht1, width = 15)
            saisieHT1.pack()
            ht2Label = tk.Label(window, text=demande2)
            ht2Label.pack() 
            ht2 = tk.DoubleVar()
            ht2.set(ht2)
            saisieHT2 = tk.Entry(window, textvariable=ht2, width = 15)
            saisieHT2.pack()
            ht3Label = tk.Label(window, text=demande3)
            ht3Label.pack() 
            ht3 = tk.IntVar()
            ht3.set(ht3)
            saisieHT3 = tk.Entry(window, textvariable=ht3, width = 15)
            saisieHT3.pack()
            bouton1 = tk.Button(window, text="Ok", width = 10, command=window.destroy)
            bouton1.pack()
            window.mainloop()
            tdh = ht0.get() + ht1.get() + 0.1*ht2.get() + ht3.get()*10
            return tdh
    
    

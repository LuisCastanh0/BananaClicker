from tkinter import *

class Upgrade:
    def __init__(self, frame, cost, plus):
        self.frame = frame
        self.cost = cost
        self.plus = plus
        self.button = Button(frame, text='Comprar',
                             font=('Impact', 16),
                             foreground=preto,
                             background=amarelo_banana,
                             activebackground=amarelo_highlight,
                             width=10, height=2, bd=4, relief=RAISED,
                             command=self.ValueUp)

    def ValueUp(self):
        global cont
        if cont >= self.cost:
            cont -= self.cost
            with open("data.txt", "w") as f:  
                f.write(str(cont))  
            new_click_value = self.plus
            global click_value
            click_value = new_click_value
        else:
            message_label = Label(self.frame, text="Bananas insuficientes", font=('Impact', 20, 'underline'),
                                  bg='#82929E', fg='#F1EC5D')
            message_label.grid(row=10, column=0)
            self.frame.after(3000, message_label.destroy)

#Color Pallet
amarelo_banana = '#F1EC5D'
amarelo_highlight = '#FFF600'
cinza = '#82929E'
marrom = '#6B3E26'
preto= '#000000'

def read_clicks(): # Função para ler a pontuação salva em um arquivo.
    with open("data.txt", "r") as file:
        return int(file.read())

# Valor do clique
click_value = 1
# N de cliques
cont = read_clicks()

def update_click(label,click_value): #Função para atualizar a pontuação (no arquivo e na tela)
    cont = int(label.cget("text"))
    cont += click_value
    label.config(text=cont) 
    with open("data.txt", "w") as f:  
        f.write(str(cont))  

# GUI
def MenuWindow(window):
    frame = Frame(window,background=cinza)
    frame.pack(fill=BOTH, expand=True)

    BananaLabel = Label(frame,text='BANANA CLICKER',
                        font=('Impact',50,'underline'),
                        bg=cinza,fg=amarelo_banana)
    BananaLabel.place(anchor = 'n',relx=0.5,rely=0.1)

    StartButton = Button(frame, text='INICIAR',
                         font=('Impact',16),
                         bg=amarelo_banana,fg='Black',
                         command=lambda: MainWindow(window),
                         activebackground=amarelo_highlight, 
                         width=10, height=2, bd=4,relief=RAISED
                         )
    StartButton.place(anchor='center', relx=0.5,rely=0.5)

    label = Label(frame,text='Código e imagens criados por Luis Castanho\n',
                  font=('Impact',16),fg=amarelo_banana,
                  bg=cinza)
    label.place(anchor='s',relx=0.5,rely=0.9)

def MainWindow(window):
    for widget in window.winfo_children():
        widget.destroy()

    global cont
    cont = read_clicks()
    frame = Frame(window,background=cinza)
    frame.pack(fill=BOTH, expand=True)
    
    imagem = PhotoImage(file='./images/Banana.png')
    Bananabutton = Button(frame, 
                    image=imagem,
                    bg=cinza,
                    activebackground=cinza, 
                    activeforeground=cinza,
                    bd=0,
                    command=lambda: update_click(clicks_label,click_value),
                    width=100,
                    height=100)
    Bananabutton.image=imagem
    Bananabutton.place(relx=0.5, rely=0.5, anchor=CENTER)

    clicks_label = Label(frame,
                  text=cont,
                  font=('Impact',35),
                  background=cinza,
                  foreground=amarelo_banana)
    clicks_label.place(relx=0.5, rely=0.1, anchor=N)

    click_value_label = Label(frame,
                  text=f'+ {click_value}',
                  font=('Impact',35),
                  background=cinza,
                  foreground=amarelo_banana)
    click_value_label.place(relx=0.8, rely=0.1, anchor=NE)

    StoreButton = Button(frame,
                         text='Loja',
                         font=('Impact',16),
                         foreground='Black',
                         background=amarelo_banana,
                         activebackground=amarelo_highlight,  
                         command=lambda: StoreWindow(window),
                         width=10,height=2,bd=4,relief=RAISED)
    StoreButton.place(relx=0.5, rely=0.9, anchor='s')

def StoreWindow(window):
    for widget in window.winfo_children():
        widget.destroy()

    global cont 
    cont = read_clicks()
    frame = Frame(window, background=cinza)
    frame.pack(fill=BOTH, expand=True)

    # Upgrade 1 - Clique x2
    Upgrade1 = Upgrade(frame,500,2)

    # Label Upgrade 1
    TwoBananas_Label = Label(frame,text="O que é melhor que uma banana? DUAS BANANAS!",
                             bg=amarelo_banana,fg=preto,
                             bd=2,relief=SOLID,
                             font=('Impact',16),
                             width=50,height=2
                             )
    TwoBananas_Label.grid(row=0,column=0,pady=20,padx=50)

    # Imagem Upgrade 1
    image1 = PhotoImage(file='./images/Banana2.png')
    TwoBananas_Pic = Label(frame,image=image1,width=64,height=64,bg=cinza)
    TwoBananas_Pic.image = image1
    TwoBananas_Pic.grid(row=0,column=1,pady=20,padx=20)
    # Botao Upgrade 1
    Upgrade1.button.grid(row=0,column=2,pady=20,padx=50)

    # Upgrade 2 - Três Bananas
    # Label Upgrade 2
    Upgrade2 = Upgrade(frame,1000,3)

    ThreeBananas = Label(frame,text="TRÊS?????",
                         bg=amarelo_banana,fg=preto,
                         bd=2,relief=SOLID,
                         font=('Impact',16),
                         width=50,height=2)
    ThreeBananas.grid(row=1,column=0,pady=20)
    
    # Imagem  Upgrade 2
    image2 = PhotoImage(file='./images/Banana3.png')
    ThreeBananas_Pic = Label(frame,image=image2,width=64,height=64,bg=cinza)
    ThreeBananas_Pic.image = image2
    ThreeBananas_Pic.grid(row=1,column=1,pady=20,padx=20)

    # Botao  Upgrade 2
    Upgrade2.button.grid(row=1,column=2,pady=20,padx=50)

    # Upgrade 3 - Cacho de Banana (6x)
    Upgrade3 = Upgrade(frame,2000,6)
    # Label Upgrade 3
    BananaBunch = Label(frame,text="Compra um cacho todo...",
                         bg=amarelo_banana,fg=preto,
                         bd=2,relief=SOLID,
                         font=('Impact',16),
                         width=50,height=2)
    BananaBunch.grid(row=2,column=0,pady=20)

    # Imagem Upgrade 3
    image2 = PhotoImage(file='./images/BananaCacho.png')
    BananaBunch_Pic = Label(frame,image=image2,width=64,height=64,bg=cinza)
    BananaBunch_Pic.image = image2
    BananaBunch_Pic.grid(row=2,column=1,pady=20,padx=20)

    # Botao
    Upgrade3.button.grid(row=2,column=2,pady=20,padx=50)

    # Botao Retornar
    Return_Button = Button(frame,text='Voltar',
                           command=lambda: MainWindow(window),
                           font=('Impact',16),
                           foreground=preto,
                           background=amarelo_banana,
                           activebackground=amarelo_highlight,  
                           width=10, height=2,bd=4,relief=RAISED)
    Return_Button.grid(row=4,column=2,pady=20,padx=50)

def main():
    window = Tk()
    window.title("Banana Clicker")
    window.geometry("1024x1024")

    MenuWindow(window)
    
    window.mainloop()
if __name__ == "__main__":
    main()

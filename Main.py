from tkinter import *

#Color Pallet
amarelo_banana = '#F1EC5D'
amarelo_highlight = '#FFF600'
cinza = '#82929E'
marrom = '#6B3E26'
preto= '#000000'

def read_clicks(): # Função para ler a pontuação salva em um arquivo.
    with open("data.txt", "r") as file:
        return int(file.read())

def update_click(label,value): #Função para atualizar a pontuação (no arquivo e na tela)
    cont = int(label.cget("text"))
    cont += value
    label.config(text=cont) 
    with open("data.txt", "w") as f:  
        f.write(str(cont))  

def MenuWindow(window,cont):
    frame = Frame(window,background=cinza)
    frame.pack(fill=BOTH, expand=True)

    BananaLabel = Label(frame,text='BANANA CLICKER',
                        font=('Impact',50,'underline'),
                        bg=cinza,fg=amarelo_banana)
    BananaLabel.place(anchor = 'n',relx=0.5,rely=0.1)

    StartButton = Button(frame, text='INICIAR',
                         font=('Impact',16),
                         bg=amarelo_banana,fg='Black',
                         command=lambda: MainWindow(window,cont),
                         activebackground=amarelo_highlight, 
                         width=10, height=2, bd=4,relief=RAISED
                         )
    StartButton.place(anchor='center', relx=0.5,rely=0.4)

    MoreButton = Button(frame, text='MAIS',
                         font=('Impact',16),
                         bg=amarelo_banana,fg='Black',
                         command=lambda: MoreFunction(frame),
                         activebackground=amarelo_highlight, 
                         width=10, height=2, bd=4,relief=RAISED
                         )
    MoreButton.place(anchor='center', relx=0.5,rely=0.5)

def MoreFunction(frame):
    label = Label(frame,text='Código e imagens criados por Luis Castanho\n',
                  font=('Impact',16),fg=amarelo_banana,
                  bg=cinza)
    label.place(anchor='s',relx=0.5,rely=0.9)

def MainWindow(window, cont):
    for widget in window.winfo_children():
        widget.destroy()

    frame = Frame(window,background=cinza)
    frame.pack(fill=BOTH, expand=True)
    
    imagem = PhotoImage(file='./images/Banana.png')
    button = Button(frame, 
                    image=imagem,
                    bg=cinza,
                    activebackground=cinza, 
                    activeforeground=cinza,
                    bd=0,
                    command=lambda: update_click(label,1),
                    width=100,
                    height=100)
    button.image=imagem
    button.place(relx=0.5, rely=0.5, anchor=CENTER)

    label = Label(frame,
                  text=cont,
                  font=('Impact',35),
                  background=cinza,
                  foreground=amarelo_banana)
    label.place(relx=0.5, rely=0.1, anchor=N)

    StoreButton = Button(frame,
                         text='Loja',
                         font=('Impact',16),
                         foreground='Black',
                         background=amarelo_banana,
                         activebackground=amarelo_highlight,  
                         command=lambda: StoreWindow(window,cont),
                         width=10,height=2,bd=4,relief=RAISED)
    StoreButton.place(relx=0.5, rely=0.9, anchor='s')

def StoreWindow(window,cont):
    for widget in window.winfo_children():
        widget.destroy()

    frame = Frame(window, background=cinza)
    frame.pack(fill=BOTH, expand=True)

    # Primeira Compra - Duas bananas
    # Label
    TwoBananas_Label = Label(frame,text="O que é melhor que uma banana? DUAS BANANAS!",
                             bg=amarelo_banana,fg=preto,
                             bd=2,relief=SOLID,
                             font=('Impact',16),
                             width=50,height=2
                             )
    TwoBananas_Label.grid(row=0,column=0,pady=20,padx=50)
    # Imagem
    image1 = PhotoImage(file='./images/Banana2.png')
    TwoBananas_Pic = Label(frame,image=image1,width=64,height=64,bg=cinza)
    TwoBananas_Pic.image = image1
    TwoBananas_Pic.grid(row=0,column=1,pady=20,padx=20)
    # Botao
    TwoBananas_Button = Button(frame,text='Comprar',
                               font=('Impact',16),
                               foreground=preto,
                               background=amarelo_banana,
                               activebackground=amarelo_highlight,  
                               width=10, height=2,bd=4,relief=RAISED)
    TwoBananas_Button.grid(row=0,column=2,pady=20,padx=20)

    # Segunda Compra - Três Bananas
    # Label
    ThreeBananas = Label(frame,text="TRÊS?????",
                         bg=amarelo_banana,fg=preto,
                         bd=2,relief=SOLID,
                         font=('Impact',16),
                         width=50,height=2)
    ThreeBananas.grid(row=1,column=0,pady=20)

    # Imagem
    image2 = PhotoImage(file='./images/Banana3.png')
    ThreeBananas_Pic = Label(frame,image=image2,width=64,height=64,bg=cinza)
    ThreeBananas_Pic.image = image2
    ThreeBananas_Pic.grid(row=1,column=1,pady=20,padx=20)
    # Botao
    ThreeBananas_Button = Button(frame,text='Comprar',
                                 font=('Impact',16),
                                 foreground=preto,
                                 background=amarelo_banana,
                                 activebackground=amarelo_highlight, 
                                 width=10, height=2,bd=4,relief=RAISED)
    ThreeBananas_Button.grid(row=1,column=2,pady=20,padx=50)

    # Terceira Compra - Cacho de Banana
    # Label
    BananaBunch = Label(frame,text="Compra um cacho todo...",
                         bg=amarelo_banana,fg=preto,
                         bd=2,relief=SOLID,
                         font=('Impact',16),
                         width=50,height=2)
    BananaBunch.grid(row=2,column=0,pady=20)

    # Imagem
    image2 = PhotoImage(file='./images/BananaCacho.png')
    BananaBunch_Pic = Label(frame,image=image2,width=64,height=64,bg=cinza)
    BananaBunch_Pic.image = image2
    BananaBunch_Pic.grid(row=2,column=1,pady=20,padx=20)
    # Botao
    BananaBunch = Button(frame,text='Comprar',
                                 font=('Impact',16),
                                 foreground=preto,
                                 background=amarelo_banana,
                                 activebackground=amarelo_highlight, 
                                 width=10, height=2,bd=4,relief=RAISED)
    BananaBunch.grid(row=2,column=2,pady=20,padx=50)

    # Botao Retornar
    Return_Button = Button(frame,text='Voltar',
                           command=lambda: MainWindow(window, cont),
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

    cont = read_clicks()
    MenuWindow(window,cont)
    
    window.mainloop()
if __name__ == "__main__":
    main()

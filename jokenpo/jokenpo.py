from tkinter import *
from random import choice

player = ''


def Game_Start():
    mao = ['pedra', 'papel', 'tesoura']
    pc = choice(mao)

    global MainMenu
    MainMenu = Tk()  # cria um model Tk()
    MainMenu.title("Jokenpo")
    MainMenu.geometry("800x600+100+100")  # largura x altura posX posY
    MainMenu.resizable(False, False)
    MainMenu.iconbitmap("image/icon.ico")

    Label(MainMenu, text="JOKENPÔ", font=('Arial Black', 15)).pack(side=TOP, pady=10)

    photoPapel = PhotoImage(file="image/papel.png")
    photoimagePapel = photoPapel.subsample(4, 4)
    photoPedra = PhotoImage(file="image/pedra.png")
    photoimagePedra = photoPedra.subsample(4, 4)
    photoTesoura = PhotoImage(file="image/tesoura.png")
    photoimageTesoura = photoTesoura.subsample(4, 4)

    bottomframe = Frame(MainMenu)
    bottomframe.pack(side=TOP)
    Label(bottomframe, text="Pedra, Papel ou Tesoura", font=('Arial', 12)).pack(side=TOP, pady=10)

    def teste(msg):
        global player
        player = msg
        bottomframe.destroy()
        MainMenu.after(0, start())

    Button(bottomframe, text="Pedra", image=photoimagePedra, compound=TOP, cursor="hand2",
           command=lambda: teste('pedra')).pack(side=LEFT, padx=5)
    Button(bottomframe, text="Papel", image=photoimagePapel, compound=TOP, cursor="hand2",
           command=lambda: teste('papel')).pack(side=LEFT, padx=5)
    Button(bottomframe, text="Tesoura", image=photoimageTesoura, compound=TOP, cursor="hand2",
           command=lambda: teste('tesoura')).pack(side=LEFT, padx=5)

    labelframe = Frame(MainMenu)
    labelframe.pack(side=TOP)

    def start():
        Label(labelframe, text="JO", font=('Arial Black', 30)).pack(side=LEFT, pady=20)
        MainMenu.after(1000, carregando)

    def carregando():
        Label(labelframe, text="KEN", font=('Arial Black', 30)).pack(side=LEFT, pady=20)
        MainMenu.after(1000, concluido)

    def concluido():
        Label(labelframe, text="PÔ", font=('Arial Black', 30)).pack(side=LEFT, pady=20)
        MainMenu.after(5, mostrarResultado)

    infoframe = Frame(MainMenu)
    infoframe.pack(side=TOP)

    btinfoframe = Frame(MainMenu)
    btinfoframe.pack(side=TOP)

    resulframe = Frame(MainMenu)
    resulframe.pack(side=TOP)

    opframe = Frame(MainMenu)
    opframe.pack(side=TOP)

    def mostrarResultado():
        Label(infoframe, text="Você escolheu", font=('Arial', 12)).pack(side=LEFT, pady=2, padx=20)
        Label(infoframe, text="PC escolheu", font=('Arial', 12)).pack(side=LEFT, pady=2, padx=20)
        ShowPlayer()
        ShowPc()
        if player == pc:
            Label(resulframe, text="Empate", font=('Arial Black', 15)).pack(side=LEFT, pady=10)
        elif (player == 'pedra' and pc == 'tesoura') or (player == 'papel' and pc == 'pedra') or (
                player == 'tesoura' and pc == 'papel'):
            Label(resulframe, text="Você venceu!", font=('Arial Black', 15)).pack(side=LEFT, pady=10)
        elif (pc == 'pedra' and player == 'tesoura') or (pc == 'papel' and player == 'pedra') or (
                pc == 'tesoura' and player == 'papel'):
            Label(resulframe, text="O PC venceu", font=('Arial Black', 15)).pack(side=LEFT, pady=10)
        else:
            print('Escolha invalida')

        Button(opframe, text="Reiniciar", cursor="hand2", font=('Arial Black', 12), command=lambda: restart()).pack(
            side=LEFT, pady=20, padx=5)

    def ShowPc():
        if (pc == 'pedra'):
            return Button(btinfoframe, text="Pedra", image=photoimagePedra, compound=TOP).pack(side=LEFT, padx=5)
        elif (pc == 'papel'):
            return Button(btinfoframe, text="Papel", image=photoimagePapel, compound=TOP).pack(side=LEFT, padx=5)
        else:
            return Button(btinfoframe, text="Tesoura", image=photoimageTesoura, compound=TOP).pack(side=LEFT, padx=5)

    def ShowPlayer():
        if (player == 'pedra'):
            return Button(btinfoframe, text="Pedra", image=photoimagePedra, compound=TOP).pack(side=LEFT, padx=5)
        elif (player == 'papel'):
            return Button(btinfoframe, text="Papel", image=photoimagePapel, compound=TOP).pack(side=LEFT, padx=5)
        else:
            return Button(btinfoframe, text="Tesoura", image=photoimageTesoura, compound=TOP).pack(side=LEFT, padx=5)

    MainMenu.mainloop()


if __name__ == "__main__":
    def restart():
        MainMenu.destroy()
        global player
        player = ''
        Game_Start()


    Game_Start()

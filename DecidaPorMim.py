import random
import PySimpleGUI as sg


class DecidaPorMim:

    def __init__(self):
        self.respostas = [
            'Você, com certeza deve fazer isso!', 'Você que sabe!',
            'Faz isso!', 'Faz isso não!', 'Apenas na hora certa!'
        ]

    def Ligar(self):

        layout = [[sg.Text('Pergunte alguma coisa')], [sg.Input()],
                  [sg.Output(size=(50, 10))], [sg.Button('Decida por mim')]]

        self.janela = sg.Window('Decida Por Mim!', layout=layout)

        while True:

            self.eventos, self.valores = self.janela.Read()

            if self.eventos == "Decida por mim":

                print(random.choice(self.respostas))


decida = DecidaPorMim()
decida.Ligar()
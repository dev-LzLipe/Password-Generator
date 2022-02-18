import random
import PySimpleGUI as Ui
import string


class PassGen:

    def __init__(self):
        # Layout

        Ui.theme('Black')
        layout = [
            [Ui.Text('Matricula', size=(10, 1)),
             Ui.Input(key='DRT', size=(20, 1))],
            [Ui.Text('Quantidade de caracteres'), Ui.Combo(values=list(
                range(11)), key='qnt_chars', default_value=10, size=(3, 1))],
            [Ui.Output(size=(40, 0))],
            [Ui.Button('Gerar Senha')]
        ]

        # Window
        self.windowz = Ui.Window('Password Generator v1', layout)

    def start(self):
        while True:
            event, values = self.windowz.read()
            if event == Ui.WINDOW_CLOSED:
                break
            if event == 'Gerar Senha':
                nw_pass = self.generate_pass(values)
                print(nw_pass)
                self.save_pass(nw_pass, values)

    def generate_pass(self, values):
        print('\n')
        char_list = string.ascii_letters + string.digits + string.punctuation
        chars = random.choices(char_list, k=int(values['qnt_chars']))
        new_pass = ''.join(chars)
        return new_pass

    def save_pass(self, nw_pass, values):
        with open('senhas.txt', 'a', newline='') as arquivo:
            arquivo.write(
                f"Matricula: {values['DRT']}, nova senha: {nw_pass} \n")

        print('Dados salvos em senhas.txt')


generator = PassGen()
generator.start()

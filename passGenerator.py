import string
from random import choice
############################
from PySimpleGUI import PySimpleGUI as sg
# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Tamanho de senha'), sg.Input(key='tamanhoSenha')],
    [sg.Checkbox('Caracteres?', key='strings')],
    [sg.Checkbox('Maiusculo?', key='uppercase')],
    [sg.Checkbox('Simbolos?', key='simbols')],
    [sg.Checkbox('Números?', key='numbers')],
    [sg.Button('Gerar')],
    [sg.Button('Resetar')]
]
# JANELA
janela = sg.Window('GERADOR DE SENHA v1', layout)
#Ler os eventos
while True:
  eventos, valores = janela.read()
  if eventos == sg.WINDOW_CLOSED:
    break

tamanhoSenha = 10
valoresFormato = string.ascii_letters + string.digits + string.punctuation
senhaGerada = ''
for i in range(tamanhoSenha):
  senhaGerada += choice(valoresFormato)
  if eventos == 'Gerar':
    print(senhaGerada)

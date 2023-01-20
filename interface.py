import PySimpleGUI as sg


def tclube():

    sg.theme('DarkGreen2')
    sp = sg.T('',size=(30,1))
    layout = [
        [sp, sg.Text('Nome do Clube'), sg.Image('ball.png',subsample=8)]
    ]

    return sg.Window('Nome do Clube',layout,finalize=True,text_justification='center',size=(800,500))

janela = tclube()
while True:
    event, value = janela.read()

    if event == sg.WIN_CLOSED:
        break

janela.close()
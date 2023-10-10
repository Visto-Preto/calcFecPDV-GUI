import PySimpleGUI as sg

def make_window(theme):
    sg.theme(theme)
    layout = [
    			[sg.Text('Janela de teste 01')],
    			[sg.Button('Clique aqui 01')]
    		]

    window = sg.Window('Teste de jalena 01', layout=layout,size=(400, 400))

    return window


def func_2(theme):
    sg.theme(theme)
    layout = [
    			[sg.Text('janela de teste 02')],
    			[sg.Button('Clique aqui 02')]
    		]

    window = sg.Window('Teste de jalena 02', layout=layout,size=(400, 400))

    return window


def main():
    window = make_window(sg.theme())
    
    while True:
    	event, values = window.read(timeout=100)

    	if event == sg.WIN_CLOSED:
    		window.close()
    		exit()
    	if event == 'Clique aqui 01':
    		window.close()
    		window = func_2(sg.theme())

    	if event == 'Clique aqui 02':
    		window.close()
    		window = make_window(sg.theme())



main()
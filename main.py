import PySimpleGUI as sg 

sg.theme('random')

# Inicio da tab de calculos de moedas

layout_moedas = 	[	[sg.InputText('', size=(None, None),readonly=True, key='-DISPLAY_C-')],
						[sg.Text('R$ 0,05', background_color='white', text_color='green' ,justification='c', size=(7, 1)), sg.Text('X'), sg.InputText('', justification='r', size=(10, 1)), sg.Text('='), sg.Text('', background_color='white', size=(15, 1))],
						[sg.Text('R$ 0,10', background_color='white', text_color='green' ,justification='c', size=(7, 1)), sg.Text('X'), sg.InputText('', justification='r', size=(10, 1)), sg.Text('='), sg.Text('', background_color='white', size=(15, 1))],
						[sg.Text('R$ 0,25', background_color='white', text_color='green' ,justification='c', size=(7, 1)), sg.Text('X'), sg.InputText('', justification='r', size=(10, 1)), sg.Text('='), sg.Text('', background_color='white', size=(15, 1))],
						[sg.Text('R$ 0,50', background_color='white', text_color='green' ,justification='c', size=(7, 1)), sg.Text('X'), sg.InputText('', justification='r', size=(10, 1)), sg.Text('='), sg.Text('', background_color='white', size=(15, 1))],
						[sg.Text('R$ 1,00', background_color='white', text_color='green' ,justification='c', size=(7, 1)), sg.Text('X'), sg.InputText('', justification='r', size=(10, 1)), sg.Text('='), sg.Text('', background_color='white', size=(15, 1))]
					]

# fim da tab de calculos de moedas




layout_cedulas = [	[sg.Text('Menu de tab 02')],
					[sg.Button('Click Aqui')]	]

layout_calc = [	[sg.Text('Menu de tab 03')],
					[sg.Button('Click Aqui')]	]

layout_config = [	[sg.Text('Menu de tab 04')],
					[sg.Button('Click Aqui')]	]


layout_tab_group = [	[	sg.Tab('Moedas', layout_moedas), 
							sg.Tab('Cédulas', layout_cedulas),
							sg.Tab('Calculos PDV', layout_calc),
							sg.Tab('Configurações', layout_config)	]]




layout_menu = [	['Arquivo', ['Abrir','Salvar', 'Sair']],
				['Temas'],
				['Sobre']	]




layout = [ 	[sg.Menu(layout_menu)],
			[sg.TabGroup(layout_tab_group)],
			[sg.Text('Desenvolvido por Leonardo Sousa')], 
			[sg.Button('Sair')] ] 

window = sg.Window('Fechamento de Caixa', layout) 
while True: 
# Event Loop 
	event, values = window.read() 
	print(event, values) 
	if event in (None, 'Sair'): 
		break 
window.close()
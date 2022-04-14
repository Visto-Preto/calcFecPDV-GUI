import PySimpleGUI as sg 
from module import calc

sg.theme('random')

# Inicio da tab de calculos de moedas

layout_moedas = 	[	[sg.InputText('R$ 0,00', text_color='green', justification='r', size=(None, None),readonly=True, key='-DISPLAY_C-')],
						[sg.Text('R$ 0,05', background_color='white', text_color='green' ,justification='c', size=(7, 1)), sg.Text('X'), sg.InputText('', justification='r', size=(10, 1), enable_events=True, key='-IN005-'), sg.Text('='), sg.Text('', background_color='white', text_color='green', size=(15, 1), justification='r', key='-OUT005-')],
						[sg.Text('R$ 0,10', background_color='white', text_color='green' ,justification='c', size=(7, 1)), sg.Text('X'), sg.InputText('', justification='r', size=(10, 1), enable_events=True, key='-IN010-'), sg.Text('='), sg.Text('', background_color='white', text_color='green', size=(15, 1), justification='r', key='-OUT010-')],
						[sg.Text('R$ 0,25', background_color='white', text_color='green' ,justification='c', size=(7, 1)), sg.Text('X'), sg.InputText('', justification='r', size=(10, 1), enable_events=True, key='-IN025-'), sg.Text('='), sg.Text('', background_color='white', text_color='green', size=(15, 1), justification='r', key='-OUT025-')],
						[sg.Text('R$ 0,50', background_color='white', text_color='green' ,justification='c', size=(7, 1)), sg.Text('X'), sg.InputText('', justification='r', size=(10, 1), enable_events=True, key='-IN050-'), sg.Text('='), sg.Text('', background_color='white', text_color='green', size=(15, 1), justification='r', key='-OUT050-')],
						[sg.Text('R$ 1,00', background_color='white', text_color='green' ,justification='c', size=(7, 1)), sg.Text('X'), sg.InputText('', justification='r', size=(10, 1), enable_events=True, key='-IN100-'), sg.Text('='), sg.Text('', background_color='white', text_color='green', size=(15, 1), justification='r', key='-OUT100-')]
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
				['Temas', sg.theme()],
				['Sobre']	]




layout = [ 	[sg.Menu(layout_menu)],
			[sg.TabGroup(layout_tab_group)],
			[sg.Text('Desenvolvido por Leonardo Sousa')], 
			[sg.Button('Sair')] ] 

window = sg.Window('Fechamento de Caixa', layout) 
while True: 


# Event Loop 
	event, values = window.read() 

	if event in (None, 'Sair'): 
		break

# Eventos da tab 01
	if event == '-IN005-' and len(values['-IN005-']) and values['-IN005-'][-1] not in ('0123456789'):
		window['-IN005-'].update(values['-IN005-'][:-1])
		
		window['-OUT005-'].update( calc.str_real_format( calc.insert_result( float( values['-IN005-'][:-1] ) * (0.05)	) ))
		



		window['-DISPLAY_C-'].update( calc.str_real_format( calc.insert_result(	float( values['-IN005-'][:-1] ) * (0.05)	)))



window.close()
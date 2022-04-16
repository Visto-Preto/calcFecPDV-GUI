import PySimpleGUI as sg 
from module import calc


sg.theme('random')

# Inicio da tab de calculos de moedas

layout_moedas = 	[	
						[sg.Input('R$ 0,00', background_color='white', text_color='green', justification='r', size=(28, 1),  disabled=True, key='-DISPLAY_M-', font='_ 15')],
						[sg.Text('R$   0,05', background_color='white', text_color='green' ,justification='c', size=(8, 1)), sg.Text('X'), sg.InputText('', justification='r', size=(10, 1), enable_events=True, key='-IN005-'), sg.Text('='), sg.Input('R$ 0,00', background_color='white', text_color='green', size=(15, 1), justification='r', disabled=True, key='-OUT005-')],
						[sg.Text('R$   0,10', background_color='white', text_color='green' ,justification='c', size=(8, 1)), sg.Text('X'), sg.InputText('', justification='r', size=(10, 1), enable_events=True, key='-IN010-'), sg.Text('='), sg.Input('R$ 0,00', background_color='white', text_color='green', size=(15, 1), justification='r', disabled=True, key='-OUT010-')],
						[sg.Text('R$   0,25', background_color='white', text_color='green' ,justification='c', size=(8, 1)), sg.Text('X'), sg.InputText('', justification='r', size=(10, 1), enable_events=True, key='-IN025-'), sg.Text('='), sg.Input('R$ 0,00', background_color='white', text_color='green', size=(15, 1), justification='r', disabled=True, key='-OUT025-')],
						[sg.Text('R$   0,50', background_color='white', text_color='green' ,justification='c', size=(8, 1)), sg.Text('X'), sg.InputText('', justification='r', size=(10, 1), enable_events=True, key='-IN050-'), sg.Text('='), sg.Input('R$ 0,00', background_color='white', text_color='green', size=(15, 1), justification='r', disabled=True, key='-OUT050-')],
						[sg.Text('R$   1,00', background_color='white', text_color='green' ,justification='c', size=(8, 1)), sg.Text('X'), sg.InputText('', justification='r', size=(10, 1), enable_events=True, key='-IN100-'), sg.Text('='), sg.Input('R$ 0,00', background_color='white', text_color='green', size=(15, 1), justification='r', disabled=True, key='-OUT100-')]

					]
# fim da tab de calculos de moedas


# Inicio da tab de calculos de cedulas

layout_cedulas = [	
					[sg.Input('R$ 0,00', background_color='white', text_color='green', justification='r', size=(28, 1),  disabled=True, key='-DISPLAY_C-', font='_ 15')],
					[sg.Text('R$   2,00', background_color='white', text_color='green' ,justification='c', size=(8, 1)), sg.Text('X'), sg.InputText('', justification='r', size=(10, 1), enable_events=True, key='-IN200-'), sg.Text('='), sg.Input('R$ 0,00', background_color='white', text_color='green', size=(15, 1), justification='r', readonly=True, key='-OUT200-')],
					[sg.Text('R$   5,00', background_color='white', text_color='green' ,justification='c', size=(8, 1)), sg.Text('X'), sg.InputText('', justification='r', size=(10, 1), enable_events=True, key='-IN500-'), sg.Text('='), sg.Input('R$ 0,00', background_color='white', text_color='green', size=(15, 1), justification='r', readonly=True, key='-OUT500-')],
					[sg.Text('R$  10,00', background_color='white', text_color='green' ,justification='c', size=(8, 1)), sg.Text('X'), sg.InputText('', justification='r', size=(10, 1), enable_events=True, key='-IN1000-'), sg.Text('='), sg.Input('R$ 0,00', background_color='white', text_color='green', size=(15, 1), justification='r', readonly=True, key='-OUT1000-')],
					[sg.Text('R$  20,00', background_color='white', text_color='green' ,justification='c', size=(8, 1)), sg.Text('X'), sg.InputText('', justification='r', size=(10, 1), enable_events=True, key='-IN2000-'), sg.Text('='), sg.Input('R$ 0,00', background_color='white', text_color='green', size=(15, 1), justification='r', readonly=True, key='-OUT2000-')],
					[sg.Text('R$  50,00', background_color='white', text_color='green' ,justification='c', size=(8, 1)), sg.Text('X'), sg.InputText('', justification='r', size=(10, 1), enable_events=True, key='-IN5000-'), sg.Text('='), sg.Input('R$ 0,00', background_color='white', text_color='green', size=(15, 1), justification='r', readonly=True, key='-OUT5000-')],
					[sg.Text('R$ 100,00', background_color='white', text_color='green' ,justification='c', size=(8, 1)), sg.Text('X'), sg.InputText('', justification='r', size=(10, 1), enable_events=True, key='-IN10000-'), sg.Text('='), sg.Input('R$ 0,00', background_color='white', text_color='green', size=(15, 1), justification='r', readonly=True, key='-OUT10000-')],
					[sg.Text('R$ 200,00', background_color='white', text_color='green' ,justification='c', size=(8, 1)), sg.Text('X'), sg.InputText('', justification='r', size=(10, 1), enable_events=True, key='-IN20000-'), sg.Text('='), sg.Input('R$ 0,00', background_color='white', text_color='green', size=(15, 1), justification='r', readonly=True, key='-OUT20000-')]

					]

# fim da tab de calculos de cedulas



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
				['Calculadora'],
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

	# Incio da logica do campo de R$ 0,05

	if event == '-IN005-' and len(values['-IN005-']) and values['-IN005-'][-1] not in ('0123456789'):
		window['-IN005-'].update(values['-IN005-'][:-1])
	if event == '-IN005-' and len(values['-IN005-']) and values['-IN005-'][-1] in ('0123456789'):

		if (len(values['-IN005-']) > 8):
			window['-IN005-'].update(values['-IN005-'][:-1])
		if (len(values['-IN005-']) < 9):	
			window['-OUT005-'].update(	calc.str_real_format(	calc.insert_result(	float( values['-IN005-']) * (0.05)	)))
	if values['-IN005-'] == '':
		window['-OUT005-'].update('R$ 0,00')


	# Incio da logica do campo de R$ 0,10

	if event == '-IN010-' and len(values['-IN010-']) and values['-IN010-'][-1] not in ('0123456789'):
		window['-IN010-'].update(values['-IN010-'][:-1])
	if event == '-IN010-' and len(values['-IN010-']) and values['-IN010-'][-1] in ('0123456789'):
		if (len(values['-IN010-']) > 8):
			window['-IN010-'].update(values['-IN010-'][:-1])
		if (len(values['-IN010-']) < 9):	
			window['-OUT010-'].update(	calc.str_real_format(	calc.insert_result(	float( values['-IN010-']) * (0.1)	)))

	if values['-IN010-'] == '':
		window['-OUT010-'].update('R$ 0,00')

	# Incio da logica do campo de R$ 0,25

	if event == '-IN025-' and len(values['-IN025-']) and values['-IN025-'][-1] not in ('0123456789'):
		window['-IN025-'].update(values['-IN025-'][:-1])
	if event == '-IN025-' and len(values['-IN025-']) and values['-IN025-'][-1] in ('0123456789'):
		if (len(values['-IN025-']) > 8):
			window['-IN025-'].update(values['-IN025-'][:-1])
		if (len(values['-IN025-']) < 9):	
			window['-OUT025-'].update(	calc.str_real_format(	calc.insert_result(	float( values['-IN025-']) * (0.25)	)))
	if values['-IN025-'] == '':
		window['-OUT025-'].update('R$ 0,00')

	# Incio da logica do campo de R$ 0,50

	if event == '-IN050-' and len(values['-IN050-']) and values['-IN050-'][-1] not in ('0123456789'):
		window['-IN050-'].update(values['-IN050-'][:-1])
	if event == '-IN050-' and len(values['-IN050-']) and values['-IN050-'][-1] in ('0123456789'):
		if (len(values['-IN050-']) > 8):
			window['-IN050-'].update(values['-IN050-'][:-1])
		if (len(values['-IN050-']) < 9):	
			window['-OUT050-'].update(	calc.str_real_format(	calc.insert_result(	float( values['-IN050-']) * (0.5)	)))
	if values['-IN050-'] == '':
		window['-OUT050-'].update('R$ 0,00')

	# Incio da logica do campo de R$ 1,00

	if event == '-IN100-' and len(values['-IN100-']) and values['-IN100-'][-1] not in ('0123456789'):
		window['-IN100-'].update(values['-IN100-'][:-1])
	if event == '-IN100-' and len(values['-IN100-']) and values['-IN100-'][-1] in ('0123456789'):
		if (len(values['-IN100-']) > 8):
			window['-IN100-'].update(values['-IN100-'][:-1])
		if (len(values['-IN100-']) < 9):	
			window['-OUT100-'].update(	calc.str_real_format(	calc.insert_result(	float( values['-IN100-']) * (1)	)))
	if values['-IN100-'] == '':
		window['-OUT100-'].update('R$ 0,00')

	# Incio da logica do campo de Resultado do Display de Moedas
	if event in ('-IN005-', '-IN010-', '-IN025-', '-IN050-', '-IN100-'):
		window['-DISPLAY_M-'].update( calc.str_real_format( calc.insert_result( calc.float_calc_format( values['-OUT005-']) + calc.float_calc_format( values['-OUT010-']) + calc.float_calc_format( values['-OUT025-']) + calc.float_calc_format( values['-OUT050-']) + calc.float_calc_format( values['-OUT100-']) )))
	


window.close()
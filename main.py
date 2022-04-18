
import PySimpleGUI as sg 
from module import calc


sg.theme('random')

valor = 'R$ 0,00'
a = valor
b = valor
c = valor
d = valor
e = valor

def real(x):
	return calc.str_real_format( calc.insert_result( x))

def soma(x):
	return calc.float_calc_format(x)

def main():
	
	# Inicio da tab de calculos de moedas

	layout_moedas = 	[	
							[sg.Text(valor, background_color='white', text_color='green', justification='r', expand_x=True, key='-DISPLAY_M-', font='_ 15')],
							[sg.Text('R$   0,05', background_color='white', text_color='green' ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.InputText('', justification='r', size=(10, 1),  expand_x=True, focus=True,  enable_events=True, key='-IN005-'), sg.Text('=', expand_x=True, justification='c'), sg.Text(valor, background_color='white', text_color='green', size=(20, 1), expand_x=True, justification='r', key='-OUT005-')],
							[sg.Text('R$   0,10', background_color='white', text_color='green' ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.InputText('', justification='r', size=(10, 1),  expand_x=True,  enable_events=True, key='-IN010-'), sg.Text('=', expand_x=True, justification='c'), sg.Text(valor, background_color='white', text_color='green', size=(20, 1), expand_x=True, justification='r',  key='-OUT010-')],
							[sg.Text('R$   0,25', background_color='white', text_color='green' ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.InputText('', justification='r', size=(10, 1),  expand_x=True, enable_events=True, key='-IN025-'), sg.Text('=', expand_x=True, justification='c'), sg.Text(valor, background_color='white', text_color='green', size=(20, 1), expand_x=True, justification='r',  key='-OUT025-')],
							[sg.Text('R$   0,50', background_color='white', text_color='green' ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.InputText('', justification='r', size=(10, 1),  expand_x=True, enable_events=True, key='-IN050-'), sg.Text('=', expand_x=True, justification='c'), sg.Text(valor, background_color='white', text_color='green', size=(20, 1), expand_x=True, justification='r',  key='-OUT050-')],
							[sg.Text('R$   1,00', background_color='white', text_color='green' ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.InputText('', justification='r', size=(10, 1),  expand_x=True, enable_events=True, key='-IN100-'), sg.Text('=', expand_x=True, justification='c'), sg.Text(valor, background_color='white', text_color='green', size=(20, 1), expand_x=True, justification='r',  key='-OUT100-')],

						]
	# fim da tab de calculos de moedas


	# Inicio da tab de calculos de cedulas

	layout_cedulas = [	
						[sg.Input(valor, background_color='white', text_color='green', justification='r', expand_x=True,  disabled=True, key='-DISPLAY_C-', font='_ 15')],
						[sg.Text('R$   2,00', background_color='white', text_color='green' ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.InputText('', justification='r', size=(10, 1),  expand_x=True, enable_events=True, key='-IN200-'), sg.Text('=', expand_x=True, justification='c'), sg.Input(valor, background_color='white', text_color='green', size=(15, 1), expand_x=True, justification='r', readonly=True, key='-OUT200-')],
						[sg.Text('R$   5,00', background_color='white', text_color='green' ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.InputText('', justification='r', size=(10, 1),  expand_x=True, enable_events=True, key='-IN500-'), sg.Text('=', expand_x=True, justification='c'), sg.Input(valor, background_color='white', text_color='green', size=(15, 1), expand_x=True, justification='r', readonly=True, key='-OUT500-')],
						[sg.Text('R$  10,00', background_color='white', text_color='green' ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.InputText('', justification='r', size=(10, 1),  expand_x=True, enable_events=True, key='-IN1000-'), sg.Text('=', expand_x=True, justification='c'), sg.Input(valor, background_color='white', text_color='green', size=(15, 1), expand_x=True, justification='r', readonly=True, key='-OUT1000-')],
						[sg.Text('R$  20,00', background_color='white', text_color='green' ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.InputText('', justification='r', size=(10, 1),  expand_x=True, enable_events=True, key='-IN2000-'), sg.Text('=', expand_x=True, justification='c'), sg.Input(valor, background_color='white', text_color='green', size=(15, 1), expand_x=True, justification='r', readonly=True, key='-OUT2000-')],
						[sg.Text('R$  50,00', background_color='white', text_color='green' ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.InputText('', justification='r', size=(10, 1),  expand_x=True, enable_events=True, key='-IN5000-'), sg.Text('=', expand_x=True, justification='c'), sg.Input(valor, background_color='white', text_color='green', size=(15, 1), expand_x=True, justification='r', readonly=True, key='-OUT5000-')],
						[sg.Text('R$ 100,00', background_color='white', text_color='green' ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.InputText('', justification='r', size=(10, 1),  expand_x=True, enable_events=True, key='-IN10000-'), sg.Text('=', expand_x=True, justification='c'), sg.Input(valor, background_color='white', text_color='green', size=(15, 1), expand_x=True, justification='r', readonly=True, key='-OUT10000-')],
						[sg.Text('R$ 200,00', background_color='white', text_color='green' ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.InputText('', justification='r', size=(10, 1),  expand_x=True, enable_events=True, key='-IN20000-'), sg.Text('=', expand_x=True, justification='c'), sg.Input(valor, background_color='white', text_color='green', size=(15, 1), expand_x=True, justification='r', readonly=True, key='-OUT20000-')]

						]

	# fim da tab de calculos de cedulas

	# Inicio da tab de calculos do PDV


	layout_recibos = [	[sg.Text('Recibos', background_color='white', text_color='green' ,justification='l', size=(15, 1), expand_x=True), sg.Input(valor, text_color='green', justification='r', disabled=True, size=(26, 1), expand_x=True)],
						[sg.Text('Venda avista', background_color='white', text_color='green' ,justification='l', size=(15, 1), expand_x=True), sg.Input(valor, text_color='green', justification='r', disabled=True, size=(26, 1), expand_x=True)],
						[sg.Text('Venda a prazo', background_color='white', text_color='green' ,justification='l', size=(15, 1), expand_x=True), sg.Input(valor, text_color='green', justification='r', disabled=True, size=(26, 1), expand_x=True)],
						[sg.Text('Cartão', background_color='white', text_color='green' ,justification='l', size=(15, 1), expand_x=True), sg.Input(valor, text_color='green', justification='r', disabled=True, size=(26, 1), expand_x=True)],
						[sg.Text('Carta crédito', background_color='white', text_color='green' ,justification='l', size=(15, 1), expand_x=True), sg.Input(valor, text_color='green', justification='r', disabled=True,size=(26, 1), expand_x=True)],
						[sg.Text( 'Total Recebido', size=(15, 1), expand_x=True), sg.Input(valor, text_color='green', justification='r', size=(26, 1), expand_x=True, disabled=True, )],
						[sg.Text( 'Total Dinheiro', size=(15, 1), expand_x=True), sg.Input(valor, text_color='green', justification='r', size=(26, 1), expand_x=True, disabled=True)]

					]
	layout_calc = [
						[sg.Text('Cédulas', background_color='white', text_color='green' ,justification='l', size=(15, 1), expand_x=True), sg.Input(valor, text_color='green', justification='r', disabled=True, size=(26, 1), expand_x=True)],
						[sg.Text('Moedas', background_color='white', text_color='green' ,justification='l', size=(15, 1), expand_x=True), sg.Input(valor, text_color='green', justification='r', disabled=True, size=(26, 1), expand_x=True)],
						[sg.Text('Despesas', background_color='white', text_color='green' ,justification='l', size=(15, 1), expand_x=True), sg.Input(valor, text_color='green', justification='r', disabled=True, size=(26, 1), expand_x=True)],
						[sg.Text('Saidas', background_color='white', text_color='green' ,justification='l', size=(15, 1), expand_x=True), sg.Input(valor, text_color='green', justification='r', disabled=True, size=(26, 1), expand_x=True)],
						[sg.Text('Trocados', background_color='white', text_color='green' ,justification='l', size=(15, 1), expand_x=True), sg.Input(valor, text_color='green', justification='r', disabled=True, size=(26, 1), expand_x=True)],
						[sg.Text( 'Total Recebido', size=(15, 1), expand_x=True), sg.Input(valor, text_color='green', justification='r', disabled=True, size=(26, 1), expand_x=True)],
						[sg.Text( 'Total Dinheiro', size=(15, 1), expand_x=True), sg.Input(valor, text_color='green', justification='r', disabled=True, size=(26, 1), expand_x=True)],
						[sg.Input(valor, background_color='white', text_color='green', justification='r', expand_x=True,  disabled=True, key='-DISPLAY_C-', font='_ 15')],
						[sg.Button('Imprimir', size=(7, 1), expand_x=True), sg.Button('Vizualizar', size=(7, 1), expand_x=True), sg.Button('Salvar', size=(7, 1), expand_x=True)]	]

	# Fim da tab de calculos do PDV




	layout_tab_group = [	[	sg.Tab('Moedas', layout_moedas), 
								sg.Tab('Cédulas', layout_cedulas),
								sg.Tab('Recibos', layout_recibos),
								sg.Tab('Calculos PDV', layout_calc)	]]




	layout_menu = [	['Arquivo', ['Abrir','Salvar', 'Configs', 'Sair']],
					['Temas', sg.theme()],
					['Calculadora'],
					['Sobre']	]




	layout = [ 	[sg.Menu(layout_menu)],
				[sg.TabGroup(layout_tab_group, expand_x=True, expand_y=True)],
				[sg.Text('Adm', background_color='white', text_color='green' ,justification='c', size=(5, 1), expand_x=False), sg.Text('Gerente', background_color='white', text_color='green' ,justification='c', size=(10, 1), expand_x=True), sg.Text('Leonardo', background_color='white', text_color='green' ,justification='c', size=(20, 1), expand_x=True)]
				] 

	return sg.Window('Terminal: Adm | Usuário: Leonardo', size=(350,320), resizable=False, layout=layout, use_default_focus=False) 

window = main()

while True: 


# Event Loop 
	event, values = window.read() 

	if event in (None, 'Sair'): 
		break
# somente numeros nos inputs

	if len(values[event]) and values[event][-1] not in ('0123456789'):
		window[event].update(values[event][:-1])

# Eventos da tab 01

	# Incio da logica do campo de R$ 0,05
	if event == '-IN005-' and len(values['-IN005-']) and values['-IN005-'][-1] in ('0123456789'):	
		if (len(values['-IN005-']) > 7):
			window['-IN005-'].update(values['-IN005-'][:-1])
		if (len(values['-IN005-']) < 8):	
			a = calc.str_real_format( calc.insert_result(	float( values['-IN005-']) * (0.05)	) )
			window['-OUT005-'].update( a )
			window['-DISPLAY_M-'].update( real( soma(a) + soma(b) + soma(c) + soma(d) + soma(e) ))
	if event == '-IN005-' and values[event] == '':
		window['-DISPLAY_M-'].update( real( soma( window['-DISPLAY_M-'].get() ) - soma( window['-OUT005-'].get() ) ))
		a = valor
		window['-OUT005-'].update(valor)

	# Incio da logica do campo de R$ 0,10	
	if event == '-IN010-' and len(values['-IN010-']) and values['-IN010-'][-1] in ('0123456789'):
		if (len(values['-IN010-']) > 7):
			window['-IN010-'].update(values['-IN010-'][:-1])
		if (len(values['-IN010-']) < 8):	
			b = calc.str_real_format( calc.insert_result(	float( values['-IN010-']) * (0.10)	))
			window['-OUT010-'].update( b )
			window['-DISPLAY_M-'].update( real( soma(a) + soma(b) + soma(c) + soma(d) + soma(e) ))
	if event == '-IN010-' and values[event] == '':
		window['-DISPLAY_M-'].update( real( soma( window['-DISPLAY_M-'].get() ) - soma( window['-OUT010-'].get() ) ))
		b = valor
		window['-OUT010-'].update(valor)
		
	# Incio da logica do campo de R$ 0,25	
	if event == '-IN025-' and len(values['-IN025-']) and values['-IN025-'][-1] in ('0123456789'):
		if (len(values['-IN025-']) > 7):
			window['-IN025-'].update(values['-IN025-'][:-1])
		if (len(values['-IN025-']) < 8):	
			c = calc.str_real_format( calc.insert_result(	float( values['-IN025-']) * (0.25)	) )
			window['-OUT025-'].update( c )
			window['-DISPLAY_M-'].update( real( soma(a) + soma(b) + soma(c) + soma(d) + soma(e) ))
	if event == '-IN025-' and values[event] == '':
		window['-DISPLAY_M-'].update( real( soma( window['-DISPLAY_M-'].get() ) - soma( window['-OUT025-'].get() ) ))
		c = valor
		window['-OUT025-'].update(valor)

	# Incio da logica do campo de R$ 0,50	
	if event == '-IN050-' and len(values['-IN050-']) and values['-IN050-'][-1] in ('0123456789'):
		if (len(values['-IN050-']) > 7):
			window['-IN050-'].update(values['-IN050-'][:-1])
		if (len(values['-IN050-']) < 8):	
			d = calc.str_real_format( calc.insert_result(	float( values['-IN050-']) * (0.50)	) )
			window['-OUT050-'].update( d )
			window['-DISPLAY_M-'].update( real( soma(a) + soma(b) + soma(c) + soma(d) + soma(e) ))
	if event == '-IN050-' and values[event] == '':
		window['-DISPLAY_M-'].update( real( soma( window['-DISPLAY_M-'].get() ) - soma( window['-OUT050-'].get() ) ))
		d = valor
		window['-OUT050-'].update(valor)

	# Incio da logica do campo de R$ 1,00	
	if event == '-IN100-' and len(values['-IN100-']) and values['-IN100-'][-1] in ('0123456789'):
		if (len(values['-IN100-']) > 7):
			window['-IN100-'].update(values['-IN100-'][:-1])
		if (len(values['-IN100-']) < 8):	
			e = calc.str_real_format( calc.insert_result(	float( values['-IN100-']) * (1.00)	) )
			window['-OUT100-'].update( e )
			window['-DISPLAY_M-'].update( real( soma(a) + soma(b) + soma(c) + soma(d) + soma(e) ))
	if event == '-IN100-' and values[event] == '':
		window['-DISPLAY_M-'].update( real( soma( window['-DISPLAY_M-'].get() ) - soma( window['-OUT100-'].get() ) ))
		e = valor
		window['-OUT100-'].update(valor)


window.close(); del window
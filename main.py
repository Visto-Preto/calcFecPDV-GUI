
import PySimpleGUI as sg 
from module import calc
from module.realsymbol import Real as rs


sg.theme('random')

valor = ' R$ 0,00'
a = valor
b = valor
c = valor
d = valor
e = valor
f = valor
g = valor
h = valor
i = valor
j = valor
k = valor
l = valor

rec = valor
vda = valor
vdap = valor
ca = valor
cac = valor

def real(x):
	return calc.str_real_format( calc.insert_result( x))

def soma(x):
	return calc.float_calc_format(x)

def main():
	
	# Inicio da tab de calculos de moedas
	layout_moedas = 	[	
							[sg.Text(valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', expand_x=True, key='-DISPLAY_M-', font='_ 15')],
							[ sg.HorizontalSeparator()],
							[sg.Text('R$   0,05', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.Input('', justification='r', size=(10, 1),  expand_x=True, focus=True,  enable_events=True, key='-IN005-'), sg.Text('=', expand_x=True, justification='c'), sg.Text(valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), size=(20, 1), expand_x=True, justification='r', key='-OUT005-')],
							[sg.Text('R$   0,10', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.Input('', justification='r', size=(10, 1),  expand_x=True,  enable_events=True, key='-IN010-'), sg.Text('=', expand_x=True, justification='c'), sg.Text(valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), size=(20, 1), expand_x=True, justification='r',  key='-OUT010-')],
							[sg.Text('R$   0,25', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.Input('', justification='r', size=(10, 1),  expand_x=True, enable_events=True, key='-IN025-'), sg.Text('=', expand_x=True, justification='c'), sg.Text(valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), size=(20, 1), expand_x=True, justification='r',  key='-OUT025-')],
							[sg.Text('R$   0,50', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.Input('', justification='r', size=(10, 1),  expand_x=True, enable_events=True, key='-IN050-'), sg.Text('=', expand_x=True, justification='c'), sg.Text(valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), size=(20, 1), expand_x=True, justification='r',  key='-OUT050-')],
							[sg.Text('R$   1,00', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.Input('', justification='r', size=(10, 1),  expand_x=True, enable_events=True, key='-IN100-'), sg.Text('=', expand_x=True, justification='c'), sg.Text(valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), size=(20, 1), expand_x=True, justification='r',  key='-OUT100-')],

						]

	# Inicio da tab de calculos de cedulas
	layout_cedulas = [	
						[sg.Text(valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', expand_x=True, key='-DISPLAY_C-', font='_ 15')],
						[ sg.HorizontalSeparator()],
						[sg.Text('R$   2,00', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.Input('', justification='r', size=(10, 1),  expand_x=True, enable_events=True, key='-IN200-'), sg.Text('=', expand_x=True, justification='c'), sg.Text(valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), size=(15, 1), expand_x=True, justification='r', key='-OUT200-')],
						[sg.Text('R$   5,00', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.Input('', justification='r', size=(10, 1),  expand_x=True, enable_events=True, key='-IN500-'), sg.Text('=', expand_x=True, justification='c'), sg.Text(valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), size=(15, 1), expand_x=True, justification='r', key='-OUT500-')],
						[sg.Text('R$  10,00', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.Input('', justification='r', size=(10, 1),  expand_x=True, enable_events=True, key='-IN1000-'), sg.Text('=', expand_x=True, justification='c'), sg.Text(valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), size=(15, 1), expand_x=True, justification='r', key='-OUT1000-')],
						[sg.Text('R$  20,00', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.Input('', justification='r', size=(10, 1),  expand_x=True, enable_events=True, key='-IN2000-'), sg.Text('=', expand_x=True, justification='c'), sg.Text(valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), size=(15, 1), expand_x=True, justification='r', key='-OUT2000-')],
						[sg.Text('R$  50,00', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.Input('', justification='r', size=(10, 1),  expand_x=True, enable_events=True, key='-IN5000-'), sg.Text('=', expand_x=True, justification='c'), sg.Text(valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), size=(15, 1), expand_x=True, justification='r', key='-OUT5000-')],
						[sg.Text('R$ 100,00', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.Input('', justification='r', size=(10, 1),  expand_x=True, enable_events=True, key='-IN10000-'), sg.Text('=', expand_x=True, justification='c'), sg.Text(valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), size=(15, 1), expand_x=True, justification='r', key='-OUT10000-')],
						[sg.Text('R$ 200,00', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.Input('', justification='r', size=(10, 1),  expand_x=True, enable_events=True, key='-IN20000-'), sg.Text('=', expand_x=True, justification='c'), sg.Text(valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), size=(15, 1), expand_x=True, justification='r', key='-OUT20000-')]

						]

	# Inicio da tab de calculos dos Recibos
	layout_recibos = [	[sg.Text('Recibos', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='l', size=(15, 1), expand_x=True), sg.Input('', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', size=(26, 1), expand_x=True, enable_events=True, key='-REC-' )],
						[sg.Text('Venda avista', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='l', size=(15, 1), expand_x=True), sg.Input('', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', size=(26, 1), expand_x=True, enable_events=True, key='-VDA-' )],
						[sg.Text('Venda a prazo', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='l', size=(15, 1), expand_x=True), sg.Input('', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r',size=(26, 1), expand_x=True, enable_events=True, key='-VDAP-' )],
						[sg.Text('Cartão', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='l', size=(15, 1), expand_x=True), sg.Input('', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', size=(26, 1), expand_x=True, enable_events=True, key='-CA-' )],
						[sg.Text('Carta crédito', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='l', size=(15, 1), expand_x=True), sg.Input('', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', size=(26, 1), expand_x=True, enable_events=True, key='-CAC-' )],
						[ sg.HorizontalSeparator()],
						[sg.Text( 'Total Recebido', size=(15, 1), expand_x=True), sg.Text(valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', size=(26, 1), expand_x=True, key='-DIS_TR-')],
						[sg.Text( 'Total Dinheiro', size=(15, 1), expand_x=True), sg.Text(valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', size=(26, 1), expand_x=True, key='-DIS_TD-')]
						]
	
	# Inicio da tab de calculos do PDV
	layout_calc = [
						[sg.Text('Moedas', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='l', size=(15, 1), expand_x=True), sg.Input(valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', size=(26, 1), expand_x=True)],
						[sg.Text('Cédulas', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='l', size=(15, 1), expand_x=True), sg.Input(valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', size=(26, 1), expand_x=True)],
						[sg.Text('Despesas', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='l', size=(15, 1), expand_x=True), sg.Input(valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', size=(26, 1), expand_x=True)],
						[sg.Text('Saidas', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='l', size=(15, 1), expand_x=True), sg.Input(valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', size=(26, 1), expand_x=True)],
						[sg.Text('Trocados', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='l', size=(15, 1), expand_x=True), sg.Input(valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r',  size=(26, 1), expand_x=True)],
						[ sg.HorizontalSeparator()],
						[sg.Text( 'Total Recebido', size=(15, 1), expand_x=True), sg.Text(valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', size=(26, 1), expand_x=True)],
						[sg.Text( 'Total Dinheiro', size=(15, 1), expand_x=True), sg.Text(valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', size=(26, 1), expand_x=True)],
						[ sg.HorizontalSeparator()],
						[sg.Text(valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', expand_x=True, key='-DISPLAY_C-', font='_ 15')],
						[sg.Button('Imprimir', size=(7, 1), expand_x=True), sg.Button('Vizualizar', size=(7, 1), expand_x=True), sg.Button('Salvar', size=(7, 1), expand_x=True)]	]


	layout_tab_group = [	[	sg.Tab('Moedas', layout_moedas), 
								sg.Tab('Cédulas', layout_cedulas),
								sg.Tab('Recibos', layout_recibos),
								sg.Tab('Calculos PDV', layout_calc)	]]


	layout_menu = [	['Arquivo', ['Abrir','Salvar', 'Configs', 'Sair']],
					['Temas', sg.theme_list()],
					['Calculadora'],
					['Sobre']	]


	layout = [ 	[sg.Menu(layout_menu)],
				[sg.TabGroup(layout_tab_group, expand_x=True, expand_y=True)],
				[sg.StatusBar('Adm', justification='c', size=(5, 1), expand_x=False), sg.StatusBar('Gerente', justification='c', size=(10, 1), expand_x=True), sg.StatusBar('Leonardo', justification='c', size=(20, 1), expand_x=True)]
				] 

	return sg.Window('Terminal: Adm | Usuário: Leonardo', size=(350,335), resizable=False, layout=layout, use_default_focus=False, return_keyboard_events=False) 

window = main()

while True: 

	# Event Loop 
	event, values = window.read() 

	print(event)
	if event in (None, 'Sair'): 
		break

	# Eventos da tab 01
	# Incio da logica do campo de R$ 0,05
	if event == '-IN005-' and len(values['-IN005-']) and values['-IN005-'][-1] not in ('0123456789'):
		window['-IN005-'].update(values['-IN005-'][:-1])
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
	if event == '-IN010-' and len(values['-IN010-']) and values['-IN010-'][-1] not in ('0123456789'):
		window['-IN010-'].update(values['-IN010-'][:-1])	
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
	if event == '-IN025-' and len(values['-IN025-']) and values['-IN025-'][-1] not in ('0123456789'):
		window['-IN025-'].update(values['-IN025-'][:-1])
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
	if event == '-IN050-' and len(values['-IN050-']) and values['-IN050-'][-1] not in ('0123456789'):
		window['-IN050-'].update(values['-IN050-'][:-1])
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
	if event == '-IN100-' and len(values['-IN100-']) and values['-IN100-'][-1] not in ('0123456789'):
		window['-IN100-'].update(values['-IN100-'][:-1])
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

	# Eventos da tab 02
	# Incio da logica do campo de R$ 2,00	
	if event == '-IN200-' and len(values['-IN200-']) and values['-IN200-'][-1] not in ('0123456789'):
		window['-IN200-'].update(values['-IN200-'][:-1])
	if event == '-IN200-' and len(values['-IN200-']) and values['-IN200-'][-1] in ('0123456789'):
		if (len(values['-IN200-']) > 6):
			window['-IN200-'].update(values['-IN200-'][:-1])
		if (len(values['-IN200-']) < 7):	
			f = calc.str_real_format( calc.insert_result(	float( values['-IN200-']) * (2.00)	) )
			window['-OUT200-'].update( f )
			window['-DISPLAY_C-'].update( real( soma(f) + soma(g) + soma(h) + soma(i) + soma(j) + soma(k) + soma(l) ))
	if event == '-IN200-' and values[event] == '':
		window['-DISPLAY_C-'].update( real( soma( window['-DISPLAY_C-'].get() ) - soma( window['-OUT200-'].get() ) ))
		f = valor
		window['-OUT200-'].update(valor)

	# Incio da logica do campo de R$ 5,00	
	if event == '-IN500-' and len(values['-IN500-']) and values['-IN500-'][-1] not in ('0123456789'):
		window['-IN500-'].update(values['-IN500-'][:-1])
	if event == '-IN500-' and len(values['-IN500-']) and values['-IN500-'][-1] in ('0123456789'):
		if (len(values['-IN500-']) > 6):
			window['-IN500-'].update(values['-IN500-'][:-1])
		if (len(values['-IN500-']) < 7):	
			g = calc.str_real_format( calc.insert_result(	float( values['-IN500-']) * (5.00)	) )
			window['-OUT500-'].update( g )
			window['-DISPLAY_C-'].update( real( soma(f) + soma(g) + soma(h) + soma(i) + soma(j) + soma(k) + soma(l) ))
	if event == '-IN500-' and values[event] == '':
		window['-DISPLAY_C-'].update( real( soma( window['-DISPLAY_C-'].get() ) - soma( window['-OUT500-'].get() ) ))
		g = valor
		window['-OUT500-'].update(valor)

	# Incio da logica do campo de R$ 10,00	
	if event == '-IN1000-' and len(values['-IN1000-']) and values['-IN1000-'][-1] not in ('0123456789'):
		window['-IN1000-'].update(values['-IN1000-'][:-1])
	if event == '-IN1000-' and len(values['-IN1000-']) and values['-IN1000-'][-1] in ('0123456789'):
		if (len(values['-IN1000-']) > 6):
			window['-IN1000-'].update(values['-IN1000-'][:-1])
		if (len(values['-IN1000-']) < 7):	
			h = calc.str_real_format( calc.insert_result(	float( values['-IN1000-']) * (10.00)	) )
			window['-OUT1000-'].update( h )
			window['-DISPLAY_C-'].update( real( soma(f) + soma(g) + soma(h) + soma(i) + soma(j) + soma(k) + soma(l) ))
	if event == '-IN1000-' and values[event] == '':
		window['-DISPLAY_C-'].update( real( soma( window['-DISPLAY_C-'].get() ) - soma( window['-OUT1000-'].get() ) ))
		h = valor
		window['-OUT1000-'].update(valor)

	# Incio da logica do campo de R$ 20,00	
	if event == '-IN2000-' and len(values['-IN2000-']) and values['-IN2000-'][-1] not in ('0123456789'):
		window['-IN2000-'].update(values['-IN2000-'][:-1])
	if event == '-IN2000-' and len(values['-IN2000-']) and values['-IN2000-'][-1] in ('0123456789'):
		if (len(values['-IN2000-']) > 5):
			window['-IN2000-'].update(values['-IN2000-'][:-1])
		if (len(values['-IN2000-']) < 6):	
			i = calc.str_real_format( calc.insert_result(	float( values['-IN2000-']) * (20.00)	) )
			window['-OUT2000-'].update( i )
			window['-DISPLAY_C-'].update( real( soma(f) + soma(g) + soma(h) + soma(i) + soma(j) + soma(k) + soma(l) ))
	if event == '-IN2000-' and values[event] == '':
		window['-DISPLAY_C-'].update( real( soma( window['-DISPLAY_C-'].get() ) - soma( window['-OUT2000-'].get() ) ))
		i = valor
		window['-OUT2000-'].update(valor)

	# Incio da logica do campo de R$ 50,00	
	if event == '-IN5000-' and len(values['-IN5000-']) and values['-IN5000-'][-1] not in ('0123456789'):
		window['-IN5000-'].update(values['-IN5000-'][:-1])
	if event == '-IN5000-' and len(values['-IN5000-']) and values['-IN5000-'][-1] in ('0123456789'):
		if (len(values['-IN5000-']) > 5):
			window['-IN5000-'].update(values['-IN5000-'][:-1])
		if (len(values['-IN5000-']) < 6):	
			j = calc.str_real_format( calc.insert_result(	float( values['-IN5000-']) * (50.00)	) )
			window['-OUT5000-'].update( j )
			window['-DISPLAY_C-'].update( real( soma(f) + soma(g) + soma(h) + soma(i) + soma(j) + soma(k) + soma(l) ))
	if event == '-IN5000-' and values[event] == '':
		window['-DISPLAY_C-'].update( real( soma( window['-DISPLAY_C-'].get() ) - soma( window['-OUT5000-'].get() ) ))
		j = valor
		window['-OUT5000-'].update(valor)

	# Incio da logica do campo de R$ 100,00	
	if event == '-IN10000-' and len(values['-IN10000-']) and values['-IN10000-'][-1] not in ('0123456789'):
		window['-IN10000-'].update(values['-IN10000-'][:-1])
	if event == '-IN10000-' and len(values['-IN10000-']) and values['-IN10000-'][-1] in ('0123456789'):
		if (len(values['-IN10000-']) > 5):
			window['-IN10000-'].update(values['-IN10000-'][:-1])
		if (len(values['-IN10000-']) < 6):	
			k = calc.str_real_format( calc.insert_result(	float( values['-IN10000-']) * (100.00)	) )
			window['-OUT10000-'].update( k )
			window['-DISPLAY_C-'].update( real( soma(f) + soma(g) + soma(h) + soma(i) + soma(j) + soma(k) + soma(l) ))
	if event == '-IN10000-' and values[event] == '':
		window['-DISPLAY_C-'].update( real( soma( window['-DISPLAY_C-'].get() ) - soma( window['-OUT10000-'].get() ) ))
		k = valor
		window['-OUT10000-'].update(valor)

	# Incio da logica do campo de R$ 200,00	
	if event == '-IN20000-' and len(values['-IN20000-']) and values['-IN20000-'][-1] not in ('0123456789'):
		window['-IN20000-'].update(values['-IN20000-'][:-1])
	if event == '-IN20000-' and len(values['-IN20000-']) and values['-IN20000-'][-1] in ('0123456789'):
		if (len(values['-IN20000-']) > 4):
			window['-IN20000-'].update(values['-IN20000-'][:-1])
		if (len(values['-IN20000-']) < 5):	
			l = calc.str_real_format( calc.insert_result(	float( values['-IN20000-']) * (200.00)	) )
			window['-OUT20000-'].update( l )
			window['-DISPLAY_C-'].update( real( soma(f) + soma(g) + soma(h) + soma(i) + soma(j) + soma(k) + soma(l) ))
	if event == '-IN20000-' and values[event] == '':
		window['-DISPLAY_C-'].update( real( soma( window['-DISPLAY_C-'].get() ) - soma( window['-OUT20000-'].get() ) ))
		l = valor
		window['-OUT20000-'].update(valor)

	# Eventos da tab 03
	# Eventos do campo de recibos
	if event == '-REC-' and len(values['-REC-']) and values['-REC-'][-1] not in ('0123456789'):
		window['-REC-'].update(values['-REC-'][:-1])
	if event == '-REC-' and len(values['-REC-']) and values['-REC-'][-1] in ('0123456789'):
		if (len(values['-REC-']) > 19): # limite maximo de caracter 12
			window['-REC-'].update(values['-REC-'][:-1])
		if (len(values['-REC-']) < 20): #
			if len(values['-REC-']) == 1:
				rec = int( values['-REC-'] )
				window['-REC-'].update( rs.float_to_s(rec) )
			else:
				rec = values['-REC-']
				window['-REC-'].update( rs.del_caracter(rec) )

	# Eventos do campo de venda avista
	if event == '-VDA-' and len(values['-VDA-']) and values['-VDA-'][-1] not in ('0123456789'):
		window['-VDA-'].update(values['-VDA-'][:-1])
	if event == '-VDA-' and len(values['-VDA-']) and values['-VDA-'][-1] in ('0123456789'):
		if (len(values['-VDA-']) > 19): # limite maximo de caracter 12
			window['-VDA-'].update(values['-VDA-'][:-1])
		if (len(values['-VDA-']) < 20): #
			if len(values['-VDA-']) == 1:
				vda = int( values['-VDA-'] )
				window['-VDA-'].update( rs.float_to_s(vda) )
			else:
				vda = values['-VDA-']
				window['-VDA-'].update( rs.del_caracter(vda) )

	# Eventos do campo de venda a prazo
	if event == '-VDAP-' and len(values['-VDAP-']) and values['-VDAP-'][-1] not in ('0123456789'):
		window['-VDAP-'].update(values['-VDAP-'][:-1])
	if event == '-VDAP-' and len(values['-VDAP-']) and values['-VDAP-'][-1] in ('0123456789'):
		if (len(values['-VDAP-']) > 19): # limite maximo de caracter 12
			window['-VDAP-'].update(values['-VDAP-'][:-1])
		if (len(values['-VDAP-']) < 20): #
			if len(values['-VDAP-']) == 1:
				vdap = int( values['-VDAP-'] )
				window['-VDAP-'].update( rs.float_to_s(vdap) )
			else:
				vdap = values['-VDAP-']
				window['-VDAP-'].update( rs.del_caracter(vdap) )				

	# Eventos do campo de cartao de credito
	if event == '-CA-' and len(values['-CA-']) and values['-CA-'][-1] not in ('0123456789'):
		window['-CA-'].update(values['-CA-'][:-1])
	if event == '-CA-' and len(values['-CA-']) and values['-CA-'][-1] in ('0123456789'):
		if (len(values['-CA-']) > 19): # limite maximo de caracter 12
			window['-CA-'].update(values['-CA-'][:-1])
		if (len(values['-CA-']) < 20): #
			if len(values['-CA-']) == 1:
				ca = int( values['-CA-'] )
				window['-CA-'].update( rs.float_to_s(ca) )
			else:
				ca = values['-CA-']
				window['-CA-'].update( rs.del_caracter(ca) )	

	# Eventos do campo de carta credito
	if event == '-CAC-' and len(values['-CAC-']) and values['-CAC-'][-1] not in ('0123456789'):
		window['-CAC-'].update(values['-CAC-'][:-1])
	if event == '-CAC-' and len(values['-CAC-']) and values['-CAC-'][-1] in ('0123456789'):
		if (len(values['-CAC-']) > 19): # limite maximo de caracter 12
			window['-CAC-'].update(values['-CAC-'][:-1])
		if (len(values['-CAC-']) < 20): #
			if len(values['-CAC-']) == 1:
				cac = int( values['-CAC-'] )
				window['-CAC-'].update( rs.float_to_s(cac) )
			else:
				cac = values['-CAC-']
				window['-CAC-'].update( rs.del_caracter(cac) )	

	# display somas dos recibos		
	if type(rec) == int or type(vda) == int or type(vdap) == int or type(ca) == int or type(cac) == int :

		if type(rec) == int:
			rec = rs.float_to_s(rec)# int
		else:
			rec = rs.del_caracter(rec)# float

		if type(vda) == int:
			vda = rs.float_to_s(vda)# int
		else:
			vda = rs.del_caracter(vda)# float

		if type(vdap) == int:
			vdap = rs.float_to_s(vdap)# int
		else:
			vdap = rs.del_caracter(vdap)# float


		if type(ca) == int:
			ca = rs.float_to_s(ca)# int
		else:
			ca = rs.del_caracter(ca)# float

		if type(cac) == int:
			cac = rs.float_to_s(cac)# int
		else:
			cac = rs.del_caracter(cac)# float


		dstr = ( rs.string_to_f(rec) + rs.string_to_f(vda) + rs.string_to_f(vdap) )
		dstr = rs.float_to_s(dstr) 

		dstd = ( (rs.string_to_f(rec) + rs.string_to_f(vda) + rs.string_to_f(vdap) ) - (rs.string_to_f(ca) + rs.string_to_f(cac) ) )
		dstd = rs.float_to_s(dstd) 


		window['-DIS_TR-'].update( dstr )
		window['-DIS_TD-'].update( dstd )
	else:
		rec = rs.del_caracter(rec)# float
		vda = rs.del_caracter(vda)# float
		vdap = rs.del_caracter(vdap)# float
		ca = rs.del_caracter(ca)# float
		cac = rs.del_caracter(cac)# float

		dstr = ( rs.string_to_f(rec) + rs.string_to_f(vda) + rs.string_to_f(vdap))
		dstr = rs.float_to_s(dstr) 

		dstd = ( (rs.string_to_f(rec) + rs.string_to_f(vda) + rs.string_to_f(vdap) ) - (rs.string_to_f(ca) + rs.string_to_f(cac) ) )
		dstd = rs.float_to_s(dstd) 

		window['-DIS_TR-'].update( dstr )
		window['-DIS_TD-'].update( dstd )

window.close(); del window

from unittest import TextTestRunner
import PySimpleGUI as sg 
from module import calc

sg.theme('random')

valor = 'R$ 0,00'
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

def real(x):
	return calc.str_real_format( calc.insert_result( x))

def soma(x):
	return calc.float_calc_format(x)

def MyI(key): return sg.Input('', justification='r', size=(10, 1),  expand_x=True, key=key)

def MyT(key): return sg.Text(valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), size=(20, 1), expand_x=True, justification='r', key=key)

def next_element(key):
	if key <= 15:
		if key < 15:
			next_elem = window[key+1]
			next_elem.set_focus()
		else:
			window[11].set_focus()
	elif key >= 16:
		if key < 22:
			next_elem = window[key+1]
			next_elem.set_focus()
		else:
			window[16].set_focus()

def main():
	
	# Inicio da tab de calculos de moedas
	layout_moedas = 	[	
							[sg.Text(valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', expand_x=True, key='-DISPLAY_M-', font='_ 15')],
							[ sg.HorizontalSeparator()],
							[sg.Text('R$   0,05', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.Input('', justification='r', size=(10, 1),  expand_x=True, focus=True,key=11), sg.Text('=', expand_x=True, justification='c'), MyT(111) ],
							[sg.Text('R$   0,10', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), MyI(12), sg.Text('=', expand_x=True, justification='c'), MyT(112) ],
							[sg.Text('R$   0,25', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), MyI(13), sg.Text('=', expand_x=True, justification='c') , MyT(113) ],
							[sg.Text('R$   0,50', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), MyI(14), sg.Text('=', expand_x=True, justification='c') , MyT(114) ],
							[sg.Text('R$   1,00', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), MyI(15), sg.Text('=', expand_x=True, justification='c') , MyT(115) ],

						]

	# Inicio da tab de calculos de cedulas
	layout_cedulas = [	
						[sg.Text(valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', expand_x=True, key='-DISPLAY_C-', font='_ 15')],
						[ sg.HorizontalSeparator()],
						[sg.Text('R$   2,00', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), MyI(16), sg.Text('=', expand_x=True, justification='c'), MyT(116)],
						[sg.Text('R$   5,00', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), MyI(17), sg.Text('=', expand_x=True, justification='c') ,MyT(117)],
						[sg.Text('R$  10,00', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), MyI(18), sg.Text('=', expand_x=True, justification='c'),MyT(118)],
						[sg.Text('R$  20,00', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), MyI(19), sg.Text('=', expand_x=True, justification='c') ,MyT(119)],
						[sg.Text('R$  50,00', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), MyI(20), sg.Text('=', expand_x=True, justification='c'),MyT(120)],
						[sg.Text('R$ 100,00', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), MyI(21), sg.Text('=', expand_x=True, justification='c') ,MyT(121)],
						[sg.Text('R$ 200,00', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), MyI(22), sg.Text('=', expand_x=True, justification='c') ,MyT(122)]

						]

	# Inicio da tab de calculos dos Recibos
	layout_recibos = [	[sg.Text('Recibos', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='l', size=(15, 1), expand_x=True), sg.Input('', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', size=(26, 1), expand_x=True, enable_events=True, key='-REC-' )],
						[sg.Text('Venda avista', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='l', size=(15, 1), expand_x=True), sg.Input('', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', size=(26, 1), expand_x=True)],
						[sg.Text('Venda a prazo', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='l', size=(15, 1), expand_x=True), sg.Input('', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r',size=(26, 1), expand_x=True)],
						[sg.Text('Cartão', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='l', size=(15, 1), expand_x=True), sg.Input(' ', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', size=(26, 1), expand_x=True)],
						[sg.Text('Carta crédito', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='l', size=(15, 1), expand_x=True), sg.Input('', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', size=(26, 1), expand_x=True)],
						[ sg.HorizontalSeparator()],
						[sg.Text( 'Total Recebido', size=(15, 1), expand_x=True), sg.Text(valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', size=(26, 1), expand_x=True)],
						[sg.Text( 'Total Dinheiro', size=(15, 1), expand_x=True), sg.Text(valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', size=(26, 1), expand_x=True)]
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

	return sg.Window('Terminal: Adm | Usuário: Leonardo', size=(350,335), resizable=False, layout=layout, use_default_focus=False, return_keyboard_events=True) 

window = main()

while True: 
	
	# Event Loop 
	event, values = window.read()
	if event in (None, 'Sair'):
		break

	elem = window.find_element_with_focus()
	if elem is not None and len(elem.get()):
		if elem.get()[-1] not in ('0123456789'):
			elem.update(	elem.get()[:-1] ) 

	if event in ('0123456789\r') or event ==  'BackSpace:8' :
		if elem is not None:
			key = elem.Key

			keyout = (key + 100)

			if (len( elem.get() ) > 7):
				elem.update(	elem.get()[:-1] )
			elif len( elem.get() ) in range(1, 8):

				if key <= 15:
				
					if key == 11:
						moeda = 0.05
						a = calc.str_real_format( calc.insert_result(	float( values[key]) * moeda	) )
						window[keyout].update( a )
					elif key == 12:
						moeda = 0.10
						b = calc.str_real_format( calc.insert_result(	float( values[key]) * moeda	) )
						window[keyout].update( b )
					elif key == 13:
						moeda = 0.25
						c = calc.str_real_format( calc.insert_result(	float( values[key]) * moeda	) )
						window[keyout].update( c )
					elif key == 14:
						moeda = 0.50
						d = calc.str_real_format( calc.insert_result(	float( values[key]) * moeda	) )
						window[keyout].update( d )
					elif key == 15:
						moeda = 1.00
						e = calc.str_real_format( calc.insert_result(	float( values[key]) * moeda	) )
						window[keyout].update( e )
						
					window['-DISPLAY_M-'].update( real( soma(a) + soma(b) + soma(c) + soma(d) + soma(e) ))
					
					if event == '\r':
						next_element(key)

				elif key >= 16:
					if key == 16:
						moeda = 2.00
						f = calc.str_real_format( calc.insert_result(	float( values[key]) * moeda	) )
						window[keyout].update( f )
					elif key == 17:
						moeda = 5.00
						g = calc.str_real_format( calc.insert_result(	float( values[key]) * moeda	) )
						window[keyout].update( g )
					elif key == 18:
						moeda = 10.00
						h = calc.str_real_format( calc.insert_result(	float( values[key]) * moeda	) )
						window[keyout].update( h )
					elif key == 19:
						moeda = 20.00
						i = calc.str_real_format( calc.insert_result(	float( values[key]) * moeda	) )
						window[keyout].update( i )
					elif key == 20:
						moeda = 50.00
						j = calc.str_real_format( calc.insert_result(	float( values[key]) * moeda	) )
						window[keyout].update( j )
					elif key == 21:
						moeda = 100.00
						k = calc.str_real_format( calc.insert_result(	float( values[key]) * moeda	) )
						window[keyout].update( k )
					elif key == 22:
						moeda = 200.00
						l = calc.str_real_format( calc.insert_result(	float( values[key]) * moeda	) )
						window[keyout].update( l )						

					window['-DISPLAY_C-'].update( real( soma(f) + soma(g) + soma(h) + soma(i) + soma(j) + soma(k) + soma(l) ))

					if event == '\r':
						next_element(key)

			elif elem.get() == '':

				if key <= 15:
					window['-DISPLAY_M-'].update( real( soma( window['-DISPLAY_M-'].get() ) - soma( window[keyout].get() ) ))

					if key == 11:
						a = valor
						window[keyout].update(valor)
					elif key == 12:
						b = valor
						window[keyout].update(valor)
					elif key == 13:
						c = valor
						window[keyout].update(valor)
					elif key == 14:
						e = valor
						window[keyout].update(valor)
					elif key == 15:
						e = valor
						window[keyout].update(valor)

					if event == '\r':
						next_element(key)

				elif key > 16:
					window['-DISPLAY_C-'].update( real( soma( window['-DISPLAY_C-'].get() ) - soma( window[keyout].get() ) ))
					
					if key == 16:
						f = valor
						window[keyout].update(valor)
					elif key == 17:
						g = valor
						window[keyout].update(valor)
					elif key == 18:
						h = valor
						window[keyout].update(valor)
					elif key == 19:
						i = valor
						window[keyout].update(valor)
					elif key == 20:
						j = valor
						window[keyout].update(valor)
					elif key == 21:
						k = valor
						window[keyout].update(valor)
					elif key == 22:
						l = valor
						window[keyout].update(valor)

					if event == '\r':
						next_element(key)

window.close(); del window
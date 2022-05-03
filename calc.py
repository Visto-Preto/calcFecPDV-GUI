#coding: utf-8
import PySimpleGUI as sg
from module.realsymbol import Real as rs

sg.theme('random')


layout_menu = [	['Histórico'],
				['Ajuda']	]


layout = [ 
[sg.Menu(layout_menu)],
[sg.Text(' R$ 0,00', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='r', expand_x=True, key='-DIS_CALC_R-'), 
sg.Text('', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(2,1), key='-OP-'), 
sg.Text(0, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(5,1), key='-CONT-') ],
[sg.Input('', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', expand_x=True, font='_ 15', enable_events=True,key='-DIS_CALC-')]
 ]

class App():
	def __init__(self):
		self.window = sg.Window('PyCalculator', return_keyboard_events=True, layout=layout, resizable=True, size=(250, 100))
		self.window.read(timeout=1)
		self.cont = 0

	def run(self):
		while True:
			event, values = self.window.read()
			if event in (None, sg.WIN_CLOSED):
				break

			if event == '+':
				self.cont += 1
				self.window['-CONT-'].update(self.cont)
				self.window['-OP-'].update('+')
				self.dc = rs.string_to_f( self.window['-DIS_CALC-'].get() )
				self.dr = rs.string_to_f( self.window['-DIS_CALC_R-'].get() )
				self.resultsoma = rs.float_to_s( self.dc + self.dr )
				self.window['-DIS_CALC_R-'].update( self.resultsoma )
				self.window['-DIS_CALC-'].update('')

			elif event == '-':
				self.cont = 0
				self.window['-CONT-'].update(self.cont)
				self.window['-OP-'].update('-')
				self.dc = rs.string_to_f( self.window['-DIS_CALC-'].get() )
				self.dr = rs.string_to_f( self.window['-DIS_CALC_R-'].get() )
				if self.window['-DIS_CALC_R-'].get() == ' R$ 0,00':
					self.resultsoma = rs.float_to_s( self.dc - self.dr )
				else:
					self.resultsoma = rs.float_to_s( self.dr - self.dc )
				self.window['-DIS_CALC_R-'].update( self.resultsoma )
				self.window['-DIS_CALC-'].update('')




			if event == '-DIS_CALC-' and len(values['-DIS_CALC-']) and values['-DIS_CALC-'][-1] not in ('0123456789'):
				self.window['-DIS_CALC-'].update(values['-DIS_CALC-'][:-1])
			if event == '-DIS_CALC-' and len(values['-DIS_CALC-']) and values['-DIS_CALC-'][-1] in ('0123456789'):
				if (len(values['-DIS_CALC-']) > 19): # limite maximo de caracter 12
					self.window['-DIS_CALC-'].update(values['-DIS_CALC-'][:-1])
				if (len(values['-DIS_CALC-']) < 20): #
					if len(values['-DIS_CALC-']) == 1:
						discalc = int( values['-DIS_CALC-'] )
						self.window['-DIS_CALC-'].update( rs.float_to_s(discalc) )
					else:
						discalc = values['-DIS_CALC-']
						self.window['-DIS_CALC-'].update( rs.del_caracter(discalc) )	


		self.window.close()

App().run()
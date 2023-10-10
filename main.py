#coding: utf-8

import PySimpleGUI as sg 
from module import calc
from module.realsymbol import Real as rs
from module.pages import Page_Printers

import os, sqlite3, win32print, win32api, time, sys

__author__ = "Visto-Preto"
__version__ = "1.0.0"

mainWindowIcon_32 = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAAOpgAABdwnLpRPAAAAu5QTFRFAAAAgdLrf9Drf9DpgdHrgdLsf9LtgdTtgdPrgtLqgdLqgdPsf9TrgdPrgdLrgdLrgdLrgdLrgdLrgdLrgdLrgdLrgdLrgdLrgdLrgdLrgdLrgdLrgdLrgdLrgdLrgdLrgdLrgdLrgdLrgdLrgdLrgdLrgdLrgdLrgdLrgdLrgdLrgdLrgdLqgdLrgdLrgNPrgdLrgdLrgdLrgdLrgdLrgdLrgdLrgdLrgdLrgdLsgdLrgdLrgdLrgdLrgdLrgdLrgdLrgdLrgtLrgdLrgdLrgdLrgdLrgtPtg9Ttg9XugdPsgNLrgNHqYLHJUaK5UqO6UpmuUpKlVpeqeMbdgtPsgtLrhNPri9btfc7nK32SDV9yDmF1DVJjDDdCCzI8EDhDZavBg9TuhtTsueb0s+Tz4fT6DF5y4PT6/P7+/v7/idXsg9LqZLPJVaO5UpOmOnB+TYmaU5OmVZeqg9Pr8vv9+f3+8/v98vr9y+33y+32zO74ze/5wN/nwejyouDyhNXujNbt1/H41PL5btXvXdHuXtHuXc3pccvisOPwiNTsjdbtzO33v+j1vuj1u+n2G73nALTkALXkALDeAKDLL6/QruLwiNXs0e/4z+/3ze73zu73zO/4bNXvW9DuVs3rTMHeS7vYaMffjtft3fP66/j86vj76fj75Pb6ze72xuv0vejzitXsf9HrqeDx9vz+9/z+/f7/9fv9+v3+9fz94PX63vT62fL53/T62vL5ndzvgNHr0+/4wOj1tOTz0u/4yuz2suTzqODx2PL5r+Pyxev2vej0ltru8Pn9/P7/6ff83fP51vH40vD41fD42/P5kdjtxuv28Pr95fb7wOn1uuf0wur1tuXz3PP5rOLy4/X71/H54fX61PD4h9TsnNzw4vb85vj85/j92/T71fL60fH5mNvvgdLsh8ncj7rFkLrFVJSnEjlCEjlDFkFMFkFLDDM9CzE7K25/KGl6CzI7E0BLEj9KbrjPUZGkUpGk////2TPGWAAAAEZ0Uk5TAAAAAAAAAAAAAAAAAAMqcq3V9POuKwM5mN/8OBqK6ukZNcH+vzJG2NZCG8ACAjoCk95rpfLU6DeFAr690z80MYaUA6anbA+YvgoAAAABYktHRPlMZFfwAAAACXBIWXMAAES4AABEuAH3N9d6AAAChElEQVQ4y2NggAJGXj5+AUEhNzdhQRF+UTFGBlTAKCYuISnlBgVSkhLSKEqYGGVk5dxQgLysAiMzTJ6FUVFJ2Q0NKKuoMrJCjWdUU3fDAjQ0GcHWsDEqosi7e3h4eHp6erm5CSqCbWHU0obJeQOxj6+fv39AYFBwiJubthbQCEYdWYhsaJhbuFtYaERkVHRMbFx8QiJQTFaXkYFRD+r+pOSU1JTkpIjINKA8VIG8NCODvgTU/KT0jMyM9KzsnNy8/ILCIpAVbm4GugyikhD54pSS0rLS8orKquqKmtq6ei+wqKEoAz8k/LwbGkuBCkqbmltaW9vaOzqhYWrEIAD1QFd3T09vT09f/4SJkyZPmToNarExgyBMwfQZM2fNnDF7ztx58xcs7IApEGQQhipYtHjJUiBYtnT5ipUrV65a7Q0RF2aAqlyzdt36DRs3rNu0ecvWbdt3bNu5CyoBUxC6e8eesr3le/btP9B48NDhI0dDYQogVngfK19//MSSEydPbTu9/cz2s+caz0PsMIE6ck1v6YWLu9MvXd6y5cqsC1dPX7t+A6LAFOJN79U3T9zamH5zx5Hbty/cmdW94+r27rtQb4IDate9+w8ePnjwqOlxU9NjIADST556QwIKHNTPnr9ABy+fP4MEtS4osjxfvX4DAW/fQRmvX3lCIotRXB6oIDDuPRh8+PjpA4QVFwhUYGYOTA+6siAFn+Mg4MtXKOMzSIGFJShJyVi5hXwLhILvP2CsbyFu1gqM4EyhKugW4okBQtxsVBnZIcleUxBbsrexZeSAZAxORjttDGllK3subljW4sGS9RwUIObDM6+5AXLmdTTHzN9OfEbO4Oyv4eKKlP0BCbpYmGYkkRMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTktMDMtMjlUMTA6NTk6NTIrMDA6MDCxMXwMAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE5LTAzLTI5VDEwOjU5OjUyKzAwOjAwwGzEsAAAAEZ0RVh0c29mdHdhcmUASW1hZ2VNYWdpY2sgNi43LjgtOSAyMDE5LTAyLTAxIFExNiBodHRwOi8vd3d3LmltYWdlbWFnaWNrLm9yZ0F74sgAAAAYdEVYdFRodW1iOjpEb2N1bWVudDo6UGFnZXMAMaf/uy8AAAAYdEVYdFRodW1iOjpJbWFnZTo6aGVpZ2h0ADUxMsDQUFEAAAAXdEVYdFRodW1iOjpJbWFnZTo6V2lkdGgANTEyHHwD3AAAABl0RVh0VGh1bWI6Ok1pbWV0eXBlAGltYWdlL3BuZz+yVk4AAAAXdEVYdFRodW1iOjpNVGltZQAxNTUzODU3MTkyxeDSqQAAABN0RVh0VGh1bWI6OlNpemUAMjAuOUtCQt6Nn64AAAA/dEVYdFRodW1iOjpVUkkAZmlsZTovLy4vdXBsb2Fkcy81Ni92dFN5d2I5LzE4NTkvY2FzaGllcjJfMTE3OTUxLnBuZ7x2vmYAAAAASUVORK5CYII='
mainWindowIcon_64 = b'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'

class Control_DB():

	def ver():
		if os.path.isfile('settings/calcfecpdv.db'):
			pass
		else:
			con = sqlite3.connect('settings/calcfecpdv.db')
			cur = con.cursor()
			cur.execute('''CREATE TABLE login_cfgs(theme TEXT,pathc  TEXT)''')
			cur.execute('''INSERT INTO login_cfgs VALUES('{}', '{}')'''.format('DefaultNoMoreNagging', 'settings'))
			con.commit()
			con.close()

	def login_cfgs_out():
		con = sqlite3.connect('settings/calcfecpdv.db')
		cur = con.cursor()
		for row in cur.execute('''SELECT * FROM login_cfgs'''):
			theme = row[0]
		return theme
		con.commit()
		con.close()

	def login_cfgs_in(x):
		con = sqlite3.connect('settings/calcfecpdv.db')
		cur = con.cursor()
		cur.execute('''DROP TABLE login_cfgs''')
		cur.execute('''CREATE TABLE login_cfgs(theme TEXT,pathc  TEXT)''')
		cur.execute('''INSERT INTO login_cfgs VALUES('{}', '{}')'''.format(x, 'settings'))
		con.commit()
		con.close()

	def add_users(x, y, z):
		con = sqlite3.connect('settings/calcfecpdv.db')
		cur = con.cursor()
		cur.execute('''CREATE TABLE {} (user TEXT,job  TEXT,pswd TEXT )'''.format(x))
		cur.execute('''INSERT INTO {} VALUES('{}', '{}', '{}' )'''.format(x, x, y, z))
		con.commit()
		con.close()

	def login_users(x):
		con = sqlite3.connect('settings/calcfecpdv.db')
		cur = con.cursor()
		for row in cur.execute('''SELECT * FROM {}'''.format(x)):
			usr = row[0]
			fun = row[1]
			pwd = row[2]
		return usr, fun, pwd

def theme():
	Control_DB.ver()
	return Control_DB.login_cfgs_out()

sg.theme(theme())


class MainApp():
	def __init__(self):
		pass

	def printers():
		l_imp_local = lista_impressoras = win32print.EnumPrinters(2)
		l_imp_rede = lista_impressoras = win32print.EnumPrinters(4)

		def list_imp(x):
			l = []
			t = len(x)
			c = t
			for i in range(0, t):
				c = c - 1
				l += [x[c][2]]

			return l
		local = list_imp(l_imp_local)
		rede = list_imp(l_imp_rede)
		all_printers = local + rede
		return all_printers
		
	def add_users(self):

		self.lmenu = [ ['Arquivo', ['Temas', sg.theme_list(), 'Sair']], ['Sobre', ['Ajuda', 'Sobre o Desenvolvedor']] ]

		self.lgroup = [	[sg.Text('Por favor insira os seus dados ')], [sg.Column([ [sg.Text('Usuário:'), sg.Input('', size=(26,1), key='-USR-')], [sg.Text('Função:'), sg.Input('', size=(26,1), key='-FUN-')] ,[sg.Text('Senha  :'), sg.Input('', password_char='*' ,size=(26,1), key='-PWD-')], [sg.Text('', key='-LBL-')]],  element_justification='r', expand_x=True ) ]]

		self.layout = [	[sg.Menu(self.lmenu)], [sg.Frame('Dados de cadastro', self.lgroup, expand_x=True)], 
							[sg.Column([[sg.Button('OK', size=(7,1)), sg.Button('Voltar', size=(7,1))]], element_justification='r', expand_x=True)]	
								] 
		self.window = sg.Window('Cadrastro de Usuário', size=(350,240), finalize=True,resizable=False, return_keyboard_events=True,layout=self.layout, keep_on_top=True,  grab_anywhere=True, use_custom_titlebar=True, titlebar_icon=mainWindowIcon_32, titlebar_font=(sg.DEFAULT_FONT, 12, 'bold'), icon=mainWindowIcon_64)
		self.window.read(timeout=1)
		while True:
			self.event, self.values = self.window.read()

			if self.event in ('Sair', None, sg.WIN_CLOSED):
				self.window.close()
				sys.exit()
			if self.event == 'Voltar':
				self.window.close()
				MainApp.configs(self)

			if self.event in ('OK', '\r'):
				if len(self.values['-USR-']) >= 2 and len(self.values['-PWD-']) <= 5:
						self.window['-LBL-'].Update('A senha deve conter no minino 6 caracteres')

				elif len(self.values['-USR-']) < 2 and len(self.values['-PWD-']) >= 5:
					self.window['-LBL-'].Update('O usuário deve conter no minino 2 caracteres')

				elif len(self.values['-USR-']) >= 2 and len(self.values['-PWD-']) >= 6:
					usr = self.values['-USR-']
					func = self.values['-FUN-']
					pwd = self.values['-PWD-']

					usr = usr.capitalize()
					func = func.capitalize()
					pwd = pwd.lower()

					try:
						Control_DB.add_users(usr, func, pwd)
						self.window['-LBL-'].Update('Cadrastro efetuado')
						self.window['-USR-'].Update('')
						self.window['-FUN-'].Update('')
						self.window['-PWD-'].Update('')
						self.window['-USR-'].set_focus()

					except sqlite3.OperationalError as error:
						print(error)
						if str(error) == ('table {} already exists'.format(usr)):
							self.window['-LBL-'].Update('Esse usuário já esta em uso')
						else:
							self.window['-LBL-'].Update('Caracteres não aceito')

	def calcfecpdv(self, user, func, pwd):

		self.a = self.b = self.c = self.d = self.e = self.f = self.g = self.h = self.i = self.j = self.k = self.l = self.rec = self.vda = self.vdap = self.ca = self.pix = self.cac = self.dsp = self.desp = self.said = self.troc = self.valor = ' R$ 0,00'
		self.printer_defualt = win32print.GetDefaultPrinter()

		def real(x):
			return calc.str_real_format( calc.insert_result( x))

		def soma(x):
			return calc.float_calc_format(x)

		self.layout_moedas = 	[	
							[sg.Text(self.valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', expand_x=True, key='-DISPLAY_M-', font='_ 15')],
							[ sg.HorizontalSeparator()],
							[sg.Text('R$   1,00', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.Input('', justification='r', size=(10, 1),  expand_x=True, focus=True, enable_events=True, key='-IN100-'), sg.Text('=', expand_x=True, justification='c'), sg.Text(self.valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), size=(20, 1), expand_x=True, justification='r',  key='-OUT100-')],
							[sg.Text('R$   0,50', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.Input('', justification='r', size=(10, 1),  expand_x=True, enable_events=True, key='-IN050-'), sg.Text('=', expand_x=True, justification='c'), sg.Text(self.valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), size=(20, 1), expand_x=True, justification='r',  key='-OUT050-')],
							[sg.Text('R$   0,25', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.Input('', justification='r', size=(10, 1),  expand_x=True, enable_events=True, key='-IN025-'), sg.Text('=', expand_x=True, justification='c'), sg.Text(self.valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), size=(20, 1), expand_x=True, justification='r',  key='-OUT025-')],
							[sg.Text('R$   0,10', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.Input('', justification='r', size=(10, 1),  expand_x=True,  enable_events=True, key='-IN010-'), sg.Text('=', expand_x=True, justification='c'), sg.Text(self.valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), size=(20, 1), expand_x=True, justification='r',  key='-OUT010-')],
							[sg.Text('R$   0,05', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.Input('', justification='r', size=(10, 1),  expand_x=True, enable_events=True, key='-IN005-'), sg.Text('=', expand_x=True, justification='c'), sg.Text(self.valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), size=(20, 1), expand_x=True, justification='r', key='-OUT005-')]

							]

		# Inicio da tab de calculos de cedulas
		self.layout_cedulas = [	
							[sg.Text(self.valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', expand_x=True, key='-DISPLAY_C-', font='_ 15')],
							[ sg.HorizontalSeparator()],
							[sg.Text('R$ 200,00', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.Input('', justification='r', size=(10, 1),  expand_x=True, enable_events=True, key='-IN20000-'), sg.Text('=', expand_x=True, justification='c'), sg.Text(self.valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), size=(15, 1), expand_x=True, justification='r', key='-OUT20000-')],
							[sg.Text('R$ 100,00', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.Input('', justification='r', size=(10, 1),  expand_x=True, enable_events=True, key='-IN10000-'), sg.Text('=', expand_x=True, justification='c'), sg.Text(self.valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), size=(15, 1), expand_x=True, justification='r', key='-OUT10000-')],
							[sg.Text('R$  50,00', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.Input('', justification='r', size=(10, 1),  expand_x=True, enable_events=True, key='-IN5000-'), sg.Text('=', expand_x=True, justification='c'), sg.Text(self.valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), size=(15, 1), expand_x=True, justification='r', key='-OUT5000-')],
							[sg.Text('R$  20,00', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.Input('', justification='r', size=(10, 1),  expand_x=True, enable_events=True, key='-IN2000-'), sg.Text('=', expand_x=True, justification='c'), sg.Text(self.valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), size=(15, 1), expand_x=True, justification='r', key='-OUT2000-')],
							[sg.Text('R$  10,00', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.Input('', justification='r', size=(10, 1),  expand_x=True, enable_events=True, key='-IN1000-'), sg.Text('=', expand_x=True, justification='c'), sg.Text(self.valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), size=(15, 1), expand_x=True, justification='r', key='-OUT1000-')],
							[sg.Text('R$   5,00', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.Input('', justification='r', size=(10, 1),  expand_x=True, enable_events=True, key='-IN500-'), sg.Text('=', expand_x=True, justification='c'), sg.Text(self.valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), size=(15, 1), expand_x=True, justification='r', key='-OUT500-')],
							[sg.Text('R$   2,00', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c', size=(8,1),expand_x=True), sg.Text('X', expand_x=True, justification='c'), sg.Input('', justification='r', size=(10, 1),  expand_x=True, enable_events=True, key='-IN200-'), sg.Text('=', expand_x=True, justification='c'), sg.Text(self.valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), size=(15, 1), expand_x=True, justification='r', key='-OUT200-')]
							]

		# Inicio da tab de calculos dos Recibos
		self.layout_recibos = [	
							[sg.Text('Recibos', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='l', size=(15, 1), expand_x=True), sg.Input('', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', size=(26, 1), expand_x=True, enable_events=True, key='-REC-' )],
							[sg.Text('Venda avista', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='l', size=(15, 1), expand_x=True), sg.Input('', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', size=(26, 1), expand_x=True, enable_events=True, key='-VDA-' )],
							[sg.Text('Venda a prazo', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='l', size=(15, 1), expand_x=True), sg.Input('', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r',size=(26, 1), expand_x=True, enable_events=True, key='-VDAP-' )],
							[sg.Text('Cartão', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='l', size=(15, 1), expand_x=True), sg.Input('', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', size=(26, 1), expand_x=True, enable_events=True, key='-CA-' )],
							[sg.Text('Pagto PIX', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='l', size=(15, 1), expand_x=True), sg.Input('', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', size=(26, 1), expand_x=True, enable_events=True, key='-PIX-' )],
							[sg.Text('Carta crédito', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='l', size=(15, 1), expand_x=True), sg.Input('', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', size=(26, 1), expand_x=True, enable_events=True, key='-CAC-' )],
							[sg.Text('Despedas', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='l', size=(15, 1), expand_x=True), sg.Input('', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', size=(26, 1), expand_x=True, enable_events=True, key='-DSP-' )],
							[ sg.HorizontalSeparator()],
							[sg.Text( 'Total Recebido', size=(15, 1), expand_x=True), sg.Text(self.valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', size=(26, 1), expand_x=True, key='-DIS_TR-')],
							[sg.Text( 'Total Dinheiro', size=(15, 1), expand_x=True), sg.Text(self.valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', size=(26, 1), expand_x=True, key='-DIS_TD-')],
							[ sg.HorizontalSeparator()],
							[sg.Text( 'Depósito diário', size=(15, 1), expand_x=True), sg.Text(self.valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', size=(26, 1), expand_x=True, font='_ 15', key='-DIS_DD-')]
							]
	
		# Inicio da tab de calculos do PDV
		
		self.layout_imp = [
												[sg.Text('')],		
												[sg.Frame('Impressão', 
													[
														[sg.Text('')],[sg.Combo(MainApp.printers(), default_value=self.printer_defualt, expand_x=True, readonly=True, key='-PRINTERS-')], 
														[sg.Text('')],
														[sg.Frame('Opções de Impressão', 
															[
																[sg.Radio('Detalhado', "impressao", default=True, size=(10,1), k='-R1-'), sg.Radio('Resumido', "impressao", default=False, size=(10,1), k='-R2-')], 
																[sg.HorizontalSeparator()],
																[sg.Radio('Modelo 1', "pagina", default=True, size=(10,1), k='-R3-'), sg.Radio('Modelo 2', "pagina", default=False, size=(10,1), k='-R4-')]
															] )
														], 
													[sg.Text('')], 
													[sg.Button('Imprimir', size=(7, 1), expand_x=True)]
													], 

												expand_x=True)]
											]
							

		self.layout_calc = [
							[sg.Text('Moedas', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='l', size=(17, 1), expand_x=True), sg.Text(self.valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', size=(26, 1), expand_x=True, key='-MO-')],
							[sg.Text('Cédulas', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='l', size=(17, 1), expand_x=True), sg.Text(self.valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', size=(26, 1), expand_x=True, key='-CE-')],
							[sg.Text('Despesas', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='l', size=(15, 1), expand_x=True), sg.Input('', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', size=(26, 1), enable_events=True, expand_x=True, key='-DESP-')],
							[sg.Text('Saidas', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='l', size=(15, 1), expand_x=True), sg.Input('', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', size=(26, 1), enable_events=True, expand_x=True, key='-SAID-')],
							[sg.Text('Trocados', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='l', size=(15, 1), expand_x=True), sg.Input('', background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r',  size=(26, 1), enable_events=True, expand_x=True, key='-TROC-')],
							[ sg.HorizontalSeparator()],
							[sg.Text( 'Valor D/ Caixa', size=(15, 1), expand_x=True), sg.Text(self.valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', size=(26, 1), expand_x=True, key='-DICA-')],
							[sg.Text( 'Total Dinheiro', size=(15, 1), expand_x=True), sg.Text(self.valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', size=(26, 1), expand_x=True, key='-DINPDV-')],
							[ sg.HorizontalSeparator()],
							[sg.Text('  ', size=(15, 2))],
							[ sg.HorizontalSeparator()],
							[sg.Text(self.valor, background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color(), justification='r', expand_x=True, key='-RESULT-', font='_ 15')]
							]

		self.layout_tab_group = [	
							[	sg.Tab('Moedas', self.layout_moedas), 
								sg.Tab('Cédulas', self.layout_cedulas),
								sg.Tab('Recibos', self.layout_recibos),
								sg.Tab('Calculos PDV', self.layout_calc),
								sg.Tab('Impressão', self.layout_imp)	]
							]

		self.layout_menu = [	
							['Arquivo', [['Limpar'], 'Configs', 'Sair']],
							['Calculadora'],
							['Sobre']
							]

		self.layout = [ 	
							[sg.Menu(self.layout_menu)],
							[sg.TabGroup(self.layout_tab_group, expand_x=True, expand_y=True)],
							[sg.StatusBar(self.func, justification='c', size=(10, 1), expand_x=True), sg.StatusBar(self.user, justification='c', size=(20, 1), expand_x=True)]
							] 

		self.window = sg.Window('Usuário: {}'.format(self.user), size=(372,380), resizable=False, layout=self.layout, use_default_focus=False, return_keyboard_events=False, keep_on_top=True,  finalize=True,grab_anywhere=True, use_custom_titlebar=True, titlebar_icon=mainWindowIcon_32, titlebar_font=(sg.DEFAULT_FONT, 12, 'bold'), icon=mainWindowIcon_64)
		self.window.read(timeout=1)
		while True: 
		# Event Loop 
			self.event, self.values = self.window.read() 
			if self.event in (None, 'Sair'):
				self.window.close()
				MainApp().login()
			if self.event == 'Limpar':
				self.window.close()
				MainApp.calcfecpdv(self, user, func, pwd)
			if self.event == 'Imprimir':
				def tipo_imp():
					if self.values['-R2-'] == True and self.values['-R3-'] == True:
						Page_Printers.resumido_page_1(self.user,self.window['-DIS_TR-'].get(),self.window['-DIS_TD-'].get() ,self.window['-MO-'].get(),self.window['-CE-'].get(),self.window['-DESP-'].get(),self.window['-SAID-'].get(),self.window['-TROC-'].get(),self.window['-DICA-'].get(),  self.window['-RESULT-'].get() )
						return 'resumido_page_1'
					elif self.values['-R2-'] == True and self.values['-R4-'] == True:
						Page_Printers.resumido_page_2(self.window['-DIS_TR-'].get(),self.window['-DIS_TD-'].get(),self.window['-MO-'].get(),self.window['-CE-'].get(),self.window['-DESP-'].get(),self.window['-SAID-'].get(),self.window['-TROC-'].get(),self.window['-DICA-'].get(),  self.window['-RESULT-'].get(), self.user )
						return 'resumido_page_2'					

					elif self.values['-R1-'] == True and self.values['-R3-'] == True:
						Page_Printers.detalhado_page_1(self.user, self.window['-REC-'].get(), self.window['-VDA-'].get(), self.window['-VDAP-'].get(),self.window['-CA-'].get(),self.window['-PIX-'].get(), self.window['-CAC-'].get(),self.window['-DSP-'].get(),self.window['-DIS_TR-'].get(),self.window['-DIS_TD-'].get(),self.window['-DIS_DD-'].get(),self.window['-MO-'].get(),self.window['-CE-'].get(),self.window['-DESP-'].get(),self.window['-SAID-'].get(),self.window['-TROC-'].get(),self.window['-DICA-'].get(),  self.window['-RESULT-'].get() )
						return 'detalhado_page_1'
					elif self.values['-R1-'] == True and self.values['-R4-'] == True:
						Page_Printers.detalhado_page_2(self.window['-REC-'].get(), self.window['-VDA-'].get(), self.window['-VDAP-'].get(),self.window['-CA-'].get(),self.window['-PIX-'].get(), self.window['-CAC-'].get(),self.window['-DSP-'].get(),self.window['-DIS_TR-'].get(),self.window['-DIS_TD-'].get(),self.window['-DIS_DD-'].get(),self.window['-MO-'].get(),self.window['-CE-'].get(),self.window['-DESP-'].get(),self.window['-SAID-'].get(),self.window['-TROC-'].get(),self.window['-DICA-'].get(),  self.window['-RESULT-'].get(), self.user)
						return 'detalhado_page_2'

				path_for_file = r'settings\tmp'
				impressora = self.values['-PRINTERS-']
				file = tipo_imp()
				win32print.SetDefaultPrinter(impressora)
				win32api.ShellExecute(0, 'print', file + '.txt', None, path_for_file, 0) #impressao da pagina com a impressora selecionada
				time.sleep(1) # delay
				win32print.SetDefaultPrinter(self.printer_defualt)

		# Inicio da logica dos campos de Moedas
			# Campo de R$ 0,05
			if self.event == '-IN005-' and len(self.values['-IN005-']) and self.values['-IN005-'][-1] not in ('0123456789'):
				self.window['-IN005-'].update(self.values['-IN005-'][:-1])
			if self.event == '-IN005-' and len(self.values['-IN005-']) and self.values['-IN005-'][-1] in ('0123456789'):	
				if (len(self.values['-IN005-']) > 7):
					self.window['-IN005-'].update(self.values['-IN005-'][:-1])
				if (len(self.values['-IN005-']) < 8):	
					self.a = calc.str_real_format( calc.insert_result(	float( self.values['-IN005-']) * (0.05)	) )
					self.window['-OUT005-'].update( self.a )
					self.window['-DISPLAY_M-'].update( real( soma(self.a) + soma(self.b) + soma(self.c) + soma(self.d) + soma(self.e) ))
			if self.event == '-IN005-' and self.values[self.event] == '':
				self.window['-DISPLAY_M-'].update( real( soma( self.window['-DISPLAY_M-'].get() ) - soma( self.window['-OUT005-'].get() ) ))
				self.a = self.valor
				self.window['-OUT005-'].update(self.valor)

			# Campo de R$ 0,10
			if self.event == '-IN010-' and len(self.values['-IN010-']) and self.values['-IN010-'][-1] not in ('0123456789'):
				self.window['-IN010-'].update(self.values['-IN010-'][:-1])	
			if self.event == '-IN010-' and len(self.values['-IN010-']) and self.values['-IN010-'][-1] in ('0123456789'):
				if (len(self.values['-IN010-']) > 7):
					self.window['-IN010-'].update(self.values['-IN010-'][:-1])
				if (len(self.values['-IN010-']) < 8):	
					self.b = calc.str_real_format( calc.insert_result(	float( self.values['-IN010-']) * (0.10)	))
					self.window['-OUT010-'].update( self.b )
					self.window['-DISPLAY_M-'].update( real( soma(self.a) + soma(self.b) + soma(self.c) + soma(self.d) + soma(self.e) ))
			if self.event == '-IN010-' and self.values[self.event] == '':
				self.window['-DISPLAY_M-'].update( real( soma( self.window['-DISPLAY_M-'].get() ) - soma( self.window['-OUT010-'].get() ) ))
				self.b = self.valor
				self.window['-OUT010-'].update(self.valor)
				
			# Campo de R$ 0,25	
			if self.event == '-IN025-' and len(self.values['-IN025-']) and self.values['-IN025-'][-1] not in ('0123456789'):
				self.window['-IN025-'].update(self.values['-IN025-'][:-1])
			if self.event == '-IN025-' and len(self.values['-IN025-']) and self.values['-IN025-'][-1] in ('0123456789'):
				if (len(self.values['-IN025-']) > 7):
					self.window['-IN025-'].update(self.values['-IN025-'][:-1])
				if (len(self.values['-IN025-']) < 8):	
					self.c = calc.str_real_format( calc.insert_result(	float( self.values['-IN025-']) * (0.25)	) )
					self.window['-OUT025-'].update( self.c )
					self.window['-DISPLAY_M-'].update( real( soma(self.a) + soma(self.b) + soma(self.c) + soma(self.d) + soma(self.e) ))
			if self.event == '-IN025-' and self.values[self.event] == '':
				self.window['-DISPLAY_M-'].update( real( soma( self.window['-DISPLAY_M-'].get() ) - soma( self.window['-OUT025-'].get() ) ))
				self.c = self.valor
				self.window['-OUT025-'].update(self.valor)

			# Campo de R$ 0,50	
			if self.event == '-IN050-' and len(self.values['-IN050-']) and self.values['-IN050-'][-1] not in ('0123456789'):
				self.window['-IN050-'].update(self.values['-IN050-'][:-1])
			if self.event == '-IN050-' and len(self.values['-IN050-']) and self.values['-IN050-'][-1] in ('0123456789'):
				if (len(self.values['-IN050-']) > 7):
					self.window['-IN050-'].update(self.values['-IN050-'][:-1])
				if (len(self.values['-IN050-']) < 8):	
					self.d = calc.str_real_format( calc.insert_result(	float( self.values['-IN050-']) * (0.50)	) )
					self.window['-OUT050-'].update( self.d )
					self.window['-DISPLAY_M-'].update( real( soma(self.a) + soma(self.b) + soma(self.c) + soma(self.d) + soma(self.e) ))
			if self.event == '-IN050-' and self.values[self.event] == '':
				self.window['-DISPLAY_M-'].update( real( soma( self.window['-DISPLAY_M-'].get() ) - soma( self.window['-OUT050-'].get() ) ))
				self.d = self.valor
				self.window['-OUT050-'].update(self.valor)

			# Campo de R$ 1,00	
			if self.event == '-IN100-' and len(self.values['-IN100-']) and self.values['-IN100-'][-1] not in ('0123456789'):
				self.window['-IN100-'].update(self.values['-IN100-'][:-1])
			if self.event == '-IN100-' and len(self.values['-IN100-']) and self.values['-IN100-'][-1] in ('0123456789'):
				if (len(self.values['-IN100-']) > 7):
					self.window['-IN100-'].update(self.values['-IN100-'][:-1])
				if (len(self.values['-IN100-']) < 8):	
					self.e = calc.str_real_format( calc.insert_result(	float( self.values['-IN100-']) * (1.00)	) )
					self.window['-OUT100-'].update( self.e )
					self.window['-DISPLAY_M-'].update( real( soma(self.a) + soma(self.b) + soma(self.c) + soma(self.d) + soma(self.e) ))
			if self.event == '-IN100-' and self.values[self.event] == '':
				self.window['-DISPLAY_M-'].update( real( soma( self.window['-DISPLAY_M-'].get() ) - soma( self.window['-OUT100-'].get() ) ))
				self.e = self.valor
				self.window['-OUT100-'].update(self.valor)

		# Inicio da logica dos campos das Cedulas
			# Inicio da logica do campo de R$ 2,00	
			if self.event == '-IN200-' and len(self.values['-IN200-']) and self.values['-IN200-'][-1] not in ('0123456789'):
				self.window['-IN200-'].update(self.values['-IN200-'][:-1])
			if self.event == '-IN200-' and len(self.values['-IN200-']) and self.values['-IN200-'][-1] in ('0123456789'):
				if (len(self.values['-IN200-']) > 6):
					self.window['-IN200-'].update(self.values['-IN200-'][:-1])
				if (len(self.values['-IN200-']) < 7):	
					self.f = calc.str_real_format( calc.insert_result(	float( self.values['-IN200-']) * (2.00)	) )
					self.window['-OUT200-'].update( self.f )
					self.window['-DISPLAY_C-'].update( real( soma(self.f) + soma(self.g) + soma(self.h) + soma(self.i) + soma(self.j) + soma(self.k) + soma(self.l) ))
			if self.event == '-IN200-' and self.values[self.event] == '':
				self.window['-DISPLAY_C-'].update( real( soma( self.window['-DISPLAY_C-'].get() ) - soma( self.window['-OUT200-'].get() ) ))
				self.f = self.valor
				self.window['-OUT200-'].update(self.valor)

			# Incio da logica do campo de R$ 5,00	
			if self.event == '-IN500-' and len(self.values['-IN500-']) and self.values['-IN500-'][-1] not in ('0123456789'):
				self.window['-IN500-'].update(self.values['-IN500-'][:-1])
			if self.event == '-IN500-' and len(self.values['-IN500-']) and self.values['-IN500-'][-1] in ('0123456789'):
				if (len(self.values['-IN500-']) > 6):
					self.window['-IN500-'].update(self.values['-IN500-'][:-1])
				if (len(self.values['-IN500-']) < 7):	
					self.g = calc.str_real_format( calc.insert_result(	float( self.values['-IN500-']) * (5.00)	) )
					self.window['-OUT500-'].update( self.g )
					self.window['-DISPLAY_C-'].update( real( soma(self.f) + soma(self.g) + soma(self.h) + soma(self.i) + soma(self.j) + soma(self.k) + soma(self.l) ))
			if self.event == '-IN500-' and self.values[self.event] == '':
				self.window['-DISPLAY_C-'].update( real( soma( self.window['-DISPLAY_C-'].get() ) - soma( self.window['-OUT500-'].get() ) ))
				self.g = self.valor
				self.window['-OUT500-'].update(self.valor)

			# Incio da logica do campo de R$ 10,00	
			if self.event == '-IN1000-' and len(self.values['-IN1000-']) and self.values['-IN1000-'][-1] not in ('0123456789'):
				self.window['-IN1000-'].update(self.values['-IN1000-'][:-1])
			if self.event == '-IN1000-' and len(self.values['-IN1000-']) and self.values['-IN1000-'][-1] in ('0123456789'):
				if (len(self.values['-IN1000-']) > 6):
					self.window['-IN1000-'].update(self.values['-IN1000-'][:-1])
				if (len(self.values['-IN1000-']) < 7):	
					self.h = calc.str_real_format( calc.insert_result(	float( self.values['-IN1000-']) * (10.00)	) )
					self.window['-OUT1000-'].update( self.h )
					self.window['-DISPLAY_C-'].update( real( soma(self.f) + soma(self.g) + soma(self.h) + soma(self.i) + soma(self.j) + soma(self.k) + soma(self.l) ))
			if self.event == '-IN1000-' and self.values[self.event] == '':
				self.window['-DISPLAY_C-'].update( real( soma( self.window['-DISPLAY_C-'].get() ) - soma( self.window['-OUT1000-'].get() ) ))
				self.h = self.valor
				self.window['-OUT1000-'].update(self.valor)

			# Incio da logica do campo de R$ 20,00	
			if self.event == '-IN2000-' and len(self.values['-IN2000-']) and self.values['-IN2000-'][-1] not in ('0123456789'):
				self.window['-IN2000-'].update(self.values['-IN2000-'][:-1])
			if self.event == '-IN2000-' and len(self.values['-IN2000-']) and self.values['-IN2000-'][-1] in ('0123456789'):
				if (len(self.values['-IN2000-']) > 5):
					self.window['-IN2000-'].update(self.values['-IN2000-'][:-1])
				if (len(self.values['-IN2000-']) < 6):	
					self.i = calc.str_real_format( calc.insert_result(	float( self.values['-IN2000-']) * (20.00)	) )
					self.window['-OUT2000-'].update( self.i )
					self.window['-DISPLAY_C-'].update( real( soma(self.f) + soma(self.g) + soma(self.h) + soma(self.i) + soma(self.j) + soma(self.k) + soma(self.l) ))
			if self.event == '-IN2000-' and self.values[self.event] == '':
				self.window['-DISPLAY_C-'].update( real( soma( self.window['-DISPLAY_C-'].get() ) - soma( self.window['-OUT2000-'].get() ) ))
				self.i = self.valor
				self.window['-OUT2000-'].update(self.valor)

			# Incio da logica do campo de R$ 50,00	
			if self.event == '-IN5000-' and len(self.values['-IN5000-']) and self.values['-IN5000-'][-1] not in ('0123456789'):
				self.window['-IN5000-'].update(self.values['-IN5000-'][:-1])
			if self.event == '-IN5000-' and len(self.values['-IN5000-']) and self.values['-IN5000-'][-1] in ('0123456789'):
				if (len(self.values['-IN5000-']) > 5):
					self.window['-IN5000-'].update(self.values['-IN5000-'][:-1])
				if (len(self.values['-IN5000-']) < 6):	
					self.j = calc.str_real_format( calc.insert_result(	float( self.values['-IN5000-']) * (50.00)	) )
					self.window['-OUT5000-'].update( self.j )
					self.window['-DISPLAY_C-'].update( real( soma(self.f) + soma(self.g) + soma(self.h) + soma(self.i) + soma(self.j) + soma(self.k) + soma(self.l) ))
			if self.event == '-IN5000-' and self.values[self.event] == '':
				self.window['-DISPLAY_C-'].update( real( soma( self.window['-DISPLAY_C-'].get() ) - soma( self.window['-OUT5000-'].get() ) ))
				self.j = self.valor
				self.window['-OUT5000-'].update(self.valor)

			# Incio da logica do campo de R$ 100,00	
			if self.event == '-IN10000-' and len(self.values['-IN10000-']) and self.values['-IN10000-'][-1] not in ('0123456789'):
				self.window['-IN10000-'].update(self.values['-IN10000-'][:-1])
			if self.event == '-IN10000-' and len(self.values['-IN10000-']) and self.values['-IN10000-'][-1] in ('0123456789'):
				if (len(self.values['-IN10000-']) > 5):
					self.window['-IN10000-'].update(self.values['-IN10000-'][:-1])
				if (len(self.values['-IN10000-']) < 6):	
					self.k = calc.str_real_format( calc.insert_result(	float( self.values['-IN10000-']) * (100.00)	) )
					self.window['-OUT10000-'].update( self.k )
					self.window['-DISPLAY_C-'].update( real( soma(self.f) + soma(self.g) + soma(self.h) + soma(self.i) + soma(self.j) + soma(self.k) + soma(self.l) ))
			if self.event == '-IN10000-' and self.values[self.event] == '':
				self.window['-DISPLAY_C-'].update( real( soma( self.window['-DISPLAY_C-'].get() ) - soma( self.window['-OUT10000-'].get() ) ))
				self.k = self.valor
				self.window['-OUT10000-'].update(self.valor)

			# Incio da logica do campo de R$ 200,00	
			if self.event == '-IN20000-' and len(self.values['-IN20000-']) and self.values['-IN20000-'][-1] not in ('0123456789'):
				self.window['-IN20000-'].update(self.values['-IN20000-'][:-1])
			if self.event == '-IN20000-' and len(self.values['-IN20000-']) and self.values['-IN20000-'][-1] in ('0123456789'):
				if (len(self.values['-IN20000-']) > 4):
					self.window['-IN20000-'].update(self.values['-IN20000-'][:-1])
				if (len(self.values['-IN20000-']) < 5):	
					self.l = calc.str_real_format( calc.insert_result(	float( self.values['-IN20000-']) * (200.00)	) )
					self.window['-OUT20000-'].update( self.l )
					self.window['-DISPLAY_C-'].update( real( soma(self.f) + soma(self.g) + soma(self.h) + soma(self.i) + soma(self.j) + soma(self.k) + soma(self.l) ))
			if self.event == '-IN20000-' and self.values[self.event] == '':
				self.window['-DISPLAY_C-'].update( real( soma( self.window['-DISPLAY_C-'].get() ) - soma( self.window['-OUT20000-'].get() ) ))
				self.l = self.valor
				self.window['-OUT20000-'].update(self.valor)

		# Inicio da logica dos campos de Recibos
			# Campo de recibos
			if self.event == '-REC-' and len(self.values['-REC-']) and self.values['-REC-'][-1] not in ('0123456789'):
				self.window['-REC-'].update(self.values['-REC-'][:-1])
			if self.event == '-REC-' and len(self.values['-REC-']) and self.values['-REC-'][-1] in ('0123456789'):
				if (len(self.values['-REC-']) > 19): # limite maximo de caracter 12
					self.window['-REC-'].update(self.values['-REC-'][:-1])
				if (len(self.values['-REC-']) < 20): #
					if len(self.values['-REC-']) == 1:
						self.rec = int( self.values['-REC-'] )
						self.window['-REC-'].update( rs.float_to_s(self.rec) )
					else:
						self.rec = self.values['-REC-']
						self.window['-REC-'].update( rs.del_caracter(self.rec) )

			# Campo de venda avista
			if self.event == '-VDA-' and len(self.values['-VDA-']) and self.values['-VDA-'][-1] not in ('0123456789'):
				self.window['-VDA-'].update(self.values['-VDA-'][:-1])
			if self.event == '-VDA-' and len(self.values['-VDA-']) and self.values['-VDA-'][-1] in ('0123456789'):
				if (len(self.values['-VDA-']) > 19): # limite maximo de caracter 12
					self.window['-VDA-'].update(self.values['-VDA-'][:-1])
				if (len(self.values['-VDA-']) < 20): #
					if len(self.values['-VDA-']) == 1:
						self.vda = int( self.values['-VDA-'] )
						self.window['-VDA-'].update( rs.float_to_s(self.vda) )
					else:
						self.vda = self.values['-VDA-']
						self.window['-VDA-'].update( rs.del_caracter(self.vda) )

			# Campo de venda a prazo
			if self.event == '-VDAP-' and len(self.values['-VDAP-']) and self.values['-VDAP-'][-1] not in ('0123456789'):
				self.window['-VDAP-'].update(self.values['-VDAP-'][:-1])
			if self.event == '-VDAP-' and len(self.values['-VDAP-']) and self.values['-VDAP-'][-1] in ('0123456789'):
				if (len(self.values['-VDAP-']) > 19): # limite maximo de caracter 12
					self.window['-VDAP-'].update(self.values['-VDAP-'][:-1])
				if (len(self.values['-VDAP-']) < 20): #
					if len(self.values['-VDAP-']) == 1:
						self.vdap = int( self.values['-VDAP-'] )
						self.window['-VDAP-'].update( rs.float_to_s(self.vdap) )
					else:
						self.vdap = self.values['-VDAP-']
						self.window['-VDAP-'].update( rs.del_caracter(self.vdap) )

			# Cartao de credito
			if self.event == '-CA-' and len(self.values['-CA-']) and self.values['-CA-'][-1] not in ('0123456789'):
				self.window['-CA-'].update(self.values['-CA-'][:-1])
			if self.event == '-CA-' and len(self.values['-CA-']) and self.values['-CA-'][-1] in ('0123456789'):
				if (len(self.values['-CA-']) > 19): # limite maximo de caracter 12
					self.window['-CA-'].update(self.values['-CA-'][:-1])
				if (len(self.values['-CA-']) < 20): #
					if len(self.values['-CA-']) == 1:
						self.ca = int( self.values['-CA-'] )
						self.window['-CA-'].update( rs.float_to_s(self.ca) )
					else:
						self.ca = self.values['-CA-']
						self.window['-CA-'].update( rs.del_caracter(self.ca) )	

			# Campo do pix
			if self.event == '-PIX-' and len(self.values['-PIX-']) and self.values['-PIX-'][-1] not in ('0123456789'):
				self.window['-PIX-'].update(self.values['-PIX-'][:-1])
			if self.event == '-PIX-' and len(self.values['-PIX-']) and self.values['-PIX-'][-1] in ('0123456789'):
				if (len(self.values['-PIX-']) > 19): # limite maximo de caracter 12
					self.window['-PIX-'].update(self.values['-PIX-'][:-1])
				if (len(self.values['-PIX-']) < 20): #
					if len(self.values['-PIX-']) == 1:
						self.pix = int( self.values['-PIX-'] )
						self.window['-PIX-'].update( rs.float_to_s(self.pix) )
					else:
						self.pix = self.values['-PIX-']
						self.window['-PIX-'].update( rs.del_caracter(self.pix) )

			# Campo de carta credito
			if self.event == '-CAC-' and len(self.values['-CAC-']) and self.values['-CAC-'][-1] not in ('0123456789'):
				self.window['-CAC-'].update(self.values['-CAC-'][:-1])
			if self.event == '-CAC-' and len(self.values['-CAC-']) and self.values['-CAC-'][-1] in ('0123456789'):
				if (len(self.values['-CAC-']) > 19): # limite maximo de caracter 12
					self.window['-CAC-'].update(self.values['-CAC-'][:-1])
				if (len(self.values['-CAC-']) < 20): #
					if len(self.values['-CAC-']) == 1:
						self.cac = int( self.values['-CAC-'] )
						self.window['-CAC-'].update( rs.float_to_s(self.cac) )
					else:
						self.cac = self.values['-CAC-']
						self.window['-CAC-'].update( rs.del_caracter(self.cac) )	

			# Campo de despesas
			if self.event == '-DSP-' and len(self.values['-DSP-']) and self.values['-DSP-'][-1] not in ('0123456789'):
				self.window['-DSP-'].update(self.values['-DSP-'][:-1])
			if self.event == '-DSP-' and len(self.values['-DSP-']) and self.values['-DSP-'][-1] in ('0123456789'):
				if (len(self.values['-DSP-']) > 19): # limite maximo de caracter 12
					self.window['-DSP-'].update(self.values['-DSP-'][:-1])
				if (len(self.values['-DSP-']) < 20): #
					if len(self.values['-DSP-']) == 1:
						self.dsp = int( self.values['-DSP-'] )
						self.window['-DSP-'].update( rs.float_to_s(self.dsp) )
					else:
						self.dsp = self.values['-DSP-']
						self.window['-DSP-'].update( rs.del_caracter(self.dsp) )
		
		# Inicio da logica dos campos e Calculos PDV
			# Campo de despesas extras
			if self.event == '-DESP-' and len(self.values['-DESP-']) and self.values['-DESP-'][-1] not in ('0123456789'):
				self.window['-DESP-'].update(self.values['-DESP-'][:-1])
			if self.event == '-DESP-' and len(self.values['-DESP-']) and self.values['-DESP-'][-1] in ('0123456789'):
				if (len(self.values['-DESP-']) > 19): # limite maximo de caracter 12
					self.window['-DESP-'].update(self.values['-DESP-'][:-1])
				if (len(self.values['-DESP-']) < 20): #
					if len(self.values['-DESP-']) == 1:
						self.desp = int( self.values['-DESP-'] )
						self.window['-DESP-'].update( rs.float_to_s(self.desp) )
					else:
						self.desp = self.values['-DESP-']
						self.window['-DESP-'].update( rs.del_caracter(self.desp) )	

			# Campo de saidas
			if self.event == '-SAID-' and len(self.values['-SAID-']) and self.values['-SAID-'][-1] not in ('0123456789'):
				self.window['-SAID-'].update(self.values['-SAID-'][:-1])
			if self.event == '-SAID-' and len(self.values['-SAID-']) and self.values['-SAID-'][-1] in ('0123456789'):
				if (len(self.values['-SAID-']) > 19): # limite maximo de caracter 12
					self.window['-SAID-'].update(self.values['-SAID-'][:-1])
				if (len(self.values['-SAID-']) < 20): #
					if len(self.values['-SAID-']) == 1:
						self.said = int( self.values['-SAID-'] )
						self.window['-SAID-'].update( rs.float_to_s(self.said) )
					else:
						self.said = self.values['-SAID-']
						self.window['-SAID-'].update( rs.del_caracter(self.said) )	

			# Campo trocados
			if self.event == '-TROC-' and len(self.values['-TROC-']) and self.values['-TROC-'][-1] not in ('0123456789'):
				self.window['-TROC-'].update(self.values['-TROC-'][:-1])
			if self.event == '-TROC-' and len(self.values['-TROC-']) and self.values['-TROC-'][-1] in ('0123456789'):
				if (len(self.values['-TROC-']) > 19): # limite maximo de caracter 12
					self.window['-TROC-'].update(self.values['-TROC-'][:-1])
				if (len(self.values['-TROC-']) < 20): #
					if len(self.values['-TROC-']) == 1:
						self.troc = int( self.values['-TROC-'] )
						self.window['-TROC-'].update( rs.float_to_s(self.troc) )
					else:
						self.troc = self.values['-TROC-']
						self.window['-TROC-'].update( rs.del_caracter(self.troc) )

		# Inicio da logica do display do Recibos e Calculos PDV

		# display somas dos recibos e pdv
			if type(self.rec) == int or type(self.vda) == int or type(self.vdap) == int  or type(self.ca) == int or type(self.pix) == int or type(self.cac) == int or type(self.dsp) == int or type(self.desp) == int or type(self.said) == int or type(self.troc) == int:

				if type(self.rec) == int:
					self.rec = rs.float_to_s(self.rec)# int
				else:
					self.rec = rs.del_caracter(self.rec)# float

				if type(self.vda) == int:
					self.vda = rs.float_to_s(self.vda)# int
				else:
					self.vda = rs.del_caracter(self.vda)# float

				if type(self.vdap) == int:
					self.vdap = rs.float_to_s(self.vdap)# int
				else:
					self.vdap = rs.del_caracter(self.vdap)# float

				if type(self.ca) == int:
					self.ca = rs.float_to_s(self.ca)# int
				else:
					self.ca = rs.del_caracter(self.ca)# float

				if type(self.pix) == int:
					self.pix = rs.float_to_s(self.pix)# int
				else:
					self.pix = rs.del_caracter(self.pix)# float

				if type(self.cac) == int:
					self.cac = rs.float_to_s(self.cac)# int
				else:
					self.cac = rs.del_caracter(self.cac)# float

				if type(self.dsp) == int:
					self.dsp = rs.float_to_s(self.dsp)# int
				else:
					self.dsp = rs.del_caracter(self.dsp)# float

				if type(self.desp) == int:
					self.desp = rs.float_to_s(self.desp)# int
				else:
					self.desp = rs.del_caracter(self.desp)# float

				if type(self.said) == int:
					self.said = rs.float_to_s(self.said)# int
				else:
					self.said = rs.del_caracter(self.said)# float


				if type(self.troc) == int:
					self.troc = rs.float_to_s(self.troc)# int
				else:
					self.troc = rs.del_caracter(self.troc)# float


				self.dstr = ( rs.string_to_f(self.rec) + rs.string_to_f(self.vda) + rs.string_to_f(self.vdap) )
				self.dstr = rs.float_to_s(self.dstr) 

				self.dstd = ( (rs.string_to_f(self.rec) + rs.string_to_f(self.vda) + rs.string_to_f(self.vdap) ) - (rs.string_to_f(self.ca) + (rs.string_to_f(self.pix)) + rs.string_to_f(self.cac) ) )
				self.dstd = rs.float_to_s(self.dstd) 
				
				self.dica =  ( rs.string_to_f( rs.del_caracter(self.window['-DISPLAY_M-'].get())) + rs.string_to_f( rs.del_caracter(self.window['-DISPLAY_C-'].get())) + rs.string_to_f(self.desp) + rs.string_to_f(self.said) - rs.string_to_f(self.troc) )
				self.dica = rs.float_to_s(self.dica)

				self.disdd = rs.string_to_f(rs.del_caracter(self.dstd)) - rs.string_to_f(self.dsp)
				self.disdd = rs.float_to_s(self.disdd) 

				self.window['-DIS_TR-'].update( self.dstr )
				self.window['-DIS_TD-'].update( self.dstd )
				self.window['-DICA-'].update( self.dica )

				self.window['-DIS_DD-'].update( self.disdd )

			else:
				self.rec = rs.del_caracter(self.rec)# float
				self.vda = rs.del_caracter(self.vda)# float
				self.vdap = rs.del_caracter(self.vdap)# float
				self.ca = rs.del_caracter(self.ca)# float
				self.pix = rs.del_caracter(self.pix)# float
				self.cac = rs.del_caracter(self.cac)# float
				self.dsp = rs.del_caracter(self.dsp)# float
				self.desp = rs.del_caracter(self.desp)
				self.said = rs.del_caracter(self.said)
				self.troc =rs.del_caracter(self.troc)

				self.dstr = ( rs.string_to_f(self.rec) + rs.string_to_f(self.vda) + rs.string_to_f(self.vdap))
				self.dstr = rs.float_to_s(self.dstr) 

				self.dstd = ( (rs.string_to_f(self.rec) + rs.string_to_f(self.vda) + rs.string_to_f(self.vdap) ) - (rs.string_to_f(self.ca) + rs.string_to_f(self.pix) + rs.string_to_f(self.cac) ) )
				self.dstd = rs.float_to_s(self.dstd) 

				self.dica =  ( rs.string_to_f( rs.del_caracter(self.window['-DISPLAY_M-'].get())) + rs.string_to_f( rs.del_caracter(self.window['-DISPLAY_C-'].get())) + rs.string_to_f(self.desp) + rs.string_to_f(self.said) - rs.string_to_f(self.troc) )
				self.dica = rs.float_to_s(self.dica)

				self.disdd = rs.string_to_f(rs.del_caracter(self.dstd)) - rs.string_to_f(self.dsp)
				self.disdd = rs.float_to_s(self.disdd) 

				self.window['-DIS_TR-'].update( self.dstr )
				self.window['-DIS_TD-'].update( self.dstd )
				self.window['-DICA-'].update( self.dica )

				self.window['-DIS_DD-'].update( self.disdd )


			self.window['-MO-'].update( self.window['-DISPLAY_M-'].get() )
			self.window['-CE-'].update( self.window['-DISPLAY_C-'].get() )
			self.window['-DINPDV-'].update( self.window['-DIS_TD-'].get() )
			self.window['-RESULT-'].update( rs.float_to_s( rs.string_to_f( rs.del_caracter(self.window['-DICA-'].get())) - rs.string_to_f( rs.del_caracter(self.window['-DINPDV-'].get()))))

	def login(self):

		self.lmenu = [ ['Arquivo', ['Configurações', 'Sair']], ['Sobre', ['Ajuda', 'Sobre o Desenvolvedor']] ]

		self.lgroup = [	[sg.Text('Por favor entre com seus dados de login')], [sg.Column([ [sg.Text('Usuário:'), sg.Input('', size=(26,1), key='-USR-')], [sg.Text('Senha  :'), sg.Input('', password_char='*' ,size=(26,1), key='-PWD-')], [sg.Text('',)], [sg.Text('', key='-LBL-')]],  element_justification='r', expand_x=True ) ]]

		self.l_login = [	[sg.Menu(self.lmenu)], [sg.Frame('Dados de Login', self.lgroup, expand_x=True)], 
							[sg.Column([[sg.Button('OK', size=(7,1)), sg.Button('Cancelar', size=(7,1))]], element_justification='r', expand_x=True)]
								] 
		self.window = sg.Window('Login - CalcFecPDV', size=(350,240), return_keyboard_events=True, layout=self.l_login, keep_on_top=True,  grab_anywhere=True, use_custom_titlebar=True, titlebar_icon=mainWindowIcon_32, titlebar_font=(sg.DEFAULT_FONT, 12, 'bold'), icon=mainWindowIcon_64)
		self.window.read(timeout=1)
		while True:
			self.event, self.values = self.window.read()

			if self.event in ('Cancelar', 'Sair', None, sg.WIN_CLOSED):
				self.window.close()
				sys.exit()

			if self.event in ('OK', '\r'):
				if len(self.values['-USR-']) and len(self.values['-PWD-']):
					usr = self.values['-USR-']
					pwd = self.values['-PWD-']
					usr = usr.capitalize()
					usr.upper()
					pwd = pwd.lower()
					try:
						self.user, self.func, self.pwd = Control_DB.login_users(usr)
						if self.user == usr and self.pwd == pwd:
							self.window.close()
							MainApp.calcfecpdv(self, self.user, self.func ,self.pwd)
						else:
							self.window['-PWD-'].Update('')
							self.window['-LBL-'].Update('Senha inválida')

					except sqlite3.OperationalError as error:
						print(error)
						if str(error) == ('no such table: {}'.format(usr)):
							self.window['-LBL-'].Update('Usuário não cadrastrado')

			if self.event == 'Configurações':
				self.window.close()
				MainApp.configs(self)

			if self.event in sg.theme_list():

				self.window.close()
				Control_DB.login_cfgs_in(self.event)
				sg.theme(theme())
				MainApp.login(self)

		self.window.close()

	def configs(self):
		self.printer_defualt = win32print.GetDefaultPrinter()

		self.lmenu = [ ['Arquivo', ['Salvar', 'Sair']], ['Sobre', ['Ajuda', 'Sobre o Desenvolvedor']] ]
		
		self.configs_user = [	
								[sg.Frame('Cadastro de usuário',
									[
										[sg.Button('Cadastrar novo usuário', expand_x=True)]
									], expand_x=True)],	

								[sg.Frame('Usuários Cadastrados',
									[
										[sg.Listbox(values = ['Leonardo', 'Ana', 'Leidi'], size =(50, 8), key ='-USERS_DB-', enable_events = True)],
										[sg.Button('Excluir', expand_x=True), sg.Button('Alterar Senha', expand_x=True)]
									]
								)]
							]

		self.configs_imp = [	[sg.Menu(self.lmenu)],
										[sg.Frame('Nome da Empresa',
											[
												[sg.Input('BIG LAR MAGAZINE - TOME-AÇÚ', expand_x=True)]
											], expand_x=True
										)],

										[sg.Frame('Definições padrão de Impressão', 
											[
												[sg.Text('Impressora padrão:'), sg.Combo( MainApp.printers(), default_value=self.printer_defualt, expand_x=True, readonly=True, key='-PRINTERS-')],
												[sg.Text('')],
												[sg.Radio('Detalhado', "impressao", default=True, size=(10,1), k='-R1-'), sg.Radio('Resumido', "impressao", default=False, size=(10,1), k='-R2-')], 
												[sg.Radio('Modelo 1', "pagina", default=True, size=(10,1), k='-R3-'), sg.Radio('Modelo 2', "pagina", default=False, size=(10,1), k='-R4-')]
											], expand_x=True
										)],
										[sg.Text('')],
										[sg.Button('Salvar', size=(7, 1), expand_x=True)]
										
									]

		self.theming = 	[
							[sg.Frame('Tema atual', 
								[ 
									[sg.Text(theme(), size=(40, 1), background_color=sg.theme_input_background_color(), text_color=sg.theme_input_text_color() ,justification='c',expand_x=True)]], 
									expand_x=True
								)],
							[sg.Frame('Definir novo tema', 
                    			[
                    				[sg.Listbox(values = sg.theme_list(), size =(50, 8), key ='-THEME_CF-', enable_events = True)],
                      			]
								)],
							[sg.Button("Definir tema", expand_x=True)]
						]

		
		self.configs_tabs =	[
								[
									sg.Tab('Usuários', self.configs_user),
									sg.Tab('Impressão', self.configs_imp),
									sg.Tab('Temas', self.theming)
								]
							]

		self.layout = 	[
							[sg.TabGroup(self.configs_tabs)],
							[sg.Column( [[sg.Button('Voltar', size=(10,1)), sg.Button('Sair', size=(10, 1))]], element_justification='r', expand_x=True )]
				
						]

		self.window = sg.Window('Configurações', size=(372,365),return_keyboard_events=True, layout=self.layout, keep_on_top=True,  grab_anywhere=True, use_custom_titlebar=True, titlebar_icon=mainWindowIcon_32, titlebar_font=(sg.DEFAULT_FONT, 12, 'bold'), icon=mainWindowIcon_64)
		self.window.read(timeout=1)
		while True:
			self.event, self.values = self.window.read()
			if self.event in ('Sair', None, sg.WIN_CLOSED):
				self.window.close()
				sys.exit()
			if self.event == ('Voltar'):
				self.window.close()
				MainApp.login(self)
			if self.event == 'Cancelar':
				self.window.close()
				MainApp.login(self)
			if self.event == 'Salvar':
				print(self.values)
			if self.event == 'Cadastrar novo usuário':
				self.window.close()
				MainApp.add_users(self)

			if self.event == 'Definir tema':
				self.window.close()
				Control_DB.login_cfgs_in(self.values['-THEME_CF-'][0])
				sg.theme(theme())
				MainApp.configs(self)

MainApp().login()
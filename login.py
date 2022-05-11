#coding: utf-8

from PySimpleGUI import PySimpleGUI as sg

sg.theme('BrightColors')


class MainApp():
	def __init__(self):
		pass

	def calcfecpdv(self):
		print('ok')
	def login(self):

		self.lmenu = [ ['Arquivo', ['Cadrastra Usuário', 'Calculara', 'Sair']], ['Sobre', ['Ajuda', 'Sobre o Desenvolvedor']] ]

		self.lgroup = [	[sg.Text('Por favor entre com seus dados de login')], [sg.Column([ [sg.Text('Usuário:'), sg.Input('', size=(26,1))], [sg.Text('Senha  :'), sg.Input('', size=(26,1))], [sg.Text('')]],  element_justification='r', expand_x=True ) ]]

		self.l_login = [	[sg.Menu(self.lmenu)], [sg.Frame('Dados de Login', self.lgroup, expand_x=True)], 
							[sg.Column([[sg.Button('Ok', size=(7,1)), sg.Button('Cancelar', size=(7,1))]], element_justification='r', expand_x=True)]	
								] 
		self.window = sg.Window('Login - CalcFecPDV', icon='ico.ico', size=(350,180), layout=self.l_login)
		
		while True:
			self.event, self.values = self.window.read()
			if self.event in ('Cancelar', 'Sair', None, sg.WIN_CLOSED):
				break
			if self.event == 'Logar':
				self.window.close()
				MainApp().calcfecpdv()
		self.window.close()

MainApp().login()
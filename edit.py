import PySimpleGUI as sg
import sys


if len(sys.argv) == 1:
	arg = ''
	tmp = arg
elif len(sys.argv) == 2:
	arg = sys.argv[1]
	db = open( arg ,'r')
	tmp = db.read()
	db.close()


sg.theme('Dark')

# tmp = open('tmp.txt', 'r')
# text = tmp.read()
# tmp.close()

class MainApp():
	def __init__(self):
		pass

	def edit(self):

		self.menu =	[
						['Arquivo', ['Abrir', 'Fechar', 'Imprimir', 'Sair']], 
						['Ajuda']
					]
		self.layout = 	[
							[sg.Menu( self.menu )],
							
							[sg.Multiline(tmp,expand_x=True, expand_y=True, disabled=True, font=('Consolas'), key='-TEXT-' )]
						]

		self.window = self.window = sg.Window('Editor CalcFecPDV-GUI',size=(400, 400), layout=self.layout, finalize=True, resizable=True)
		self.window.maximize()
		
		while True:
			self.event, self.values = self.window.read(timeout=1)
			if self.event in ('Sair', sg.WIN_CLOSED):
				sys.exit()
			if self.event == 'Fechar':
				self.window['-TEXT-'].Update('')



MainApp().edit()
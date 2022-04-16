# coding: utf-8

__author__ = 'Leonardo Sousa'

__version__ = 'versão 1.2.7'

'''
#################################################
                 CALCULADORA
#################################################
'''



import PySimpleGUI as sg
from module import calc
import configparser

cfg = configparser.ConfigParser()
cfg.read('configs.ini')

sg.theme(cfg.get('configs', 'tema'))

# Menu layout

menu_layout = [  ['Arquivo',['Salvar', 'Sair']],
            ['Config', ['Temas']],
            ['Ajuda', ['Sobre']] ]
vvalor = 'R$ 0,00'
# menu

layout = [      [sg.Menu(menu_layout)], 

# row 1
                [sg.Input(vvalor, justification='right', readonly=True, disabled_readonly_text_color='SpringGreen4', size=(24,1), font=('Consolas', 14), key='-CAIXAI-' ), 
                sg.Input(' ', justification='center' ,  readonly=True, disabled_readonly_text_color='SpringGreen4', font=('Consolas', 10), size=(2,1), key='-OP-'), 
                sg.Button('←',  expand_x=True, expand_y=True, font=('Consolas', 10), size=(2,1), key='-APAGAR-'), 
                sg.Button('C', expand_x=True, expand_y=True,  font=('Consolas', 10), size=(2,1), key='-LIMPAR-')],

# row 2              
                [sg.Input(vvalor, justification='right',  readonly=True, disabled_readonly_text_color='SpringGreen4', expand_x=True, expand_y=True, size=(23, 1), font=('Consolas', 25), key='-CAIXAII-' )],

# row 3
                [sg.Button('7', expand_x=True, expand_y=True,font=('Consolas', 16), size=(2,1), key='-SETE-'),
                sg.Button('8', expand_x=True, expand_y=True, font=('Consolas', 16), size=(2,1),key='-OITO-'),
                sg.Button('9', expand_x=True, expand_y=True, font=('Consolas', 16), size=(2,1),key='-NOVE-'),
                sg.Button('-', expand_x=True, expand_y=True, font=('Consolas', 16), size=(2,1),key='-MENOS-'),
                sg.Button('+', expand_x=True, expand_y=True, font=('Consolas', 16), size=(2,1),key='-MAIS-'),
                sg.Button('±', expand_x=True, expand_y=True, font=('Consolas', 16), size=(2,1),key='-MM-')],

  
                [sg.Button('4', expand_x=True, expand_y=True, font=('Consolas', 16), size=(2,1),key='-QUATRO-'),
                sg.Button('5', expand_x=True, expand_y=True, font=('Consolas', 16), size=(2,1),key='-CINCO-'),
                sg.Button('6', expand_x=True, expand_y=True, font=('Consolas', 16), size=(2,1),key='-SEIS-'),
                sg.Button('/', expand_x=True, expand_y=True, font=('Consolas', 16), size=(2,1),key='-DIVIDI-'), 
                sg.Button('*', expand_x=True, expand_y=True, font=('Consolas', 16), size=(2,1),key='-MULTIPLICAR-'),
                sg.Button('%', expand_x=True, expand_y=True,  font=('Consolas', 16), size=(2,1),key='-PORCENTO-')],


                [sg.Button('1', expand_x=True, expand_y=True, font=('Consolas', 16), size=(2,1),key='-UM-'),
                sg.Button('2', expand_x=True, expand_y=True, font=('Consolas', 16), size=(2,1),key='-DOIS-'),
                sg.Button('3', expand_x=True, expand_y=True, font=('Consolas', 16), size=(2,1),key='-TRES-'), 
                sg.Button('0', expand_x=True, expand_y=True, font=('Consolas', 16), size=(2,1),key='-ZERO-'),
                sg.Button(',', expand_x=True, expand_y=True,  font=('Consolas', 16), size=(2,1),key='-PONTO-'),
                sg.Button('=', expand_x=True, expand_y=True,  font=('Consolas', 16), size=(2,1),key='-RESULT-')] ]



class App():
    def __init__(self):
        self.window = sg.Window('PyCalculator', return_keyboard_events=True, icon='ico.ico',layout=layout, margins=(0, 0), resizable=False)
        self.result = None
        self.operesult = None
        self.oper = None
        self.window.read(timeout=1)

    def start(self):
        while True:
                event, self.values = self.window.read()
# Fechar janela
                if event in ('Sair', sg.WIN_CLOSED, 'Escape:27'):
                        break

# Limpas as duas telas
                if event == '-LIMPAR-' or event == 'Delete:46':
                        self.window['-CAIXAII-'].Update(vvalor)
                        self.window['-CAIXAI-'].Update(vvalor)
                        self.window['-OP-'].Update('')
# Apagar ultimo numero digitado
                if event in ('-APAGAR-', 'BackSpace:8', ','):
                        self.window['-CAIXAII-'].Update ( calc.str_real_format(  calc.insert_cls( calc.float_calc_format (self.values['-CAIXAII-']    ))))
                        if self.values['-CAIXAII-'] == 'R$ -0,00':
                                self.window['-CAIXAII-'].Update(vvalor)





# Operador de somar
                if event in ('-MAIS-',  '+'):

                        self.oper = '+'
                        self.window['-CAIXAI-'].Update(self.values['-CAIXAII-'])
                        self.window['-OP-'].Update(self.oper)
                        self.window['-CAIXAII-'].Update(vvalor)
                        if self.values['-CAIXAI-'] == vvalor:
                               self.window['-CAIXAI-'].Update(self.values['-CAIXAII-'])
                               if self.values['-CAIXAII-'] != vvalor:
                                        self.result = calc.str_real_format( calc.insert_result( calc.float_calc_format( self.values['-CAIXAII-'] ) + calc.float_calc_format( self.values['-CAIXAI-'] )) )
                                        self.window['-CAIXAII-'].Update(vvalor)
                        else:
                                self.result = calc.str_real_format( calc.insert_result( calc.float_calc_format( self.values['-CAIXAI-'] ) + calc.float_calc_format( self.values['-CAIXAII-'] )) )
                                self.window['-CAIXAII-'].Update(vvalor)
                                self.window['-CAIXAI-'].Update(self.result)



# Operador de subitração

                if event in ('-MENOS-',  '-'):
                        self.oper = '-'
                        self.window['-CAIXAI-'].Update(self.values['-CAIXAII-'])
                        self.window['-OP-'].Update(self.oper)
                        self.window['-CAIXAII-'].Update(vvalor)
                        if self.values['-CAIXAI-'] == vvalor:
                               self.window['-CAIXAI-'].Update(self.values['-CAIXAII-'])
                               if self.values['-CAIXAII-'] != vvalor:
                                        self.result = calc.str_real_format( calc.insert_result( calc.float_calc_format( self.values['-CAIXAII-'] ) - calc.float_calc_format( self.values['-CAIXAI-'] )) )
                                        self.window['-CAIXAII-'].Update(vvalor)
                        else:
                                self.result = calc.str_real_format( calc.insert_result( calc.float_calc_format( self.values['-CAIXAI-'] ) - calc.float_calc_format( self.values['-CAIXAII-'] )) )
                                self.window['-CAIXAII-'].Update(vvalor)
                                self.window['-CAIXAI-'].Update(self.result)



# Operador de multiplicação


                if event in ('-MULTIPLICAR-',  '*'):
                        self.oper = '*'
                        self.window['-CAIXAI-'].Update(self.values['-CAIXAII-'])
                        self.window['-OP-'].Update(self.oper)
                        self.window['-CAIXAII-'].Update(vvalor)
                        if self.values['-CAIXAI-'] == vvalor:
                               self.window['-CAIXAI-'].Update(self.values['-CAIXAII-'])
                               if self.values['-CAIXAII-'] != vvalor:
                                        self.result = calc.str_real_format( calc.insert_result( calc.float_calc_format( self.values['-CAIXAII-'] ) * calc.float_calc_format( self.values['-CAIXAI-'] )) )
                                        self.window['-CAIXAII-'].Update(vvalor)
                        else:
                                self.result = calc.str_real_format( calc.insert_result( calc.float_calc_format( self.values['-CAIXAI-'] ) * calc.float_calc_format( self.values['-CAIXAII-'] )) )
                                self.window['-CAIXAII-'].Update(vvalor)
                                self.window['-CAIXAI-'].Update(self.result)



# Operador de divisão





# Ver Resultado
                if event in ('-RESULT-', '\r'):
                        if self.oper == '+':
                                self.result = calc.str_real_format( calc.insert_result( calc.float_calc_format( self.values['-CAIXAI-'] ) + calc.float_calc_format( self.values['-CAIXAII-'] )) )
                        elif self.oper == '-':
                                self.result = calc.str_real_format( calc.insert_result( calc.float_calc_format( self.values['-CAIXAI-'] ) - calc.float_calc_format( self.values['-CAIXAII-'] )) )

                        elif self.oper == '*':
                                self.result = calc.str_real_format( calc.insert_result( calc.float_calc_format( self.values['-CAIXAI-'] ) * calc.float_calc_format( self.values['-CAIXAII-'] )) )


                        self.window['-CAIXAI-'].Update(vvalor)
                        self.window['-CAIXAII-'].Update(self.result)
                        self.window['-OP-'].Update('')








# pelo keyboard

                if event in ('1', '2', '3',  '4', '5',  '6', '7',  '8', '9', '0'):
                        if len(self.values['-CAIXAII-']) >= 23:
                                pass
                        else:
                                self.window['-CAIXAII-'].Update( calc.str_real_format( calc.insert_valor( calc.float_calc_format( self.values['-CAIXAII-']), event ) )   )



# por key
                if event == '-UM-':
                        if len(self.values['-CAIXAII-']) >= 23:
                                pass
                        else:
                                self.window['-CAIXAII-'].Update( calc.str_real_format( calc.insert_valor( calc.float_calc_format( self.values['-CAIXAII-']), '1' ) )   )


                if event == '-DOIS-':
                        if len(self.values['-CAIXAII-']) >= 23:
                                pass
                        else:
                                self.window['-CAIXAII-'].Update( calc.str_real_format( calc.insert_valor( calc.float_calc_format( self.values['-CAIXAII-']), '2' ) )   )


                if event == '-TRES-':
                        if len(self.values['-CAIXAII-']) >= 23:
                                pass
                        else:
                                self.window['-CAIXAII-'].Update( calc.str_real_format( calc.insert_valor( calc.float_calc_format( self.values['-CAIXAII-']), '3' ) )   )


                if event == '-QUATRO-':
                        if len(self.values['-CAIXAII-']) >= 23:
                                pass
                        else:
                                self.window['-CAIXAII-'].Update( calc.str_real_format( calc.insert_valor( calc.float_calc_format( self.values['-CAIXAII-']), '4' ) )   )


                if event == '-CINCO-':
                        if len(self.values['-CAIXAII-']) >= 23:
                                pass
                        else:
                                self.window['-CAIXAII-'].Update( calc.str_real_format( calc.insert_valor( calc.float_calc_format( self.values['-CAIXAII-']), '5' ) )   )


                if event == '-SEIS-':
                        if len(self.values['-CAIXAII-']) >= 23:
                                pass
                        else:
                                self.window['-CAIXAII-'].Update( calc.str_real_format( calc.insert_valor( calc.float_calc_format( self.values['-CAIXAII-']), '6' ) )   )


                if event == '-SETE-':
                        if len(self.values['-CAIXAII-']) >= 23:
                                pass
                        else:
                                self.window['-CAIXAII-'].Update( calc.str_real_format( calc.insert_valor( calc.float_calc_format( self.values['-CAIXAII-']), '7' ) )   )


                if event == '-OITO-':
                        if len(self.values['-CAIXAII-']) >= 23:
                                pass
                        else:
                                self.window['-CAIXAII-'].Update( calc.str_real_format( calc.insert_valor( calc.float_calc_format( self.values['-CAIXAII-']), '8' ) )   )


                if event == '-NOVE-':
                        if len(self.values['-CAIXAII-']) >= 23:
                                pass
                        else:
                                self.window['-CAIXAII-'].Update( calc.str_real_format( calc.insert_valor( calc.float_calc_format( self.values['-CAIXAII-']), '9' ) )   )


                if event == '-ZERO-':
                        if len(self.values['-CAIXAII-']) >= 23:
                                pass
                        else:
                                self.window['-CAIXAII-'].Update( calc.str_real_format( calc.insert_valor( calc.float_calc_format( self.values['-CAIXAII-']), '0' ) )   )


App().start()
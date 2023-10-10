#print documento com python
import win32print
import win32api
import os
import time
lista_impressoras = win32print.EnumPrinters(4) # 2 impressoras locais e 4 impressoras em rede
print(lista_impressoras)

default = win32print.GetDefaultPrinter() # verificar impressora default
impressora = lista_impressoras[1] # index da impressora selecionda
win32print.SetDefaultPrinter(impressora[2]) # Nome da impressora selecionada

win32api.ShellExecute(0, 'print', 'resumida.txt', None, r'D:\Leo s files\Projects\PySimpleGUI\calcFecPDV-GUI\print', 0) #impressao da pagina com a impressora selecionada

'''ShellExecute(0,            // NULL since it's not associated with a window
             "print",        // execute the "print" verb defined for the file type
             path_for_file, // path to the document file to print
             None,         // no parameters, since the target is a document file
             ".",         // current directory, same as NULL here
             0)          // SW_HIDE passed to app associated with the file type'''

time.sleep(1) # delay
win32print.SetDefaultPrinter(default) # selecionar novamente a impressora que ao inicar era a default
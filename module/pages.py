from datetime import datetime

#data = datetime.today().strftime('%d/%m/%Y')
#hora = datetime.today().strftime('%H:%M:%S')

class Page_Printers():


	def resumido_page_1(user = None, trec = ' R$ 0,00',tdin = ' R$ 0,00', moe = ' R$ 0,00', ced = ' R$ 0,00', desp2 = ' R$ 0,00', said = ' R$ 0,00', troc = ' R$ 0,00',vdc = ' R$ 0,00', res = ' R$ 0,00'):
		def print_values(x):
			if x == None or x == '':
				x = ' R$ 0,00'

			x = ((16 - len(x)) * ' ' + x)
			return x

		trec = print_values(trec)
		tdin = print_values(tdin)
		moe = print_values(moe)
		ced = print_values(ced)
		desp2 = print_values(desp2)
		said = print_values(said)
		troc = print_values(troc)
		vdc = print_values(vdc)
		res = print_values(res)

		tmp = '''=================================
   BIG LAR MAGAZINE - TOME-ACU    
=================================
Data: {}   Hora: {}
Usuário: {}
=================================
  RESUMO DE FECHAMENTO DO CAIXA  
           (Resumido)            
=================================
Total Recebido:  {}
Total Dinheiro:  {}
=================================
Moedas:          {}
Cedulas:         {}
Despesas:        {}
Saidas:          {}
Trocados:        {}
=================================
Valor do Caixa:  {}
=================================
Resumo do dia:   {}

_________________________________
         VISTO DO CAIXA          
================================='''.format(datetime.today().strftime('%d/%m/%Y'), datetime.today().strftime('%H:%M:%S'), user, trec,tdin, moe, ced, desp2, said, troc ,vdc, res )
		with open(r'settings\tmp\resumido_page_1.txt', 'w') as db:
			db.write(tmp)
			db.close()

	def resumido_page_2(trec = ' R$ 0,00',tdin = ' R$ 0,00', moe = ' R$ 0,00', ced = ' R$ 0,00', desp2 = ' R$ 0,00', said = ' R$ 0,00', troc = ' R$ 0,00',vdc = ' R$ 0,00', res = ' R$ 0,00', user = 'Admin'):
		def print_values(x):
			if x == None or x == '':
				x = ' R$ 0,00'

			x = ((57 - len(x)) * ' ' + x)
			return x

		def print_values_2(x):
			if x == None or x == '':
				x = ' R$ 0,00'

			x = ((18 - len(x)) * ' ' + x)
			return x

		trec = print_values(trec)
		tdin = print_values(tdin)
		moe = print_values(moe)
		ced = print_values(ced)
		desp2 = print_values(desp2)
		said = print_values(said)
		troc = print_values(troc)
		vdc = print_values_2(vdc)
		res = print_values_2(res)

		tmp = '''===============================================================================================
BIG LAR MAGAZINE - TOME-ACU                                                    Data: {}
RESUMO DE FECHAMENTO DO CAIXA             (Resumido)                           Hora:   {}
          ---------------------------------------------------------------------------          
          Total Recebido:   {}
          Total Dinheiro:   {}  
          ---------------------------------------------------------------------------
          Moedas:           {}
          Cedulas:          {}
          Despesas:         {}
          Saidas:           {}
          Trocados:         {}
          ---------------------------------------------------------------------------          


                              -----------------------------------                              
                              Valor do Caixa:  {}                  
                              -----------------------------------                              
                              Resumo do dia:   {}
                              -----------------------------------                              
                                                                                               
                                                                                               
                                                                                               
                                                                                               
                                                                                               
                                                                                               
Usuário: {}   
Visto do Responsavel: ______________________________
==============================================================================================='''.format(datetime.today().strftime('%d/%m/%Y'), datetime.today().strftime('%H:%M:%S'), trec,tdin, moe, ced, desp2, said, troc ,vdc, res, user )
		with open(r'settings\tmp\resumido_page_2.txt', 'w') as db:
			db.write(tmp)
			db.close()



	def detalhado_page_1(user = 'Leonardo', rec = ' R$ 0,00', va = ' R$ 0,00',vda = ' R$ 0,00',ca = ' R$ 0,00', pix = ' R$ 0,00',cac = ' R$ 0,00',desp = ' R$ 0,00',trec = ' R$ 0,00',tdin = ' R$ 0,00', dedia = ' R$ 0,00', moe = ' R$ 0,00', ced = ' R$ 0,00', desp2 = ' R$ 0,00', said = ' R$ 0,00', troc = ' R$ 0,00',vdc = ' R$ 0,00', res = ' R$ 0,00'):

		def print_values(x):
			if x == None or x == '':
				x = ' R$ 0,00'
				
			x = ((16 - len(x)) * ' ' + x)
			return x

		rec = print_values(rec)
		va = print_values(va)
		vda = print_values(vda)
		ca = print_values(ca)
		pix = print_values(pix)
		cac = print_values(cac)
		desp = print_values(desp)
		trec = print_values(trec)
		tdin = print_values(tdin)
		dedia = print_values(dedia)
		moe = print_values(moe)
		ced = print_values(ced)
		desp2 = print_values(desp2)
		said = print_values(said)
		troc = print_values(troc)
		vdc = print_values(vdc)
		res = print_values(res)

		tmp = '''=================================
   BIG LAR MAGAZINE - TOME-ACU   
=================================
Data: {}   Hora: {}
Usuário: {}
=================================
  RESUMO DE FECHAMENTO DO CAIXA  
           (Detalhado)                       
=================================
Recibos:         {}
Venda avista:    {}
Venda a prazo:   {}
Cartao:          {}
Pagto Pix:       {}
Carta credito:   {}
Despedas:        {}
=================================
Total Recebido:  {}
Total Dinheiro:  {}
=================================
Deposito Diario: {}
=================================
Moedas:          {}
Cedulas:         {}
Despesas:        {}
Saidas:          {}
Trocados:        {}
=================================
Valor do Caixa:  {}
=================================
Resumo do dia:   {}

_________________________________
         VISTO DO CAIXA          
================================='''.format(datetime.today().strftime('%d/%m/%Y'), datetime.today().strftime('%H:%M:%S'), user, rec, va,vda,ca, pix,cac,desp,trec,tdin, dedia, moe, ced, desp2, said, troc ,vdc, res ) 
		with open(r'settings\tmp\detalhado_page_1.txt', 'w') as db:
			db.write(tmp)
			db.close()



	def detalhado_page_2(rec = ' R$ 0,00', va = ' R$ 0,00',vda = ' R$ 0,00',ca = ' R$ 0,00', pix = ' R$ 0,00',cac = ' R$ 0,00',desp = ' R$ 0,00',trec = ' R$ 0,00',tdin = ' R$ 0,00', dedia = ' R$ 0,00', moe = ' R$ 0,00', ced = ' R$ 0,00', desp2 = ' R$ 0,00', said = ' R$ 0,00', troc = ' R$ 0,00',vdc = ' R$ 0,00', res = ' R$ 0,00', user = 'Admin'):

		def print_values(x):
			if x == None or x == '':
				x = ' R$ 0,00'
				
			x = ((57 - len(x)) * ' ' + x)
			return x

		def print_values_2(x):
			if x == None or x == '':
				x = ' R$ 0,00'

			x = ((18 - len(x)) * ' ' + x)
			return x


		rec = print_values(rec)
		va = print_values(va)
		vda = print_values(vda)
		ca = print_values(ca)
		pix = print_values(pix)
		cac = print_values(cac)
		desp = print_values(desp)
		trec = print_values(trec)
		tdin = print_values(tdin)
		dedia = print_values_2(dedia)
		moe = print_values(moe)
		ced = print_values(ced)
		desp2 = print_values(desp2)
		said = print_values(said)
		troc = print_values(troc)
		vdc = print_values_2(vdc)
		res = print_values_2(res)

		tmp = '''===============================================================================================
BIG LAR MAGAZINE - TOME-ACU                                                    Data: {}
RESUMO DE FECHAMENTO DO CAIXA             (Detalhado)                          Hora:   {}
          ---------------------------------------------------------------------------          
          Recibos:          {}  
          Venda avista:     {}
          Venda a prazo:    {}
          Cartao:           {}
          Pagto Pix:        {}
          Carta credito     {}
          Despedas:         {}    
          ---------------------------------------------------------------------------          
          Total Recebido:   {}      
          Total Dinheiro:   {}     
                              -----------------------------------                              
                              Deposito Diário: {}
          ---------------------------------------------------------------------------         
          Moedas:           {}
          Cedulas:          {}
          Despesas:         {}
          Saidas:           {}
          Trocados:         {}
          ---------------------------------------------------------------------------          
                              Valor do Caixa:  {}             
                              -----------------------------------                              
                              Resumo do dia:   {}
Usuário: {}   
Visto do Responsavel: ______________________________
==============================================================================================='''.format(datetime.today().strftime('%d/%m/%Y'), datetime.today().strftime('%H:%M:%S'), rec, va,vda,ca, pix,cac,desp,trec,tdin, dedia, moe, ced, desp2, said, troc ,vdc, res, user ) 
		with open(r'settings\tmp\detalhado_page_2.txt', 'w') as db:
			db.write(tmp)
			db.close()
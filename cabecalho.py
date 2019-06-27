from datetime import datetime

datahr = datetime.now()

def cabecalho():
    print('****************************************')
    print('*                                      *')
    print('* Aluno: IUDI ZURBA MELGAREJO          *')
    print('*                                      *')
    print('* Curso: ADS11                         *')
    print('*                                      *')
    print(datahr.strftime('* Data: %d/%m/%Y - %H:%M             *'))
    print('*                                      *')
    print('****************************************')
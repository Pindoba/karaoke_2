import datetime
from timeit import repeat
from PyQt5 import uic, QtWidgets
import sqlite3
import time


from pyrsistent import b

numero_id = 0


def iniciar():
    data = datetime.datetime.now()
    data_str = data.strftime("%d/%m/%y")
    nome = 'RAUL ROCK BAR'
    banco = sqlite3.connect('banco_dados.db')
    cursor = banco.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS dados (id INTEGER PRIMARY KEY AUTOINCREMENT, nome text, status text)")
    cursor.execute("INSERT INTO dados (nome, status) VALUES ('" + nome + "', '" + data_str + "')")
    banco.commit()
    banco.close()


def add():
    nome = forme.lineEdit.text()
    status = ''
    if nome == '':
        forme.lineEdit.setText('')
    else:

        try:
            banco = sqlite3.connect('banco_dados.db')
            cursor = banco.cursor()
            cursor.execute("INSERT INTO dados (nome, status) VALUES ('" + nome + "', '" + status + "')")
            banco.commit()
            banco.close()
            print('dados inseridos com sucesso')

        except sqlite3.Error as erro:
            print("deu erro", erro)
            print(nome, status)


    listar_dados()
    forme.lineEdit.setText("")


def listar_dados():
    banco = sqlite3.connect('banco_dados.db')
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM dados")
    # cursor.execute("SELECT * FROM dados WHERE status = ''")
    dados_lidos = cursor.fetchall()
    forme.tableWidget.setRowCount(len(dados_lidos))
    forme.tableWidget.setColumnCount(4)
    # soma = 0
    # linha = forme.tableWidget.currentRow()
    banco.close()

    falta = [(range(0, len(dados_lidos), 1))]
    # print(falta)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 3):
            forme.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
    for i in range(1, len(dados_lidos)):
        for j in range(2, 3):
            forme.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem('Falta '+str(falta[0][i])+' pessoas - '+ str(int(falta[0][i]*5.3))+' Min.'))
    forme.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem('PRÓXIMO'))
    hora_atualiza()


def excluir():
    linha = forme.tableWidget.currentRow()
    forme.tableWidget.removeRow(linha)
    banco = sqlite3.connect('banco_dados.db')

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM dados")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM dados WHERE id=" + str(valor_id))
    banco.commit()
    banco.close()
    listar_dados()
    hora_atualiza()


def editar():
    linha = forme.tableWidget.currentRow()
    global numero_id
    banco = sqlite3.connect('banco_dados.db')

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM dados")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM dados WHERE id=" + str(valor_id))
    status = cursor.fetchall()
    numero_id = valor_id
    hora_atualiza()
    
    editor.show()

    editor.lineEdit.setText(str(status[0][0]))
    editor.lineEdit_2.setText(str(status[0][1]))
    editor.lineEdit_3.setText(str(status[0][2]))


def cantou():
    banco = sqlite3.connect('banco_dados.db')
    linha = forme.tableWidget.currentRow()
    cursor = banco.cursor()
    cursor.execute("SELECT id FROM dados")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]

    cursor.execute("SELECT id FROM dados")
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM dados WHERE id=" + str(valor_id))
    status = cursor.fetchall()
    
    banco.close()


    linha = forme.tableWidget.currentRow()
    global numero_id
    banco = sqlite3.connect('banco_dados.db')
    cursor = banco.cursor()
    cursor.execute("SELECT id FROM dados")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM dados WHERE id=" + str(valor_id))
    status = cursor.fetchall()
    nome = status[0][1]
    status_2 = status[0][2]
    data = datetime.datetime.now()
    data_str = data.strftime("%d/%m/%y")
    hora = datetime.datetime.now()
    hora_str = hora.strftime("%H:%M")
    cursor.execute("UPDATE dados SET status = 'Cantou' WHERE id = " + str(valor_id))
    cursor.execute("CREATE TABLE IF NOT EXISTS cantou (id INTEGER PRIMARY KEY AUTOINCREMENT, nome text, status text, data text, hora text)")
    cursor.execute("INSERT INTO cantou (nome, status, data, hora) VALUES ('" + nome + "', '" + status_2 + "', '" + data_str + "', '" + hora_str + "')")
    cursor.execute("DELETE FROM dados WHERE id=" + str(valor_id))
    banco.commit()
    forme.tableWidget.removeRow(linha)
    listar_dados()
    banco.close()


def salvar():
    global numero_id
    nome = editor.lineEdit_2.text()
    status = editor.lineEdit_3.text()
    banco = sqlite3.connect('banco_dados.db')
    cursor = banco.cursor()
    cursor.execute("UPDATE dados SET nome = '{}', status = '{}' WHERE id = {}".format(nome, status, numero_id))
    banco.commit()


    listar_dados()
    banco.close()
    editor.close()
    hora_atualiza()

def hora_atualiza():
    hora = datetime.datetime.now()
    hora_str = hora.strftime("%H:%M")
    forme.label_4.setText(hora_str)
    # print(hora_str)


def histo():
    historico.show()
    banco = sqlite3.connect('banco_dados.db')
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM cantou")
    # cursor.execute("SELECT * FROM dados WHERE status = ''")
    dados_lidos = cursor.fetchall()
    historico.tableWidget.setRowCount(len(dados_lidos))
    historico.tableWidget.setColumnCount(5)

    linha = forme.tableWidget.currentRow()


    banco.close()


    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
            historico.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    hora_atualiza()


app = QtWidgets.QApplication([])

forme = uic.loadUi("karaoke.ui")

editor = uic.loadUi("editar.ui")
historico = uic.loadUi("historico.ui")
forme.show()

iniciar()
listar_dados()
hora_atualiza()


forme.pushButton_5.clicked.connect(add)
forme.pushButton_9.clicked.connect(listar_dados)
forme.pushButton_4.clicked.connect(excluir)
forme.pushButton_2.clicked.connect(editar)
forme.pushButton.clicked.connect(cantou)
editor.pushButton.clicked.connect(salvar)
forme.pushButton_3.clicked.connect(histo)

# time.sleep(2)


app.exec_()

# while 1:
#     hora_atualiza()
#     time.sleep(2)



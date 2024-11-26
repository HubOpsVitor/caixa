import sys
# importar os componentes para a construção da janela
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTableView, QBoxLayout, QVBoxLayout, QHBoxLayout
# construção do class janela com nome da caixa
class caixa(QWidget):
# criação do método _init_ que inicia a janela e exibe em tela
    def __init__(self):
        super().__init__()
# vamos definir a posição e o tamanho de tela
        self.setGeometry(0,30,1000,800)
# agora o título da janela
        self.setWindowTitle("Caixa da Loja")

# vamos criar as labels que representam as colunas esquerda e direita
        
        #label da esquerda
        self.label_coluna_esquerda = QLabel()
        self.label_coluna_esquerda.setStyleSheet("QLabel{background-color:#04ab77}")
#label da esquerda
        self.label_coluna_direita = QLabel()
        self.label_coluna_direita.setStyleSheet("QLabel{background-color:#04ab90}")
# criar o layout horizontal para as colunas
        self.h_layout = QHBoxLayout()
# vamos adicionar as colunas da esquerda e da direita ao layout horizontal
        self.h_layout.addWidget(self.label_coluna_esquerda)
        self.h_layout.addWidget(self.label_coluna_direita)
# adicionar o layout na tela
        self.setLayout(self.h_layout)

app = QApplication(sys.argv)
cx = caixa()
cx.show()
app.exec_()

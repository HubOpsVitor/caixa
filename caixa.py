import sys
# importar os componentes para a construção da janela
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTableWidget, QBoxLayout, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap
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
        self.label_coluna_esquerda.setStyleSheet("QLabel{background-color:#2f99bd}")
#label da direita
        self.label_coluna_direita = QLabel()
        self.label_coluna_direita.setStyleSheet("QLabel{background-color:#2f99bd}")

# - - - - - - - - Criar o conteúdo da coluna da esquerda!!!
        self.v_layout_esquerda = QVBoxLayout()

# Vamos criar uma label pra adcionar a logo da nossa loja
        self.logo_label = QLabel()
        self.logo_label.setPixmap(QPixmap("C:/Users/allan.vssilva1/Documents/Janela Caixa/.venv/logo.png"))
# Ajudar a label e a image para ficar no tamanho ideal
        self.logo_label.setScaledContents(True)
        self.logo_label.setFixedHeight(200)
# adicionar a label com a imagem na tela
        self.v_layout_esquerda.addWidget(self.logo_label)

# Vamos cruar as labels e as LineEdis que irão ficar na coluna da esquerda
# dentro do layout vertical da esquerda
        self.codigo_produto_label = QLabel("Código do Produto")
        self.codigo_produto_label.setStyleSheet("QLabel{font-size:15pt;}")
        self.codigo_produto_edit = QLineEdit()
        self.v_layout_esquerda.addWidget(self.codigo_produto_label)
        self.v_layout_esquerda.addWidget(self.codigo_produto_edit)

        self.nome_produto_label = QLabel("Nome do Produto")
        self.nome_produto_label.setStyleSheet("QLabel{font-size:15pt;}")
        self.nome_produto_edit = QLineEdit()
        self.v_layout_esquerda.addWidget(self.nome_produto_label)
        self.v_layout_esquerda.addWidget(self.nome_produto_edit)

        self.descricao_produto_label = QLabel("Descrição do Produto")
        self.descricao_produto_label.setStyleSheet("QLabel{font-size:15pt;}")
        self.descricao_produto_edit = QLineEdit()
        self.descricao_produto_label.setStyleSheet("QLabel{padding 10px}")
        self.v_layout_esquerda.addWidget(self.descricao_produto_label)
        self.v_layout_esquerda.addWidget(self.descricao_produto_edit)

        self.quantidade_produto_label = QLabel("Quantidade do Produto")
        self.quantidade_produto_label.setStyleSheet("QLabel{font-size:15pt;}")
        self.quantidade_produto_edit = QLineEdit()
        self.v_layout_esquerda.addWidget(self.quantidade_produto_label)
        self.v_layout_esquerda.addWidget(self.quantidade_produto_edit)

        self.preco_produto_label = QLabel("Preço Unitário do Produto")
        self.preco_produto_label.setStyleSheet("QLabel{font-size:15pt;}")
        self.preco_produto_edit = QLineEdit()
        self.v_layout_esquerda.addWidget(self.preco_produto_label)
        self.v_layout_esquerda.addWidget(self.preco_produto_edit)

        self.subtotal_produto_label = QLabel("Subtotal: ")
        self.subtotal_produto_label.setStyleSheet("QLabel{font-size:15pt;}")
        self.subtotal_produto_edit = QLineEdit()
        self.v_layout_esquerda.addWidget(self.subtotal_produto_label)
        self.v_layout_esquerda.addWidget(self.subtotal_produto_edit)

# adicionar layout vertical da esquerda com todos os controles: label e lineEdit dentro da coluna
# da coluna da esqueda(label_coluna_esquerda) 
        self.label_coluna_esquerda.setLayout(self.v_layout_esquerda)


# - - - - - - - - Controles da coluna da direita!!!
        self.v_layout_direita = QVBoxLayout()
        
        # Criar uma tabela e adicionar na coluna da direita, esta tabela terá o nome dos campos que estão na direita
        
        # Colunas da Tabela
        colunas = ["Cod.Produto", "Nome do Produto", "Descrição", "Quantidade", "Preço Unitário", "Subtotal"]
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(6)
        self.tabela.setHorizontalHeaderLabels(colunas)
        self.tabela.setRowCount(10)
        self.v_layout_direita.addWidget(self.tabela)

        self.total_pagar_label = QLabel()
        self.total_pagar_edit = QLineEdit("0,00")
        self.v_layout_direita.addWidget(self.total_pagar_label)
        self.v_layout_direita.addWidget(self.total_pagar_edit)

        self.label_coluna_direita.setLayout(self.v_layout_direita)



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

import sys
import qdarkstyle
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QFileDialog
from reports_generator import generate_report
import os

# Interface
def main():
  # Criação do app qt
  app = QApplication(sys.argv)
  app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
  
  # Janela do app
  window = QWidget()
  window.setWindowTitle('Gerador de Relatórios')
  window.setGeometry(100, 100, 400, 300) # Posição e tamanho da janela
  
  # Layout vertical
  layout = QVBoxLayout()
  
  # Mensagem de "welcome"
  label = QLabel('Bem-vindo ao seu gerador automático de relatórios!', window)
  layout.addWidget(label)
  
  # Form para captura de dados do user
  name_input = QLineEdit(window)
  name_input.setPlaceholderText('Seu Nome')
  layout.addWidget(name_input)
  
  date_input = QLineEdit(window)
  date_input.setPlaceholderText('Data que o documento esta sendo gerado')
  layout.addWidget(date_input)
  
  add_file_btn = QPushButton('Selecionar arquivos a serem lidos', window)
  layout.addWidget(add_file_btn)
  
  selected_file = None
  
  def select_file():
    nonlocal selected_file
    selected_file, _ = QFileDialog.getOpenFileName(window, 'Selecionar Arquivo', "", "All Files (*)")
    if selected_file:
      print(f'Arquivo selecionado: {selected_file}')
    
  add_file_btn.clicked.connect(select_file)
  
  # Função de callback pro botão
  def generate_report():
    name = name_input.text()
    date = date_input.text()
    
    path_options = QFileDialog.Options() # Seleciona o diretório para envio do pdf
    folder = QFileDialog.getExistingDirectory(window, 'Selecione o local para salvar o pdf', options=path_options)
    
    if folder:
      generate_report(name, date, selected_file, folder)
  
  # Botão
  button = QPushButton('Gerar Relatório', window)
  button.clicked.connect(generate_report)
  layout.addWidget(button)
  
  # Config do layout
  window.setLayout(layout)
  
  # Exibir a window
  window.show()
  
  # exec o loop do app
  sys.exit(app.exec_())
  
if __name__ == '__main__':
  main()
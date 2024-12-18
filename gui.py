from PySide6.QtWidgets import QApplication, QMainWindow, QFormLayout, QWidget, QPushButton, QInputDialog, QLineEdit, QVBoxLayout, QLabel, QFileDialog, QCheckBox
from PySide6.QtCore import Qt

import sys

# class EditableTextField(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Ebay Scraping Tool")  

#         self.btn = QPushButton('Dialog', self)
#         self.btn.move(20, 20)
#         self.btn.clicked.connect(self.showDialog)
        
#         self.le = QLineEdit(self)
#         self.le.move(130, 22)
        
#         self.setGeometry(300, 300, 290, 150)
#         self.show()
        
#     def showDialog(self):
#         text, ok = QInputDialog.getText(self, 'Input', 
#             'Enter data here:')
        
#         if ok:
#             self.le.setText(str(text))
            
class ScraperApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ebay Scraper")
        self.setFixedWidth(500)
        self.setFixedHeight(500)
        
        login_form_layout = QFormLayout()
        
        self.username_edit = QLineEdit()
        self.password_edit = QLineEdit()
        self.username_edit.setFixedWidth(120)
        self.password_edit.setFixedWidth(120)

        self.button = QPushButton("Select Existing Excel File")
        self.button.clicked.connect(self.open_file_dialog)
        
        self.create_file_label = QLabel("Create New File?")
        self.create_file_checkbox = QCheckBox()
        
        self.input_file_label = QLabel("Input File Name")
        self.input_file_field = QLineEdit("[Input File Name]")
        
        self.output_file_label = QLabel("Output File Name")
        self.output_file_field = QLineEdit("[Output File Name]")
        
        self.run_button = QPushButton("Run Program")
        
        self.status_label = QLabel("")

        layout = QFormLayout()
        
        login_form_layout.addRow(QLabel(
            "Username"), self.username_edit)
        login_form_layout.addRow(QLabel(
            "Password"), self.password_edit)
        
        layout.addWidget(self.create_file_checkbox)
        layout.addWidget(self.run_button)
        layout.addWidget(self.status_label)
        layout.addWidget(self.button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_file_dialog(self):
        # Open the file dialog
        file_name, _ = QFileDialog.getOpenFileName(
            self, 
            "Select an existing Excel file to store data",
            "",               
            "Excel Files (*.xlsx)"
        )
        if file_name:
            print(f"Selected file: {file_name}")
            self.input_file_field.setText(file_name)
            self.output_file_field.setText(file_name)           

        
def main():
    
    app = QApplication(sys.argv)
    # ex = EditableTextField()
    window = ScraperApp()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
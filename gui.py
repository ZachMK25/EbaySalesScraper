from PySide6.QtWidgets import QApplication, QMainWindow, QFormLayout, QWidget, QPushButton, QInputDialog, QLineEdit, QVBoxLayout, QLabel, QFileDialog, QCheckBox
from PySide6.QtCore import Qt

import sys
import os

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
        
        self.output_file_path = None
        self.input_file_path = None
        
        form_layout = QFormLayout()
        
        self.username_edit = QLineEdit()
        self.password_edit = QLineEdit()
        self.username_edit.setFixedWidth(120)
        self.password_edit.setFixedWidth(120)
        form_layout.addRow(QLabel(
            "Ebay Username"), self.username_edit)
        form_layout.addRow(QLabel(
            "Ebay Password"), self.password_edit)

        self.file_selector_button = QPushButton("Select Existing Excel File")
        self.file_selector_button.clicked.connect(self.open_file_dialog)
        
        self.include_existing_data = QCheckBox()
        form_layout.addRow(QLabel("Include Data from Existing File?"), self.include_existing_data)
        
        self.input_file_field = QLineEdit("[Input File Name]")
        self.input_file_field.setFixedWidth(250)
        form_layout.addRow(QLabel("Input File Name"), self.input_file_field)
        
        form_layout.addWidget(self.file_selector_button)
        
        self.output_file_field = QLineEdit("[Output File Name]")
        self.output_file_field.setFixedWidth(250)
        form_layout.addRow(QLabel("Output File Name"), self.output_file_field)
        self.output_file_field.textChanged.connect(self.change_status_message_on_output_name_update)
        
        self.run_button = QPushButton("Run Program")
        
        self.status_label = QLabel("")
        
        form_layout.addRow(self.status_label)
        form_layout.addRow(self.run_button)
        
        form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignCenter)
        
        
        # set output file name to mirror input file name
        self.input_file_field.textChanged.connect(self.update_output_file_name)
        
        # self.layout.setFormAlignment(Qt.AlignCenter)

        central_widget = QWidget()
        central_widget.setLayout(form_layout)
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
            self.update_output_file_name(file_name)
            
    
    def toggle_output_file_editable(self):
        """Enable or disable the output file field and browse button based on the checkbox state."""
        if self.include_existing_data.isChecked():
            self.input_file_field.setEnabled(True)  
            self.file_selector_button.setEnabled(False)   
        else:
            self.input_file_field.setEnabled(False)
            self.file_selector_button.setEnabled(True)
            
    def change_status_message_on_output_name_update(self, output_file_name):
        if output_file_name and self.input_file_field.text and output_file_name == self.input_file_field.text:
            self.status_label.setText("Warning: Output file will overwrite existing input file.\nMight be safer to give the file a different name to avoid accidental deletion of data.")
        elif output_file_name and self.input_file_field.text and output_file_name != self.input_file_field.text:
            self.status_label.setText("")
              
    def update_output_file_name(self, input_file_name):
        """Automatically update the output file name field to mirror the input file name."""
        if input_file_name:
            base_name = os.path.splitext(os.path.basename(input_file_name))[0]
            self.output_file_field.setText(base_name)
            
            self.status_label.setText("Warning: Output file will overwrite existing input file.\nMight be safer to give the file a different name\n to avoid accidental deletion of data.")
    
    def prep_run_scraper(self):
        input_file_name = self.input_file_field
        output_file_name = self.output_file_field
        
        if self.include_existing_data.isChecked() and not (input_file_name):
            print("invalid configuration: make sure to include an input file if you want to add the scraped data to an existing file")
        # elif self.
            
        
def main():
    
    app = QApplication(sys.argv)
    window = ScraperApp()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
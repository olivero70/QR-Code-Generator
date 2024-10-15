import sys
import qrcode
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import io
from PIL import Image

class QRCodeApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        # Set the window title and size
        self.setWindowTitle('QR Code Generator mit Logo')
        self.setGeometry(100, 100, 300, 500)

        # Create layout
        layout = QVBoxLayout()

        # Create input field for URL/text
        self.text_input = QLineEdit(self)
        self.text_input.setPlaceholderText('Geben Sie den Text oder die URL ein...')
        layout.addWidget(self.text_input)

        # Create label for displaying QR code
        self.qr_label = QLabel(self)
        self.qr_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.qr_label)

        # Create button to select logo
        self.select_logo_button = QPushButton('Logo auswählen', self)
        self.select_logo_button.clicked.connect(self.select_logo)
        layout.addWidget(self.select_logo_button)

        # Create button to generate QR code
        self.generate_button = QPushButton('QR Code generieren', self)
        self.generate_button.clicked.connect(self.generate_qr_code)
        layout.addWidget(self.generate_button)

        # Set the layout
        self.setLayout(layout)

        # Placeholder for the logo image
        self.logo_path = None

    def select_logo(self):
        # Open file dialog to select logo image
        logo_file, _ = QFileDialog.getOpenFileName(self, 'Wählen Sie ein Logo', '', 'Image Files (*.png *.jpg *.bmp)')
        if logo_file:
            self.logo_path = logo_file

    def generate_qr_code(self):
        # Get the text from the input field
        input_text = self.text_input.text()

        if input_text:
            # Generate the QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,  # Höhere Fehlerkorrektur, um Platz für das Logo zu schaffen
                box_size=10,
                border=4,
            )
            qr.add_data(input_text)
            qr.make(fit=True)

            img = qr.make_image(fill='black', back_color='white').convert('RGB')

            # Open the logo image
            if self.logo_path:
                logo = Image.open(self.logo_path)

                # Resize the logo
                logo_size = min(img.size[0] // 3, img.size[1] // 3)  # Das Logo nimmt 1/3 des QR-Codes ein
                logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

                # Berechne die Position, um das Logo in die Mitte des QR-Codes zu setzen
                logo_position = (
                    (img.size[0] - logo_size) // 2,
                    (img.size[1] - logo_size) // 2
                )

                # Füge das Logo zum QR-Code hinzu
                img.paste(logo, logo_position, mask=logo)

            # Convert PIL image to QImage and then QPixmap
            img_byte_array = io.BytesIO()
            img.save(img_byte_array, format='PNG')
            img_byte_array.seek(0)
            img_qt = QImage.fromData(img_byte_array.read())
            pixmap = QPixmap.fromImage(img_qt)

            # Set the QR code image to the label
            self.qr_label.setPixmap(pixmap.scaled(200, 200, Qt.KeepAspectRatio))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QRCodeApp()
    window.show()
    sys.exit(app.exec_())

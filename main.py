from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_clima import Ui_Form
import requests #libreria para comunicar con server 
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #boton
        self.ui.btn_buscar.clicked.connect(self.BuscarClima)

    #funcion a ejecutar
    @Slot()
    def BuscarClima(self):
        try:
            #parametro de caja de txt
            ciudad=self.ui.txt_buscar.text()

            #llave y url de pagina para uso de api
            API_key = "a6f5f05685afab9c96996f9f6cb0becc"
            URL = "https://api.openweathermap.org/data/2.5/weather"

            #llamando al archivo en formato json
            parametros = {"APPID":API_key, "q": ciudad, 'units':'metric', 'lang':'es'}
            response = requests.get(URL, params=parametros)
            clima = response.json()

            #asignando los valores a mostrar
            nombre = clima['name']
            temperature = clima['main']['temp']
            descrpcion = clima['weather'][0]['description']
            strinTemperatura = str(temperature)

            #mostrando en cajas label
            self.ui.lbl_ciudad.setText(nombre)
            self.ui.lbl_grados.setText(strinTemperatura+"°C")
            self.ui.lbl_caracteristica.setText(descrpcion)

        except:
            #mostrando error en caja de texto
            return self.ui.lbl_ciudad.setText("Error 404"),self.ui.lbl_caracteristica.setText("Ciudad NO valida")
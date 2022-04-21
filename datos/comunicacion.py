from distutils.command.config import config
import serial, serial.tools.list_ports
from threading import Thread, Event
import time
from .models import Configuracion

#% clase de comunicación serial

class Comunicacion(object):
    espera = 0.5
    lectura = None
    def configuracion(self):
        self.lectura = serial.Serial()
        self.lectura.timeout = 0.5
        
        self.puertos = []
        
        # para manejar el hilo
        self.hilo = None
        self.alive = Event() #para indicar que el hilo esta activo
        
    def puertosDisponibles(self):
        self.puertos = [port.device for port in serial.tools.list_ports.comports()]
        
    def conexionSerial(self):
        try:
            self.lectura.open()
            print('Conexión exitosa')
        except Exception:
            print('Error al conectar el serial')
            
        if(self.lectura.is_open): #inicio del hilo cuando el puerto esta abierto
            self.iniciar_hilo()
            
    def enviarDatos(self,data):
        if(self.lectura.is_open):
            self.datos = str(data)
            self.lectura.write(bytes([data]))   
        else:
             print('No conectado')
                   
    def desconectar(self):
        self.stop_hilo()
        self.lectura.close()
        print('Desconexión exitosa')
        
    def leerDatos(self):
        while(self.alive.isSet() and self.lectura.is_open):       
            try:
                data = self.lectura.readline()
                data = self.calculo(data)
                configuracion = Configuracion.objects.first()
                configuracion.lectura = data
                configuracion.save()
                time.sleep(self.espera)
            except Exception:
                pass

    def calculo(self, data):
        a = data.decode().strip()
        b = a.split(' ')[-1].split('kg')[0]
        return b
                
    def iniciar_hilo(self):
        self.hilo = Thread(target=self.leerDatos)
        self.hilo.setDaemon(1)
        self.alive.set()
        self.hilo.start()
        
    def stop_hilo(self):
        if(self.hilo is not None):
            self.alive.clear()
            self.hilo.join()
            self.hilo = None

    def conectarm(self):
        configuracion = Configuracion.objects.first()
        self.configuracion()
        self.lectura.port = configuracion.puerto
        self.lectura.baudrate  = configuracion.velocidad
        self.conexionSerial()
        self.iniciar_hilo()
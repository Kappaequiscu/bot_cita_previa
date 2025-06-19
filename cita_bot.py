import cv2
import numpy as np
import pyautogui
import time
import logging
from pathlib import Path
import os

class CitaBotImagenes:
    def __init__(self, carpeta_imagenes="imagenes_bot"):
        self.carpeta_imagenes = Path(carpeta_imagenes)
        self.intentos = 0
        self.max_intentos = 100
        self.tipo_actual = 'presencial'  # Empezamos con presencial
        self.confianza = 0.8  # Umbral de confianza para reconocimiento
        
        # Configurar pyautogui para ser más rápido
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.1  # Reducido de 0.5 a 0.1
        
        # Configurar logging más silencioso
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
        self.logger = logging.getLogger(__name__)
        
        # Crear carpeta de imágenes si no existe
        self.carpeta_imagenes.mkdir(exist_ok=True)
        
        # Rutas de las imágenes de referencia
        self.imagenes = {
            'selector': self.carpeta_imagenes / 'selector.png',
            'presencial': self.carpeta_imagenes / 'presencial.png',
            'telefonica': self.carpeta_imagenes / 'telefonica.png',
            'mensaje_no_disponible': self.carpeta_imagenes / 'mensaje_no_disponible.png'
        }

    def verificar_imagenes(self):
        """Verifica que todas las imágenes de referencia existan"""
        imagenes_faltantes = []
        
        for nombre, ruta in self.imagenes.items():
            if not ruta.exists():
                imagenes_faltantes.append(f"{nombre}.png")
        
        if imagenes_faltantes:
            self.logger.error("❌ Faltan las siguientes imágenes de referencia:")
            for img in imagenes_faltantes:
                self.logger.error(f"   - {img}")
            self.logger.info(f"📁 Coloca las imágenes en la carpeta: {self.carpeta_imagenes}")
            return False
        
        return True

    def encontrar_imagen(self, imagen_path, confianza=None):
        """Busca una imagen en la pantalla y devuelve su posición"""
        if confianza is None:
            confianza = self.confianza
            
        try:
            posicion = pyautogui.locateOnScreen(str(imagen_path), confidence=confianza)
            if posicion:
                centro = pyautogui.center(posicion)
                return centro
        except pyautogui.ImageNotFoundException:
            pass
        except Exception:
            pass
        
        return None

    def hacer_click_imagen(self, imagen_path, descripcion="elemento"):
        """Busca una imagen y hace click en ella - versión silenciosa y rápida"""
        # Intentar con diferentes niveles de confianza rápidamente
        confianzas = [0.9, 0.8, 0.7]
        
        for confianza in confianzas:
            posicion = self.encontrar_imagen(imagen_path, confianza)
            if posicion:
                pyautogui.click(posicion)
                return True
            time.sleep(0.1)  # Pausa muy corta entre intentos
        
        return False

    def detectar_mensaje_no_disponible(self):
        """Detecta si aparece el mensaje de no disponibilidad - versión rápida"""
        time.sleep(0.5)  # Reducido de 2 segundos a 0.5
        
        posicion = self.encontrar_imagen(self.imagenes['mensaje_no_disponible'])
        return posicion is not None

    def capturar_pantalla_debug(self):
        """Captura la pantalla para debug"""
        timestamp = int(time.time())
        nombre_archivo = self.carpeta_imagenes / f"debug_screenshot_{timestamp}.png"
        screenshot = pyautogui.screenshot()
        screenshot.save(nombre_archivo)

    def cambiar_tipo_consulta(self):
        """Alterna entre presencial y telefónica"""
        if self.tipo_actual == 'presencial':
            self.tipo_actual = 'telefonica'
        else:
            self.tipo_actual = 'presencial'

    def iniciar(self):
        """Inicia el bot y comienza la búsqueda"""
        try:
            self.logger.info("🤖 Iniciando bot...")
            
            # Verificar que las imágenes existan
            if not self.verificar_imagenes():
                return
            
            self.logger.info("📸 Imágenes encontradas. Iniciando en 3 segundos...")
            time.sleep(3)  # Reducido de 5 a 3 segundos
            
            self.buscar_cita_disponible()
            
        except KeyboardInterrupt:
            self.logger.info("🛑 Bot detenido")
        except Exception as e:
            self.logger.error(f"❌ Error: {e}")

    def buscar_cita_disponible(self):
        """Bucle principal para buscar citas disponibles - versión optimizada"""
        while self.intentos < self.max_intentos:
            self.intentos += 1
            
            try:
                # Log simplificado cada 10 intentos
                if self.intentos % 10 == 1:
                    self.logger.info(f"🔄 Intento {self.intentos} - {self.tipo_actual.upper()}")
                
                # Si es el primer intento, abrir selector y seleccionar opción inicial
                if self.intentos == 1:
                    if not self.hacer_click_imagen(self.imagenes['selector']):
                        time.sleep(1)
                        continue
                    
                    time.sleep(0.5)  # Reducido de 1 segundo
                    
                    if self.tipo_actual == 'presencial':
                        if not self.hacer_click_imagen(self.imagenes['presencial']):
                            self.cambiar_tipo_consulta()
                            continue
                    else:
                        if not self.hacer_click_imagen(self.imagenes['telefonica']):
                            self.cambiar_tipo_consulta()
                            continue
                
                # Verificar mensaje de disponibilidad
                if self.detectar_mensaje_no_disponible():
                    # Hacer click en la misma opción para cerrar
                    if self.tipo_actual == 'presencial':
                        self.hacer_click_imagen(self.imagenes['presencial'])
                    else:
                        self.hacer_click_imagen(self.imagenes['telefonica'])
                    
                    time.sleep(0.5)  # Reducido
                    
                    # Cambiar a la otra opción
                    self.cambiar_tipo_consulta()
                    
                    # Hacer click en la otra opción
                    if self.tipo_actual == 'presencial':
                        self.hacer_click_imagen(self.imagenes['presencial'])
                    else:
                        self.hacer_click_imagen(self.imagenes['telefonica'])
                    
                    continue
                        
                else:
                    # ¡Encontramos disponibilidad!
                    self.logger.info("🎉 ¡CITA DISPONIBLE ENCONTRADA!")
                    self.logger.info(f"✅ Tipo: {self.tipo_actual.upper()}")
                    self.logger.info(f"📊 Intentos: {self.intentos}")
                    
                    self.notificar_cita_disponible()
                    break
                
                # Pausa mínima entre intentos
                time.sleep(0.5)  # Total: ~1 segundo por ciclo completo
                
            except Exception as e:
                if self.intentos % 20 == 0:  # Solo mostrar errores cada 20 intentos
                    self.logger.error(f"❌ Error en intento {self.intentos}: {e}")
                time.sleep(1)
        
        if self.intentos >= self.max_intentos:
            self.logger.warning("⚠️ Límite máximo alcanzado")

    def notificar_cita_disponible(self):
        """Notifica cuando se encuentra una cita disponible"""
        print("\n" + "="*50)
        print("🎉 ¡CITA DISPONIBLE ENCONTRADA!")
        print("="*50)
        print(f"Tipo de cita: {self.tipo_actual.upper()}")
        print(f"Intentos realizados: {self.intentos}")
        print("="*50)
        
        # Capturar pantalla del momento del éxito
        timestamp = int(time.time())
        nombre_archivo = self.carpeta_imagenes / f"cita_encontrada_{timestamp}.png"
        screenshot = pyautogui.screenshot()
        screenshot.save(nombre_archivo)
        
        # Reproducir sonido de notificación
        try:
            import winsound
            for _ in range(3):
                winsound.Beep(1000, 500)
                time.sleep(0.2)
        except ImportError:
            print("🔔 ¡Revisa la página!")
        
        input("\n⏸️  Presiona Enter para cerrar...")


def crear_script_captura():
    """Crea un script auxiliar para capturar imágenes de referencia"""
    script_captura = '''import pyautogui
import time
from pathlib import Path

def capturar_imagen(nombre, descripcion):
    print(f"\\n📸 Capturando: {descripcion}")
    print("Posiciona el cursor sobre el elemento y presiona ENTER...")
    input()
    
    print("Captura en 3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    
    # Obtener posición del cursor
    x, y = pyautogui.position()
    
    # Capturar un área pequeña alrededor del cursor
    screenshot = pyautogui.screenshot(region=(x-50, y-20, 100, 40))
    
    # Guardar imagen
    Path("imagenes_bot").mkdir(exist_ok=True)
    screenshot.save(f"imagenes_bot/{nombre}.png")
    print(f"✅ Guardado: imagenes_bot/{nombre}.png")

if __name__ == "__main__":
    print("🎯 Asistente para capturar imágenes de referencia")
    print("=" * 50)
    
    capturar_imagen("selector", "Dropdown '--- Seleccionar ---'")
    capturar_imagen("presencial", "Opción 'Presencial'")
    capturar_imagen("telefonica", "Opción 'Telefónica'")
    capturar_imagen("mensaje_no_disponible", "Mensaje de no disponibilidad")
    
    print("\\n🎉 ¡Todas las imágenes capturadas!")
    print("Ya puedes ejecutar el bot principal.")
'''
    
    with open("capturar_imagenes.py", "w", encoding="utf-8") as f:
        f.write(script_captura)
    
    print("📝 Script 'capturar_imagenes.py' creado")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear el script auxiliar para capturar imágenes
    crear_script_captura()
    
    # Crear y ejecutar el bot
    bot = CitaBotImagenes()
    bot.iniciar()
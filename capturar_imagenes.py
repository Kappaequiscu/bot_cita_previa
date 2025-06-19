import pyautogui
import time
from pathlib import Path

def capturar_imagen(nombre, descripcion):
    print(f"\n📸 Capturando: {descripcion}")
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
    
    print("\n🎉 ¡Todas las imágenes capturadas!")
    print("Ya puedes ejecutar el bot principal.")

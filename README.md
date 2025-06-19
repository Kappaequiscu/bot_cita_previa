# 🤖 Bot Automático para Citas Previas

Bot automatizado que busca continuamente citas disponibles (presenciales o telefónicas) en páginas web que usan selectores dropdown. Perfecto para conseguir citas médicas, administrativas o cualquier servicio con alta demanda.

## 📋 ¿Qué hace este bot?

- ✅ Busca automáticamente citas disponibles 24/7
- 🔄 Alterna entre citas presenciales y telefónicas
- 🔍 Detecta cuando aparecen citas libres
- 🔊 Te notifica con sonidos cuando encuentra disponibilidad
- 📸 Captura pantallas para verificar el éxito
- ⚡ Funciona a alta velocidad (1 intento por segundo)

## 🚀 Instalación Paso a Paso

### 1. O descarga el ZIP desde GitHub y extráelo en tu ordenador.

https://github.com/Kappaequiscu/bot_cita_previa/archive/refs/heads/master.zip

### 2. Instalar Python

1. Ve a [python.org](https://www.python.org/downloads/)
2. Descarga Python 3.8 o superior
3. **IMPORTANTE**: Durante la instalación marca ✅ "Add Python to PATH"
4. Completa la instalación

### 3. Instalar dependencias

Abre **Símbolo del sistema** (CMD) en la carpeta del proyecto y ejecuta:

```bash
pip install pyautogui opencv-python numpy pathlib
```

## 🎮 Uso del Bot

### Ejecutar el bot

1. Abre la página de citas en tu navegador
2. Ejecuta el bot:
   ```bash
   python cita_bot.py
   ```

3. **¡El bot empezará a funcionar automáticamente!**

### ⚡ Funcionamiento

1. **Busca el selector** y hace click
2. **Selecciona "Presencial"** y verifica disponibilidad  
3. Si no hay citas → **Cambia a "Telefónica"**
4. Si no hay citas → **Vuelve a "Presencial"**
5. **Repite continuamente** hasta encontrar disponibilidad

### 🎉 Cuando encuentra una cita

- ✨ **Se detiene automáticamente**
- 🔊 **Reproduce 3 pitidos de alerta**
- 📸 **Captura una pantalla de prueba**
- 📝 **Muestra información detallada en consola**

## ⚠️ Requisitos y Consejos

### 🖥️ Configuración necesaria
- **Mantén el navegador visible** (no minimizado)
- **Zoom del navegador al 100%**
- **No muevas las ventanas** mientras funciona
- **Resolución estable** (misma que cuando capturaste)

### 🔧 Si no funciona correctamente

1. **Recaptura las imágenes**: Las páginas web cambian frecuentemente
2. **Verifica el zoom**: Debe estar al 100%
3. **Comprueba la resolución**: Debe coincidir con la captura
4. **Revisa las imágenes**: En `imagenes_bot/` deben estar las 4 imágenes

## 📊 Personalización

### Velocidad del bot
Edita `time.sleep(0.5)` en el código:
- `1.0` = Más lento
- `0.2` = Más rápido

### Número máximo de intentos
```python
self.max_intentos = 100  # Cambiar según preferencia
```

### Sensibilidad de reconocimiento
```python
self.confianza = 0.8  # Entre 0.6 (permisivo) y 0.9 (estricto)
```

## 🛑 Detener el Bot

- **Ctrl + C** en la consola
- **Cerrar** la ventana de CMD
- **Mover cursor** a esquina superior izquierda (failsafe)

## 📁 Estructura del Proyecto

```
bot_cita_previa/
├── cita_bot.py                 # Bot principal ⭐
├── requirements.txt            # Dependencias
├── README.md                   # Esta guía
├── capturar_imagenes.py        # Auto-generado
└── imagenes_bot/               # Auto-creado
    ├── selector.png
    ├── presencial.png
    ├── telefonica.png
    ├── mensaje_no_disponible.png
    └── cita_encontrada_*.png   # Capturas de éxito
```

## 🐛 Solución de Problemas

### Error: "No se pudo encontrar selector dropdown"
**Causa**: Imagen de referencia obsoleta o incorrecta  
**Solución**: Ejecuta `python capturar_imagenes.py` y recaptura

### Error: "No module named 'pyautogui'"
**Causa**: Dependencias no instaladas  
**Solución**: `pip install -r requirements.txt`

### Bot muy lento o muy rápido
**Causa**: Tiempos de espera inadecuados  
**Solución**: Ajusta valores `time.sleep()` en el código

### No detecta imágenes
**Causa**: Zoom o resolución diferente  
**Solución**: Zoom 100%, misma resolución que al capturar

## 🎯 Consejos de Éxito

1. **🕐 Horarios estratégicos**: Usa durante horarios de menor tráfico
2. **🔄 Reinicio periódico**: Reinicia cada 2-3 horas por seguridad  
3. **📸 Mantén actualizadas**: Recaptura imágenes si la página cambia
4. **⚡ Conexión estable**: Internet rápido y estable
5. **🖥️ Dedicación**: No uses el PC para tareas pesadas mientras funciona

## 📈 Características Técnicas

- **Velocidad**: ~1 intento por segundo
- **Eficiencia**: Alternancia inteligente entre opciones
- **Recursos**: Bajo consumo de CPU y memoria
- **Compatibilidad**: Windows 10/11, Python 3.8+
- **Detección**: OpenCV para reconocimiento de imágenes

## 🤝 Contribuir

¿Quieres mejorar el bot?

1. Fork el repositorio
2. Crea una rama: `git checkout -b feature/mejora`
3. Commit cambios: `git commit -m 'Añadir mejora'`
4. Push: `git push origin feature/mejora`
5. Abre un Pull Request

## ⚖️ Uso Responsable

Este bot automatiza tareas repetitivas de forma ética. Úsalo responsablemente:

- ✅ Respeta los términos de servicio de las páginas web
- ✅ No sobrecargues los servidores
- ✅ Usa con moderación y pausas
- ❌ No uses para actividades maliciosas

## 📄 Licencia

MIT License - Ver [LICENSE](LICENSE) para más detalles.

## 🆘 Soporte

¿Problemas o dudas?

1. **Revisa** esta guía completa
2. **Verifica** que seguiste todos los pasos
3. **Abre un issue** en GitHub con detalles del problema
4. **Incluye** capturas de pantalla si es posible

---

**¡Buena suerte consiguiendo tu cita! 🍀**

⭐ **Si te ayudó, dale una estrella al repositorio en GitHub!**

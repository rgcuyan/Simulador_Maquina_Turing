"""
Simulador de Máquina de Turing
Archivo: main.py
Descripción: Archivo principal para ejecutar el simulador

Autor: [Tu Nombre]
Fecha: Noviembre 2025
Curso: Teoría de la Computación
"""

import sys
import tkinter as tk
from tkinter import messagebox

def verificar_dependencias():
    """
    Verifica que todas las dependencias estén disponibles.
    
    Returns:
        bool: True si todas las dependencias están disponibles
    """
    try:
        import tkinter
        return True
    except ImportError as e:
        print("Error: tkinter no está instalado")
        print("Por favor, instala tkinter:")
        print("  - Windows: Incluido con Python")
        print("  - Linux: sudo apt-get install python3-tk")
        print("  - macOS: brew install python-tk")
        return False

def main():
    """
    Función principal que inicia el simulador.
    """
    print("=" * 60)
    print("  SIMULADOR DE MÁQUINA DE TURING")
    print("=" * 60)
    print()
    print("Iniciando simulador...")
    print()
    
    # Verificar dependencias
    if not verificar_dependencias():
        sys.exit(1)
    
    try:
        # Importar la interfaz gráfica
        from interfaz_grafica import InterfazSimulador
        
        # Crear ventana principal
        root = tk.Tk()
        
        # Centrar la ventana en la pantalla
        ancho_ventana = 1000
        alto_ventana = 700
        
        ancho_pantalla = root.winfo_screenwidth()
        alto_pantalla = root.winfo_screenheight()
        
        x = (ancho_pantalla - ancho_ventana) // 2
        y = (alto_pantalla - alto_ventana) // 2
        
        root.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
        
        # Crear la aplicación
        app = InterfazSimulador(root)
        
        print("✓ Simulador iniciado correctamente")
        print("✓ Interfaz gráfica lista")
        print()
        print("Instrucciones rápidas:")
        print("  1. Selecciona una expresión regular")
        print("  2. Ingresa una cadena de entrada")
        print("  3. Haz clic en 'Cargar Cadena'")
        print("  4. Usa los botones de control para ejecutar")
        print()
        print("Presiona Ctrl+C en la terminal para cerrar el programa")
        print("=" * 60)
        
        # Iniciar el loop de la interfaz
        root.mainloop()
        
    except ImportError as e:
        print(f"Error al importar módulos: {e}")
        print("Asegúrate de que todos los archivos estén en el mismo directorio:")
        print("  - cinta.py")
        print("  - maquina_turing.py")
        print("  - expresiones_regulares.py")
        print("  - interfaz_grafica.py")
        sys.exit(1)
        
    except Exception as e:
        print(f"Error inesperado: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
"""
Simulador de Máquina de Turing
Archivo: maquina_turing.py
Descripción: Clase principal que representa la Máquina de Turing
"""

from typing import Dict, Tuple, Set, Optional
from enum import Enum

class Direccion(Enum):
    """Dirección de movimiento del cabezal."""
    IZQUIERDA = 'L'
    DERECHA = 'R'
    QUIETO = 'S'

class MaquinaTuring:
    """
    Implementa la lógica de una Máquina de Turing determinista.
    """
    
    def __init__(self, estados: Set[str], alfabeto_entrada: Set[str],
                 alfabeto_cinta: Set[str], transiciones: Dict,
                 estado_inicial: str, simbolo_blanco: str,
                 estados_aceptacion: Set[str]):
        """
        Inicializa la Máquina de Turing.
        
        Args:
            estados: Conjunto de estados
            alfabeto_entrada: Alfabeto de entrada
            alfabeto_cinta: Alfabeto de la cinta
            transiciones: Función de transición
            estado_inicial: Estado inicial
            simbolo_blanco: Símbolo blanco
            estados_aceptacion: Estados de aceptación
        """
        self.estados = estados
        self.alfabeto_entrada = alfabeto_entrada
        self.alfabeto_cinta = alfabeto_cinta
        self.transiciones = transiciones
        self.estado_inicial = estado_inicial
        self.simbolo_blanco = simbolo_blanco
        self.estados_aceptacion = estados_aceptacion
        
        # Estado de ejecución
        self.estado_actual = None
        self.posicion_cabezal = 0
        self.cinta = None
        self.pasos_ejecutados = 0
        self.cadena_aceptada = None
        
    def cargar_cadena(self, cadena: str):
        """
        Carga una cadena en la cinta y reinicia la máquina.
        
        Args:
            cadena: Cadena de entrada
        """
        from cinta import Cinta
        self.cinta = Cinta(cadena if cadena else self.simbolo_blanco, 
                          self.simbolo_blanco)
        self.estado_actual = self.estado_inicial
        self.posicion_cabezal = 0
        self.pasos_ejecutados = 0
        self.cadena_aceptada = None
        
    def paso(self) -> bool:
        """
        Ejecuta un paso de la máquina.
        
        Returns:
            True si puede continuar, False si terminó
        """
        if self.cadena_aceptada is not None:
            return False
            
        # Leer símbolo actual
        simbolo_actual = self.cinta.leer(self.posicion_cabezal)
        
        # Buscar transición
        clave = (self.estado_actual, simbolo_actual)
        
        if clave not in self.transiciones:
            # No hay transición, rechazar
            self.cadena_aceptada = False
            return False
            
        # Aplicar transición
        nuevo_estado, nuevo_simbolo, direccion = self.transiciones[clave]
        
        # Escribir nuevo símbolo
        self.cinta.escribir(self.posicion_cabezal, nuevo_simbolo)
        
        # Mover cabezal
        if direccion == Direccion.IZQUIERDA.value:
            self.posicion_cabezal -= 1
        elif direccion == Direccion.DERECHA.value:
            self.posicion_cabezal += 1
            
        # Actualizar estado
        self.estado_actual = nuevo_estado
        self.pasos_ejecutados += 1
        
        # Verificar si llegó a un estado de aceptación
        if self.estado_actual in self.estados_aceptacion:
            self.cadena_aceptada = True
            return False
            
        return True
        
    def ejecutar_completo(self, max_pasos: int = 1000) -> bool:
        """
        Ejecuta la máquina hasta que termine o alcance el máximo de pasos.
        
        Args:
            max_pasos: Máximo número de pasos permitidos
            
        Returns:
            True si la cadena fue aceptada, False en caso contrario
        """
        while self.pasos_ejecutados < max_pasos:
            if not self.paso():
                break
                
        if self.cadena_aceptada is None:
            self.cadena_aceptada = False
            
        return self.cadena_aceptada
        
    def obtener_estado(self) -> dict:
        """
        Obtiene el estado actual completo de la máquina.
        
        Returns:
            Diccionario con el estado actual
        """
        return {
            'estado': self.estado_actual,
            'posicion_cabezal': self.posicion_cabezal,
            'simbolo_actual': self.cinta.leer(self.posicion_cabezal) if self.cinta else '',
            'pasos': self.pasos_ejecutados,
            'aceptada': self.cadena_aceptada,
            'cinta': self.cinta.obtener_contenido() if self.cinta else {}
        }
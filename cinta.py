"""
Simulador de Máquina de Turing
Archivo: cinta.py
Descripción: Clase que representa la cinta de la Máquina de Turing
"""

class Cinta:
    """
    Representa la cinta infinita de la Máquina de Turing.
    Utiliza un diccionario para simular una cinta infinita en ambas direcciones.
    """
    
    def __init__(self, cadena_entrada: str, simbolo_blanco: str = '_'):
        """
        Inicializa la cinta con una cadena de entrada.
        
        Args:
            cadena_entrada: Cadena inicial en la cinta
            simbolo_blanco: Símbolo que representa una celda vacía
        """
        self.simbolo_blanco = simbolo_blanco
        self.cinta = {}
        
        # Inicializar la cinta con la cadena de entrada
        for i, simbolo in enumerate(cadena_entrada):
            self.cinta[i] = simbolo
            
        self.posicion_inicio = 0
        self.posicion_fin = len(cadena_entrada) - 1 if cadena_entrada else 0
    
    def leer(self, posicion: int) -> str:
        """
        Lee el símbolo en la posición especificada.
        
        Args:
            posicion: Posición en la cinta
            
        Returns:
            Símbolo en la posición especificada
        """
        return self.cinta.get(posicion, self.simbolo_blanco)
    
    def escribir(self, posicion: int, simbolo: str):
        """
        Escribe un símbolo en la posición especificada.
        
        Args:
            posicion: Posición en la cinta
            simbolo: Símbolo a escribir
        """
        self.cinta[posicion] = simbolo
        
        # Actualizar los límites de la cinta
        if posicion < self.posicion_inicio:
            self.posicion_inicio = posicion
        if posicion > self.posicion_fin:
            self.posicion_fin = posicion
    
    def obtener_contenido(self, rango: int = 10) -> dict:
        """
        Obtiene el contenido visible de la cinta.
        
        Args:
            rango: Número de celdas a mostrar alrededor del contenido
            
        Returns:
            Diccionario con posiciones y símbolos
        """
        inicio = self.posicion_inicio - rango
        fin = self.posicion_fin + rango
        
        contenido = {}
        for i in range(inicio, fin + 1):
            contenido[i] = self.leer(i)
            
        return contenido
    
    def __str__(self) -> str:
        """
        Representación en cadena de la cinta.
        """
        if not self.cinta:
            return f"[{self.simbolo_blanco}]"
        
        inicio = min(self.cinta.keys())
        fin = max(self.cinta.keys())
        
        resultado = []
        for i in range(inicio, fin + 1):
            resultado.append(self.leer(i))
            
        return ''.join(resultado)
"""
Simulador de Máquina de Turing
Archivo: expresiones_regulares.py
Descripción: Definición de las expresiones regulares como Máquinas de Turing
"""

from typing import Dict, Set, Tuple

class ExpresionesRegulares:
    """
    Contiene las definiciones de las expresiones regulares como Máquinas de Turing.
    """
    
    @staticmethod
    def obtener_expresion_1() -> Dict:
        """
        Expresión regular: (a|b)*abb
        Acepta cadenas que terminan en 'abb'
        """
        return {
            'nombre': '(a|b)*abb',
            'descripcion': 'Acepta cadenas que terminan en "abb"',
            'estados': {'q0', 'q1', 'q2', 'q3', 'q_aceptar'},
            'alfabeto_entrada': {'a', 'b'},
            'alfabeto_cinta': {'a', 'b', '_'},
            'transiciones': {
                ('q0', 'a'): ('q1', 'a', 'R'),
                ('q0', 'b'): ('q0', 'b', 'R'),
                ('q1', 'a'): ('q1', 'a', 'R'),
                ('q1', 'b'): ('q2', 'b', 'R'),
                ('q2', 'a'): ('q1', 'a', 'R'),
                ('q2', 'b'): ('q3', 'b', 'R'),
                ('q3', '_'): ('q_aceptar', '_', 'S'),
            },
            'estado_inicial': 'q0',
            'simbolo_blanco': '_',
            'estados_aceptacion': {'q_aceptar'}
        }
    
    @staticmethod
    def obtener_expresion_2() -> Dict:
        """
        Expresión regular: 0*1*
        Acepta cero o más 0s seguidos de cero o más 1s
        """
        return {
            'nombre': '0*1*',
            'descripcion': 'Acepta cero o más 0s seguidos de cero o más 1s',
            'estados': {'q0', 'q1', 'q_aceptar'},
            'alfabeto_entrada': {'0', '1'},
            'alfabeto_cinta': {'0', '1', '_'},
            'transiciones': {
                ('q0', '0'): ('q0', '0', 'R'),
                ('q0', '1'): ('q1', '1', 'R'),
                ('q0', '_'): ('q_aceptar', '_', 'S'),
                ('q1', '1'): ('q1', '1', 'R'),
                ('q1', '_'): ('q_aceptar', '_', 'S'),
            },
            'estado_inicial': 'q0',
            'simbolo_blanco': '_',
            'estados_aceptacion': {'q_aceptar'}
        }
    
    @staticmethod
    def obtener_expresion_3() -> Dict:
        """
        Expresión regular: (ab)*
        Acepta cero o más repeticiones de 'ab'
        """
        return {
            'nombre': '(ab)*',
            'descripcion': 'Acepta cero o más repeticiones de "ab"',
            'estados': {'q0', 'q1', 'q_aceptar'},
            'alfabeto_entrada': {'a', 'b'},
            'alfabeto_cinta': {'a', 'b', '_'},
            'transiciones': {
                ('q0', 'a'): ('q1', 'a', 'R'),
                ('q0', '_'): ('q_aceptar', '_', 'S'),
                ('q1', 'b'): ('q0', 'b', 'R'),
            },
            'estado_inicial': 'q0',
            'simbolo_blanco': '_',
            'estados_aceptacion': {'q_aceptar'}
        }
    
    @staticmethod
    def obtener_expresion_4() -> Dict:
        """
        Expresión regular: 1(01)*0
        Acepta cadenas que empiezan con 1, terminan con 0, y tienen (01)* en medio
        """
        return {
            'nombre': '1(01)*0',
            'descripcion': 'Acepta cadenas que empiezan con 1, terminan con 0',
            'estados': {'q0', 'q1', 'q2', 'q3', 'q_aceptar'},
            'alfabeto_entrada': {'0', '1'},
            'alfabeto_cinta': {'0', '1', '_'},
            'transiciones': {
                ('q0', '1'): ('q1', '1', 'R'),
                ('q1', '0'): ('q2', '0', 'R'),
                ('q2', '1'): ('q1', '1', 'R'),
                ('q2', '_'): ('q_aceptar', '_', 'S'),
            },
            'estado_inicial': 'q0',
            'simbolo_blanco': '_',
            'estados_aceptacion': {'q_aceptar'}
        }
    
    @staticmethod
    def obtener_expresion_5() -> Dict:
        """
        Expresión regular: (a+b)*a(a+b)*
        Acepta cadenas que contienen al menos una 'a'
        """
        return {
            'nombre': '(a+b)*a(a+b)*',
            'descripcion': 'Acepta cadenas que contienen al menos una "a"',
            'estados': {'q0', 'q1', 'q_aceptar'},
            'alfabeto_entrada': {'a', 'b'},
            'alfabeto_cinta': {'a', 'b', '_'},
            'transiciones': {
                ('q0', 'a'): ('q1', 'a', 'R'),
                ('q0', 'b'): ('q0', 'b', 'R'),
                ('q1', 'a'): ('q1', 'a', 'R'),
                ('q1', 'b'): ('q1', 'b', 'R'),
                ('q1', '_'): ('q_aceptar', '_', 'S'),
            },
            'estado_inicial': 'q0',
            'simbolo_blanco': '_',
            'estados_aceptacion': {'q_aceptar'}
        }
    
    @staticmethod
    def obtener_expresion_6() -> Dict:
        """
        Expresión regular: a*b*
        Acepta cero o más 'a's seguidas de cero o más 'b's
        """
        return {
            'nombre': 'a*b*',
            'descripcion': 'Acepta cero o más "a" seguidas de cero o más "b"',
            'estados': {'q0', 'q1', 'q_aceptar'},
            'alfabeto_entrada': {'a', 'b'},
            'alfabeto_cinta': {'a', 'b', '_'},
            'transiciones': {
                ('q0', 'a'): ('q0', 'a', 'R'),
                ('q0', 'b'): ('q1', 'b', 'R'),
                ('q0', '_'): ('q_aceptar', '_', 'S'),
                ('q1', 'b'): ('q1', 'b', 'R'),
                ('q1', '_'): ('q_aceptar', '_', 'S'),
            },
            'estado_inicial': 'q0',
            'simbolo_blanco': '_',
            'estados_aceptacion': {'q_aceptar'}
        }
    
    @staticmethod
    def obtener_expresion_7() -> Dict:
        """
        Expresión regular: (0|1)*00
        Acepta cadenas que terminan en '00'
        """
        return {
            'nombre': '(0|1)*00',
            'descripcion': 'Acepta cadenas que terminan en "00"',
            'estados': {'q0', 'q1', 'q2', 'q_aceptar'},
            'alfabeto_entrada': {'0', '1'},
            'alfabeto_cinta': {'0', '1', '_'},
            'transiciones': {
                ('q0', '0'): ('q1', '0', 'R'),
                ('q0', '1'): ('q0', '1', 'R'),
                ('q1', '0'): ('q2', '0', 'R'),
                ('q1', '1'): ('q0', '1', 'R'),
                ('q2', '0'): ('q2', '0', 'R'),
                ('q2', '1'): ('q0', '1', 'R'),
                ('q2', '_'): ('q_aceptar', '_', 'S'),
            },
            'estado_inicial': 'q0',
            'simbolo_blanco': '_',
            'estados_aceptacion': {'q_aceptar'}
        }
    
    @staticmethod
    def obtener_expresion_8() -> Dict:
        """
        Expresión regular: 1*0*1*
        Acepta cadenas con 1s, luego 0s, luego 1s
        """
        return {
            'nombre': '1*0*1*',
            'descripcion': 'Acepta 1s, luego 0s, luego 1s',
            'estados': {'q0', 'q1', 'q2', 'q_aceptar'},
            'alfabeto_entrada': {'0', '1'},
            'alfabeto_cinta': {'0', '1', '_'},
            'transiciones': {
                ('q0', '1'): ('q0', '1', 'R'),
                ('q0', '0'): ('q1', '0', 'R'),
                ('q0', '_'): ('q_aceptar', '_', 'S'),
                ('q1', '0'): ('q1', '0', 'R'),
                ('q1', '1'): ('q2', '1', 'R'),
                ('q1', '_'): ('q_aceptar', '_', 'S'),
                ('q2', '1'): ('q2', '1', 'R'),
                ('q2', '_'): ('q_aceptar', '_', 'S'),
            },
            'estado_inicial': 'q0',
            'simbolo_blanco': '_',
            'estados_aceptacion': {'q_aceptar'}
        }
    
    @staticmethod
    def obtener_expresion_9() -> Dict:
        """
        Expresión regular: a(a|b)*b
        Acepta cadenas que empiezan con 'a' y terminan con 'b'
        """
        return {
            'nombre': 'a(a|b)*b',
            'descripcion': 'Acepta cadenas que empiezan con "a" y terminan con "b"',
            'estados': {'q0', 'q1', 'q2', 'q_aceptar'},
            'alfabeto_entrada': {'a', 'b'},
            'alfabeto_cinta': {'a', 'b', '_'},
            'transiciones': {
                ('q0', 'a'): ('q1', 'a', 'R'),
                ('q1', 'a'): ('q1', 'a', 'R'),
                ('q1', 'b'): ('q2', 'b', 'R'),
                ('q2', 'a'): ('q1', 'a', 'R'),
                ('q2', 'b'): ('q2', 'b', 'R'),
                ('q2', '_'): ('q_aceptar', '_', 'S'),
            },
            'estado_inicial': 'q0',
            'simbolo_blanco': '_',
            'estados_aceptacion': {'q_aceptar'}
        }
    
    @staticmethod
    def obtener_expresion_10() -> Dict:
        """
        Expresión regular: (ba)*
        Acepta cero o más repeticiones de 'ba'
        """
        return {
            'nombre': '(ba)*',
            'descripcion': 'Acepta cero o más repeticiones de "ba"',
            'estados': {'q0', 'q1', 'q_aceptar'},
            'alfabeto_entrada': {'a', 'b'},
            'alfabeto_cinta': {'a', 'b', '_'},
            'transiciones': {
                ('q0', 'b'): ('q1', 'b', 'R'),
                ('q0', '_'): ('q_aceptar', '_', 'S'),
                ('q1', 'a'): ('q0', 'a', 'R'),
            },
            'estado_inicial': 'q0',
            'simbolo_blanco': '_',
            'estados_aceptacion': {'q_aceptar'}
        }
    
    @staticmethod
    def obtener_todas() -> list:
        """
        Obtiene todas las expresiones regulares definidas.
        
        Returns:
            Lista con todas las definiciones de expresiones regulares
        """
        return [
            ExpresionesRegulares.obtener_expresion_1(),
            ExpresionesRegulares.obtener_expresion_2(),
            ExpresionesRegulares.obtener_expresion_3(),
            ExpresionesRegulares.obtener_expresion_4(),
            ExpresionesRegulares.obtener_expresion_5(),
            ExpresionesRegulares.obtener_expresion_6(),
            ExpresionesRegulares.obtener_expresion_7(),
            ExpresionesRegulares.obtener_expresion_8(),
            ExpresionesRegulares.obtener_expresion_9(),
            ExpresionesRegulares.obtener_expresion_10(),
        ]
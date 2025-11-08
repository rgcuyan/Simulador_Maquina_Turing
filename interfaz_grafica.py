"""
Simulador de Máquina de Turing
Archivo: interfaz_grafica.py
Descripción: Interfaz gráfica del simulador usando tkinter
"""

import tkinter as tk
from tkinter import ttk, scrolledtext
import time
from maquina_turing import MaquinaTuring
from expresiones_regulares import ExpresionesRegulares

class InterfazSimulador:
    """
    Interfaz gráfica para el simulador de Máquina de Turing.
    """
    
    def __init__(self, root):
        """
        Inicializa la interfaz gráfica.
        
        Args:
            root: Ventana principal de tkinter
        """
        self.root = root
        self.root.title("Simulador de Máquina de Turing")
        self.root.geometry("1200x800")
        self.root.resizable(True, True)
        
        # Configurar colores y estilos
        self.COLOR_PRIMARIO = "#2C3E50"
        self.COLOR_SECUNDARIO = "#3498DB"
        self.COLOR_EXITO = "#27AE60"
        self.COLOR_ERROR = "#E74C3C"
        self.COLOR_FONDO = "#ECF0F1"
        self.COLOR_BLANCO = "#FFFFFF"
        
        self.root.configure(bg=self.COLOR_FONDO)
        
        # Variables
        self.maquina = None
        self.expresiones = ExpresionesRegulares.obtener_todas()
        self.ejecutando = False
        self.velocidad = 500  # milisegundos entre pasos
        
        # Configurar estilos
        self._configurar_estilos()
        
        # Configurar la interfaz
        self._crear_widgets()
        
    def _configurar_estilos(self):
        """Configura los estilos personalizados."""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Estilo para LabelFrames
        style.configure('Custom.TLabelframe', background=self.COLOR_BLANCO, 
                       borderwidth=2, relief='solid')
        style.configure('Custom.TLabelframe.Label', font=('Arial', 11, 'bold'),
                       foreground=self.COLOR_PRIMARIO, background=self.COLOR_BLANCO)
        
        # Estilo para botones
        style.configure('Primary.TButton', font=('Arial', 10, 'bold'),
                       padding=10, background=self.COLOR_SECUNDARIO)
        style.configure('Success.TButton', font=('Arial', 10, 'bold'),
                       padding=10, background=self.COLOR_EXITO)
        style.configure('Danger.TButton', font=('Arial', 10, 'bold'),
                       padding=10, background=self.COLOR_ERROR)
        
    def _crear_widgets(self):
        """Crea todos los widgets de la interfaz."""
        
        # Frame principal con padding
        main_frame = tk.Frame(self.root, bg=self.COLOR_FONDO)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # === SECCIÓN SUPERIOR: Título y configuración ===
        self._crear_seccion_titulo(main_frame)
        self._crear_seccion_configuracion(main_frame)
        
        # === SECCIÓN MEDIA: Entrada y controles ===
        self._crear_seccion_entrada_controles(main_frame)
        
        # === SECCIÓN PRINCIPAL: Visualización de la cinta ===
        self._crear_seccion_cinta(main_frame)
        
        # === SECCIÓN INFERIOR: Estado y mensajes ===
        self._crear_seccion_estado(main_frame)
        self._crear_seccion_mensajes(main_frame)
        
        # Cargar la primera expresión
        self._cambiar_expresion()
        
    def _crear_seccion_titulo(self, parent):
        """Crea la sección del título."""
        frame_titulo = tk.Frame(parent, bg=self.COLOR_PRIMARIO, height=80)
        frame_titulo.pack(fill=tk.X, pady=(0, 15))
        frame_titulo.pack_propagate(False)
        
        titulo = tk.Label(frame_titulo, text="🖥️ SIMULADOR DE MÁQUINA DE TURING",
                         font=('Arial', 20, 'bold'), fg=self.COLOR_BLANCO,
                         bg=self.COLOR_PRIMARIO)
        titulo.pack(expand=True)
        
        subtitulo = tk.Label(frame_titulo, 
                            text="LENGUAJES FORMALES Y AUTOMATAS",
                            font=('Arial', 11), fg='#BDC3C7', bg=self.COLOR_PRIMARIO)
        subtitulo.pack()
        
    def _crear_seccion_configuracion(self, parent):
        """Crea la sección de configuración."""
        frame_config = ttk.LabelFrame(parent, text="⚙️  CONFIGURACIÓN DE EXPRESIÓN REGULAR", 
                                     style='Custom.TLabelframe', padding=15)
        frame_config.pack(fill=tk.X, pady=(0, 10))
        
        # Frame interno para organizar
        inner_frame = tk.Frame(frame_config, bg=self.COLOR_BLANCO)
        inner_frame.pack(fill=tk.X)
        
        # Selector de expresión
        label_expr = tk.Label(inner_frame, text="Seleccionar Expresión:",
                             font=('Arial', 10, 'bold'), bg=self.COLOR_BLANCO,
                             fg=self.COLOR_PRIMARIO)
        label_expr.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        
        self.combo_expresion = ttk.Combobox(inner_frame, width=50, 
                                           font=('Courier', 11), state='readonly')
        self.combo_expresion.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
        self.combo_expresion['values'] = [f"{i+1}. {exp['nombre']}" 
                                          for i, exp in enumerate(self.expresiones)]
        self.combo_expresion.current(0)
        self.combo_expresion.bind('<<ComboboxSelected>>', self._cambiar_expresion)
        
        # Descripción
        self.label_descripcion = tk.Label(inner_frame, text="", 
                                         font=('Arial', 10, 'italic'),
                                         fg=self.COLOR_SECUNDARIO, bg=self.COLOR_BLANCO,
                                         wraplength=1000, justify=tk.LEFT)
        self.label_descripcion.grid(row=1, column=0, columnspan=2, 
                                   sticky=tk.W, padx=5, pady=(5, 0))
        
    def _crear_seccion_entrada_controles(self, parent):
        """Crea la sección de entrada y controles."""
        frame_container = tk.Frame(parent, bg=self.COLOR_FONDO)
        frame_container.pack(fill=tk.X, pady=(0, 10))
        
        # Frame de entrada (izquierda)
        frame_entrada = ttk.LabelFrame(frame_container, text="📝  CADENA DE ENTRADA", 
                                      style='Custom.TLabelframe', padding=15)
        frame_entrada.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        entrada_inner = tk.Frame(frame_entrada, bg=self.COLOR_BLANCO)
        entrada_inner.pack(fill=tk.X)
        
        tk.Label(entrada_inner, text="Cadena:", font=('Arial', 10, 'bold'),
                bg=self.COLOR_BLANCO, fg=self.COLOR_PRIMARIO).grid(row=0, column=0, 
                                                                    sticky=tk.W, padx=5)
        
        self.entry_cadena = tk.Entry(entrada_inner, width=40, font=('Courier', 14, 'bold'),
                                     bg='#F8F9FA', relief='solid', borderwidth=2)
        self.entry_cadena.grid(row=0, column=1, padx=10, pady=5, ipady=5)
        
        btn_cargar = tk.Button(entrada_inner, text="▶ Cargar", 
                              command=self._cargar_cadena,
                              font=('Arial', 10, 'bold'), bg=self.COLOR_SECUNDARIO,
                              fg=self.COLOR_BLANCO, relief='flat', padx=20, pady=8,
                              cursor='hand2')
        btn_cargar.grid(row=0, column=2, padx=5)
        
        # Frame de controles (derecha)
        frame_controles = ttk.LabelFrame(frame_container, text="🎮  CONTROLES DE EJECUCIÓN", 
                                        style='Custom.TLabelframe', padding=15)
        frame_controles.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(5, 0))
        
        controles_inner = tk.Frame(frame_controles, bg=self.COLOR_BLANCO)
        controles_inner.pack()
        
        # Botones de control en cuadrícula
        self.btn_paso = tk.Button(controles_inner, text="⏭️ Un Paso", 
                                 command=self._ejecutar_paso,
                                 font=('Arial', 9, 'bold'), bg='#95A5A6',
                                 fg=self.COLOR_BLANCO, relief='flat', 
                                 padx=15, pady=8, cursor='hand2', width=12)
        self.btn_paso.grid(row=0, column=0, padx=5, pady=3)
        
        self.btn_ejecutar = tk.Button(controles_inner, text="▶️ Ejecutar", 
                                     command=self._ejecutar_automatico,
                                     font=('Arial', 9, 'bold'), bg=self.COLOR_EXITO,
                                     fg=self.COLOR_BLANCO, relief='flat',
                                     padx=15, pady=8, cursor='hand2', width=12)
        self.btn_ejecutar.grid(row=0, column=1, padx=5, pady=3)
        
        self.btn_detener = tk.Button(controles_inner, text="⏸️ Detener", 
                                    command=self._detener, state=tk.DISABLED,
                                    font=('Arial', 9, 'bold'), bg=self.COLOR_ERROR,
                                    fg=self.COLOR_BLANCO, relief='flat',
                                    padx=15, pady=8, cursor='hand2', width=12)
        self.btn_detener.grid(row=0, column=2, padx=5, pady=3)
        
        self.btn_reiniciar = tk.Button(controles_inner, text="🔄 Reiniciar", 
                                      command=self._reiniciar,
                                      font=('Arial', 9, 'bold'), bg='#E67E22',
                                      fg=self.COLOR_BLANCO, relief='flat',
                                      padx=15, pady=8, cursor='hand2', width=12)
        self.btn_reiniciar.grid(row=0, column=3, padx=5, pady=3)
        
        # Control de velocidad
        vel_frame = tk.Frame(controles_inner, bg=self.COLOR_BLANCO)
        vel_frame.grid(row=1, column=0, columnspan=4, pady=(10, 0))
        
        tk.Label(vel_frame, text="⚡ Velocidad:", font=('Arial', 9, 'bold'),
                bg=self.COLOR_BLANCO, fg=self.COLOR_PRIMARIO).pack(side=tk.LEFT, padx=5)
        
        self.scale_velocidad = ttk.Scale(vel_frame, from_=100, to=2000, 
                                        orient=tk.HORIZONTAL, length=200,
                                        command=self._cambiar_velocidad)
        self.scale_velocidad.set(500)
        self.scale_velocidad.pack(side=tk.LEFT, padx=5)
        
        self.label_velocidad = tk.Label(vel_frame, text="500 ms", 
                                       font=('Arial', 9, 'bold'),
                                       bg=self.COLOR_BLANCO, fg=self.COLOR_SECUNDARIO,
                                       width=8)
        self.label_velocidad.pack(side=tk.LEFT, padx=5)
        
    def _crear_seccion_cinta(self, parent):
        """Crea la sección de visualización de la cinta."""
        frame_cinta = ttk.LabelFrame(parent, text="📼  CINTA DE LA MÁQUINA DE TURING", 
                                    style='Custom.TLabelframe', padding=15)
        frame_cinta.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Canvas para la cinta con fondo blanco
        self.canvas_cinta = tk.Canvas(frame_cinta, height=150, bg=self.COLOR_BLANCO,
                                     highlightthickness=0)
        self.canvas_cinta.pack(fill=tk.BOTH, expand=True)
        
    def _crear_seccion_estado(self, parent):
        """Crea la sección de estado de la máquina."""
        frame_estado = ttk.LabelFrame(parent, text="📊  ESTADO DE LA MÁQUINA", 
                                     style='Custom.TLabelframe', padding=15)
        frame_estado.pack(fill=tk.X, pady=(0, 10))
        
        estado_inner = tk.Frame(frame_estado, bg=self.COLOR_BLANCO)
        estado_inner.pack(fill=tk.X)
        
        # Estado actual
        estado_frame = tk.Frame(estado_inner, bg='#3498DB', relief='solid', 
                               borderwidth=2, padx=15, pady=8)
        estado_frame.pack(side=tk.LEFT, padx=10)
        
        tk.Label(estado_frame, text="Estado Actual:", font=('Arial', 9),
                fg=self.COLOR_BLANCO, bg='#3498DB').pack()
        self.label_estado_actual = tk.Label(estado_frame, text="N/A", 
                                           font=('Courier', 16, 'bold'),
                                           fg=self.COLOR_BLANCO, bg='#3498DB')
        self.label_estado_actual.pack()
        
        # Número de pasos
        pasos_frame = tk.Frame(estado_inner, bg='#9B59B6', relief='solid',
                              borderwidth=2, padx=15, pady=8)
        pasos_frame.pack(side=tk.LEFT, padx=10)
        
        tk.Label(pasos_frame, text="Pasos Ejecutados:", font=('Arial', 9),
                fg=self.COLOR_BLANCO, bg='#9B59B6').pack()
        self.label_pasos = tk.Label(pasos_frame, text="0", 
                                   font=('Courier', 16, 'bold'),
                                   fg=self.COLOR_BLANCO, bg='#9B59B6')
        self.label_pasos.pack()
        
        # Símbolo actual
        simbolo_frame = tk.Frame(estado_inner, bg='#E67E22', relief='solid',
                                borderwidth=2, padx=15, pady=8)
        simbolo_frame.pack(side=tk.LEFT, padx=10)
        
        tk.Label(simbolo_frame, text="Símbolo Actual:", font=('Arial', 9),
                fg=self.COLOR_BLANCO, bg='#E67E22').pack()
        self.label_simbolo = tk.Label(simbolo_frame, text="-", 
                                     font=('Courier', 16, 'bold'),
                                     fg=self.COLOR_BLANCO, bg='#E67E22')
        self.label_simbolo.pack()
        
        # Resultado
        resultado_frame = tk.Frame(estado_inner, bg='#95A5A6', relief='solid',
                                  borderwidth=2, padx=15, pady=8)
        resultado_frame.pack(side=tk.LEFT, padx=10)
        
        tk.Label(resultado_frame, text="Resultado:", font=('Arial', 9),
                fg=self.COLOR_BLANCO, bg='#95A5A6').pack()
        self.label_resultado = tk.Label(resultado_frame, text="En espera", 
                                       font=('Arial', 12, 'bold'),
                                       fg=self.COLOR_BLANCO, bg='#95A5A6')
        self.label_resultado.pack()
        
    def _crear_seccion_mensajes(self, parent):
        """Crea la sección de mensajes del sistema."""
        frame_mensajes = ttk.LabelFrame(parent, text="💬  MENSAJES DEL SISTEMA", 
                                       style='Custom.TLabelframe', padding=10)
        frame_mensajes.pack(fill=tk.X)
        
        # Área de texto para mensajes
        self.text_mensajes = scrolledtext.ScrolledText(frame_mensajes, height=4,
                                                       font=('Consolas', 9),
                                                       bg='#2C3E50', fg='#ECF0F1',
                                                       relief='flat', padx=10, pady=5)
        self.text_mensajes.pack(fill=tk.X)
        self.text_mensajes.config(state=tk.DISABLED)
        
        # Mensaje de bienvenida
        self._agregar_mensaje("✓ Simulador iniciado correctamente", "info")
        self._agregar_mensaje("► Seleccione una expresión regular e ingrese una cadena para comenzar", "info")
        
    def _agregar_mensaje(self, mensaje, tipo="info"):
        """
        Agrega un mensaje al área de mensajes.
        
        Args:
            mensaje: Texto del mensaje
            tipo: Tipo de mensaje (info, success, error, warning)
        """
        self.text_mensajes.config(state=tk.NORMAL)
        
        # Configurar colores según tipo
        colores = {
            "info": "#3498DB",
            "success": "#27AE60",
            "error": "#E74C3C",
            "warning": "#F39C12"
        }
        
        iconos = {
            "info": "ℹ️",
            "success": "✓",
            "error": "✗",
            "warning": "⚠️"
        }
        
        color = colores.get(tipo, "#ECF0F1")
        icono = iconos.get(tipo, "•")
        
        # Insertar mensaje con timestamp
        import datetime
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        
        self.text_mensajes.insert(tk.END, f"[{timestamp}] {icono} {mensaje}\n")
        
        # Auto-scroll al final
        self.text_mensajes.see(tk.END)
        self.text_mensajes.config(state=tk.DISABLED)
        
    def _cambiar_expresion(self, event=None):
        """Cambia la expresión regular seleccionada."""
        indice = self.combo_expresion.current()
        if indice >= 0:
            exp_config = self.expresiones[indice]
            self.label_descripcion.config(
                text=f"📖 {exp_config['descripcion']}"
            )
            self._agregar_mensaje(
                f"Expresión seleccionada: {exp_config['nombre']}", "info"
            )
            
    def _cargar_cadena(self):
        """Carga la cadena ingresada en la máquina."""
        cadena = self.entry_cadena.get()
        
        # Obtener configuración de la expresión seleccionada
        indice = self.combo_expresion.current()
        if indice < 0:
            self._agregar_mensaje("Debe seleccionar una expresión regular primero", "error")
            return
            
        exp_config = self.expresiones[indice]
        
        # Crear la máquina de Turing
        self.maquina = MaquinaTuring(
            estados=exp_config['estados'],
            alfabeto_entrada=exp_config['alfabeto_entrada'],
            alfabeto_cinta=exp_config['alfabeto_cinta'],
            transiciones=exp_config['transiciones'],
            estado_inicial=exp_config['estado_inicial'],
            simbolo_blanco=exp_config['simbolo_blanco'],
            estados_aceptacion=exp_config['estados_aceptacion']
        )
        
        # Cargar la cadena
        self.maquina.cargar_cadena(cadena)
        
        # Actualizar visualización
        self._actualizar_visualizacion()
        
        # Limpiar resultado anterior
        self.label_resultado.config(text="En proceso", bg='#95A5A6')
        
        self._agregar_mensaje(
            f"Cadena '{cadena if cadena else '(vacía)'}' cargada correctamente", "success"
        )
        
    def _ejecutar_paso(self):
        """Ejecuta un paso de la máquina."""
        if self.maquina is None:
            self._agregar_mensaje("Debe cargar una cadena primero", "warning")
            return
            
        if self.maquina.cadena_aceptada is not None:
            self._agregar_mensaje("La simulación ya ha terminado. Use 'Reiniciar' para comenzar de nuevo", "info")
            return
            
        # Ejecutar un paso
        puede_continuar = self.maquina.paso()
        
        # Actualizar visualización
        self._actualizar_visualizacion()
        
        self._agregar_mensaje(
            f"Paso {self.maquina.pasos_ejecutados}: Estado {self.maquina.estado_actual}", "info"
        )
        
        if not puede_continuar:
            self._mostrar_resultado()
            
    def _ejecutar_automatico(self):
        """Ejecuta la máquina de forma automática."""
        if self.maquina is None:
            self._agregar_mensaje("Debe cargar una cadena primero", "warning")
            return
            
        if self.maquina.cadena_aceptada is not None:
            self._agregar_mensaje("La simulación ya ha terminado. Use 'Reiniciar' para comenzar de nuevo", "info")
            return
            
        self.ejecutando = True
        self.btn_ejecutar.config(state=tk.DISABLED)
        self.btn_paso.config(state=tk.DISABLED)
        self.btn_detener.config(state=tk.NORMAL)
        
        self._agregar_mensaje("Iniciando ejecución automática...", "info")
        
        self._paso_automatico()
        
    def _paso_automatico(self):
        """Ejecuta un paso automático con delay."""
        if not self.ejecutando or self.maquina is None:
            return
            
        if self.maquina.cadena_aceptada is not None:
            self._detener()
            self._mostrar_resultado()
            return
            
        puede_continuar = self.maquina.paso()
        self._actualizar_visualizacion()
        
        if puede_continuar and self.ejecutando:
            self.root.after(self.velocidad, self._paso_automatico)
        else:
            self._detener()
            if self.maquina.cadena_aceptada is not None:
                self._mostrar_resultado()
                
    def _detener(self):
        """Detiene la ejecución automática."""
        self.ejecutando = False
        self.btn_ejecutar.config(state=tk.NORMAL)
        self.btn_paso.config(state=tk.NORMAL)
        self.btn_detener.config(state=tk.DISABLED)
        
        if self.maquina and self.maquina.cadena_aceptada is None:
            self._agregar_mensaje("Ejecución detenida por el usuario", "warning")
        
    def _reiniciar(self):
        """Reinicia la simulación."""
        self._detener()
        if self.maquina is not None:
            cadena_original = self.entry_cadena.get()
            self.maquina.cargar_cadena(cadena_original)
            self._actualizar_visualizacion()
            self.label_resultado.config(text="En proceso", bg='#95A5A6')
            self._agregar_mensaje("Simulación reiniciada", "info")
        else:
            self._agregar_mensaje("No hay ninguna cadena cargada para reiniciar", "warning")
            
    def _cambiar_velocidad(self, valor):
        """Cambia la velocidad de ejecución."""
        self.velocidad = int(float(valor))
        if hasattr(self, 'label_velocidad'):
            self.label_velocidad.config(text=f"{self.velocidad} ms")
        
    def _actualizar_visualizacion(self):
        """Actualiza la visualización de la cinta y el estado."""
        if self.maquina is None:
            return
            
        estado = self.maquina.obtener_estado()
        
        # Actualizar labels de estado
        self.label_estado_actual.config(text=estado['estado'])
        self.label_pasos.config(text=str(estado['pasos']))
        self.label_simbolo.config(text=estado['simbolo_actual'])
        
        # Dibujar la cinta
        self._dibujar_cinta(estado['cinta'], estado['posicion_cabezal'])
        
    def _dibujar_cinta(self, cinta_contenido, posicion_cabezal):
        """Dibuja la cinta en el canvas."""
        self.canvas_cinta.delete("all")
        
        ancho = self.canvas_cinta.winfo_width()
        if ancho <= 1:
            ancho = 1000
            
        alto = self.canvas_cinta.winfo_height()
        if alto <= 1:
            alto = 150
            
        celda_ancho = 60
        celda_alto = 70
        
        # Obtener posiciones para mostrar
        posiciones = sorted(cinta_contenido.keys())
        if not posiciones:
            return
            
        # Centrar en el cabezal
        inicio_x = (ancho - celda_ancho) // 2
        
        for i, pos in enumerate(posiciones):
            offset = pos - posicion_cabezal
            x = inicio_x + offset * celda_ancho
            
            # Solo dibujar si está visible
            if -celda_ancho < x < ancho:
                y = (alto - celda_alto) // 2 + 20
                
                # Color de la celda
                if pos == posicion_cabezal:
                    color_fondo = '#FFD700'
                    color_borde = '#F39C12'
                    grosor = 4
                else:
                    color_fondo = '#F8F9FA'
                    color_borde = '#BDC3C7'
                    grosor = 2
                
                # Dibujar celda con sombra
                self.canvas_cinta.create_rectangle(x+2, y+2, x + celda_ancho+2, 
                                                  y + celda_alto+2,
                                                  fill='#BDC3C7', outline='')
                
                self.canvas_cinta.create_rectangle(x, y, x + celda_ancho, y + celda_alto,
                                                   fill=color_fondo, outline=color_borde, 
                                                   width=grosor)
                
                # Dibujar símbolo
                simbolo = cinta_contenido[pos]
                self.canvas_cinta.create_text(x + celda_ancho//2, y + celda_alto//2,
                                             text=simbolo, font=('Courier', 20, 'bold'),
                                             fill=self.COLOR_PRIMARIO)
                
                # Dibujar posición
                self.canvas_cinta.create_text(x + celda_ancho//2, y + celda_alto + 10,
                                             text=str(pos), font=('Arial', 9),
                                             fill='#7F8C8D')
                
        # Dibujar cabezal (flecha mejorada)
        if posicion_cabezal in cinta_contenido:
            x_cabezal = inicio_x + celda_ancho // 2
            y_cabezal = (alto - celda_alto) // 2 - 15
            
            # Flecha con sombra
            self.canvas_cinta.create_polygon(
                x_cabezal+2, y_cabezal+2,
                x_cabezal - 12+2, y_cabezal - 20+2,
                x_cabezal + 12+2, y_cabezal - 20+2,
                fill='#95A5A6', outline=''
            )
            
            self.canvas_cinta.create_polygon(
                x_cabezal, y_cabezal,
                x_cabezal - 12, y_cabezal - 20,
                x_cabezal + 12, y_cabezal - 20,
                fill='#E74C3C', outline='#C0392B', width=2
            )
            
            self.canvas_cinta.create_text(x_cabezal, y_cabezal - 35,
                                         text="▼ CABEZAL", font=('Arial', 10, 'bold'),
                                         fill='#E74C3C')
            
    def _mostrar_resultado(self):
        """Muestra el resultado de la simulación."""
        if self.maquina is None:
            return
            
        if self.maquina.cadena_aceptada:
            self.label_resultado.config(text="✓ ACEPTADA", bg=self.COLOR_EXITO)
            self._agregar_mensaje(
                f"RESULTADO: La cadena fue ACEPTADA por la máquina (en {self.maquina.pasos_ejecutados} pasos)", 
                "success"
            )
        else:
            self.label_resultado.config(text="✗ RECHAZADA", bg=self.COLOR_ERROR)
            self._agregar_mensaje(
                f"RESULTADO: La cadena fue RECHAZADA por la máquina (en {self.maquina.pasos_ejecutados} pasos)", 
                "error"
            )
            
def main():
    """Función principal."""
    root = tk.Tk()
    app = InterfazSimulador(root)
    root.mainloop()

if __name__ == "__main__":
    main()
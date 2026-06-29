# =================================================================================================
# PROYECTO: ANALIZADOR DE LOGS DE SEGURIDAD INDUSTRIAL 
# DESCRIPCIÓN: Script para el análisis de eventos críticos en sistemas OT.
# AUTOR: emgCybersec
# VERSIÓN: 1.0
# =================================================================================================

import datetime
import os

archivo_entrada = "log_planta.txt"
archivo_salida = "informe_seguridad.txt"

# 1. Verifica si el archivo de entrada existe antes de intentar abrirlo
if not os.path.exists(archivo_entrada):
    print("Error: El archivo de log no existe.")
else:
    # 2. Abre los archivos de forma segura
    with open(archivo_entrada, 'r') as f_entrada, open(archivo_salida, 'w') as f_salida:
        
        # Añade la fecha y hora del análisis (Trazabilidad)
        fecha_actual = datetime.datetime.now()
        f_salida.write(f"--- REPORTE DE ANÁLISIS GENERADO: {fecha_actual} ---\n\n")
        
        # 3. Procesa el archivo línea a línea
        for linea in f_entrada:
            if "ALERTA" in linea:
                f_salida.write("INCIDENCIA: " + linea)
        
    print(f"Análisis completado. Reporte generado en: {archivo_salida}")
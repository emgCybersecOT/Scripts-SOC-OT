# =================================================================================================
# PROYECTO: ENTORNO DE PRUEBAS - FILTRADO DE ALERTAS OT
# LOGICA: Equivalencias de Python con Texto Estructurado (ST) en programación de PLC (IEC 61131-3)
# =================================================================================================

# Lista (Python): Equivalente a un ARRAY en ST para almacenar registros de la planta
registro_red = ["PLC_Schneider_Linea1 - OK", "Robot Kuka_Celdas - ALERTA", "Servidor_SCADA_Siemens - OK"]

# BUCLE DE CONTROL: Equivalente al bucle FOR en ST para recorrer arrays de activos
for dispositivo in registro_red:
    
    # EVALUACIÓN CONDICIONAL: Equivalente a un IF-THEN en ST. Para activar avisos de Alarma
    if "ALERTA" in dispositivo:
        # Genera la salida de alarma en la terminal incluyendo el identificador del activo afectado
        print("ALERTA DE SEGURIDAD!! Amenaza detectada en: " + dispositivo)
        
    else:
        # Registro estándar de operación segura
        print("Dispositivo seguro: " + dispositivo)
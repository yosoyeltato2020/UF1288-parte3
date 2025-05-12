import psutil
import os
import time

def mostrar_uso_cpu():
    time.sleep(2)  # Espera 2 segundos antes de medir el uso de CPU
    uso_cpu = psutil.cpu_percent()  
    print(f"USO CPU: {uso_cpu}%")

def mostrar_uso_memoria():
    memoria = psutil.virtual_memory()
    print(f"Memoria RAM total: {memoria.total}")
    print(f"Memoria RAM usada: {memoria.used }")
    print(f"Porcentaje de uso: {memoria.percent} %")

def mostrar_uso_disco():
    if os.name == 'nt':  
        particion = 'C:\\'
    else:  
        particion = '/'
    disco = psutil.disk_usage(particion)
    print(f"Espacio total en disco: {disco.total}")
    print(f"Espacio usado: {disco.used}")
    print(f"Porcentaje de uso: {disco.percent} %")

def mostrar_numero_total_procesos():
   
    procesos = list(psutil.process_iter())
    total = len(procesos)
    print(f"Número total de procesos: {total}")
    
    if total > 100:
        print("Alerta: demasiados procesos")


print("INFORMACION DE ESTE SISTEMA QUE ESTOY USANDO AHORITA MISMO:\n")
mostrar_uso_cpu()
mostrar_uso_memoria()
mostrar_uso_disco()
mostrar_numero_total_procesos()


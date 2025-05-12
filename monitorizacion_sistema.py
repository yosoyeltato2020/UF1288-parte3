import psutil
import time

def obtener_procesos():
    procesos = list(psutil.process_iter(['pid', 'name', 'cpu_percent']))
    return procesos

def clave_cpu(proceso):
    return proceso.info['cpu_percent']

def mostrar_info(procesos):
    total = len(procesos)
    print("Total de procesos en ejecución:", total)
    
    if total > 100:
        print("Alerta: demasiados procesos")

    
    procesos.sort(key=clave_cpu, reverse=True)

    print("Top 3 procesos por uso de CPU:")
    for proc in procesos[:3]:
        nombre = proc.info['name']
        pid = proc.info['pid']
        cpu = proc.info['cpu_percent']
        print(f"{nombre} (PID {pid}): {cpu}% CPU")

def monitorear():
    
    obtener_procesos()  
    time.sleep(2)       # Espera 2 segundos pero se cambia si quiere mas.
    procesos = obtener_procesos()
    mostrar_info(procesos)


monitorear()

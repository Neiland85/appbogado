import os
import subprocess

# Eliminar Archivos Innecesarios
def eliminar_archivos_innecesarios():
    archivos_eliminar = [".DS_Store", "__pycache__", ".pytest_cache"]
    for root, dirs, files in os.walk('.'):
        for archivo in archivos_eliminar:
            if archivo in files:
                os.remove(os.path.join(root, archivo))
                print(f"Archivo eliminado: {os.path.join(root, archivo)}")
            if archivo in dirs:
                subprocess.run(['rm', '-r', os.path.join(root, archivo)])
                print(f"Directorio eliminado: {os.path.join(root, archivo)}")

def main():
    print("Eliminando archivos innecesarios...")
    eliminar_archivos_innecesarios()
    print("Proceso de limpieza completado.")

if __name__ == "__main__":
    main()


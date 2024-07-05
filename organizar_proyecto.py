import os
import subprocess

# 1. Eliminar Archivos Innecesarios
def eliminar_archivos_innecesarios():
    archivos_eliminar = [".DS_Store", "__pycache__", ".pytest_cache"]
    for root, dirs, files in os.walk('.'):
        for archivo en archivos_eliminar:
            if archivo en files:
                os.remove(os.path.join(root, archivo))
            if archivo en dirs:
                subprocess.run(['rm', '-r', os.path.join(root, archivo)])

# 2. Actualizar Dependencias
def actualizar_dependencias():
    subprocess.run(['python3', '-m', 'pip', 'install', '--upgrade', 'spacy', 'openai'])
    with open('requirements.txt', 'w') as f:
        subprocess.run(['python3', '-m', 'pip', 'freeze'], stdout=f)

# 3. Estandarizar y Limpiar el Código
def estandarizar_codigo():
    subprocess.run(['python3', '-m', 'pip', 'install', 'flake8', 'black'])
    subprocess.run(['python3', '-m', 'flake8', 'appbogado/'])
    subprocess.run(['python3', '-m', 'black', 'appbogado/'])

# 4. Revisar y Mejorar la Documentación
def revisar_documentacion():
    # Aquí puedes añadir código para revisar y mejorar el README.md y otros documentos.
    print("Revisar y mejorar la documentación en README.md")

# 5. Ejecutar Pruebas y Revisar Cobertura
def ejecutar_pruebas():
    subprocess.run(['python3', '-m', 'pytest', '--cov=appbogado', 'tests/'])

def main():
    print("Eliminando archivos innecesarios...")
    eliminar_archivos_innecesarios()

    print("Actualizando dependencias...")
    actualizar_dependencias()

    print("Estandarizando y limpiando el código...")
    estandarizar_codigo()

    print("Revisando y mejorando la documentación...")
    revisar_documentacion()

    print("Ejecutando pruebas y revisando la cobertura...")
    ejecutar_pruebas()

    print("Proceso de limpieza y organización completado.")

if __name__ == "__main__":
    main()


from pathlib import Path

def limpiar_repositorio(directorio):
    path = Path(directorio)
    for file in path.rglob('*'):
        if file.suffix in ('.pyc', '.log'):
            try:
                file.unlink()
                print(f"Removed {file}")
            except Exception as e:
                print(f"Error removing {file}: {e}")

if __name__ == "__main__":
    limpiar_repositorio('.')

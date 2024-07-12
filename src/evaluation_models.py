def calcular_equidad_judicial(datos):
    """
    Calcula la equidad judicial basada en los datos proporcionados.

    Args:
        datos (list): Lista de datos de casos judiciales.

    Returns:
        float: Porcentaje de equidad judicial.
    """
    # Implementación simulada
    total_casos = len(datos)
    casos_equidad = sum(1 for caso in datos if caso['resultado'] == 'equitativo')
    return (casos_equidad / total_casos) * 100 if total_casos > 0 else 0.0

def calcular_transparencia_judicial(datos):
    """
    Calcula la transparencia judicial basada en los datos proporcionados.

    Args:
        datos (list): Lista de datos de casos judiciales.

    Returns:
        float: Porcentaje de transparencia judicial.
    """
    # Implementación simulada
    total_casos = len(datos)
    casos_transparencia = sum(1 for caso in datos if caso['transparente'])
    return (casos_transparencia / total_casos) * 100 if total_casos > 0 else 0.0

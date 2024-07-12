def calcular_equidad_judicial(datos):
    """
    Calcula la equidad judicial basada en los datos proporcionados.

    Args:
        datos (list): Lista de datos de casos judiciales.

    Returns:
        float: Porcentaje de equidad judicial.
    """
    if not datos:
        return 0.0

    total_casos = len(datos)
    casos_equidad = sum(1 for caso in datos if caso.get('resultado') == 'equitativo')
    return (casos_equidad / total_casos) * 100

def calcular_transparencia_judicial(datos):
    """
    Calcula la transparencia judicial basada en los datos proporcionados.

    Args:
        datos (list): Lista de datos de casos judiciales.

    Returns:
        float: Porcentaje de transparencia judicial.
    """
    if not datos:
        return 0.0

    total_casos = len(datos)
    casos_transparencia = sum(1 for caso in datos if caso.get('transparente'))
    return (casos_transparencia / total_casos) * 100

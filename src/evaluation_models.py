# appbogado/evaluation_models.py

def calcular_equidad_judicial(imparcialidad, acceso, consistencia, tiempo, derechos):
    """
    Calcula la Equidad Judicial basada en los factores proporcionados.
    E = w1*I + w2*A + w3*C + w4*(1/T) + w5*H
    
    :param imparcialidad: Valor de la imparcialidad (I)
    :param acceso: Valor del acceso a la justicia (A)
    :param consistencia: Valor de la consistencia en las sentencias (C)
    :param tiempo: Valor del tiempo de resolución (T)
    :param derechos: Valor del cumplimiento de derechos humanos (H)
    :return: Valor de la Equidad Judicial (E)
    """
    # Pesos relativos de cada factor
    w1, w2, w3, w4, w5 = 0.2, 0.2, 0.2, 0.2, 0.2
    
    equidad = (w1 * imparcialidad + 
               w2 * acceso + 
               w3 * consistencia + 
               w4 / tiempo + 
               w5 * derechos)
    return equidad

def calcular_transparencia_judicial(acceso_info, justificacion, publicacion, independencia, rendicion):
    """
    Calcula la Transparencia Judicial basada en los factores proporcionados.
    T = v1*AI + v2*JD + v3*PS + v4*IJ + v5*RC
    
    :param acceso_info: Valor del acceso a la información (AI)
    :param justificacion: Valor de la justificación de decisiones (JD)
    :param publicacion: Valor de la publicación de sentencias (PS)
    :param independencia: Valor de la independencia judicial (IJ)
    :param rendicion: Valor de la rendición de cuentas (RC)
    :return: Valor de la Transparencia Judicial (T)
    """
    # Pesos relativos de cada factor
    v1, v2, v3, v4, v5 = 0.2, 0.2, 0.2, 0.2, 0.2
    
    transparencia = (v1 * acceso_info + 
                     v2 * justificacion + 
                     v3 * publicacion + 
                     v4 * independencia + 
                     v5 * rendicion)
    return transparencia


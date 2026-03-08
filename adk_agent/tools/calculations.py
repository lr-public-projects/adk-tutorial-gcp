def calcular_media(numeros: list[float]) -> float:
    """
    Calcula a média aritmética de uma lista de números.

    Args:
        numeros: Lista de números para cálculo.

    Returns:
        Média aritmética.
    """
    if not numeros:
        return 0.0
    return sum(numeros) / len(numeros)

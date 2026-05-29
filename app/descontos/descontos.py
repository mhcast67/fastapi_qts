def calcular_descontos(valor: float, cliente_vip: bool) -> str:
    if valor <= 0:
        return 0
    
    elif cliente_vip == True:
        return valor * 0.20
    
    elif cliente_vip == False:
        return valor * 0.10
    
    return "valor invalido"


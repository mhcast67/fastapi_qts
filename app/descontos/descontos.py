def calcular_descontos(valor: float, cliente_vip: bool):
    if valor <= 0:
        return 0
    
    if cliente_vip == True:
        return valor * 0.20
    
    if cliente_vip == False:
        return valor * 0.10



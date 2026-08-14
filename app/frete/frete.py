def classificar_frete(peso_kg: float, regiao: str, premium: bool) -> str:
    if peso_kg <= 0:
        return "invalido"
    elif regiao != "local" or regiao != "estadual" or regiao != "nacional":
        return "regiao invalido"
    elif premium == True:
        return "frete gratis"
    elif regiao == "local":
        return "frete reduzido"
    return "frete padrao"
    
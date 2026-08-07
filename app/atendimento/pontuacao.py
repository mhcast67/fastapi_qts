def calcular_pontuacao_atendimento(tempo_minutos: int, resolvido_primeiro_contato: bool, reincidencia:bool) -> int:
    if tempo_minutos <= 0:
        return 0
    
    if resolvido_primeiro_contato == True:
        if tempo_minutos <= 10:
            base = 10

        elif tempo_minutos <= 20:
            base = 8

        else:
            base = 6
        
    else:
        if tempo_minutos <= 10:
            base = 5
        elif tempo_minutos <= 20:
            base = 3
        else:
            base = 1

    if reincidencia == True:
        base -= 2

    if base < 0:
        base = 0

    return base


def classificar_atendimento(pontuacao: int) -> str:
    if pontuacao >= 9:
        return "Excelente"
        
    elif pontuacao >= 7:
        return "Bom"
        
    elif pontuacao >= 4:
        return "Regular"

    else:
        return "Crítico"




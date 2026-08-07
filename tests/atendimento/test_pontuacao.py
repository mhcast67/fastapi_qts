from app.atendimento.pontuacao import calcular_pontuacao_atendimento, classificar_atendimento


def test_calcular_tempo_igual_zero():
    assert calcular_pontuacao_atendimento(0, True, False) == 0

def test_calcular_tempo_invalido():
    assert calcular_pontuacao_atendimento(-3, True, False) == 0

def test_calcular_tempo_dez_minutos_com_resolucao_sem_reincidencia():
    assert calcular_pontuacao_atendimento(10, True, False) == 10

def test_calcular_tempo_igual_onze_com_resolucao_sem_reincidencia():
    assert calcular_pontuacao_atendimento(11, True, False) == 8

def test_calcular_tempo_vinteum_com_resolucao_true_com_reincidencia():
    assert calcular_pontuacao_atendimento(21, True, True) == 4

def test_calcular_tempo_dez_sem_resolucao_sem_reincidencia():
    assert calcular_pontuacao_atendimento(10, False, False) == 5

def test_calcular_tempo_quinze_sem_resolucao_com_reincidencia():
    assert calcular_pontuacao_atendimento(15, False, True) == 1

def test_calcular_tempo_vintecinco_sem_resolucao_com_reincidencia():
    assert calcular_pontuacao_atendimento(25, False, True) == 0


def test_calcular_atendimento_excelente():
    assert classificar_atendimento(calcular_pontuacao_atendimento(10, True, False)) == "Excelente"

def test_calcular_atendimento_bom():
    assert classificar_atendimento(calcular_pontuacao_atendimento(10, True, True)) == "Bom"

def test_calcular_atendimento_regular():
    assert classificar_atendimento(calcular_pontuacao_atendimento(15, True, True)) == "Regular"

def test_calcular_atendimento_critico():
    assert classificar_atendimento(calcular_pontuacao_atendimento(22, False, True)) == "Crítico"

def test_classificar_excelente():
    assert classificar_atendimento(10) == "Excelente"

def test_classificar_bom():
    assert classificar_atendimento(8) == "Bom"

def test_classificar_regular():
    assert classificar_atendimento(5) == "Regular"

def test_classificar_critico():
    assert classificar_atendimento(2) == "Crítico"


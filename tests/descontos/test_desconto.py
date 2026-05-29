from app.descontos.descontos import calcular_descontos


def test_calcular_valor_invalido_menor_que_zero():
    assert calcular_descontos(-1, True) == 0

def test_calcular_valor_invalido_igual_zero():
    assert calcular_descontos(0, False) == 0

def test_calcular_cliente_vip_com_valor_valido():
    assert calcular_descontos(25, True) == 25 * 0.20

def test_calcular_cliente_nao_vip_com_valor_valido():
    assert calcular_descontos(25, False) == 25 * 0.10

# def test_calcular_valor_valido_baixo():
#     assert calcular_descontos(0.01, True) == 0.01 * 0.20

def test_calcular_valor_valido_baixo():
    resultado = calcular_descontos(0.01, True)
    assert round(resultado, 3) == 0.002

def test_calcular_valor_valido_alto():
    assert calcular_descontos(200, True) == 200 * 0.20

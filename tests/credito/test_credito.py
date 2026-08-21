import pytest
from app.credito.credito import classificar_credito

@pytest.mark.parametrize(
    "renda_mensal, score_credito, restricao, retorno",
    [
        (0, 300, False, "renda invalida"),
        (-1, -100, True, "renda invalida"),
        (1780.00, -50, False, "score invalido"),
        (2800.00, 1050, False, "score invalido"),
        (2100.00, 550, True, "reprovado"),
        (1900.00, 250, False, "reprovado"),
        (2700.00, 525, False, "aprovado padrao"),
        (3200.00, 895, False, "aprovado premium"),

        # testes de fronteiras
        (0, 205, False, "renda invalida"),
        (0.01, 200, False, "reprovado"),
        (1200.00, -1, True, "score invalido"),
        (2125.00, 0, False, "score invalido"),
        (2780.00, 399, False, "reprovado"),
        (4100.00, 400, False, "aprovado padrao"),
        (2550.00, 699, False, "aprovado padrao"),
        (1900.00, 700, False, "aprovado premium"),
        (2000.00, 1000, False, "aprovado premium"),
        (1980.00, 1001, False, "score invalido")
    ],
)
def test_classificar_credito(renda_mensal, score_credito, restricao, retorno):
    assert classificar_credito(renda_mensal, score_credito, restricao) == retorno


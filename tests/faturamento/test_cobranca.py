import pytest
import time
from app.faturamento.cobranca import processar_cobranca

@pytest.mark.parametrize(
    "valor_base, plano, dias_atraso, retorno_esperado",
    [
        (-5, "ESSENCIAL", 4, -1.0),
        (0, "ELITE", 12, -1.0),
        (250, "AVANCADO", -3, -1.0),
        (175, "MEGA", 5, -2.0),
        (320, "", 0, -2.0),
        (275, "essencial ", 0, 275),
        (640, "  AVANCADO ", 0, 640 * (1.0 - 0.10)),
        (850, "ELITE", 0, 850 * (1.0 - 0.20)),
        (240, "AVANCADO", 1, (240 * (1.0 - 0.10)) + 6.0 + (240 * (1.0 - 0.10) * (1 * 0.005))),
        (180, "ELITE", 15, (180 * (1.0 - 0.20)) + 6.0 + (180 * (1.0 - 0.20) * (15 * 0.005))),
        (150, "ESSENCIAL", 16, 150 + 20.0 + 150 * 16 * 0.01),
        (620, "AVANCADO", 20, (620 * (1.0 - 0.10)) + 20.0 + (620 * (1.0 - 0.10) * (20 * 0.01))),
        (400, "ELITE", 2, (400 * (1.0 - 0.20)) + 6.0 + (400 * (1.0 - 0.20) * (2 * 0.005))),
        (720, "ESSENCIAL", 30, 720 + 20.0 + 720 * 30 * 0.01),
    ],
)
def test_cobranca(valor_base, plano, dias_atraso, retorno_esperado):
    assert processar_cobranca(valor_base, plano, dias_atraso) == retorno_esperado


def test_tempo_cobranca():
    inicio = time.perf_counter()
    resultado = processar_cobranca(180, "ELITE", 0)
    fim = time.perf_counter()
    tempo_decorrido = fim - inicio

    assert tempo_decorrido < 0.06
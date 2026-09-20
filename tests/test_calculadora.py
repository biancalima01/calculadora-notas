import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from calculadora import calcular_media, verificar_situacao


def test_calcular_media():
    assert calcular_media(8, 7, 9) == 8


def test_aluno_aprovado():
    assert verificar_situacao(8) == "Aprovado"


def test_aluno_em_recuperacao():
    assert verificar_situacao(6) == "Recuperação"


def test_aluno_reprovado():
    assert verificar_situacao(4) == "Reprovado"

def test_aluno_aprovado_nota_minima():
    assert verificar_situacao(7) == "Aprovado"
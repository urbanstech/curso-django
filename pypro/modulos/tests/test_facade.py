import pytest
from pypro.modulos import facade
from model_bakery import baker

from pypro.modulos.models import Modulo


@pytest.fixture
def modulos(db):
    return [baker.make(Modulo, titulo=s) for s in 'Antes Depois'.split()]


def test_listar_modulos_ordenados(modulos):
    assert facade.listar_modulos_ordenados() == sorted(modulos, key=lambda m: m.order)

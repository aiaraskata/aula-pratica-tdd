import pytest
from unittest.mock import MagicMock
from aluno.aluno import Aluno


# =============================================================
# PARTE 1 — Encontre os bugs
# Escreva um teste para cada bug descrito no guia da atividade.
# =============================================================
def test_calcular_media_com_tres_notas():
    aluno = Aluno(nome="Carlos", notas=[6.0, 6.0, 6.0], faltas=0)
    assert aluno.calcular_media() == 6.0

def test_situacao_media_exata_seis(aluno_reprovado):
    aluno = Aluno(nome="Pedro", notas=[6.0, 6.0, 6.0, 6.0], faltas=0)
    assert aluno.situacao() == "Aprovado"

# =============================================================
# PARTE 2 — Implemente com TDD
# Siga o ciclo: 🔴 escreva o teste → 🟢 implemente → 🟡 refatore
# =============================================================

# Requisito 1 — contar_aprovados(lista_de_alunos) -> int
# Escreva os testes ANTES de implementar a função


# Requisito 2 — situacao_final(total_aulas) -> str
# Escreva os testes ANTES de implementar o método


# Requisito 3 — enviar_boletim(email_service)
# Use MagicMock para simular o serviço de e-mail
# Escreva os testes ANTES de implementar o método

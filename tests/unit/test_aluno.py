import pytest
from unittest.mock import MagicMock
from aluno.aluno import Aluno
from aluno.aluno import Aluno, contar_aprovados
from unittest.mock import Mock

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

def test_menor_nota(aluno_aprovado):
    assert aluno_aprovado.menor_nota() == 7

def test_calcular_media_arredondada_corretamente():
    aluno = Aluno(nome="Lucas", notas=[5.0, 6.0, 6.0, 6.0], faltas=0) 
    assert aluno.calcular_media_arredondada() == 6

# =============================================================
# PARTE 2 — Implemente com TDD
# Siga o ciclo: 🔴 escreva o teste → 🟢 implemente → 🟡 refatore
# =============================================================

# Requisito 1 — contar_aprovados(lista_de_alunos) -> int
# Escreva os testes ANTES de implementar a função
def test_contar_aprovados_cenarios(aluno_aprovado, aluno_reprovado):
    assert contar_aprovados([aluno_aprovado, aluno_aprovado]) == 2
    assert contar_aprovados([aluno_reprovado]) == 0
    assert contar_aprovados([aluno_aprovado, aluno_reprovado]) == 1
    assert contar_aprovados([]) == 0

# Requisito 2 — situacao_final(total_aulas) -> str
# Escreva os testes ANTES de implementar o método
def test_situacao_final_considerando_faltas():
    assert Aluno("Rui", [9, 9, 9], faltas=11).situacao_final(40) == "Reprovado por falta"
    assert Aluno("Ana", [7, 8], faltas=2).situacao_final(40) == "Aprovado"
    assert Aluno("Beto", [4, 5], faltas=2).situacao_final(40) == "Reprovado por nota"
    assert Aluno("Cris", [8, 8], faltas=10).situacao_final(40) == "Aprovado"

# Requisito 3 — enviar_boletim(email_service)
# Use MagicMock para simular o serviço de e-mail
# Escreva os testes ANTES de implementar o método
def test_envio_boletim_por_email():
    servico_email_mock = Mock() 
    
    aluno_reprovado = Aluno("João", [4, 4, 5, 4], faltas=2) 
    aluno_reprovado.enviar_boletim(servico_email_mock)
    servico_email_mock.enviar.assert_called_once_with("João", 4.25)
    servico_email_mock.reset_mock()
    aluno_aprovado = Aluno("Maria", [8, 9, 8, 9], faltas=2)
    aluno_aprovado.enviar_boletim(servico_email_mock)
    servico_email_mock.enviar.assert_not_called()
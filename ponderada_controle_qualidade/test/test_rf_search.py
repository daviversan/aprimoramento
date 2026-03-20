"""
Testes do Requisito Funcional (RF):
O sistema deve permitir que um usuário pesquise o catálogo e retorne
informações precisas sobre um filme ou série específica pelo título.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from lib.catalog_search import CATALOG, REQUIRED_FIELDS, search_by_title
from lib.gateway import gateway_route


# ---------- search_by_title ----------


def test_exact_title_returns_item():
    """Busca por título exato deve retornar o item correspondente."""
    results = search_by_title(CATALOG, "Stranger Things")
    assert len(results) == 1
    assert results[0]["title"] == "Stranger Things"



def test_partial_title_returns_matches():
    """Busca parcial (substring) deve retornar todos os itens correspondentes."""
    results = search_by_title(CATALOG, "game")
    assert len(results) == 1
    assert results[0]["title"] == "Squid Game"

    results = search_by_title(CATALOG, "crown")
    assert len(results) == 1
    assert results[0]["title"] == "The Crown"


def test_nonexistent_title_returns_empty():
    """Título inexistente deve retornar lista vazia."""
    results = search_by_title(CATALOG, "xyznonexistent")
    assert results == []


def test_result_contains_required_fields():
    """Cada item retornado deve conter todos os campos obrigatórios."""
    results = search_by_title(CATALOG, "Squid Game")
    assert len(results) == 1
    for field in REQUIRED_FIELDS:
        assert field in results[0], f"Campo obrigatório ausente: {field}"


# ---------- gateway_route ----------


def test_gateway_routes_catalog_search():
    """Gateway deve rotear /catalog/search e retornar status 200."""
    response = gateway_route("/catalog/search", {"title": "Crown"})
    assert response["status"] == 200
    assert len(response["data"]) == 1
    assert response["data"][0]["title"] == "The Crown"


def test_gateway_returns_404_for_unknown_path():
    """Gateway deve retornar 404 para rotas desconhecidas."""
    response = gateway_route("/unknown", {"title": "Crown"})
    assert response["status"] == 404
    assert response["data"] == []

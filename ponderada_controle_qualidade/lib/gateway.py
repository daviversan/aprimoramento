"""
Simulação mínima do API Gateway Zuul da Netflix.

O Zuul atua como porta de entrada de todo tráfego externo,
roteando requisições para os serviços backend apropriados.
"""

from lib.catalog_search import CATALOG, search_by_title


def gateway_route(path: str, params: dict) -> dict:
    """
    Simula o roteamento do API Gateway Zuul.

    Args:
        path:   Rota requisitada (ex.: "/catalog/search").
        params: Query parameters (ex.: {"title": "Stranger"}).

    Returns:
        dict com "status" (int) e "data" (list).
    """
    if path == "/catalog/search" and params.get("title"):
        results = search_by_title(CATALOG, params["title"])
        return {"status": 200, "data": results}

    return {"status": 404, "data": []}

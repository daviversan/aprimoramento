"""
Teste do Requisito Não Funcional (RNF):
O sistema deve responder às requisições de busca em até 100 ms (p95),
garantindo que o Gateway não degrade a experiência do usuário.
"""

import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from lib.gateway import gateway_route

LATENCY_THRESHOLD_MS = 100
ITERATIONS = 50


def _measure_gateway_search_ms(title: str) -> float:
    """Retorna o tempo em milissegundos de uma chamada gateway_route."""
    start = time.perf_counter()
    gateway_route("/catalog/search", {"title": title})
    elapsed = time.perf_counter() - start
    return elapsed * 1000


def test_search_latency_p95_under_threshold():
    """RNF: A latência p95 do fluxo Gateway -> busca deve ser < 100 ms."""
    times = [_measure_gateway_search_ms("Stranger") for _ in range(ITERATIONS)]
    times.sort()
    p95_index = int(0.95 * len(times))
    p95 = times[p95_index]
    assert p95 < LATENCY_THRESHOLD_MS, (
        f"p95 latency {p95:.2f} ms exceeds threshold of {LATENCY_THRESHOLD_MS} ms"
    )

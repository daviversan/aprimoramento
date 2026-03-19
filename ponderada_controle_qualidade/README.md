# Ponderada - Controle de Qualidade

## Estudo de caso: Netflix API Gateway (Zuul) — Busca de Catálogo

A Netflix utiliza o **Zuul** como API Gateway, processando mais de 1 milhão de
requisições por segundo. Toda requisição externa passa pelo Zuul antes de chegar
aos serviços backend.

Este projeto implementa um **mock** do fluxo **API Gateway → Serviço de Busca de
Catálogo**, documentando requisitos em código e aferindo sua qualidade via testes
automatizados.

### Componente

API de Busca de Catálogo, roteada via API Gateway.

---

## Requisito Funcional (RF)

> O sistema deve permitir que um usuário pesquise o catálogo e retorne
> informações precisas sobre um filme ou série específica pelo título.

Documentado na docstring de `search_by_title` em `lib/catalog_search.py` e
verificado pelos testes em `test/test_rf_search.py`.

## Requisito Não Funcional (RNF)

> O sistema deve responder às requisições de busca em até 100 ms (p95).

Aferido pelo teste em `test/test_rnf_latency.py`, que executa 50 chamadas ao
fluxo completo (Gateway → busca) e valida que o percentil 95 da latência está
abaixo do threshold.

---

## Estrutura

```
lib/
  catalog_search.py   # Catálogo mock + função search_by_title (RF)
  gateway.py          # Roteamento mínimo simulando o Zuul
test/
  test_rf_search.py   # Testes do RF (6 testes)
  test_rnf_latency.py # Teste do RNF (latência p95)
```

## Como executar

```bash
pip install -r requirements.txt
pytest -v
```

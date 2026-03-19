"""
Componente: API de Busca de Catálogo (Netflix)
Roteada via API Gateway (Zuul).
"""

CATALOG = [
    {
        "id": "1",
        "title": "Stranger Things",
        "type": "SHOW",
        "description": "When a young boy vanishes, a small town uncovers a mystery involving secret experiments and supernatural forces.",
        "release_year": 2016,
        "genres": ["Sci-Fi", "Horror", "Drama"],
    },
    {
        "id": "2",
        "title": "The Crown",
        "type": "SHOW",
        "description": "Follows the political rivalries and romance of Queen Elizabeth II's reign and the events that shaped the second half of the twentieth century.",
        "release_year": 2016,
        "genres": ["Drama", "History"],
    },
    {
        "id": "3",
        "title": "Squid Game",
        "type": "SHOW",
        "description": "Hundreds of cash-strapped players accept a strange invitation to compete in children's games for a tempting prize.",
        "release_year": 2021,
        "genres": ["Thriller", "Drama"],
    },
]

REQUIRED_FIELDS = {"id", "title", "type", "description", "release_year", "genres"}


def search_by_title(catalog: list[dict], title: str) -> list[dict]:
    """
    RF: O sistema deve permitir que um usuário pesquise o catálogo e retorne
    informações precisas sobre um filme ou série específica pelo título.

    Busca case-insensitive por correspondência parcial (substring) no título.
    Retorna lista de itens com: id, title, type, description, release_year, genres.
    """
    query = title.lower()
    return [item for item in catalog if query in item["title"].lower()]

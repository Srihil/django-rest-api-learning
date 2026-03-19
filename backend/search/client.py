from algoliasearch_django import algolia_engine

def get_client():
    return algolia_engine.client

def get_index(index_name="cfe_Product"):
    client = get_client()   # ✅ call function
    index = client.init_index(index_name)
    return index

def perform_search(query, **kwargs):
    index = get_index()     # ✅ call function
    results = index.search(query)
    return results
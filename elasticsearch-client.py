from elasticsearch import Elasticsearch

es = Elasticsearch(
    ["https://elasticsearch.kkamji.net:443"],
    basic_auth=("elastic", "Rxxx9xxxv3xxxa"),
    verify_certs=False
)

indices = es.indices.get_alias(index="*")
for index_name in indices:
    print(index_name)

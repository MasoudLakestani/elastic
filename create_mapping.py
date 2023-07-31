from elasticsearch import Elasticsearch
import time

# Connect to Elasticsearch
es = Elasticsearch("http://5.34.202.146:9200")

# Ensure Elasticsearch is up
while True:
    try:
        if es.ping():
            print("Connected to Elasticsearch.")
            break
    except Exception as e:
        print(f"Waiting for Elasticsearch... Error: {e}")
        time.sleep(5)

settings = {
    "settings": {
        "analysis": {
            "char_filter": {
                "zero_width_spaces": {
                    "type": "mapping",
                    "mappings": ["\\u200C => \\u0020"]
                }
            },
            "filter": {
                "persian_stop": {
                    "type": "stop",
                    "stopwords": "_persian_"
                },
                "english_stop": {
                    "type": "stop",
                    "stopwords": "_english_"
                },
                "synonym_words":{
                    "type": "synonym",
                    "synonyms_path": "/usr/share/elasticsearch/config/synonyms/synonym.txt"
                }
            },
            "analyzer": {
                "persian_analyzer": {
                    "tokenizer": "standard",
                    "char_filter": ["zero_width_spaces"],
                    "filter": [
                        "lowercase",
                        "decimal_digit",
                        "arabic_normalization",
                        "persian_normalization",
                        "persian_stop",
                        "synonym_words",
                        "unique"
                    ]
                },
                "english_analyzer":{
                    "tokenizer": "standard",
                    "filter": [
                        "lowercase",
                        "english_stop",
                        "unique",
                        "synonym_words",
                    ]   

                }
            }
        }
    },
    "mappings": {
        "properties": {
            "id" : { "type": "integer" },
            "title_fa" : { "type": "text", "analyzer": "persian_analyzer" },
            "title_en" : {"type": "text", "analyzer": "english_analyzer" },
            "category1" : { "type": "text", "analyzer": "persian_analyzer" },
            "website" : { "enabled": "false" },
            "website_url" :{ "enabled": "false" },
            "url" : { "enabled": "false" },
            "is_active" : { "enabled": "false" },
            "image" : { "enabled": "false" },
            "selling_price" : { "enabled": "false" },
            "rrp_price" : { "enabled": "false" },
            "discount_percent" : { "enabled": "false" },



        }
    }
}

es.indices.create(index="blackeveryday_product", body=settings, ignore=400)
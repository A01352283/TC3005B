# Información importante del conjunto de datos

Una vez armado el conjunto de 1000 entradas dummy, se corrió un script para determinar ciertos datos importantes acerca del corpus de descripciones:

## Promedio de palabras de las descripciones

![Word count](./readme_images/average_word_count.png "Average word count")

## Proporción de palabras cerradas

![Stopword proportion](./readme_images/stopword_proportion.png "Stopword proportion")

Para ver cómo se realizó este conteo, se puede referir a [el script que se usó para realizarlo](stopwordCount.py)

## Configuración del índice

```
settings = {
        "index": {
            "similarity": {
                "default": {
                    "type": "BM25"
                }
            },
            "analysis": {
                "analyzer": {
                    "spanish_analyzer": {
                        "type": "custom",
                        "tokenizer": "standard",
                        "filter": ["lowercase", "snowball_spanish", "stop_spanish"]
                    }
                },
                "filter": {
                    "stop_spanish": {
                        "type": "stop",
                        "stopwords": "_spanish_"
                    },
                    "snowball_spanish": {
                        "type": "snowball",
                        "language": "Spanish"
                    }
                }
            }
        }
    }
```

## Mappings

```mappings = {
    "properties": {
        "descripcion": {
            "type": "text",
            "analyzer": "spanish_analyzer"
        },
        "colores": {
            "type": "nested",
            "properties": {
                "nombre": {"type": "text"},
                "valor_hexadecimal": {"type": "keyword"},
                "imagenes": {"type": "text"}
            }
        }
    }
}
```

## Lista de palabras cerradas

Luscene spanish stop word list: https://github.com/apache/lucene/blob/main/lucene/analysis/common/src/resources/org/apache/lucene/analysis/snowball/spanish_stop.txt
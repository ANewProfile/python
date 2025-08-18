from pprint import pprint

print = pprint

import chromadb

client = chromadb.PersistentClient(path="persistent_first_RAG_LLM")

collection = client.get_or_create_collection(name="first_RAG_LLM")


def add_to_collection(ids, docs):
    collection.add(
        ids=ids,
        documents=docs,
    )


def query_collection(queries, num_res):
    return collection.query(query_texts=queries, n_results=num_res)


print(query_collection(["This is a query about China"], 3))

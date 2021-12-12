import datetime
import json
import time

from elasticsearch import Elasticsearch, helpers

import utils_postgres

es = Elasticsearch()

res = es.cluster.health()


# doc = {
#     'author': 'kimchy',
#     'text': 'Elasticsearch: cool. bonsai cool.',
# }
# res = es.index(index="test-index", id=1, document=doc)
# print(res['result'])
#
# res = es.get(index="test-index", id=1)8
# print(res['_source'])


def reindex():
    rows = utils_postgres.get_doc_for_tweets()
    print(time.time())
    print(f'sql done')
    docs = []
    for r in rows:
        docs.append(create_doc(r))
    actions = []
    for doc in docs:
        action = {
            "_index": "tweets",
            "_id": doc['id'],
            "_source": doc
        }
        actions.append(action)

    global es
    helpers.bulk(es, actions, chunk_size=5000, request_timeout=2000)


def create_doc(row):
    doc = {
        'id': row['id'],
        'content': row['content'],
        'location': None if row['location'].strip() == '' else list(map(lambda x: float(x), row['location'].split(' '))),
        'retweet_count': row['retweet_count'],
        'favorite_count': row['favorite_count'],
        'happened_at': int(datetime.datetime.timestamp(row['happened_at'])),
        'author_id': row['author_id'],
        'country_id': row['country_id'],
        'parent_id': row['parent_id'],
        'pos': row['pos'],
        'neu': row['neu'],
        'neg': row['neg'],
        'compound': row['compound'],
        'author':
            {
                'id': row['author_id'],
                'screen_name': row['screen_name'],
                'name': row['name'],
                'description': row['description'],
                'followers_count': row['followers_count'],
                'friends_count': row['friends_count'],
                'statuses_count': row['statuses_count'],
            },

        'hashtags': row['hashtags'],
    }
    return doc






def load_json():
            with open('elastic_index.json','r') as open_file:
                yield json.load(open_file)

start = time.time()
print(start)
# helpers.bulk(es, load_json(), index='tweets')
reindex()

end = time.time()
print(end)
print(end - start)

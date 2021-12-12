
import psycopg2
from psycopg2.extras import RealDictCursor

""" Connect to the PostgreSQL database server """
conn = None


def get_doc_for_tweets():
    sql_hastag = '''select 
        t.id::bigint, t.content, t.retweet_count, t.favorite_count, t.happened_at,
        t.author_id, t.country_id, t.parent_id, t.pos, t.neu, t.neg, t.compound,
        concat(st_y(t.location), ' ',st_x(t.location)) as location,
        a.screen_name, a.name, a.description, a.followers_count, a.friends_count, a.statuses_count,
        string_agg(h.value, ' ') as hashtags 
        from tweets as t 
        inner join  accounts a on a.id = t.author_id 
        left join tweet_hashtags th on t.id = th.tweet_id 
        left join hashtags h on h.id = th.hashtag_id
        where neg is not null
        group by t.id, a.id
        '''
    return exec_sql(sql_hastag)

def exec_sql(sql: str):
    try:
        conn = psycopg2.connect("dbname=tweets_db user=postgres password=root host=192.168.48.2")
        cur = conn.cursor(cursor_factory=RealDictCursor)

        cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

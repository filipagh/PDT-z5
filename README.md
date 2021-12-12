## Autor: Filip Agh
### git: https://github.com/filipagh/PDT-z5

# uloha 1
vid docker-compose.yml

# uloha 2, 3, 4
vid elastic_index.json
main.py pred reindexom vlozi index

# uloha 5, 6
vid main.py (sql mal limit 5000)
je pouzity module elasticsearch a cez helper sa vytvara bulk zoznam ktory sa nakoniec executne

# uloha 7 
### self node
takzvany onoffator bud ide ale nejde nieco co viac dodat

### duo cluster 
je mozne nastavit jeden ako master a 2 ako "slave" 
pri vypadku slave master funguje ako self node
pri vypadku mastera cely cluster je off

### 3+ cluster
je potrebne aby nody ktore su master-elible tak nadpolovicna vadsina bola dostupna aby cluster mohol fungovat.

### downtime
osobne som si nevsimol nejaky rozdiel v nasom clustery 3 nodov a 3 shardov a 2 replik
pokial moj request siel na node ktory cely cas fungoval mohol som robit cokolvek, ak siel na nod ktory som skoro hned vypol tak poziadavka vratila 400 error

# uloha 8
`_seq_no` vzdy sa zvysil o 1 pri zmene
`_version` vzdy sa zvysil o 1 pri zmene a je od 1 narozdiel od `_seq_no`
`_primary_term` sa zmenil ak bol nedostupny primarny shard z indexu
# uloha 9
importoval som tweety ktore maju sentiment
vid main.py
# uloha 10


ked som to pisal neuvedomil som si ze `Must` musi byt realne v query a podl aprikladov som pouzil `multi_match` a filter sa tma nedla pouzit a nasiel som `post_filter` az potom som si uvedomil ze to maju byt realne dane funkcie snad to nevadi  

<details>
  <summary>query</summary>

```
POST tweetsdate/_search
{
  "explain": true,
  "query": {
    "function_score" : {
      "query": {
        "multi_match" : {
          "fuzziness": "AUTO",
          "fuzzy_transpositions": true,
          "type": "most_fields",
          "query": "gates s0ros vaccine micr0chip",
          "fields": [
            "author.name^6",
            "content^8",
            "author.description^6",
            "author.screen_name^10"
          ]
        }
      },
      "functions": [
        {
          "filter": {
            "range": {
              "retweet_count": {
                "gte": 100,
                "lte": 500
              }
            }
          },
          "weight": 6
        },
        {
          "filter": {
            "range": {
              "author.followers_count": {
                "gt": 100
              }
            }
          },
          "weight": 3
        }
      ]
    }
  },
  "post_filter": {
    "bool": {
      "must" :
      [
        {
          "range": {
            "author.statuses_count": {
              "gt": 1000
            }
          }
        },
        {
          "term": {
            "hashtags.keyword": "qanon"
          }
        }
      ]
    }
  },
  "size": 1,
  "aggs": {
    "hashtags-tems": {
      "terms": {
        "size": 100,
        "field": "hashtags.keyword"
      }
    }
  }
}
```
</details>

<details>
  <summary>result</summary>

```
{
  "took": 3,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 8056,
      "relation": "eq"
    },
    "hits": []
  },
  "aggregations": {
    "hashtags-tems": {
      "doc_count_error_upper_bound": 0,
      "sum_other_doc_count": 96613,
      "buckets": [
        {
          "key": "QAnon",
          "doc_count": 64681
        },
        {
          "key": "WWG1WGA",
          "doc_count": 21719
        },
        {
          "key": "Qanon",
          "doc_count": 17415
        },
        {
          "key": "MAGA",
          "doc_count": 10933
        },
        {
          "key": "qanon",
          "doc_count": 9690
        },
        {
          "key": "Epstein",
          "doc_count": 7273
        },
        {
          "key": "QANON",
          "doc_count": 6641
        },
        {
          "key": "BillGates",
          "doc_count": 5715
        },
        {
          "key": "TheGreatAwakening",
          "doc_count": 5025
        },
        {
          "key": "Trump",
          "doc_count": 4768
        },
        {
          "key": "TuesdayMorning",
          "doc_count": 4414
        },
        {
          "key": "COVID19",
          "doc_count": 3811
        },
        {
          "key": "KAG",
          "doc_count": 3731
        },
        {
          "key": "Q",
          "doc_count": 3717
        },
        {
          "key": "QAnon2020",
          "doc_count": 3645
        },
        {
          "key": "GreatAwakening",
          "doc_count": 3626
        },
        {
          "key": "ObamaGate",
          "doc_count": 3580
        },
        {
          "key": "QAnon2018",
          "doc_count": 3408
        },
        {
          "key": "QArmy",
          "doc_count": 3303
        },
        {
          "key": "POTUS",
          "doc_count": 2831
        },
        {
          "key": "coronavirus",
          "doc_count": 2745
        },
        {
          "key": "Vaccine",
          "doc_count": 2591
        },
        {
          "key": "TWGRP",
          "doc_count": 2572
        },
        {
          "key": "wwg1wga",
          "doc_count": 2425
        },
        {
          "key": "Vaccines",
          "doc_count": 2256
        },
        {
          "key": "Maga",
          "doc_count": 2175
        },
        {
          "key": "DemocratsHateAmerica",
          "doc_count": 2167
        },
        {
          "key": "TheMoreYouKnow",
          "doc_count": 2157
        },
        {
          "key": "WWG1WGAWORLDWIDE",
          "doc_count": 2086
        },
        {
          "key": "trumptrain1111",
          "doc_count": 2049
        },
        {
          "key": "vaccine",
          "doc_count": 2006
        },
        {
          "key": "Coronavirus",
          "doc_count": 1992
        },
        {
          "key": "Soros",
          "doc_count": 1953
        },
        {
          "key": "vaccines",
          "doc_count": 1931
        },
        {
          "key": "TheMighty200",
          "doc_count": 1921
        },
        {
          "key": "Gates",
          "doc_count": 1697
        },
        {
          "key": "WeAreTheNewsNow",
          "doc_count": 1676
        },
        {
          "key": "WednesdayThoughts",
          "doc_count": 1651
        },
        {
          "key": "WakeUpAmerica",
          "doc_count": 1518
        },
        {
          "key": "FactsMatter",
          "doc_count": 1417
        },
        {
          "key": "UnitedNotDivided",
          "doc_count": 1399
        },
        {
          "key": "qarmy",
          "doc_count": 1394
        },
        {
          "key": "MSMHatesAmerica",
          "doc_count": 1359
        },
        {
          "key": "WWG1GWA",
          "doc_count": 1358
        },
        {
          "key": "SheepNoMore",
          "doc_count": 1273
        },
        {
          "key": "SaveAmerica",
          "doc_count": 1272
        },
        {
          "key": "digitalsoldier",
          "doc_count": 1258
        },
        {
          "key": "WAKEUPAMERICA",
          "doc_count": 1255
        },
        {
          "key": "Maga2020",
          "doc_count": 1251
        },
        {
          "key": "fyi",
          "doc_count": 1251
        },
        {
          "key": "greatawaking",
          "doc_count": 1251
        },
        {
          "key": "NWO",
          "doc_count": 1250
        },
        {
          "key": "destroy5g",
          "doc_count": 1248
        },
        {
          "key": "ToiletPaperApocalypse",
          "doc_count": 1217
        },
        {
          "key": "endtrafficking",
          "doc_count": 1202
        },
        {
          "key": "NYC",
          "doc_count": 1159
        },
        {
          "key": "mondaythoughts",
          "doc_count": 1097
        },
        {
          "key": "Esptein",
          "doc_count": 1066
        },
        {
          "key": "Democrats",
          "doc_count": 1058
        },
        {
          "key": "InItTogether",
          "doc_count": 1056
        },
        {
          "key": "q",
          "doc_count": 1040
        },
        {
          "key": "DarkToLight",
          "doc_count": 987
        },
        {
          "key": "WHO",
          "doc_count": 979
        },
        {
          "key": "TuesdayMotivation",
          "doc_count": 978
        },
        {
          "key": "Covid19",
          "doc_count": 976
        },
        {
          "key": "China",
          "doc_count": 947
        },
        {
          "key": "Trump2020",
          "doc_count": 947
        },
        {
          "key": "FredoCuomo",
          "doc_count": 946
        },
        {
          "key": "BREAKING",
          "doc_count": 932
        },
        {
          "key": "DeepState",
          "doc_count": 912
        },
        {
          "key": "GetThis",
          "doc_count": 840
        },
        {
          "key": "DrainTheSwamp",
          "doc_count": 837
        },
        {
          "key": "FullMoon",
          "doc_count": 830
        },
        {
          "key": "ChinaIsAsshoe",
          "doc_count": 829
        },
        {
          "key": "Fauci",
          "doc_count": 816
        },
        {
          "key": "TheGreatAwakeningWorldwide",
          "doc_count": 806
        },
        {
          "key": "Autism",
          "doc_count": 702
        },
        {
          "key": "SaveTheChildren",
          "doc_count": 684
        },
        {
          "key": "LockThemAllUp",
          "doc_count": 677
        },
        {
          "key": "QAnons",
          "doc_count": 669
        },
        {
          "key": "KAG2020",
          "doc_count": 666
        },
        {
          "key": "obamagate",
          "doc_count": 635
        },
        {
          "key": "Mighty200",
          "doc_count": 628
        },
        {
          "key": "Wwg1wga",
          "doc_count": 627
        },
        {
          "key": "Plandemic",
          "doc_count": 622
        },
        {
          "key": "Corona",
          "doc_count": 582
        },
        {
          "key": "truth",
          "doc_count": 580
        },
        {
          "key": "TrustThePlan",
          "doc_count": 571
        },
        {
          "key": "VoteRed",
          "doc_count": 544
        },
        {
          "key": "CoronaVirus",
          "doc_count": 533
        },
        {
          "key": "Lockdown",
          "doc_count": 533
        },
        {
          "key": "BillGatesVirus",
          "doc_count": 530
        },
        {
          "key": "Flynn",
          "doc_count": 529
        },
        {
          "key": "thegreatawakening",
          "doc_count": 528
        },
        {
          "key": "Censorship",
          "doc_count": 518
        },
        {
          "key": "ChineseCoronavirus",
          "doc_count": 513
        },
        {
          "key": "Barr",
          "doc_count": 500
        },
        {
          "key": "TheStorm",
          "doc_count": 497
        },
        {
          "key": "WWG1WGA_WORLDWIDE",
          "doc_count": 493
        },
        {
          "key": "DarktoLight",
          "doc_count": 491
        }
      ]
    }
  }
}
```
</details>

# uloha 11

mam len tweety s sentimentom
problem mam taky ze po aggregacii neviem ako filtrovat resulty
a teda mam tweet a ak obsahuje hladany hashtag tak do aggregacie sa dostanu aj ostatne 

<details>
  <summary>query</summary>

```
POST tweetsdate/_search
{
  "explain": true,
  "query": {
    "bool": {
      "must": {
        "match": {
          "hashtags": "DeepstateVirus DeepStateVaccine DeepStateFauci QAnon Agenda21 CCPVirus ClimateChangeHoax GlobalWarmingHoax ChinaLiedPeopleDied SorosVirus 5GCoronavirus MAGA WWG1WGA Chemtrails flatEarth MoonLandingHoax moonhoax illuminati pizzaGateIsReal PedoGateIsReal 911truth 911insidejob reptilians"
        }
      }
    }
  },
  "size": 0,
  "aggs": {
    "orders_over_time": {
      "date_histogram": {
        "field": "happened_at",
        "calendar_interval": "1w",
        "format": "yyyy-ww",
      },
      "aggs": {
        "retweet_count_sum": {
          "sum":
          {
            "field": "retweet_count"
          }
        }
      }
    }
  }
}

```
</details>

<details>
  <summary>result</summary>

```
{
  "took": 263,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 10000,
      "relation": "gte"
    },
    "hits": []
  },
  "aggregations": {
    "orders_over_time": {
      "buckets": [
        {
          "key_as_string": "2017-22",
          "key": 1496016000000,
          "doc_count": 1,
          "retweet_count_sum": {
            "value": 4.0
          }
        },
        {
          "key_as_string": "2017-23",
          "key": 1496620800000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2017-24",
          "key": 1497225600000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2017-25",
          "key": 1497830400000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2017-26",
          "key": 1498435200000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2017-27",
          "key": 1499040000000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2017-28",
          "key": 1499644800000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2017-29",
          "key": 1500249600000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2017-30",
          "key": 1500854400000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2017-31",
          "key": 1501459200000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2017-32",
          "key": 1502064000000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2017-33",
          "key": 1502668800000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2017-34",
          "key": 1503273600000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2017-35",
          "key": 1503878400000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2017-36",
          "key": 1504483200000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2017-37",
          "key": 1505088000000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2017-38",
          "key": 1505692800000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2017-39",
          "key": 1506297600000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2017-40",
          "key": 1506902400000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2017-41",
          "key": 1507507200000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2017-42",
          "key": 1508112000000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2017-43",
          "key": 1508716800000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2017-44",
          "key": 1509321600000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2017-45",
          "key": 1509926400000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2017-46",
          "key": 1510531200000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2017-47",
          "key": 1511136000000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2017-48",
          "key": 1511740800000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2017-49",
          "key": 1512345600000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2017-50",
          "key": 1512950400000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2017-51",
          "key": 1513555200000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2017-52",
          "key": 1514160000000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-01",
          "key": 1514764800000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-02",
          "key": 1515369600000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-03",
          "key": 1515974400000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-04",
          "key": 1516579200000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-05",
          "key": 1517184000000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-06",
          "key": 1517788800000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-07",
          "key": 1518393600000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-08",
          "key": 1518998400000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-09",
          "key": 1519603200000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-10",
          "key": 1520208000000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-11",
          "key": 1520812800000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-12",
          "key": 1521417600000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-13",
          "key": 1522022400000,
          "doc_count": 1,
          "retweet_count_sum": {
            "value": 4.0
          }
        },
        {
          "key_as_string": "2018-14",
          "key": 1522627200000,
          "doc_count": 1,
          "retweet_count_sum": {
            "value": 2.0
          }
        },
        {
          "key_as_string": "2018-15",
          "key": 1523232000000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-16",
          "key": 1523836800000,
          "doc_count": 2,
          "retweet_count_sum": {
            "value": 942.0
          }
        },
        {
          "key_as_string": "2018-17",
          "key": 1524441600000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-18",
          "key": 1525046400000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-19",
          "key": 1525651200000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-20",
          "key": 1526256000000,
          "doc_count": 1,
          "retweet_count_sum": {
            "value": 849.0
          }
        },
        {
          "key_as_string": "2018-21",
          "key": 1526860800000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-22",
          "key": 1527465600000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-23",
          "key": 1528070400000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-24",
          "key": 1528675200000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-25",
          "key": 1529280000000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-26",
          "key": 1529884800000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-27",
          "key": 1530489600000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-28",
          "key": 1531094400000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-29",
          "key": 1531699200000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-30",
          "key": 1532304000000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-31",
          "key": 1532908800000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-32",
          "key": 1533513600000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-33",
          "key": 1534118400000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-34",
          "key": 1534723200000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-35",
          "key": 1535328000000,
          "doc_count": 1,
          "retweet_count_sum": {
            "value": 56.0
          }
        },
        {
          "key_as_string": "2018-36",
          "key": 1535932800000,
          "doc_count": 1,
          "retweet_count_sum": {
            "value": 11.0
          }
        },
        {
          "key_as_string": "2018-37",
          "key": 1536537600000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-38",
          "key": 1537142400000,
          "doc_count": 1,
          "retweet_count_sum": {
            "value": 190.0
          }
        },
        {
          "key_as_string": "2018-39",
          "key": 1537747200000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-40",
          "key": 1538352000000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-41",
          "key": 1538956800000,
          "doc_count": 2,
          "retweet_count_sum": {
            "value": 469.0
          }
        },
        {
          "key_as_string": "2018-42",
          "key": 1539561600000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-43",
          "key": 1540166400000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-44",
          "key": 1540771200000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-45",
          "key": 1541376000000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-46",
          "key": 1541980800000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-47",
          "key": 1542585600000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-48",
          "key": 1543190400000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-49",
          "key": 1543795200000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-50",
          "key": 1544400000000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-51",
          "key": 1545004800000,
          "doc_count": 1,
          "retweet_count_sum": {
            "value": 4.0
          }
        },
        {
          "key_as_string": "2018-52",
          "key": 1545609600000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2018-01",
          "key": 1546214400000,
          "doc_count": 1,
          "retweet_count_sum": {
            "value": 375.0
          }
        },
        {
          "key_as_string": "2019-02",
          "key": 1546819200000,
          "doc_count": 1,
          "retweet_count_sum": {
            "value": 268.0
          }
        },
        {
          "key_as_string": "2019-03",
          "key": 1547424000000,
          "doc_count": 7,
          "retweet_count_sum": {
            "value": 1017.0
          }
        },
        {
          "key_as_string": "2019-04",
          "key": 1548028800000,
          "doc_count": 1,
          "retweet_count_sum": {
            "value": 99.0
          }
        },
        {
          "key_as_string": "2019-05",
          "key": 1548633600000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2019-06",
          "key": 1549238400000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2019-07",
          "key": 1549843200000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2019-08",
          "key": 1550448000000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2019-09",
          "key": 1551052800000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2019-10",
          "key": 1551657600000,
          "doc_count": 1,
          "retweet_count_sum": {
            "value": 2.0
          }
        },
        {
          "key_as_string": "2019-11",
          "key": 1552262400000,
          "doc_count": 1,
          "retweet_count_sum": {
            "value": 14.0
          }
        },
        {
          "key_as_string": "2019-12",
          "key": 1552867200000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2019-13",
          "key": 1553472000000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2019-14",
          "key": 1554076800000,
          "doc_count": 1,
          "retweet_count_sum": {
            "value": 66.0
          }
        },
        {
          "key_as_string": "2019-15",
          "key": 1554681600000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2019-16",
          "key": 1555286400000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2019-17",
          "key": 1555891200000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2019-18",
          "key": 1556496000000,
          "doc_count": 2,
          "retweet_count_sum": {
            "value": 47.0
          }
        },
        {
          "key_as_string": "2019-19",
          "key": 1557100800000,
          "doc_count": 1,
          "retweet_count_sum": {
            "value": 8.0
          }
        },
        {
          "key_as_string": "2019-20",
          "key": 1557705600000,
          "doc_count": 2,
          "retweet_count_sum": {
            "value": 102.0
          }
        },
        {
          "key_as_string": "2019-21",
          "key": 1558310400000,
          "doc_count": 3,
          "retweet_count_sum": {
            "value": 901.0
          }
        },
        {
          "key_as_string": "2019-22",
          "key": 1558915200000,
          "doc_count": 1,
          "retweet_count_sum": {
            "value": 6.0
          }
        },
        {
          "key_as_string": "2019-23",
          "key": 1559520000000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2019-24",
          "key": 1560124800000,
          "doc_count": 1,
          "retweet_count_sum": {
            "value": 2.0
          }
        },
        {
          "key_as_string": "2019-25",
          "key": 1560729600000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2019-26",
          "key": 1561334400000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2019-27",
          "key": 1561939200000,
          "doc_count": 1,
          "retweet_count_sum": {
            "value": 15.0
          }
        },
        {
          "key_as_string": "2019-28",
          "key": 1562544000000,
          "doc_count": 3,
          "retweet_count_sum": {
            "value": 1032.0
          }
        },
        {
          "key_as_string": "2019-29",
          "key": 1563148800000,
          "doc_count": 2,
          "retweet_count_sum": {
            "value": 12.0
          }
        },
        {
          "key_as_string": "2019-30",
          "key": 1563753600000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2019-31",
          "key": 1564358400000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2019-32",
          "key": 1564963200000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2019-33",
          "key": 1565568000000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2019-34",
          "key": 1566172800000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2019-35",
          "key": 1566777600000,
          "doc_count": 1,
          "retweet_count_sum": {
            "value": 2105.0
          }
        },
        {
          "key_as_string": "2019-36",
          "key": 1567382400000,
          "doc_count": 1,
          "retweet_count_sum": {
            "value": 1226.0
          }
        },
        {
          "key_as_string": "2019-37",
          "key": 1567987200000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2019-38",
          "key": 1568592000000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2019-39",
          "key": 1569196800000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2019-40",
          "key": 1569801600000,
          "doc_count": 5,
          "retweet_count_sum": {
            "value": 110.0
          }
        },
        {
          "key_as_string": "2019-41",
          "key": 1570406400000,
          "doc_count": 1,
          "retweet_count_sum": {
            "value": 1558.0
          }
        },
        {
          "key_as_string": "2019-42",
          "key": 1571011200000,
          "doc_count": 1,
          "retweet_count_sum": {
            "value": 224.0
          }
        },
        {
          "key_as_string": "2019-43",
          "key": 1571616000000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2019-44",
          "key": 1572220800000,
          "doc_count": 4,
          "retweet_count_sum": {
            "value": 415.0
          }
        },
        {
          "key_as_string": "2019-45",
          "key": 1572825600000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2019-46",
          "key": 1573430400000,
          "doc_count": 1,
          "retweet_count_sum": {
            "value": 2.0
          }
        },
        {
          "key_as_string": "2019-47",
          "key": 1574035200000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2019-48",
          "key": 1574640000000,
          "doc_count": 1,
          "retweet_count_sum": {
            "value": 618.0
          }
        },
        {
          "key_as_string": "2019-49",
          "key": 1575244800000,
          "doc_count": 1,
          "retweet_count_sum": {
            "value": 98.0
          }
        },
        {
          "key_as_string": "2019-50",
          "key": 1575849600000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2019-51",
          "key": 1576454400000,
          "doc_count": 3,
          "retweet_count_sum": {
            "value": 153.0
          }
        },
        {
          "key_as_string": "2019-52",
          "key": 1577059200000,
          "doc_count": 1,
          "retweet_count_sum": {
            "value": 336.0
          }
        },
        {
          "key_as_string": "2019-01",
          "key": 1577664000000,
          "doc_count": 1,
          "retweet_count_sum": {
            "value": 3.0
          }
        },
        {
          "key_as_string": "2020-02",
          "key": 1578268800000,
          "doc_count": 2,
          "retweet_count_sum": {
            "value": 132.0
          }
        },
        {
          "key_as_string": "2020-03",
          "key": 1578873600000,
          "doc_count": 8,
          "retweet_count_sum": {
            "value": 756.0
          }
        },
        {
          "key_as_string": "2020-04",
          "key": 1579478400000,
          "doc_count": 1347,
          "retweet_count_sum": {
            "value": 164033.0
          }
        },
        {
          "key_as_string": "2020-05",
          "key": 1580083200000,
          "doc_count": 3120,
          "retweet_count_sum": {
            "value": 99177.0
          }
        },
        {
          "key_as_string": "2020-06",
          "key": 1580688000000,
          "doc_count": 1095,
          "retweet_count_sum": {
            "value": 334243.0
          }
        },
        {
          "key_as_string": "2020-07",
          "key": 1581292800000,
          "doc_count": 1368,
          "retweet_count_sum": {
            "value": 479920.0
          }
        },
        {
          "key_as_string": "2020-08",
          "key": 1581897600000,
          "doc_count": 597,
          "retweet_count_sum": {
            "value": 38036.0
          }
        },
        {
          "key_as_string": "2020-09",
          "key": 1582502400000,
          "doc_count": 1526,
          "retweet_count_sum": {
            "value": 132855.0
          }
        },
        {
          "key_as_string": "2020-10",
          "key": 1583107200000,
          "doc_count": 0,
          "retweet_count_sum": {
            "value": 0.0
          }
        },
        {
          "key_as_string": "2020-11",
          "key": 1583712000000,
          "doc_count": 3,
          "retweet_count_sum": {
            "value": 2499.0
          }
        },
        {
          "key_as_string": "2020-12",
          "key": 1584316800000,
          "doc_count": 24,
          "retweet_count_sum": {
            "value": 30184.0
          }
        },
        {
          "key_as_string": "2020-13",
          "key": 1584921600000,
          "doc_count": 64,
          "retweet_count_sum": {
            "value": 25148.0
          }
        },
        {
          "key_as_string": "2020-14",
          "key": 1585526400000,
          "doc_count": 110645,
          "retweet_count_sum": {
            "value": 4.7971985E7
          }
        },
        {
          "key_as_string": "2020-15",
          "key": 1586131200000,
          "doc_count": 330810,
          "retweet_count_sum": {
            "value": 3.84602208E8
          }
        },
        {
          "key_as_string": "2020-16",
          "key": 1586736000000,
          "doc_count": 341854,
          "retweet_count_sum": {
            "value": 2.46781413E8
          }
        },
        {
          "key_as_string": "2020-17",
          "key": 1587340800000,
          "doc_count": 122063,
          "retweet_count_sum": {
            "value": 4.94339E7
          }
        },
        {
          "key_as_string": "2020-18",
          "key": 1587945600000,
          "doc_count": 357549,
          "retweet_count_sum": {
            "value": 3.64091671E8
          }
        },
        {
          "key_as_string": "2020-19",
          "key": 1588550400000,
          "doc_count": 228407,
          "retweet_count_sum": {
            "value": 3.68121967E8
          }
        },
        {
          "key_as_string": "2020-20",
          "key": 1589155200000,
          "doc_count": 345407,
          "retweet_count_sum": {
            "value": 9.14523493E8
          }
        },
        {
          "key_as_string": "2020-21",
          "key": 1589760000000,
          "doc_count": 114542,
          "retweet_count_sum": {
            "value": 5.3856306E7
          }
        },
        {
          "key_as_string": "2020-22",
          "key": 1590364800000,
          "doc_count": 184618,
          "retweet_count_sum": {
            "value": 2.52186417E8
          }
        }
      ]
    }
  }
}
```
</details>




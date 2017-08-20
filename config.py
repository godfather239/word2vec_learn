#!/usr/bin/env python
# encoding=utf-8

import datetime
today = datetime.date.today()

CONFIG = {
    "today" : today,
    "stat_from" : today - datetime.timedelta(7),
    "stat_to" : today,
    "product_click_count_min" : 1500,
    "product_count_max" : 20,
    "data_dir" : '/Users/greenday/data/',
    "solr_host" : 'product-solr.int.jumei.com',
    "prefix_query_count_of_doc_term" : 5,           # doc_term覆盖的前缀相同的query数量
    "save_intermediate_date" : True,
    "save_table_name" : 'recommend.se_related_term',
    "doc_term_weight_strategy" : 'bm25',
    "rescore_boost_strategy" : 'sqrt(c.doc_freq)'
}

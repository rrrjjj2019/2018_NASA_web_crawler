# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class ApplePipeline(object):
    def open_spider(self, spider):
        self.conn = sqlite3.connect('apple.sqlite')
        self.cur = self.conn.cursor()
        self.cur.execute('create table if not exists apple(month varchar(100), year varchar(100), day varchar(100), time varchar(100), mission text);')
    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()
    def process_item(self, item, spider):
        col = ','.join(item.keys())
        placeholders = ','.join(len(item) * '?')
        sql = 'insert into apple({}) values({})'
        self.cur.execute(sql.format(col, placeholders), item.values())
        return item

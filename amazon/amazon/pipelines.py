# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# from pymongo import MongoClient 
import psycopg2 

class AmazonPipeline:
    # def open_spider(self, spider):
    #     LOCALHOST = "localhost",
    #     DBNAME = "pickledb",
    #     USER = "postgres",
    #     PORT = "",
    #     # PORT = "49495",
    #     # PORT = "5432",
    #     # PORT = "5300",
    #     PASSWORD = "12345",


    #     self.conn = psycopg2.connect(
    #     host=LOCALHOST,
    #     database=DBNAME,
    #     user=USER,
    #     port =PORT,
    #     password=PASSWORD)
    #     print(conn, "connected")
    #     # conn.commit()
    #     conn.autocommit = True
    #     self.cursor = self.conn.cursor()
    
    # def close_spider(self, spider):
    #     self.cursor.close()
    #     self.connection.close()

    # def process_item(self, item, spider):
    #     self.cursor.execute("insert into image_data(product_name,product_image) values(%s,%s)",(item['name'],item['image']))
    #     self.connection.commit()
    #     return item


    def process_item(self, item, spider):
        # self.collection.insert(dict(item))

        return item






    # def queryQuotes( conn ) :
    #     cur = conn.cursor()
    #     cur.execute( """select * from image_data""" )
    #     rows = cur.fetchall()

    #     for row in rows :
    #         print (row[1])

    # # conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
    # queryQuotes( conn )
    # conn.close()

    


# data directory : C:\Program Files\MongoDB\Server\4.4\data\
# log directory : C:\Program Files\MongoDB\Server\4.4\log\





# def __init__(self):
        # client is a name of connection which is to be define
        # self.client = MongoClient(
        #     'localhost',
        #     27017
        # )
        # # self.client = MongoClient(
        # #     'mongodb://pickle:test@1234@45.64.156.214/pickle_Product_data',
        # #     27017
        # # )
        # db = self.client['pickledb']
        # self.collection = db['pickle_prod_data']
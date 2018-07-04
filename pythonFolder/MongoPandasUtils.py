
import pandas as pd
import numpy as np
from pymongo import MongoClient

class MongoPandas:
    """
    This Class Read Mongo Collections and returned as a DF in pandas.
    """

    def __init__(self, mongo_uri=None, db=None, db_obj=None):

        if db_obj == None:
            self.conn = MongoClient(mongo_uri)
            self.db_obj = self.conn[db]
        else:
            self.db_obj = db_obj

    def collection_to_DF(self, collection, query={}, no_id=True):
        """ Read from Mongo and Store into DataFrame """
        # Make a query to the specific DB and Collection
        cursor = self.db_obj[collection].find(query)
        # Expand the cursor and construct the DataFrame
        df = pd.DataFrame(list(cursor))
        # Delete the _id
        if no_id:
            del df['_id']
        return df

    def collections_to_DFS(self, collections = [], query={}, no_id=True):
        dfs = []
        for c in collections:
            dfs.append(self.collection_to_DF(c, query, no_id))

        return dfs

    def get_mongo_db_obj(self):
        return self.db_obj

"""
Utility Function to connect to MONGO and get collection to DF and files
"""
def _connect_mongo(mongo_uri, db):
    conn = MongoClient(mongo_uri)
    return conn[db]

def collection_to_DF(db_obj, collection, query={}, no_id=True):
    """ Read from Mongo and Store into DataFrame """
    # Make a query to the specific DB and Collection
    cursor = db_obj[collection].find(query)
    # Expand the cursor and construct the DataFrame
    df = pd.DataFrame(list(cursor))
    # Delete the _id
    if no_id:
        del df['_id']
    return df

def get_df_collection():
    df1 = collection_to_DF(_connect_mongo(mongo_uri, db), collection1)
    df2 = collection_to_DF(_connect_mongo(mongo_uri, db), collection2)
    return df1, df2

def get_file(path1):
    return open(path1, 'rb')


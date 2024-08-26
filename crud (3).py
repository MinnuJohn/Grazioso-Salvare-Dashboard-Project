from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter():
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31664
        DB = 'aac'
        COL = 'animals'
        
        # Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    def create(self, data):
        """Insert a document into the collection"""
        if isinstance(data, dict):
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print(f"Insert failed: {e}")
                return False
        else:
            raise ValueError("Data must be a dictionary")

    def read(self, query):
        """Query documents from the collection"""
        if isinstance(query, dict):
            try:
                cursor = self.collection.find(query)
                results = [doc for doc in cursor]
                return results
            except Exception as e:
                print(f"Query failed: {e}")
                return []
        else:
            raise ValueError("Query must be a dictionary")
    
    def update(self, query, new_values):
        """Update document(s) in the collection"""
        if isinstance(query, dict) and isinstance(new_values, dict):
            try:
                result = self.collection.update_many(query, {"$set": new_values})
                return result.modified_count
            except Exception as e:
                print(f"Update failed: {e}")
                return []
        else:
            raise ValueError("Query and new values must be dictionaries")

    def delete(self, query):
        """Delete document(s) from the collection"""
        if isinstance(query, dict):
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print(f"Delete failed: {e}")
                return []
        else:
            raise ValueError("Query must be a dictionary")
            
    





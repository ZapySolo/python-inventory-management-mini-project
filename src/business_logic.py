from pymongo import MongoClient
import datetime
import hashlib


class BackendLogic:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['oslMiniProjectProdDB']
        self.manager_account_collection = self.db['managerAccounts']
        self.inventory_collection = self.db['inventories']
        self.customer_collection = self.db['customers']
        self.checkForDatabase()

    def checkForDatabase(self):
        #if the database is not created, this creates the database with sample collections
        if self.inventory_collection.find() is None:
            obj = [
                {"name": "iphone 6s", "noOfItems": 10},
                {"name": "Moto g4", "noOfItems": 25},
                {"name": "Zenfone m2", "noOfItems": 13},
                {"name": "redmi note 7 pro", "noOfItems": 1},
                {"name": "nokia 8", "noOfItems": 34}
            ]
            self.inventory_insert_many(obj)
        if self.customer_collection.find({}) is None:
            self.customer_collection.insert_one({
                "name": "root",
                "password": "3e42295e89a3a84ce7ee38e2ba317aeb57ca3164459bdf48f4da0e92"
            })

    def manager_account_find_one(self, username, password):
        #i have used hashed value to search for the validation
        password_entered = hashlib.sha3_224()
        password_entered.update(password.encode())

        return self.manager_account_collection.find_one({
            "name": username,
            "password": password_entered.hexdigest()
        })

    def inventory_find_one_item(self, item_name):
        return self.inventory_collection.find_one({
            "name": item_name
        })

    def inventory_insert_one_item(self, obj):
        self.inventory_collection.insert_one(obj)

    def inventory_find_by_name_update_item_no(self, name, no_of_item):
        self.inventory_collection.find_one_and_update(
            {
                "name": name
            }, {
                '$set': {
                    "noOfItems": no_of_item
                }
            },
            upsert=True
            # means to add the field if not created
        )

    def inventory_find_all(self):
        return self.inventory_collection.find({})

    def customer_find_one(self, name):
        return self.customer_collection.find_one({
            "name": name
        })

    def customer_collection_count(self):
        return self.customer_collection.count()

    def customer_insert_new(self, customer_name, product_name, product_quantity):
        self.customer_collection.insert_one({
            "name": customer_name,
            "purchase_history": [
                product_name + " " + product_quantity + " " + str(datetime.datetime.now())
            ]
        })

    def customer_find_by_name_update_one(self, customer_name, updated_purchase_history):
        print("ss")
        self.customer_collection.update_one(
            {
                "name": customer_name
            }, {
                '$set': {
                    "purchase_history": updated_purchase_history
                }
            }
        )

    def inventory_insert_many(self, obj):
        self.inventory_collection.insert_many({obj})

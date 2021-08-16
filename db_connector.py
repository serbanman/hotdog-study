from db_config import database_root
import os
import sqlite3

class Connector:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Connector, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.db_root = database_root
        self.connector = sqlite3.connect(self.db_root)
        self.cursor = self.connector.cursor()


"""
Connection strings of different environments
"""
import logging

DEV_CONNECTION_STRING = "mysql+pymysql://admin:77777777@lihkg-mining-dev-db-1.cd6iuh9hsdzr.us-west-2.rds.amazonaws.com/dev-apps"
TEST_CONNECTION_STRING = "sqlite:///data/sqlite/db_test.db"
PROD_CONNECTION_STRING = "sqlite:///data/sqlite/db_prod.db"

logging.getLogger().warning("The ConnectionStrings.py file is exposed. "
                            "Please make sure any cloud database connection is restricted")

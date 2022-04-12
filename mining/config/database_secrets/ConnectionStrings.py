"""
Connection strings of different environments
"""
import os


DEV_CONNECTION_STRING = "mysql+pymysql://admin:77777777@lihkg-mining-dev-db-1.cd6iuh9hsdzr.us-west-2.rds.amazonaws.com/dev-apps"

# Keep production environment secret
PROD_CONNECTION_STRING = os.getenv("PROD_CONNECTION_STRING")

TEST_CONNECTION_STRING = "sqlite:///data/sqlite/db_test.db"

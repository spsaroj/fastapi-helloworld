import mysqlclient

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'passwd': 'root',
    'db': 'tasks',
}

# Create a connection to the database
conn = mysqlclient.connect(**db_config)
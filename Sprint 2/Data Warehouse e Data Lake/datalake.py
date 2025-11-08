from neo4j import GraphDatabase

# URI examples: "neo4j://localhost", "neo4j+s://xxx.databases.neo4j.io"
URI = "neo4j+s://f160c50e.databases.neo4j.io"
AUTH = ("bonato16_db_user", "L2VFXXTL3uI6GvVO")

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()
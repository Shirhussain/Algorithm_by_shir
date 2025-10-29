OLAP OLTP
OLTP - Online Transactional Processing
OLAP - Online Analytical Processing

# START TRANSACTION

LOCK
SELECT ...
SELECT ...

# COMMIT

START TRANSACTION
ALTER
INSERT
UPDATE
COMMIT

OLTP
SELECT AVG(cost), \* ... JOINS ... UNION ...

OLTP -> CDC -> OLAP

OLTP - Postgres, MySQL, Oracle, MSSQL, MongDB, DynamoDB, Cassandra
OLAP - Hive, Presto, Redshift, Amazon Athena
-> Data Warehouse

Postgres, MySQL, Oracle, MSSQL

Writer -> Reader
-> Reader
-> Reader

cart
1
..

..
1,000,000,000

Writer (cart id 1-100,000,000) -> Reader
-> Reader
-> Reader

Writer (cart id 200,000,001 - 500,000,000) -> Reader
-> Reader
-> Reader

Writer (cart id 500,000,001 - 750,000,000) -> Reader
-> Reader
-> Reader

Problems:
1.) You need to build that app logic
2.) Rebalance shards
3.) Add shards

RDBMS - Relational Database Management System

NoSQL

Application -> Database

MongDB

DynamoDB -> SELECT \* from table WHERE primary_key = '' AND secondary_key = ''
Casssandra - Replication factor - 3

1
2
3
..
45 - primary_key = 1
46 - primary_key = 1
47 - primary_key = 1
..
100

3 copies of all data
entire cluster contains all the data of my universe

NewSQL
NoSQL + RDBMS

Spanner (MySQL), TiDB (MySQL), RoachDB, AWS DSQL (Postgres)

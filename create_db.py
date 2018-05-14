#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 10:54:43 2017

@author: gaelberon
"""

#############################
## DATABASE TABLES AND FIELDS
## 
import db_definition as db_def
import connect_db as db_con
import pymysql

print("Using pymysql…")

myConnection = pymysql.connect( host=db_def.hostname, user=db_def.username,
                                passwd=db_def.password, db=db_def.database,
                                connect_timeout=10 )

# Create table 'Geo_area_type'
db_con.createTable( myConnection, db_def.table_geo_area_type )
# Create foreign key for table 'Geo_area_type'
db_con.createForeignKey( myConnection, db_def.table_geo_area_type )

# Create table 'Geographique_area'
db_con.createTable( myConnection, db_def.table_geo_area )
# Create foreign key for table 'Geographique_area'
db_con.createForeignKey( myConnection, db_def.table_geo_area )

# Create table 'Geo_area_list'
db_con.createTable( myConnection, db_def.table_geo_area_list )
# Create foreign key for table 'Geo_area_list'
db_con.createForeignKey( myConnection, db_def.table_geo_area_list )

# Create table 'Customer_type'
db_con.createTable( myConnection, db_def.table_cust_type )
# Create foreign key for table 'Customer_type'
db_con.createForeignKey( myConnection, db_def.table_cust_type )

# Create table 'Customer'
db_con.createTable( myConnection, db_def.table_customer )
# Create foreign key for table 'Customer'
db_con.createForeignKey( myConnection, db_def.table_customer )

# Create table 'Customer_matching'
db_con.createTable( myConnection, db_def.table_cust_match )
# Create foreign key for table 'Customer_matching'
db_con.createForeignKey( myConnection, db_def.table_cust_match )

# Create table 'ATC'
db_con.createTable( myConnection, db_def.table_atc )
# Create foreign key for table 'ATC'
db_con.createForeignKey( myConnection, db_def.table_atc )

# Create table 'Manufacturer'
db_con.createTable( myConnection, db_def.table_manufacturer )
# Create foreign key for table 'Manufacturer'
db_con.createForeignKey( myConnection, db_def.table_manufacturer )

# Create table 'Product'
db_con.createTable( myConnection, db_def.table_product )
# Create foreign key for table 'Product'
db_con.createForeignKey( myConnection, db_def.table_product )

# Create table 'Distributor'
db_con.createTable( myConnection, db_def.table_distributor )
# Create foreign key for table 'Distributor'
db_con.createForeignKey( myConnection, db_def.table_distributor )

# Create table 'Channel'
db_con.createTable( myConnection, db_def.table_channel )
# Create foreign key for table 'Channel'
db_con.createForeignKey( myConnection, db_def.table_channel )

# Create table 'Transaction'
db_con.createTable( myConnection, db_def.table_transaction )
# Create foreign key for table 'Transaction'
db_con.createForeignKey( myConnection, db_def.table_transaction )


##################################
## Load the user referential (customer type, etc.)
##

db_con.createNewEntriesInTableNoPK( myConnection, db_def.table_cust_type_name,
                                    [db_def.field_cust_type_name],
                                    [db_def.key_cust_type_pharmacy] )

#selectFromTable( myConnection, [field_geo_a_t_id, field_geo_a_t_name], table_geo_area_type_name )

#myConnection.close()

#print("Using mysql.connector…")
#import mysql.connector
#myConnection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
#doQuery( myConnection )
#myConnection.close()

myConnection.close()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 13:16:08 2017

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
                               passwd=db_def.password, db=db_def.database )

# Drop foreign key on table 'Transaction'
db_con.dropForeignKey( myConnection, db_def.table_transaction )
# Drop table 'Transaction'
db_con.dropTable( myConnection, db_def.table_transaction )

# Drop foreign key on table 'Customer_matching'
db_con.dropForeignKey( myConnection, db_def.table_cust_match )
# Drop table 'Customer_matching'
db_con.dropTable( myConnection, db_def.table_cust_match )

# Drop foreign key on table 'Customer'
db_con.dropForeignKey( myConnection, db_def.table_customer )
# Drop table 'Customer'
db_con.dropTable( myConnection, db_def.table_customer )

# Drop foreign key on table 'Customer_type'
db_con.dropForeignKey( myConnection, db_def.table_cust_type )
# Drop table 'Customer_type'
db_con.dropTable( myConnection, db_def.table_cust_type )

# Drop foreign key on table 'Geo_area_list'
db_con.dropForeignKey( myConnection, db_def.table_geo_area_list )
# Drop table 'Geo_area_list'
db_con.dropTable( myConnection, db_def.table_geo_area_list )

# Drop foreign key on table 'Geographic_area'
db_con.dropForeignKey( myConnection, db_def.table_geo_area )
# Drop table 'Geographic_area'
db_con.dropTable( myConnection, db_def.table_geo_area )

# Drop foreign key on table 'Geo_area_type'
db_con.dropForeignKey( myConnection, db_def.table_geo_area_type )
# Drop table 'Geo_area_type'
db_con.dropTable( myConnection, db_def.table_geo_area_type )

# Drop foreign key on table 'Product'
db_con.dropForeignKey( myConnection, db_def.table_product )
# Drop table 'Product'
db_con.dropTable( myConnection, db_def.table_product )

# Drop foreign key on table 'ATC'
db_con.dropForeignKey( myConnection, db_def.table_atc )
# Drop table 'ATC'
db_con.dropTable( myConnection, db_def.table_atc )

# Drop foreign key on table 'Manufacturer'
db_con.dropForeignKey( myConnection, db_def.table_manufacturer )
# Drop table 'Manufacturer'
db_con.dropTable( myConnection, db_def.table_manufacturer )

# Drop foreign key on table 'Distributor'
db_con.dropForeignKey( myConnection, db_def.table_distributor )
# Drop table 'Distributor'
db_con.dropTable( myConnection, db_def.table_distributor )

# Drop foreign key on table 'Channel'
db_con.dropForeignKey( myConnection, db_def.table_channel )
# Drop table 'Channel'
db_con.dropTable( myConnection, db_def.table_channel )

myConnection.close()

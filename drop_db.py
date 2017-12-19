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

# Drop table table_name
def dropForeignKey( conn, table) :

    stmt = "";
    for field in table.fields :
        if table.foreign_keys[field] != "" :
            stmt = stmt + "set @var=if((SELECT true FROM information_schema.TABLE_CONSTRAINTS ";
            stmt = stmt + "WHERE CONSTRAINT_SCHEMA = DATABASE() AND ";
            stmt = stmt + "TABLE_NAME = '" + table.name + "' AND ";
            stmt = stmt + "CONSTRAINT_NAME = '" + table.foreign_keys[field] + "' AND ";
            stmt = stmt + "CONSTRAINT_TYPE = 'FOREIGN KEY') = true,'ALTER TABLE " + table.name + " ";
            stmt = stmt + "drop foreign key " + table.foreign_keys[field] + "','select 1'); ";
            stmt = stmt + "prepare stmt from @var; ";
            stmt = stmt + "execute stmt; ";
            stmt = stmt + "deallocate prepare stmt; ";
            #stmt = stmt + "system echo 'Drop " + foreign_keys_list[foreign_key] + " done...'; ";
    
    print(stmt)

    if stmt != "" :
        # Initiate the cursor on the connection
        cur = conn.cursor()
        # Execute the sql statement
        cur.execute( stmt )

# Drop table 'table'
def dropTable( conn, table ) :
    
    stmt = "DROP TABLE IF EXISTS `" + table.name + "`;"
    
    print(stmt)
    
    # DROP TABLE IF EXISTS `Geo_area_type`;

    # Initiate the cursor on the connection
    cur = conn.cursor()
    # Execute the sql statement
    cur.execute( stmt )

print("Using pymysql…")
import pymysql
myConnection = pymysql.connect( host=db_def.hostname, user=db_def.username,
                               passwd=db_def.password, db=db_def.database )

# Drop foreign key on table 'Transaction'
dropForeignKey( myConnection, db_def.table_transaction )
# Create table 'Transaction'
dropTable( myConnection, db_def.table_transaction )

# Drop foreign key on table 'Customer'
dropForeignKey( myConnection, db_def.table_customer )
# Create table 'Customer'
dropTable( myConnection, db_def.table_customer )

# Drop foreign key on table 'Customer_type'
dropForeignKey( myConnection, db_def.table_cust_type )
# Create table 'Customer_type'
dropTable( myConnection, db_def.table_cust_type )

# Drop foreign key on table 'Geo_area_list'
dropForeignKey( myConnection, db_def.table_geo_area_list )
# Create table 'Geo_area_list'
dropTable( myConnection, db_def.table_geo_area_list )

# Drop foreign key on table 'Geographic_area'
dropForeignKey( myConnection, db_def.table_geo_area )
# Create table 'Geographic_area'
dropTable( myConnection, db_def.table_geo_area )

# Drop foreign key on table 'Geo_area_type'
dropForeignKey( myConnection, db_def.table_geo_area_type )
# Create table 'Geo_area_type'
dropTable( myConnection, db_def.table_geo_area_type )

# Drop foreign key on table 'Product'
dropForeignKey( myConnection, db_def.table_product )
# Create table 'Product'
dropTable( myConnection, db_def.table_product )

# Drop foreign key on table 'ATC'
dropForeignKey( myConnection, db_def.table_atc )
# Create table 'ATC'
dropTable( myConnection, db_def.table_atc )

# Drop foreign key on table 'Manufacturer'
dropForeignKey( myConnection, db_def.table_manufacturer )
# Create table 'Manufacturer'
dropTable( myConnection, db_def.table_manufacturer )

# Drop foreign key on table 'Distributor'
dropForeignKey( myConnection, db_def.table_distributor )
# Create table 'Distributor'
dropTable( myConnection, db_def.table_distributor )

# Drop foreign key on table 'Channel'
dropForeignKey( myConnection, db_def.table_channel )
# Create table 'Channel'
dropTable( myConnection, db_def.table_channel )

myConnection.close()

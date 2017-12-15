#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 13:16:08 2017

@author: gaelberon
"""

#############################
## DATABASE TABLES AND FIELDS
## 
import db_definition

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

# Drop table table_name
def dropForeignKeyOld( conn, table_name, foreign_keys_list) :

    stmt = "";
    for foreign_key in foreign_keys_list :
        if foreign_keys_list[foreign_key] != "" :
            stmt = stmt + "set @var=if((SELECT true FROM information_schema.TABLE_CONSTRAINTS ";
            stmt = stmt + "WHERE CONSTRAINT_SCHEMA = DATABASE() AND ";
            stmt = stmt + "TABLE_NAME = '" + table_name + "' AND ";
            stmt = stmt + "CONSTRAINT_NAME = '" + foreign_keys_list[foreign_key] + "' AND ";
            stmt = stmt + "CONSTRAINT_TYPE = 'FOREIGN KEY') = true,'ALTER TABLE " + table_name + " ";
            stmt = stmt + "drop foreign key " + foreign_keys_list[foreign_key] + "','select 1'); ";
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

# Drop table table_name
def dropTableOld( conn, table_name ) :
    
    stmt = "DROP TABLE IF EXISTS `" + table_name + "`;"
    
    print(stmt)
    
    # DROP TABLE IF EXISTS `Geo_area_type`;

    # Initiate the cursor on the connection
    cur = conn.cursor()
    # Execute the sql statement
    cur.execute( stmt )

print("Using pymysql…")
import pymysql
myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database )

# Drop foreign key on table 'Customer'
dropForeignKey( myConnection, table_customer )
# Create table 'Customer'
dropTable( myConnection, table_customer )

# Drop foreign key on table 'Customer_type'
dropForeignKey( myConnection, table_cust_type )
# Create table 'Customer_type'
dropTable( myConnection, table_cust_type )

# Drop foreign key on table 'Geo_area_list'
dropForeignKey( myConnection, table_geo_area_list )
# Create table 'Geo_area_list'
dropTable( myConnection, table_geo_area_list )

# Drop foreign key on table 'Geographic_area'
dropForeignKey( myConnection, table_geo_area )
# Create table 'Geographic_area'
dropTable( myConnection, table_geo_area )

# Drop foreign key on table 'Geo_area_type'
dropForeignKey( myConnection, table_geo_area_type )
# Create table 'Geo_area_type'
dropTable( myConnection, table_geo_area_type )

# Drop foreign key on table 'Product'
dropForeignKey( myConnection, table_product )
# Create table 'Product'
dropTable( myConnection, table_product )

# Drop foreign key on table 'ATC'
dropForeignKey( myConnection, table_atc )
# Create table 'ATC'
dropTable( myConnection, table_atc )

# Drop foreign key on table 'Manufacturer'
dropForeignKey( myConnection, table_manufacturer )
# Create table 'Manufacturer'
dropTable( myConnection, table_manufacturer )

# Drop foreign key on table 'Distributor'
dropForeignKey( myConnection, table_distributor )
# Create table 'Distributor'
dropTable( myConnection, table_distributor )

# Drop foreign key on table 'Channel'
dropForeignKey( myConnection, table_channel )
# Create table 'Channel'
dropTable( myConnection, table_channel )

# Drop foreign key on table 'Transaction'
dropForeignKey( myConnection, table_transaction )
# Create table 'Transaction'
dropTable( myConnection, table_transaction )

myConnection.close()

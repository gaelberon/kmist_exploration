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
def dropForeignKey( conn, table_name, foreign_keys_list) :

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

# Drop table table_name
def dropTable( conn, table_name ) :
    
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

# Drop foreign key on table 'Geographic_area'
dropForeignKey( myConnection, table_geo_area, table_geo_area_fields_fk)

# Create table 'Geographic_area'
dropTable( myConnection, table_geo_area)

# Drop foreign key on table 'Geo_area_type'
dropForeignKey( myConnection, table_geo_area_type, table_geo_area_type_fields_fk)

# Create table 'Geo_area_type'
dropTable( myConnection, table_geo_area_type)

myConnection.close()

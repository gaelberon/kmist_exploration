#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 10:54:43 2017

@author: gaelberon
"""

#############################
## DATABASE TABLES AND FIELDS
## 
import db_definition

# Create table table_name
def createTable( conn, table_name, fields_names_list, fields_class,
                 fields_size, fields_not_null, fields_unique,
                 fields_auto_increment, fields_primary_key ) :
    
    stmt = ""
    primary_key = ""
    for field_name in fields_names_list :
        if stmt != "" :
            stmt = stmt + ", "
        
        field_size = ""
        if fields_size[field_name] != 'nan' :
            field_size = "(" + str(fields_size[field_name]) + ")"
        
        field_not_null = ""
        if fields_not_null[field_name] :
            field_not_null = "NOT NULL "
        
        field_unique = ""
        if fields_unique[field_name] :
            field_unique = "UNIQUE "
        
        field_auto_increment = ""
        if fields_auto_increment[field_name] :
            field_auto_increment = "AUTO_INCREMENT "
        
        if fields_primary_key[field_name] :
            if primary_key == "" :
                primary_key = primary_key + "PRIMARY KEY (`" + \
                              field_name + "` "
            else :
                primary_key = primary_key + ", `" + field_name + "` "
        
        stmt = stmt + "`" + field_name + "` " + \
               fields_class[field_name] + field_size + " " + \
               field_not_null + \
               field_unique + \
               field_auto_increment
    
    stmt = "CREATE TABLE `" + table_name + "` (" + \
           stmt + ", " + \
           primary_key + ")" + \
           ");"
    
    print(stmt)
    
    # "CREATE TABLE `{0}` ( \
    #  `geo_area_type_id` bigint(10) NOT NULL AUTO_INCREMENT, \
    #  `geo_area_type_char_name` char(50) NOT NULL UNIQUE, \
    #  PRIMARY KEY (`geo_area_type_id`) \
    # );".format(table_name)

    # Initiate the cursor on the connection
    cur = conn.cursor()
    # Execute the sql statement
    cur.execute( stmt )
    
# Create foreign key in table table_name
def createForeignKey( conn, table_name, fields_primary_key,
                      fields_primary_key_table ) :
    
    stmt = ""
    for field_primary_key in fields_primary_key :
        if fields_primary_key[field_primary_key] != "" :
            stmt = stmt + "ALTER TABLE `" + table_name + "` "
            stmt = stmt + "ADD CONSTRAINT `"
            stmt = stmt + fields_primary_key[field_primary_key]
            stmt = stmt + "` FOREIGN KEY (`" + field_primary_key + "`) "
            stmt = stmt + "REFERENCES `"
            stmt = stmt + fields_primary_key_table[field_primary_key]
            stmt = stmt + "`(`" + field_primary_key + "`); "
    
    print(stmt)
    
    # ALTER TABLE `Product` ADD CONSTRAINT `Product_fk0` FOREIGN KEY (`man_id`) REFERENCES `Manufacturer`(`man_id`);
    
    # Initiate the cursor on the connection
    cur = conn.cursor()
    # Execute the sql statement
    cur.execute( stmt )

print("Using pymysql…")
import pymysql
myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database )

# Create table 'Geo_area_type'
createTable( myConnection, table_geo_area_type,
             table_geo_area_type_fields_list,
             table_geo_area_type_fields_class,
             table_geo_area_type_fields_size,
             table_geo_area_type_fields_not_null,
             table_geo_area_type_fields_unique,
             table_geo_area_type_fields_auto_increment,
             table_geo_area_type_fields_primary_key)

# Create foreign key for table 'Geo_area_type'
createForeignKey( myConnection, table_geo_area_type,
                  table_geo_area_type_fields_fk,
                  table_geo_area_type_fields_fk_table)

# Create table 'Geographique_area'
createTable( myConnection, table_geo_area,
             table_geo_area_fields_list,
             table_geo_area_fields_class,
             table_geo_area_fields_size,
             table_geo_area_fields_not_null,
             table_geo_area_fields_unique,
             table_geo_area_fields_auto_increment,
             table_geo_area_fields_primary_key)

# Create foreign key for table 'Geographique_area'
createForeignKey( myConnection, table_geo_area,
                  table_geo_area_fields_fk,
                  table_geo_area_fields_fk_table)

myConnection.close()

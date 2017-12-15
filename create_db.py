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

# Create table 'table'
def createTable( conn, table ) :
    
    stmt = ""
    primary_key = ""
    
    for field in table.fields :
        
        if stmt != "" :
            stmt = stmt + ", "
        
        field_size = ""
        if table.fields_size[field] != 'nan' :
            field_size = "(" + str(table.fields_size[field]) + ")"
        
        field_not_null = ""
        if table.fields_not_null[field] :
            field_not_null = "NOT NULL "
        
        field_unique = ""
        if table.fields_unique[field] :
            field_unique = "UNIQUE "
        
        field_auto_increment = ""
        if table.fields_auto_increment[field] :
            field_auto_increment = "AUTO_INCREMENT "
        
        if table.fields_primary_key[field] :
            if primary_key == "" :
                primary_key = primary_key + "PRIMARY KEY (`" + \
                              field + "` "
            else :
                primary_key = primary_key + ", `" + field + "` "
        
        stmt = stmt + "`" + field + "` " + \
               table.fields_class[field] + field_size + " " + \
               field_not_null + \
               field_unique + \
               field_auto_increment
    
    stmt = "CREATE TABLE `" + table.name + "` (" + \
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

# Create foreign key in table 'table'
def createForeignKey( conn, table ) :
    
    stmt = ""
    for field in table.fields :
        if table.foreign_keys[field] != "" :
            stmt = stmt + "ALTER TABLE `" + table.name + "` "
            stmt = stmt + "ADD CONSTRAINT `"
            stmt = stmt + table.foreign_keys[field]
            stmt = stmt + "` FOREIGN KEY (`" + field + "`) "
            stmt = stmt + "REFERENCES `"
            stmt = stmt + table.fk_tables[field]
            stmt = stmt + "`(`" + table.fk_external_references[field] + "`); "
    
    print(stmt)
    
    # ALTER TABLE `Product` ADD CONSTRAINT `Product_fk0` FOREIGN KEY (`man_id`) REFERENCES `Manufacturer`(`man_id`);
    
    if stmt != "" :
        # Initiate the cursor on the connection
        cur = conn.cursor()
        # Execute the sql statement
        cur.execute( stmt )

print("Using pymysql…")
import pymysql
myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database )

# Create table 'Geo_area_type'
createTable( myConnection, table_geo_area_type )
# Create foreign key for table 'Geo_area_type'
createForeignKey( myConnection, table_geo_area_type )

# Create table 'Geographique_area'
createTable( myConnection, table_geo_area )
# Create foreign key for table 'Geographique_area'
createForeignKey( myConnection, table_geo_area )

# Create table 'Geo_area_list'
createTable( myConnection, table_geo_area_list )
# Create foreign key for table 'Geo_area_list'
createForeignKey( myConnection, table_geo_area_list )

# Create table 'Customer_type'
createTable( myConnection, table_cust_type )
# Create foreign key for table 'Customer_type'
createForeignKey( myConnection, table_cust_type )

# Create table 'Customer'
createTable( myConnection, table_customer )
# Create foreign key for table 'Customer'
createForeignKey( myConnection, table_customer )

# Create table 'ATC'
createTable( myConnection, table_atc )
# Create foreign key for table 'ATC'
createForeignKey( myConnection, table_atc )

# Create table 'Manufacturer'
createTable( myConnection, table_manufacturer )
# Create foreign key for table 'Manufacturer'
createForeignKey( myConnection, table_manufacturer )

# Create table 'Product'
createTable( myConnection, table_product )
# Create foreign key for table 'Product'
createForeignKey( myConnection, table_product )

# Create table 'Distributor'
createTable( myConnection, table_distributor )
# Create foreign key for table 'Distributor'
createForeignKey( myConnection, table_distributor )

# Create table 'Channel'
createTable( myConnection, table_channel )
# Create foreign key for table 'Channel'
createForeignKey( myConnection, table_channel )

# Create table 'Transaction'
createTable( myConnection, table_transaction )
# Create foreign key for table 'Transaction'
createForeignKey( myConnection, table_transaction )

myConnection.close()

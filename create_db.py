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
myConnection = pymysql.connect( host=db_def.hostname, user=db_def.username,
                                passwd=db_def.password, db=db_def.database )

# Create table 'Geo_area_type'
createTable( myConnection, db_def.table_geo_area_type )
# Create foreign key for table 'Geo_area_type'
createForeignKey( myConnection, db_def.table_geo_area_type )

# Create table 'Geographique_area'
createTable( myConnection, db_def.table_geo_area )
# Create foreign key for table 'Geographique_area'
createForeignKey( myConnection, db_def.table_geo_area )

# Create table 'Geo_area_list'
createTable( myConnection, db_def.table_geo_area_list )
# Create foreign key for table 'Geo_area_list'
createForeignKey( myConnection, db_def.table_geo_area_list )

# Create table 'Customer_type'
createTable( myConnection, db_def.table_cust_type )
# Create foreign key for table 'Customer_type'
createForeignKey( myConnection, db_def.table_cust_type )

# Create table 'Customer'
createTable( myConnection, db_def.table_customer )
# Create foreign key for table 'Customer'
createForeignKey( myConnection, db_def.table_customer )

# Create table 'ATC'
createTable( myConnection, db_def.table_atc )
# Create foreign key for table 'ATC'
createForeignKey( myConnection, db_def.table_atc )

# Create table 'Manufacturer'
createTable( myConnection, db_def.table_manufacturer )
# Create foreign key for table 'Manufacturer'
createForeignKey( myConnection, db_def.table_manufacturer )

# Create table 'Product'
createTable( myConnection, db_def.table_product )
# Create foreign key for table 'Product'
createForeignKey( myConnection, db_def.table_product )

# Create table 'Distributor'
createTable( myConnection, db_def.table_distributor )
# Create foreign key for table 'Distributor'
createForeignKey( myConnection, db_def.table_distributor )

# Create table 'Channel'
createTable( myConnection, db_def.table_channel )
# Create foreign key for table 'Channel'
createForeignKey( myConnection, db_def.table_channel )

# Create table 'Transaction'
createTable( myConnection, db_def.table_transaction )
# Create foreign key for table 'Transaction'
createForeignKey( myConnection, db_def.table_transaction )


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

#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 14:45:32 2017

@author: gaelberon
"""

#############################
## DATABASE TABLES AND FIELDS
## 
import db_definition as db_def
import numpy as np

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

# Create new entry into table table_name without primary key
def createNewEntriesInTableNoPK( conn, table_name, fields_names_list, values_names_list ) :
    createNewEntriesInTable( conn, table_name, fields_names_list, values_names_list )

# Create new entry into table table_name
def createNewEntriesInTable( conn, table_name, fields_names_list, values_names_list ) :
    # Build the lists of fields and values to be populated in the table
    fields = ""
    values = ""
    for i in range(len(fields_names_list)):
        field_name = fields_names_list[i]
        value_name = values_names_list[i]
        
        #if (value_name == "nan"):
        #    value_name = ""
            
        if ( value_name != np.NAN and value_name != np.nan and
             value_name != np.NaN and str(value_name) != "nan" and
             str(value_name) != "") :
            #print("value_name: " + str(value_name))
            if fields == "" :
                fields = field_name
            else :
                fields = fields + ", " + field_name
            if values == "" :
                values = "'" + str(value_name) + "'"
            else :
                values = values + ", " + "'" + str(value_name) + "'"
        #else :
            #print("Value is null, NaN or empty for field name: " + field_name)

#    for field_name in fields_names_list :
#        if fields == "" :
#            fields = field_name
#        else :
#            fields = fields + ", " + field_name
#    for value_name in values_names_list :
#        if (value_name == "nan"):
#            value_name = ""
#        if values == "" :
#            values = "'" + str(value_name) + "'"
#        else :
#            values = values + ", " + "'" + str(value_name) + "'"
    
    # Build the sql statement for inserting values in the table
    stmt = "INSERT INTO {0} ({1}) \
                     VALUES ({2});".format(table_name,
                                             fields,
                                             values)
                     
    print(stmt)
    
    # Initiate the cursor on the connection
    cur = conn.cursor()
    # Execute the sql statement
    cur.execute( stmt )
    # Execute the commit
    cur.execute( "COMMIT;")

# Select values of 'fields_names_list' from 'table_name'
def selectFromTable( conn, fields_names_list, table_name ) :
    
    # Build the list of fields to be populated in the table
    fields = ""
    for field_name in fields_names_list :
        if fields == "" :
            fields = field_name
        else :
            fields = fields + ", " + field_name
    
    # Build the sql statement for inserting values in the table
    stmt = "SELECT {0} FROM {1}".format(fields, table_name)
    
    print(stmt)
    
    # Initiate the cursor on the connection
    cur = conn.cursor()
    # Execute the sql statement
    cur.execute( stmt )
    result_set = cur.fetchall()

    #for field1, field2 in cur.fetchall() :
    #    print(field1, field2)

    return(result_set)
    
# Select values of 'fields_names_list' from 'table_name'
def selectFromTableWithClauses( conn, fields_names_list, table_name,
                                where_fields_names_list,
                                where_fields_values_list) :
    
    # Build the list of fields to be populated in the table
    fields = ""
    for field_name in fields_names_list :
        if fields == "" :
            fields = field_name
        else :
            fields = fields + ", " + field_name
            
    where_fields = ""
    for where_field_idx, where_field_name in enumerate(where_fields_names_list):
#    for  in len(where_fields_names_list) :
        print("Index dans la table: " + table_name + ", is: " + str(where_field_idx))
#        where_field_name = where_fields_names_list[where_field_idx]
        where_field_value = where_fields_values_list[where_field_idx]
        if where_fields == "" :
            where_fields = where_field_name + " = '" + where_field_value + "'"
        else :
            where_fields = where_fields + " and " + \
                           where_field_name + " = '" + where_field_value + "'"
    
    where_fields = " where " + where_fields
    # Build the sql statement for inserting values in the table
    stmt = "SELECT {0} FROM {1}".format(fields, table_name)
    stmt = stmt + where_fields
    
    print(stmt)
    
    # Initiate the cursor on the connection
    cur = conn.cursor()
    # Execute the sql statement
    cur.execute( stmt )
    result_set = cur.fetchall()
    
    #result_list = {}
    #for row in result_set :
    #    for field_name in fields_names_list :
    #        print("%s" % (row[field_name]))
    #        #result_list[field_name] = row[field_name]
    
    return(result_set)

#print("Using MySQLdb…")
#import MySQLdb
#myConnection = MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
#doQuery( myConnection )
#myConnection.close()

#print("Using pymysql…")
#import pymysql
#myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
#createNewEntriesInTableNoPK( myConnection, table_geo_area_type_name, [field_geo_a_t_name], ['DA NANG'] )

#selectFromTable( myConnection, [field_geo_a_t_id, field_geo_a_t_name], table_geo_area_type_name )

#myConnection.close()

#print("Using mysql.connector…")
#import mysql.connector
#myConnection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
#doQuery( myConnection )
#myConnection.close()

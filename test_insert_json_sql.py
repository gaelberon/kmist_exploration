#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 11:47:10 2018

@author: gaelberon
"""

#############################
## DATABASE TABLES AND FIELDS
## 
import db_definition as db_def
import connect_db as db_con
import pymysql
from datetime import datetime

########################################
## TABLE PHARMACY FROM SANISPHERE SCHEMA
########################################
##         Field          Type  Null  Key   Default            Extra
##            id       int(11)   NO   PRI      NULL   auto_increment
##   campaign_id       int(11)  YES   MUL      NULL
##          slug  varchar(255)   NO            NULL
##        status  varchar(255)   NO            NULL
##          data      longtext   NO            NULL
##    country_id       int(11)  YES   MUL      NULL
## ph_created_at      datetime  YES            NULL
## ph_updated_at      datetime  YES            NULL
##    created_by       int(11)  YES   MUL      NULL
##    updated_by       int(11)  YES   MUL      NULL

table_pharmacy_name = 'Pharmacy'
field_pharma_id = 'id'
field_pharma_fk_campaign_id = 'campaign_id'
field_pharma_slug = 'slug'
field_pharma_status = 'status'
field_pharma_fk_country_id = 'country_id'
field_pharma_ph_created_at = 'ph_created_at'
field_pharma_ph_updated_at = 'ph_updated_at'
field_pharma_fk_created_by = 'created_by'
field_pharma_fk_updated_by = 'updated_by'
# Json field
field_pharma_data = 'data'

## table 'Pharmacy'
table_pharma = db_def.db_table()
table_pharma.name = table_pharmacy_name

table_pharma.fields.append(field_pharma_id)
table_pharma.fields.append(field_pharma_fk_campaign_id)
table_pharma.fields.append(field_pharma_slug)
table_pharma.fields.append(field_pharma_status)
table_pharma.fields.append(field_pharma_fk_country_id)
table_pharma.fields.append(field_pharma_ph_created_at)
table_pharma.fields.append(field_pharma_ph_updated_at)
table_pharma.fields.append(field_pharma_fk_created_by)
table_pharma.fields.append(field_pharma_fk_updated_by)
table_pharma.fields.append(field_pharma_data)

table_pharma.fields_class[field_pharma_id] = db_def.primary_keys_class
table_pharma.fields_class[field_pharma_fk_campaign_id] = db_def.primary_keys_class
table_pharma.fields_class[field_pharma_slug] = 'varchar'
table_pharma.fields_class[field_pharma_status] = 'varchar'
table_pharma.fields_class[field_pharma_fk_country_id] = db_def.primary_keys_class
table_pharma.fields_class[field_pharma_ph_created_at] = 'datetime'
table_pharma.fields_class[field_pharma_ph_updated_at] = 'datetime'
table_pharma.fields_class[field_pharma_fk_created_by] = db_def.primary_keys_class
table_pharma.fields_class[field_pharma_fk_updated_by] = db_def.primary_keys_class
table_pharma.fields_class[field_pharma_data] = 'longtext'

table_pharma.fields_size[field_pharma_id] = db_def.primary_keys_size
table_pharma.fields_size[field_pharma_fk_campaign_id] = db_def.primary_keys_size
table_pharma.fields_size[field_pharma_slug] = db_def.big_char_size
table_pharma.fields_size[field_pharma_status] = db_def.big_char_size
table_pharma.fields_size[field_pharma_fk_country_id] = db_def.primary_keys_size
table_pharma.fields_size[field_pharma_ph_created_at] = 'nan'
table_pharma.fields_size[field_pharma_ph_updated_at] = 'nan'
table_pharma.fields_size[field_pharma_fk_created_by] = db_def.primary_keys_size
table_pharma.fields_size[field_pharma_fk_updated_by] = db_def.primary_keys_size
table_pharma.fields_size[field_pharma_data] = 'nan'

table_pharma.fields_not_null[field_pharma_id] = 1
table_pharma.fields_not_null[field_pharma_fk_campaign_id] = 0
table_pharma.fields_not_null[field_pharma_slug] = 0
table_pharma.fields_not_null[field_pharma_status] = 0
table_pharma.fields_not_null[field_pharma_fk_country_id] = 0
table_pharma.fields_not_null[field_pharma_ph_created_at] = 1
table_pharma.fields_not_null[field_pharma_ph_updated_at] = 1
table_pharma.fields_not_null[field_pharma_fk_created_by] = 1
table_pharma.fields_not_null[field_pharma_fk_updated_by] = 1
table_pharma.fields_not_null[field_pharma_data] = 1

table_pharma.fields_unique[field_pharma_id] = 1
table_pharma.fields_unique[field_pharma_fk_campaign_id] = 0
table_pharma.fields_unique[field_pharma_slug] = 0
table_pharma.fields_unique[field_pharma_status] = 0
table_pharma.fields_unique[field_pharma_fk_country_id] = 0
table_pharma.fields_unique[field_pharma_ph_created_at] = 0
table_pharma.fields_unique[field_pharma_ph_updated_at] = 0
table_pharma.fields_unique[field_pharma_fk_created_by] = 0
table_pharma.fields_unique[field_pharma_fk_updated_by] = 0
table_pharma.fields_unique[field_pharma_data] = 0

table_pharma.fields_auto_increment[field_pharma_id] = 1
table_pharma.fields_auto_increment[field_pharma_fk_campaign_id] = 0
table_pharma.fields_auto_increment[field_pharma_slug] = 0
table_pharma.fields_auto_increment[field_pharma_status] = 0
table_pharma.fields_auto_increment[field_pharma_fk_country_id] = 0
table_pharma.fields_auto_increment[field_pharma_ph_created_at] = 0
table_pharma.fields_auto_increment[field_pharma_ph_updated_at] = 0
table_pharma.fields_auto_increment[field_pharma_fk_created_by] = 0
table_pharma.fields_auto_increment[field_pharma_fk_updated_by] = 0
table_pharma.fields_auto_increment[field_pharma_data] = 0

table_pharma.fields_primary_key[field_pharma_id] = 1
table_pharma.fields_primary_key[field_pharma_fk_campaign_id] = 0
table_pharma.fields_primary_key[field_pharma_slug] = 0
table_pharma.fields_primary_key[field_pharma_status] = 0
table_pharma.fields_primary_key[field_pharma_fk_country_id] = 0
table_pharma.fields_primary_key[field_pharma_ph_created_at] = 0
table_pharma.fields_primary_key[field_pharma_ph_updated_at] = 0
table_pharma.fields_primary_key[field_pharma_fk_created_by] = 0
table_pharma.fields_primary_key[field_pharma_fk_updated_by] = 0
table_pharma.fields_primary_key[field_pharma_data] = 0

table_pharma.foreign_keys[field_pharma_id] = ''
table_pharma.foreign_keys[field_pharma_fk_campaign_id] = '' # 'id'
table_pharma.foreign_keys[field_pharma_slug] = ''
table_pharma.foreign_keys[field_pharma_status] = ''
table_pharma.foreign_keys[field_pharma_fk_country_id] = '' # 'id'
table_pharma.foreign_keys[field_pharma_ph_created_at] = ''
table_pharma.foreign_keys[field_pharma_ph_updated_at] = ''
table_pharma.foreign_keys[field_pharma_fk_created_by] = '' # 'id'
table_pharma.foreign_keys[field_pharma_fk_updated_by] = '' # 'id'
table_pharma.foreign_keys[field_pharma_data] = ''

table_pharma.fk_tables[field_pharma_id] = ''
table_pharma.fk_tables[field_pharma_fk_campaign_id] = '' # 'campaign'
table_pharma.fk_tables[field_pharma_slug] = ''
table_pharma.fk_tables[field_pharma_status] = ''
table_pharma.fk_tables[field_pharma_fk_country_id] = '' # 'country'
table_pharma.fk_tables[field_pharma_ph_created_at] = ''
table_pharma.fk_tables[field_pharma_ph_updated_at] = ''
table_pharma.fk_tables[field_pharma_fk_created_by] = '' # 'sanisphere_user'
table_pharma.fk_tables[field_pharma_fk_updated_by] = '' # 'sanisphere_user'
table_pharma.fk_tables[field_pharma_data] = ''

table_pharma.fk_external_references[field_pharma_id] = ''
table_pharma.fk_external_references[field_pharma_fk_campaign_id] = '' # field_campaign_id
table_pharma.fk_external_references[field_pharma_slug] = ''
table_pharma.fk_external_references[field_pharma_status] = ''
table_pharma.fk_external_references[field_pharma_fk_country_id] = '' # field_country_id
table_pharma.fk_external_references[field_pharma_ph_created_at] = ''
table_pharma.fk_external_references[field_pharma_ph_updated_at] = ''
table_pharma.fk_external_references[field_pharma_fk_created_by] = '' # field_sanisphere_user_id
table_pharma.fk_external_references[field_pharma_fk_updated_by] = '' # field_sanisphere_user_id
table_pharma.fk_external_references[field_pharma_data] = ''

## Other example of Json format for Phamarcy.data's field:

#"{
#"name":"APOTEK EMMA CIJERAH",
#"City":"BANDUNG",
#"Area":"BANDUNG KULON",
#"pharmacy_address":"JLN. CIJERAH NO. 206",
#"Pharmacist Name":"DRS. AKHMAD PRIYADI, MM, APT",
#"pharmacy_phone":"022-6034904",
#"email_address":"",
#"pharmacy_patients_per_day":"100-200",
#"pharmacy_depend_hospital":"MINOR",
#"pharmacy_type":"INDEP",
#"pharmacy_insurance":"No",
#"pharmacy_standard":"B - Average local standard",
#"Type of Area 1":"Average - 2nd quartile",
#"district_profile":"Other",
#"Place for counselling":"No",
#"Doctor Surgery":"Yes",
#"Computerized pharmacy":"Yes",
#"pharmacy_hypertension_test":"No",
#"pharmacy_blood_glucose_test":"No",
#"Staff followed":"Pharmacist assistant",
#"Pharmacist assistant, technician or vendor present":"",
#"Non Pharmacists (other than owner) selling":"",
#"Non pharmacist counselling":"",
#"Universal coverage awareness":"Aware, good understanding",
#"Universal coverage respondent":"Pharmacist assistant(s), technicians, and/or vendors",
#"pharmacy_comment":"",
#"id":"new_1_1374816106292",
#"slug":"Indonesia-1_1374818669566-BANDUNG"
#}"

json_tag_pharmacy_data_campaign = "campaign"
json_tag_pharmacy_data_name = "name"
json_tag_pharmacy_data_city = "city"
json_tag_pharmacy_data_district = "district"
json_tag_pharmacy_data_district_txt = "district_txt"
json_tag_pharmacy_data_pharmacy_address = "pharmacy_address"
json_tag_pharmacy_data_flatitude = "flatitude"
json_tag_pharmacy_data_flongitude = "flongitude"
json_tag_pharmacy_data_add_comment = "add_comment"
json_tag_pharmacy_data_location_of_the_pharmacy = "location_of_the_pharmacy"
json_tag_pharmacy_data_busy_street = "busy_street"
json_tag_pharmacy_data_pharmacist_name = "pharmacist_name"
json_tag_pharmacy_data_pharmacist_phone = "pharmacy_phone"
json_tag_pharmacy_data_pharmacist_email = "pharmacy_email"
json_tag_pharmacy_data_pharmacy_patients_per_day = "pharmacy_patients_per_day"
json_tag_pharmacy_data_dedicated_storage = "dedicated_storage"
json_tag_pharmacy_data_fridged = "fridged"
json_tag_pharmacy_data_superficy = "superficy"
json_tag_pharmacy_data_staff_vendor = "staff_vendor"
json_tag_pharmacy_data_staff_other = "staff_other"
json_tag_pharmacy_data_category_management = "category_management"
json_tag_pharmacy_data_stock_quality = "stock_quality"
json_tag_pharmacy_data_shelves = "shelves"
json_tag_pharmacy_data_otc_self = "otc_self"
json_tag_pharmacy_data_otc_rx_corner = "otc_rx_corner"
json_tag_pharmacy_data_para_corner = "para_corner"
json_tag_pharmacy_data_para_corner_area = "para_corner_area"
json_tag_pharmacy_data_pharmacy_depend_hospital = "pharmacy_depend_hospital"
json_tag_pharmacy_data_pharmacy_type_of_hospital = "pharmacy_type_of_hospital"
json_tag_pharmacy_data_pharmacy_type = "pharmacy_type"
json_tag_pharmacy_data_pharmacy_standard = "pharmacy_standard"
json_tag_pharmacy_data_type_of_area = "type_of_area"
json_tag_pharmacy_data_computerized_pharmacy = "computerized_pharmacy"
json_tag_pharmacy_data_pharmacy_insurance = "pharmacy_insurance"
json_tag_pharmacy_data_glucose = "glucose"
json_tag_pharmacy_data_pressure = "pressure"
json_tag_pharmacy_data_bmi = "bmi"
json_tag_pharmacy_data_bmi2 = "bmi2"
json_tag_pharmacy_data_pharmacy_comments = "pharmacy_comments"
json_tag_pharmacy_data_relationship = "relationship"
json_tag_pharmacy_data_country = "country"
json_tag_pharmacy_data_slug = "slug"
json_tag_pharmacy_data_id = "id"
json_tag_pharmacy_data_created = "created"
json_tag_pharmacy_data_updated = "updated"

print("Using pymysql…")

myConnection = pymysql.connect( host=db_def.hostname, user=db_def.username,
                               passwd=db_def.password, db=db_def.database )

# Drop foreign key on table 'Pharmacy'
db_con.dropForeignKey( myConnection, table_pharma )
# Drop table 'Pharmacy'
db_con.dropTable( myConnection, table_pharma )

# Create table 'Pharmacy'
db_con.createTable( myConnection, table_pharma )
# Create foreign key for table 'Pharmacy'
db_con.createForeignKey( myConnection, table_pharma )

## Initialize the data to insert into table 'Pharmacy'
table_name = 'Pharmacy'
fields_names_list = [field_pharma_id,
                     field_pharma_fk_campaign_id,
                     field_pharma_slug,
                     field_pharma_status,
                     field_pharma_fk_country_id,
                     field_pharma_ph_created_at,
                     field_pharma_ph_updated_at,
                     field_pharma_fk_created_by,
                     field_pharma_fk_updated_by,
                     field_pharma_data]

json_stmt = '{' + '"'
json_stmt += json_tag_pharmacy_data_campaign + '":"' + '160' + '","'
json_stmt += json_tag_pharmacy_data_name + '":"' + 'GUERFIA SOHAIB' + '","'
json_stmt += json_tag_pharmacy_data_city + '":"' + 'ANN' + '","'
json_stmt += json_tag_pharmacy_data_district + '":"' + 'ANNABA' + '","'
json_stmt += json_tag_pharmacy_data_district_txt + '":"' + 'ANNABA' + '","'
json_stmt += json_tag_pharmacy_data_pharmacy_address + '":"' + 'CITE DES MARTYRS' + '","'
json_stmt += json_tag_pharmacy_data_flatitude + '":"' + '","'
json_stmt += json_tag_pharmacy_data_flongitude + '":"' + '","'
json_stmt += json_tag_pharmacy_data_add_comment + '":"' + 'BT 81 N 652' + '","'
json_stmt += json_tag_pharmacy_data_location_of_the_pharmacy + '":' + '["OTHER"]' + ',"'
json_stmt += json_tag_pharmacy_data_busy_street + '":"' + 'N' + '","'
json_stmt += json_tag_pharmacy_data_pharmacist_name + '":"' + 'GUERFIA SOHAIB' + '","'
json_stmt += json_tag_pharmacy_data_pharmacist_phone + '":"' + '038417591' + '","'
json_stmt += json_tag_pharmacy_data_pharmacist_email + '":"' + '","'
json_stmt += json_tag_pharmacy_data_pharmacy_patients_per_day + '":"' + '100-200' + '","'
json_stmt += json_tag_pharmacy_data_dedicated_storage + '":"' + 'Y' + '","'
json_stmt += json_tag_pharmacy_data_fridged + '":"' + 'Y' + '","'
json_stmt += json_tag_pharmacy_data_superficy + '":"' + '1-4' + '","'
json_stmt += json_tag_pharmacy_data_staff_vendor + '":"' + '2' + '","'
json_stmt += json_tag_pharmacy_data_staff_other + '":"' + '","'
json_stmt += json_tag_pharmacy_data_category_management + '":"' + '","'
json_stmt += json_tag_pharmacy_data_stock_quality + '":"' + '","'
json_stmt += json_tag_pharmacy_data_shelves + '":"' + 'Y' + '","'
json_stmt += json_tag_pharmacy_data_otc_self + '":"' + 'N' + '","'
json_stmt += json_tag_pharmacy_data_otc_rx_corner + '":"' + 'Y' + '","'
json_stmt += json_tag_pharmacy_data_para_corner + '":"' + 'Y' + '","'
json_stmt += json_tag_pharmacy_data_para_corner_area + '":"' + '<5M2' + '","'
json_stmt += json_tag_pharmacy_data_pharmacy_depend_hospital + '":"' + 'MINOR' + '","'
json_stmt += json_tag_pharmacy_data_pharmacy_type_of_hospital + '":"' + 'CAB' + '","'
json_stmt += json_tag_pharmacy_data_pharmacy_type + '":"' + 'INDEP' + '","'
json_stmt += json_tag_pharmacy_data_pharmacy_standard + '":"' + 'B' + '","'
json_stmt += json_tag_pharmacy_data_type_of_area + '":"' + 'AVG' + '","'
json_stmt += json_tag_pharmacy_data_computerized_pharmacy + '":"' + 'Y' + '","'
json_stmt += json_tag_pharmacy_data_pharmacy_insurance + '":' + '["CHI"]' + ',"'
json_stmt += json_tag_pharmacy_data_glucose + '":"' + 'Y' + '","'
json_stmt += json_tag_pharmacy_data_pressure + '":"' + 'Y' + '","'
json_stmt += json_tag_pharmacy_data_bmi + '":"' + 'N' + '","'
json_stmt += json_tag_pharmacy_data_bmi2 + '":"' + 'N' + '","'
json_stmt += json_tag_pharmacy_data_pharmacy_comments + '":"' + '","'
json_stmt += json_tag_pharmacy_data_relationship + '":"' + 'COND' + '","'
json_stmt += json_tag_pharmacy_data_country + '":"' + '15' + '","'
json_stmt += json_tag_pharmacy_data_slug + '":"' + 'new-ALGERIA-20180513093217-ANN' + '","'
json_stmt += json_tag_pharmacy_data_id + '":"' + 'new-ALGERIA-20180513093217-ANN' + '","'
json_stmt += json_tag_pharmacy_data_created + '":"' + '2018-05-13 09:32:17' + '","'
json_stmt += json_tag_pharmacy_data_updated + '":"' + '2018-05-13 09:32:17' + '","'
json_stmt += '}'

values_names_list = [24233,
                     160,
                     'new-ALGERIA-20180513093217-ANN',
                     10,
                     15,
                     datetime.strptime('2018-05-14 04:13:34', '%Y-%m-%d  %I:%M:%S'),
                     datetime.strptime('2018-05-14 04:13:34', '%Y-%m-%d  %I:%M:%S'),
                     758,
                     758,
                     json_stmt]

db_con.createNewEntriesInTable( myConnection, table_name,
                               fields_names_list, values_names_list )

myConnection.close()

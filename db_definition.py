#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 10:55:45 2017

@author: gaelberon
"""

hostname = 'localhost'
username = 'KD'
password = 'KD'
database = 'KD'

class db_table:

	def __init__(self):
		self.name = ''
		self.fields = []
		self.fields_class = {}
		self.fields_size = {}
		self.fields_not_null = {}
		self.fields_unique = {}
		self.fields_auto_increment = {}
		self.fields_primary_key = {}
		self.foreign_keys = {}
		self.fk_tables = {}
		self.fk_external_references = {}

#####################
## DATABASE CONSTANTS
## 

## Primary keys class
primary_keys_class = 'bigint'
## Primary keys size
primary_keys_size = 10
## Standard char size
stantard_char_size = 50

#############################
## DATABASE TABLES AND FIELDS
## 
table_geo_area_type_name = 'Geo_area_type'
field_geo_area_type_id = 'geo_area_type_id'
field_geo_area_type_name = 'geo_area_type_char_name'

table_geo_area_name = 'Geographic_area'
field_geo_area_id = 'geo_area_id'
field_geo_area_name = 'geo_area_char_name'
field_geo_area_fk_geo_a_t_id = 'geo_area_type_id'

table_geo_area_list_name = 'Geo_area_list'
field_geo_area_list_id = 'geo_area_list_id'
field_geo_area_list_fk_geo_area_id = 'geo_area_id'

table_cust_type_name = 'Customer_type'
field_cust_type_id = 'cust_type_id'
field_cust_type_name = 'cust_type_char_name'

key_cust_type_pharmacy = 'pharmacy'

table_cust_match_name = 'Customer_matching'
field_cust_match_fk_cust_id = 'cust_id'
field_cust_match_sanisphere_id = 'sanisphere_id'
field_cust_match_alcon_id = 'alcon_id'
field_cust_match_novartis_id = 'novartis_id'
field_cust_match_ipsen_id = 'ipsen_id'
field_cust_match_msd_id = 'msd_id'
field_cust_match_sanofi_id = 'sanofi_id'
field_cust_match_pfizer_id = 'pfizer_id'
field_cust_match_united_id = 'united_id'

table_customer_name = 'Customer'
field_cust_id = 'cust_id'
field_cust_code_zpv = 'cust_char_code_zpv'
field_cust_name = 'cust_char_name'
field_cust_address = 'cust_char_address'
# Address fields
field_cust_add_nb = 'cust_int_add_nb'
field_cust_add_street = 'cust_char_add_street'
field_cust_add_ward = 'cust_char_add_ward'
field_cust_add_district = 'cust_char_add_district'
#field_cust_city = 'cust_char_city'
field_cust_add_city_province = 'cust_char_add_city_province'
field_cust_add_area = 'cust_char_add_area'
field_cust_add_state = 'cust_char_add_state'
field_cust_longitude = 'cust_dec_longitude'
field_cust_latitude = 'cust_dec_latitude'
field_cust_fk_geo_area_list_id = 'geo_area_list_id'
field_cust_fk_cust_type_id = 'cust_type_id'

table_manufacturer_name = 'Manufacturer'
field_man_id = 'man_id'
field_man_name = 'man_char_name'

table_atc_name = 'ATC'
field_atc_id = 'atc_id'
field_atc_name = 'atc_char_name'

table_product_name = 'Product'
field_prd_id = 'prd_id'
field_prd_name = 'prd_char_name'
field_prd_fk_man_id = 'man_id'
field_prd_fk_atc_id = 'atc_id'

table_distributor_name = 'Distributor'
field_dist_id = 'dist_id'
field_dist_name = 'dist_char_name'

table_channel_name = 'Channel'
field_chan_id = 'chan_id'
field_chan_name = 'chan_char_name'

table_transaction_name = 'Transaction'
field_tra_fk_prd_id = 'prd_id'
field_tra_fk_cust_id = 'cust_id'
field_tra_period_start = 'tra_dt_period_start'
field_tra_period_end = 'tra_dt_period_end'
field_tra_nb_item = 'tra_int_nb_item'
field_tra_fk_chan_id = 'chan_id'
field_tra_btob = 'tra_bool_btob'
field_tra_fk_dist_id = 'dist_id'

## table 'Geo_area_type'
table_geo_area_type = db_table()
table_geo_area_type.name = table_geo_area_type_name

table_geo_area_type.fields.append(field_geo_area_type_id)
table_geo_area_type.fields.append(field_geo_area_type_name)

table_geo_area_type.fields_class[field_geo_area_type_id] = primary_keys_class
table_geo_area_type.fields_class[field_geo_area_type_name] = 'char'

table_geo_area_type.fields_size[field_geo_area_type_id] = primary_keys_size
table_geo_area_type.fields_size[field_geo_area_type_name] = stantard_char_size

table_geo_area_type.fields_not_null[field_geo_area_type_id] = 1
table_geo_area_type.fields_not_null[field_geo_area_type_name] = 1

table_geo_area_type.fields_unique[field_geo_area_type_id] = 1
table_geo_area_type.fields_unique[field_geo_area_type_name] = 1

table_geo_area_type.fields_auto_increment[field_geo_area_type_id] = 1
table_geo_area_type.fields_auto_increment[field_geo_area_type_name] = 0

table_geo_area_type.fields_primary_key[field_geo_area_type_id] = 1
table_geo_area_type.fields_primary_key[field_geo_area_type_name] = 0

table_geo_area_type.foreign_keys[field_geo_area_type_id] = ''
table_geo_area_type.foreign_keys[field_geo_area_type_name] = ''

table_geo_area_type.fk_tables[field_geo_area_type_id] = ''
table_geo_area_type.fk_tables[field_geo_area_type_name] = ''

table_geo_area_type.fk_external_references[field_geo_area_type_id] = ''
table_geo_area_type.fk_external_references[field_geo_area_type_name] = ''

## table 'Geographic_area'
table_geo_area = db_table()
table_geo_area.name = table_geo_area_name

table_geo_area.fields.append(field_geo_area_id)
table_geo_area.fields.append(field_geo_area_name)
table_geo_area.fields.append(field_geo_area_fk_geo_a_t_id)

table_geo_area.fields_class[field_geo_area_id] = primary_keys_class
table_geo_area.fields_class[field_geo_area_name] = 'char'
table_geo_area.fields_class[field_geo_area_fk_geo_a_t_id] = primary_keys_class

table_geo_area.fields_size[field_geo_area_id] = primary_keys_size
table_geo_area.fields_size[field_geo_area_name] = stantard_char_size
table_geo_area.fields_size[field_geo_area_fk_geo_a_t_id] = primary_keys_size

table_geo_area.fields_not_null[field_geo_area_id] = 1
table_geo_area.fields_not_null[field_geo_area_name] = 1
table_geo_area.fields_not_null[field_geo_area_fk_geo_a_t_id] = 1

table_geo_area.fields_unique[field_geo_area_id] = 1
table_geo_area.fields_unique[field_geo_area_name] = 1
table_geo_area.fields_unique[field_geo_area_fk_geo_a_t_id] = 0

table_geo_area.fields_auto_increment[field_geo_area_id] = 1
table_geo_area.fields_auto_increment[field_geo_area_name] = 0
table_geo_area.fields_auto_increment[field_geo_area_fk_geo_a_t_id] = 0

table_geo_area.fields_primary_key[field_geo_area_id] = 1
table_geo_area.fields_primary_key[field_geo_area_name] = 0
table_geo_area.fields_primary_key[field_geo_area_fk_geo_a_t_id] = 0

table_geo_area.foreign_keys[field_geo_area_id] = ''
table_geo_area.foreign_keys[field_geo_area_name] = ''
table_geo_area.foreign_keys[field_geo_area_fk_geo_a_t_id] = 'geo_area_fk_geo_area_type_id'

table_geo_area.fk_tables[field_geo_area_id] = ''
table_geo_area.fk_tables[field_geo_area_name] = ''
table_geo_area.fk_tables[field_geo_area_fk_geo_a_t_id] = table_geo_area_type_name

table_geo_area.fk_external_references[field_geo_area_id] = ''
table_geo_area.fk_external_references[field_geo_area_name] = ''
table_geo_area.fk_external_references[field_geo_area_fk_geo_a_t_id] = field_geo_area_type_id

## table 'Geo_area_list'
table_geo_area_list = db_table()
table_geo_area_list.name = table_geo_area_list_name

table_geo_area_list.fields.append(field_geo_area_list_id)
table_geo_area_list.fields.append(field_geo_area_list_fk_geo_area_id)

table_geo_area_list.fields_class[field_geo_area_list_id] = primary_keys_class
table_geo_area_list.fields_class[field_geo_area_list_fk_geo_area_id] = primary_keys_class

table_geo_area_list.fields_size[field_geo_area_list_id] = primary_keys_size
table_geo_area_list.fields_size[field_geo_area_list_fk_geo_area_id] = primary_keys_size

table_geo_area_list.fields_not_null[field_geo_area_list_id] = 1
table_geo_area_list.fields_not_null[field_geo_area_list_fk_geo_area_id] = 1

table_geo_area_list.fields_unique[field_geo_area_list_id] = 0
table_geo_area_list.fields_unique[field_geo_area_list_fk_geo_area_id] = 0

table_geo_area_list.fields_auto_increment[field_geo_area_list_id] = 0
table_geo_area_list.fields_auto_increment[field_geo_area_list_fk_geo_area_id] = 0

table_geo_area_list.fields_primary_key[field_geo_area_list_id] = 1
table_geo_area_list.fields_primary_key[field_geo_area_list_fk_geo_area_id] = 1

table_geo_area_list.foreign_keys[field_geo_area_list_id] = ''
table_geo_area_list.foreign_keys[field_geo_area_list_fk_geo_area_id] = 'geo_area_list_fk_geo_area_id'

table_geo_area_list.fk_tables[field_geo_area_list_id] = ''
table_geo_area_list.fk_tables[field_geo_area_list_fk_geo_area_id] = table_geo_area_name

table_geo_area_list.fk_external_references[field_geo_area_list_id] = ''
table_geo_area_list.fk_external_references[field_geo_area_list_fk_geo_area_id] = field_geo_area_id

## table 'Customer_type'
table_cust_type = db_table()
table_cust_type.name = table_cust_type_name

table_cust_type.fields.append(field_cust_type_id)
table_cust_type.fields.append(field_cust_type_name)

table_cust_type.fields_class[field_cust_type_id] = primary_keys_class
table_cust_type.fields_class[field_cust_type_name] = 'char'

table_cust_type.fields_size[field_cust_type_id] = primary_keys_size
table_cust_type.fields_size[field_cust_type_name] = stantard_char_size

table_cust_type.fields_not_null[field_cust_type_id] = 1
table_cust_type.fields_not_null[field_cust_type_name] = 1

table_cust_type.fields_unique[field_cust_type_id] = 1
table_cust_type.fields_unique[field_cust_type_name] = 0

table_cust_type.fields_auto_increment[field_cust_type_id] = 1
table_cust_type.fields_auto_increment[field_cust_type_name] = 0

table_cust_type.fields_primary_key[field_cust_type_id] = 1
table_cust_type.fields_primary_key[field_cust_type_name] = 0

table_cust_type.foreign_keys[field_cust_type_id] = ''
table_cust_type.foreign_keys[field_cust_type_name] = ''

table_cust_type.fk_tables[field_cust_type_id] = ''
table_cust_type.fk_tables[field_cust_type_name] = ''

table_cust_type.fk_external_references[field_cust_type_id] = ''
table_cust_type.fk_external_references[field_cust_type_name] = ''

## table 'Customer_matching'
table_cust_match = db_table()
table_cust_match.name = table_cust_match_name

table_cust_match.fields.append(field_cust_match_fk_cust_id)
table_cust_match.fields.append(field_cust_match_sanisphere_id)
table_cust_match.fields.append(field_cust_match_pfizer_id)
table_cust_match.fields.append(field_cust_match_sanofi_id)

table_cust_match.fields_class[field_cust_match_fk_cust_id] = primary_keys_class
table_cust_match.fields_class[field_cust_match_sanisphere_id] = primary_keys_class
table_cust_match.fields_class[field_cust_match_pfizer_id] = primary_keys_class
table_cust_match.fields_class[field_cust_match_sanofi_id] = primary_keys_class

table_cust_match.fields_size[field_cust_match_fk_cust_id] = primary_keys_size
table_cust_match.fields_size[field_cust_match_sanisphere_id] = primary_keys_size
table_cust_match.fields_size[field_cust_match_pfizer_id] = primary_keys_size
table_cust_match.fields_size[field_cust_match_sanofi_id] = primary_keys_size

table_cust_match.fields_not_null[field_cust_match_fk_cust_id] = 1
table_cust_match.fields_not_null[field_cust_match_sanisphere_id] = 0
table_cust_match.fields_not_null[field_cust_match_pfizer_id] = 0
table_cust_match.fields_not_null[field_cust_match_sanofi_id] = 0

table_cust_match.fields_unique[field_cust_match_fk_cust_id] = 1
table_cust_match.fields_unique[field_cust_match_sanisphere_id] = 0
table_cust_match.fields_unique[field_cust_match_pfizer_id] = 0
table_cust_match.fields_unique[field_cust_match_sanofi_id] = 0

table_cust_match.fields_auto_increment[field_cust_match_fk_cust_id] = 0
table_cust_match.fields_auto_increment[field_cust_match_sanisphere_id] = 0
table_cust_match.fields_auto_increment[field_cust_match_pfizer_id] = 0
table_cust_match.fields_auto_increment[field_cust_match_sanofi_id] = 0

table_cust_match.fields_primary_key[field_cust_match_fk_cust_id] = 1
table_cust_match.fields_primary_key[field_cust_match_sanisphere_id] = 0
table_cust_match.fields_primary_key[field_cust_match_pfizer_id] = 0
table_cust_match.fields_primary_key[field_cust_match_sanofi_id] = 0

table_cust_match.foreign_keys[field_cust_match_fk_cust_id] = 'customer_matching_fk_cust_id'
table_cust_match.foreign_keys[field_cust_match_sanisphere_id] = ''
table_cust_match.foreign_keys[field_cust_match_pfizer_id] = ''
table_cust_match.foreign_keys[field_cust_match_sanofi_id] = ''

table_cust_match.fk_tables[field_cust_match_fk_cust_id] = table_customer_name
table_cust_match.fk_tables[field_cust_match_sanisphere_id] = ''
table_cust_match.fk_tables[field_cust_match_pfizer_id] = ''
table_cust_match.fk_tables[field_cust_match_sanofi_id] = ''

table_cust_match.fk_external_references[field_cust_match_fk_cust_id] = field_cust_id
table_cust_match.fk_external_references[field_cust_match_sanisphere_id] = ''
table_cust_match.fk_external_references[field_cust_match_pfizer_id] = ''
table_cust_match.fk_external_references[field_cust_match_sanofi_id] = ''

## table 'Customer'
table_customer = db_table()
table_customer.name = table_customer_name

table_customer.fields.append(field_cust_id)
table_customer.fields.append(field_cust_name)
table_customer.fields.append(field_cust_address)
table_customer.fields.append(field_cust_add_nb)
table_customer.fields.append(field_cust_add_street)
table_customer.fields.append(field_cust_add_ward)
table_customer.fields.append(field_cust_add_district)
#table_customer.fields.append(field_cust_city)
table_customer.fields.append(field_cust_add_city_province)
table_customer.fields.append(field_cust_add_area)
table_customer.fields.append(field_cust_add_state)
table_customer.fields.append(field_cust_longitude)
table_customer.fields.append(field_cust_latitude)
table_customer.fields.append(field_cust_fk_geo_area_list_id)
table_customer.fields.append(field_cust_fk_cust_type_id)

table_customer.fields_class[field_cust_id] = primary_keys_class
table_customer.fields_class[field_cust_name] = 'char'
table_customer.fields_class[field_cust_address] = 'char'
table_customer.fields_class[field_cust_add_nb] = 'INT'
table_customer.fields_class[field_cust_add_street] = 'char'
table_customer.fields_class[field_cust_add_ward] = 'char'
table_customer.fields_class[field_cust_add_district] = 'char'
#table_customer.fields_class[field_cust_city] = 'char'
table_customer.fields_class[field_cust_add_city_province] = 'char'
table_customer.fields_class[field_cust_add_area] = 'char'
table_customer.fields_class[field_cust_add_state] = 'char'
table_customer.fields_class[field_cust_longitude] = 'DECIMAL'
table_customer.fields_class[field_cust_latitude] = 'DECIMAL'
table_customer.fields_class[field_cust_fk_geo_area_list_id] = primary_keys_class
table_customer.fields_class[field_cust_fk_cust_type_id] = primary_keys_class

table_customer.fields_size[field_cust_id] = primary_keys_size
table_customer.fields_size[field_cust_name] = stantard_char_size
table_customer.fields_size[field_cust_address] = stantard_char_size
table_customer.fields_size[field_cust_add_nb] = 6
table_customer.fields_size[field_cust_add_street] = stantard_char_size
table_customer.fields_size[field_cust_add_ward] = stantard_char_size
table_customer.fields_size[field_cust_add_district] = stantard_char_size
#table_customer.fields_size[field_cust_city] = stantard_char_size
table_customer.fields_size[field_cust_add_city_province] = stantard_char_size
table_customer.fields_size[field_cust_add_area] = stantard_char_size
table_customer.fields_size[field_cust_add_state] = stantard_char_size
table_customer.fields_size[field_cust_longitude] = '20,16'
table_customer.fields_size[field_cust_latitude] = '20,16'
table_customer.fields_size[field_cust_fk_geo_area_list_id] = primary_keys_size
table_customer.fields_size[field_cust_fk_cust_type_id] = primary_keys_size

table_customer.fields_not_null[field_cust_id] = 1
table_customer.fields_not_null[field_cust_name] = 1
table_customer.fields_not_null[field_cust_address] = 0
table_customer.fields_not_null[field_cust_add_nb] = 0
table_customer.fields_not_null[field_cust_add_street] = 0
table_customer.fields_not_null[field_cust_add_ward] = 0
table_customer.fields_not_null[field_cust_add_district] = 0
#table_customer.fields_not_null[field_cust_city] = 0
table_customer.fields_not_null[field_cust_add_city_province] = 0
table_customer.fields_not_null[field_cust_add_area] = 0
table_customer.fields_not_null[field_cust_add_state] = 0
table_customer.fields_not_null[field_cust_longitude] = 0
table_customer.fields_not_null[field_cust_latitude] = 0
table_customer.fields_not_null[field_cust_fk_geo_area_list_id] = 0
table_customer.fields_not_null[field_cust_fk_cust_type_id] = 1

table_customer.fields_unique[field_cust_id] = 1
table_customer.fields_unique[field_cust_name] = 0
table_customer.fields_unique[field_cust_address] = 0
table_customer.fields_unique[field_cust_add_nb] = 0
table_customer.fields_unique[field_cust_add_street] = 0
table_customer.fields_unique[field_cust_add_ward] = 0
table_customer.fields_unique[field_cust_add_district] = 0
#table_customer.fields_unique[field_cust_city] = 0
table_customer.fields_unique[field_cust_add_city_province] = 0
table_customer.fields_unique[field_cust_add_area] = 0
table_customer.fields_unique[field_cust_add_state] = 0
table_customer.fields_unique[field_cust_longitude] = 0
table_customer.fields_unique[field_cust_latitude] = 0
table_customer.fields_unique[field_cust_fk_geo_area_list_id] = 0
table_customer.fields_unique[field_cust_fk_cust_type_id] = 0

table_customer.fields_auto_increment[field_cust_id] = 1
table_customer.fields_auto_increment[field_cust_name] = 0
table_customer.fields_auto_increment[field_cust_address] = 0
table_customer.fields_auto_increment[field_cust_add_nb] = 0
table_customer.fields_auto_increment[field_cust_add_street] = 0
table_customer.fields_auto_increment[field_cust_add_ward] = 0
table_customer.fields_auto_increment[field_cust_add_district] = 0
#table_customer.fields_auto_increment[field_cust_city] = 0
table_customer.fields_auto_increment[field_cust_add_city_province] = 0
table_customer.fields_auto_increment[field_cust_add_area] = 0
table_customer.fields_auto_increment[field_cust_add_state] = 0
table_customer.fields_auto_increment[field_cust_longitude] = 0
table_customer.fields_auto_increment[field_cust_latitude] = 0
table_customer.fields_auto_increment[field_cust_fk_geo_area_list_id] = 0
table_customer.fields_auto_increment[field_cust_fk_cust_type_id] = 0

table_customer.fields_primary_key[field_cust_id] = 1
table_customer.fields_primary_key[field_cust_name] = 0
table_customer.fields_primary_key[field_cust_address] = 0
table_customer.fields_primary_key[field_cust_add_nb] = 0
table_customer.fields_primary_key[field_cust_add_street] = 0
table_customer.fields_primary_key[field_cust_add_ward] = 0
table_customer.fields_primary_key[field_cust_add_district] = 0
#table_customer.fields_primary_key[field_cust_city] = 0
table_customer.fields_primary_key[field_cust_add_city_province] = 0
table_customer.fields_primary_key[field_cust_add_area] = 0
table_customer.fields_primary_key[field_cust_add_state] = 0
table_customer.fields_primary_key[field_cust_longitude] = 0
table_customer.fields_primary_key[field_cust_latitude] = 0
table_customer.fields_primary_key[field_cust_fk_geo_area_list_id] = 0
table_customer.fields_primary_key[field_cust_fk_cust_type_id] = 0

table_customer.foreign_keys[field_cust_id] = ''
table_customer.foreign_keys[field_cust_name] = ''
table_customer.foreign_keys[field_cust_address] = ''
table_customer.foreign_keys[field_cust_add_nb] = ''
table_customer.foreign_keys[field_cust_add_street] = ''
table_customer.foreign_keys[field_cust_add_ward] = ''
table_customer.foreign_keys[field_cust_add_district] = ''
#table_customer.foreign_keys[field_cust_city] = ''
table_customer.foreign_keys[field_cust_add_city_province] = ''
table_customer.foreign_keys[field_cust_add_area] = ''
table_customer.foreign_keys[field_cust_add_state] = ''
table_customer.foreign_keys[field_cust_longitude] = ''
table_customer.foreign_keys[field_cust_latitude] = ''
table_customer.foreign_keys[field_cust_fk_geo_area_list_id] = 'customer_fk_geo_area_list_id'
table_customer.foreign_keys[field_cust_fk_cust_type_id] = 'customer_fk_cust_type_id'

table_customer.fk_tables[field_cust_id] = ''
table_customer.fk_tables[field_cust_name] = ''
table_customer.fk_tables[field_cust_address] = ''
table_customer.fk_tables[field_cust_add_nb] = ''
table_customer.fk_tables[field_cust_add_street] = ''
table_customer.fk_tables[field_cust_add_ward] = ''
table_customer.fk_tables[field_cust_add_district] = ''
#table_customer.fk_tables[field_cust_city] = ''
table_customer.fk_tables[field_cust_add_city_province] = ''
table_customer.fk_tables[field_cust_add_area] = ''
table_customer.fk_tables[field_cust_add_state] = ''
table_customer.fk_tables[field_cust_longitude] = ''
table_customer.fk_tables[field_cust_latitude] = ''
table_customer.fk_tables[field_cust_fk_geo_area_list_id] = table_geo_area_list_name
table_customer.fk_tables[field_cust_fk_cust_type_id] = table_cust_type_name

table_customer.fk_external_references[field_cust_id] = ''
table_customer.fk_external_references[field_cust_name] = ''
table_customer.fk_external_references[field_cust_address] = ''
table_customer.fk_external_references[field_cust_add_nb] = ''
table_customer.fk_external_references[field_cust_add_street] = ''
table_customer.fk_external_references[field_cust_add_ward] = ''
table_customer.fk_external_references[field_cust_add_district] = ''
#table_customer.fk_external_references[field_cust_city] = ''
table_customer.fk_external_references[field_cust_add_city_province] = ''
table_customer.fk_external_references[field_cust_add_area] = ''
table_customer.fk_external_references[field_cust_add_state] = ''
table_customer.fk_external_references[field_cust_longitude] = ''
table_customer.fk_external_references[field_cust_latitude] = ''
table_customer.fk_external_references[field_cust_fk_geo_area_list_id] = field_geo_area_list_id
table_customer.fk_external_references[field_cust_fk_cust_type_id] = field_cust_type_id

## table 'Manufacturer'
table_manufacturer = db_table()
table_manufacturer.name = table_manufacturer_name

table_manufacturer.fields.append(field_man_id)
table_manufacturer.fields.append(field_man_name)

table_manufacturer.fields_class[field_man_id] = primary_keys_class
table_manufacturer.fields_class[field_man_name] = 'char'

table_manufacturer.fields_size[field_man_id] = primary_keys_size
table_manufacturer.fields_size[field_man_name] = stantard_char_size

table_manufacturer.fields_not_null[field_man_id] = 1
table_manufacturer.fields_not_null[field_man_name] = 1

table_manufacturer.fields_unique[field_man_id] = 1
table_manufacturer.fields_unique[field_man_name] = 1

table_manufacturer.fields_auto_increment[field_man_id] = 1
table_manufacturer.fields_auto_increment[field_man_name] = 0

table_manufacturer.fields_primary_key[field_man_id] = 1
table_manufacturer.fields_primary_key[field_man_name] = 0

table_manufacturer.foreign_keys[field_man_id] = ''
table_manufacturer.foreign_keys[field_man_name] = ''

table_manufacturer.fk_tables[field_man_id] = ''
table_manufacturer.fk_tables[field_man_name] = ''

table_manufacturer.fk_external_references[field_man_id] = ''
table_manufacturer.fk_external_references[field_man_name] = ''

## table 'ATC'
table_atc = db_table()
table_atc.name = table_atc_name

table_atc.fields.append(field_atc_id)
table_atc.fields.append(field_atc_name)

table_atc.fields_class[field_atc_id] = primary_keys_class
table_atc.fields_class[field_atc_name] = 'char'

table_atc.fields_size[field_atc_id] = primary_keys_size
table_atc.fields_size[field_atc_name] = stantard_char_size

table_atc.fields_not_null[field_atc_id] = 1
table_atc.fields_not_null[field_atc_name] = 1

table_atc.fields_unique[field_atc_id] = 1
table_atc.fields_unique[field_atc_name] = 1

table_atc.fields_auto_increment[field_atc_id] = 1
table_atc.fields_auto_increment[field_atc_name] = 0

table_atc.fields_primary_key[field_atc_id] = 1
table_atc.fields_primary_key[field_atc_name] = 0

table_atc.foreign_keys[field_atc_id] = ''
table_atc.foreign_keys[field_atc_name] = ''

table_atc.fk_tables[field_atc_id] = ''
table_atc.fk_tables[field_atc_name] = ''

table_atc.fk_external_references[field_atc_id] = ''
table_atc.fk_external_references[field_atc_name] = ''

## table 'Product'
table_product = db_table()
table_product.name = table_product_name

table_product.fields.append(field_prd_id)
table_product.fields.append(field_prd_name)
table_product.fields.append(field_prd_fk_man_id)
table_product.fields.append(field_prd_fk_atc_id)

table_product.fields_class[field_prd_id] = primary_keys_class
table_product.fields_class[field_prd_name] = 'char'
table_product.fields_class[field_prd_fk_man_id] = primary_keys_class
table_product.fields_class[field_prd_fk_atc_id] = primary_keys_class

table_product.fields_size[field_prd_id] = primary_keys_size
table_product.fields_size[field_prd_name] = stantard_char_size
table_product.fields_size[field_prd_fk_man_id] = primary_keys_size
table_product.fields_size[field_prd_fk_atc_id] = primary_keys_size

table_product.fields_not_null[field_prd_id] = 1
table_product.fields_not_null[field_prd_name] = 1
table_product.fields_not_null[field_prd_fk_man_id] = 1
table_product.fields_not_null[field_prd_fk_atc_id] = 1

table_product.fields_unique[field_prd_id] = 1
table_product.fields_unique[field_prd_name] = 0
table_product.fields_unique[field_prd_fk_man_id] = 0
table_product.fields_unique[field_prd_fk_atc_id] = 0

table_product.fields_auto_increment[field_prd_id] = 1
table_product.fields_auto_increment[field_prd_name] = 0
table_product.fields_auto_increment[field_prd_fk_man_id] = 0
table_product.fields_auto_increment[field_prd_fk_atc_id] = 0

table_product.fields_primary_key[field_prd_id] = 1
table_product.fields_primary_key[field_prd_name] = 0
table_product.fields_primary_key[field_prd_fk_man_id] = 0
table_product.fields_primary_key[field_prd_fk_atc_id] = 0

table_product.foreign_keys[field_prd_id] = ''
table_product.foreign_keys[field_prd_name] = ''
table_product.foreign_keys[field_prd_fk_man_id] = 'product_fk_man_id'
table_product.foreign_keys[field_prd_fk_atc_id] = 'product_fk_atc_id'

table_product.fk_tables[field_prd_id] = ''
table_product.fk_tables[field_prd_name] = ''
table_product.fk_tables[field_prd_fk_man_id] = table_manufacturer_name
table_product.fk_tables[field_prd_fk_atc_id] = table_atc_name

table_product.fk_external_references[field_prd_id] = ''
table_product.fk_external_references[field_prd_name] = ''
table_product.fk_external_references[field_prd_fk_man_id] = field_man_id
table_product.fk_external_references[field_prd_fk_atc_id] = field_atc_id

## table 'Distributor'
table_distributor = db_table()
table_distributor.name = table_distributor_name

table_distributor.fields.append(field_dist_id)
table_distributor.fields.append(field_dist_name)

table_distributor.fields_class[field_dist_id] = primary_keys_class
table_distributor.fields_class[field_dist_name] = 'char'

table_distributor.fields_size[field_dist_id] = primary_keys_size
table_distributor.fields_size[field_dist_name] = stantard_char_size

table_distributor.fields_not_null[field_dist_id] = 1
table_distributor.fields_not_null[field_dist_name] = 1

table_distributor.fields_unique[field_dist_id] = 1
table_distributor.fields_unique[field_dist_name] = 1

table_distributor.fields_auto_increment[field_dist_id] = 1
table_distributor.fields_auto_increment[field_dist_name] = 0

table_distributor.fields_primary_key[field_dist_id] = 1
table_distributor.fields_primary_key[field_dist_name] = 0

table_distributor.foreign_keys[field_dist_id] = ''
table_distributor.foreign_keys[field_dist_name] = ''

table_distributor.fk_tables[field_dist_id] = ''
table_distributor.fk_tables[field_dist_name] = ''

table_distributor.fk_external_references[field_dist_id] = ''
table_distributor.fk_external_references[field_dist_name] = ''

## table 'Channel'
table_channel = db_table()
table_channel.name = table_channel_name

table_channel.fields.append(field_chan_id)
table_channel.fields.append(field_chan_name)

table_channel.fields_class[field_chan_id] = primary_keys_class
table_channel.fields_class[field_chan_name] = 'char'

table_channel.fields_size[field_chan_id] = primary_keys_size
table_channel.fields_size[field_chan_name] = stantard_char_size

table_channel.fields_not_null[field_chan_id] = 1
table_channel.fields_not_null[field_chan_name] = 1

table_channel.fields_unique[field_chan_id] = 1
table_channel.fields_unique[field_chan_name] = 1

table_channel.fields_auto_increment[field_chan_id] = 1
table_channel.fields_auto_increment[field_chan_name] = 0

table_channel.fields_primary_key[field_chan_id] = 1
table_channel.fields_primary_key[field_chan_name] = 0

table_channel.foreign_keys[field_chan_id] = ''
table_channel.foreign_keys[field_chan_name] = ''

table_channel.fk_tables[field_chan_id] = ''
table_channel.fk_tables[field_chan_name] = ''

table_channel.fk_external_references[field_chan_id] = ''
table_channel.fk_external_references[field_chan_name] = ''

## table 'Transaction'
table_transaction = db_table()
table_transaction.name = table_transaction_name

table_transaction.fields.append(field_tra_fk_prd_id)
table_transaction.fields.append(field_tra_fk_cust_id)
table_transaction.fields.append(field_tra_period_start)
table_transaction.fields.append(field_tra_period_end)
table_transaction.fields.append(field_tra_nb_item)
table_transaction.fields.append(field_tra_fk_chan_id)
table_transaction.fields.append(field_tra_btob)
table_transaction.fields.append(field_tra_fk_dist_id)

table_transaction.fields_class[field_tra_fk_prd_id] = primary_keys_class
table_transaction.fields_class[field_tra_fk_cust_id] = primary_keys_class
table_transaction.fields_class[field_tra_period_start] = 'DATE'
table_transaction.fields_class[field_tra_period_end] = 'DATE'
table_transaction.fields_class[field_tra_nb_item] = 'INT'
table_transaction.fields_class[field_tra_fk_chan_id] = primary_keys_class
table_transaction.fields_class[field_tra_btob] = 'bool'
table_transaction.fields_class[field_tra_fk_dist_id] = primary_keys_class

table_transaction.fields_size[field_tra_fk_prd_id] = primary_keys_size
table_transaction.fields_size[field_tra_fk_cust_id] = primary_keys_size
table_transaction.fields_size[field_tra_period_start] = 'nan'
table_transaction.fields_size[field_tra_period_end] = 'nan'
table_transaction.fields_size[field_tra_nb_item] = 4
table_transaction.fields_size[field_tra_fk_chan_id] = primary_keys_size
table_transaction.fields_size[field_tra_btob] = 'nan'
table_transaction.fields_size[field_tra_fk_dist_id] = primary_keys_size

table_transaction.fields_not_null[field_tra_fk_prd_id] = 1
table_transaction.fields_not_null[field_tra_fk_cust_id] = 1
table_transaction.fields_not_null[field_tra_period_start] = 1
table_transaction.fields_not_null[field_tra_period_end] = 1
table_transaction.fields_not_null[field_tra_nb_item] = 0
table_transaction.fields_not_null[field_tra_fk_chan_id] = 1
table_transaction.fields_not_null[field_tra_btob] = 1
table_transaction.fields_not_null[field_tra_fk_dist_id] = 1

table_transaction.fields_unique[field_tra_fk_prd_id] = 0
table_transaction.fields_unique[field_tra_fk_cust_id] = 0
table_transaction.fields_unique[field_tra_period_start] = 0
table_transaction.fields_unique[field_tra_period_end] = 0
table_transaction.fields_unique[field_tra_nb_item] = 0
table_transaction.fields_unique[field_tra_fk_chan_id] = 0
table_transaction.fields_unique[field_tra_btob] = 0
table_transaction.fields_unique[field_tra_fk_dist_id] = 0

table_transaction.fields_auto_increment[field_tra_fk_prd_id] = 0
table_transaction.fields_auto_increment[field_tra_fk_cust_id] = 0
table_transaction.fields_auto_increment[field_tra_period_start] = 0
table_transaction.fields_auto_increment[field_tra_period_end] = 0
table_transaction.fields_auto_increment[field_tra_nb_item] = 0
table_transaction.fields_auto_increment[field_tra_fk_chan_id] = 0
table_transaction.fields_auto_increment[field_tra_btob] = 0
table_transaction.fields_auto_increment[field_tra_fk_dist_id] = 0

table_transaction.fields_primary_key[field_tra_fk_prd_id] = 1
table_transaction.fields_primary_key[field_tra_fk_cust_id] = 1
table_transaction.fields_primary_key[field_tra_period_start] = 1
table_transaction.fields_primary_key[field_tra_period_end] = 1
table_transaction.fields_primary_key[field_tra_nb_item] = 0
table_transaction.fields_primary_key[field_tra_fk_chan_id] = 0
table_transaction.fields_primary_key[field_tra_btob] = 0
table_transaction.fields_primary_key[field_tra_fk_dist_id] = 0

table_transaction.foreign_keys[field_tra_fk_prd_id] = 'transaction_fk_prd_id'
table_transaction.foreign_keys[field_tra_fk_cust_id] = 'transaction_fk_cust_id'
table_transaction.foreign_keys[field_tra_period_start] = ''
table_transaction.foreign_keys[field_tra_period_end] = ''
table_transaction.foreign_keys[field_tra_nb_item] = ''
table_transaction.foreign_keys[field_tra_fk_chan_id] = 'transaction_chan_id'
table_transaction.foreign_keys[field_tra_btob] = ''
table_transaction.foreign_keys[field_tra_fk_dist_id] = 'transaction_fk_dist_id'

table_transaction.fk_tables[field_tra_fk_prd_id] = table_product_name
table_transaction.fk_tables[field_tra_fk_cust_id] = table_customer_name
table_transaction.fk_tables[field_tra_period_start] = ''
table_transaction.fk_tables[field_tra_period_end] = ''
table_transaction.fk_tables[field_tra_nb_item] = ''
table_transaction.fk_tables[field_tra_fk_chan_id] = table_channel_name
table_transaction.fk_tables[field_tra_btob] = ''
table_transaction.fk_tables[field_tra_fk_dist_id] = table_distributor_name

table_transaction.fk_external_references[field_tra_fk_prd_id] = field_prd_id
table_transaction.fk_external_references[field_tra_fk_cust_id] = field_cust_id
table_transaction.fk_external_references[field_tra_period_start] = ''
table_transaction.fk_external_references[field_tra_period_end] = ''
table_transaction.fk_external_references[field_tra_nb_item] = ''
table_transaction.fk_external_references[field_tra_fk_chan_id] = field_chan_id
table_transaction.fk_external_references[field_tra_btob] = ''
table_transaction.fk_external_references[field_tra_fk_dist_id] = field_dist_id

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

#############################
## DATABASE TABLES AND FIELDS
## 
## table 'Geo_area_type'
table_geo_area_type = 'Geo_area_type'
field_geo_a_t_id = 'geo_area_type_id'
field_geo_a_t_name = 'geo_area_type_char_name'
table_geo_area_type_fields_list = [field_geo_a_t_id,
                                   field_geo_a_t_name]
table_geo_area_type_fields_class = {field_geo_a_t_id:'bigint', \
                                    field_geo_a_t_name:'char'}
table_geo_area_type_fields_size = {field_geo_a_t_id:10, \
                                   field_geo_a_t_name:50}
table_geo_area_type_fields_not_null = {field_geo_a_t_id:1, \
                                       field_geo_a_t_name:1}
table_geo_area_type_fields_unique = {field_geo_a_t_id:1, \
                                     field_geo_a_t_name:1}
table_geo_area_type_fields_auto_increment = {field_geo_a_t_id:1, \
                                             field_geo_a_t_name:0}
table_geo_area_type_fields_primary_key = {field_geo_a_t_id:1, \
                                          field_geo_a_t_name:0}
table_geo_area_type_fields_fk = {field_geo_a_t_id:'',
                                 field_geo_a_t_name:''}
table_geo_area_type_fields_fk_table = {field_geo_a_t_id:'',
                                       field_geo_a_t_name:''}

## table 'Geographic_area'
table_geo_area = 'Geographic_area'
field_geo_area_id = 'geo_area_id'
field_geo_area_name = 'geo_area_char_name'
field_geo_area_fk_geo_a_t_id = 'geo_area_type_id'
table_geo_area_fields_list = [field_geo_area_id,
                              field_geo_area_name,
                              field_geo_area_fk_geo_a_t_id]
table_geo_area_fields_class = {field_geo_area_id:'bigint',
                               field_geo_area_name:'char',
                               field_geo_area_fk_geo_a_t_id:'bigint'}
table_geo_area_fields_size = {field_geo_area_id:10,
                              field_geo_area_name:50,
                              field_geo_area_fk_geo_a_t_id:10}
table_geo_area_fields_not_null = {field_geo_area_id:1,
                                  field_geo_area_name:1,
                                  field_geo_area_fk_geo_a_t_id:1}
table_geo_area_fields_unique = {field_geo_area_id:1,
                                field_geo_area_name:1,
                                field_geo_area_fk_geo_a_t_id:0}
table_geo_area_fields_auto_increment = {field_geo_area_id:1,
                                        field_geo_area_name:0,
                                        field_geo_area_fk_geo_a_t_id:0}
table_geo_area_fields_primary_key = {field_geo_area_id:1,
                                     field_geo_area_name:0,
                                     field_geo_area_fk_geo_a_t_id:0}
table_geo_area_fields_fk = {field_geo_area_id:'',
                            field_geo_area_name:'',
                            field_geo_area_fk_geo_a_t_id:'geo_area_fk_geo_a_t_id'}
table_geo_area_fields_fk_table = {field_geo_area_id:'',
                                  field_geo_area_name:'',
                                  field_geo_area_fk_geo_a_t_id:'Geo_area_type'}

## table 'Geo_area_list'
table_geo_area_list = 'Geo_area_list'
field_geo_area_list_id = 'geo_area_list_id'
field_geo_area_list_fk_geo_area_id = 'geo_area_id'
table_geo_area_list_fields_list = [field_geo_area_list_id,
                                   field_geo_area_list_fk_geo_area_id]
table_geo_area_list_fields_class = {field_geo_area_list_id:'bigint',
                                    field_geo_area_list_fk_geo_area_id:'char'}
table_geo_area_list_fields_size = {field_geo_area_list_id:10,
                                   field_geo_area_list_fk_geo_area_id:50}

## table 'Customer_type'
table_cust_type = 'Customer_type'
field_cust_type_id = 'cust_type_id'
field_cust_type_name = 'cust_type_char_name'
table_cust_type_fields_list = [field_cust_type_id,
                               field_cust_type_name]
table_cust_type_fields_class = {field_cust_type_id:'bigint',
                                field_cust_type_name:'char'}
table_cust_type_fields_size = {field_cust_type_id:10,
                               field_cust_type_name:50}

## table 'Customer'
table_customer = 'Customer'
field_cust_id = 'cust_id'
field_cust_name = 'cust_char_name'
field_cust_fk_geo_area_list_id = 'geo_area_list_id'
field_cust_fk_cust_type_id = 'cust_type_id'
table_cust_fields_list = [field_cust_id,
                          field_cust_name,
                          field_cust_fk_geo_area_list_id,
                          field_cust_fk_cust_type_id]
table_cust_fields_class = {field_cust_id:'bigint',
                           field_cust_name:'char',
                           field_cust_fk_geo_area_list_id:'bigint',
                           field_cust_fk_cust_type_id:'bigint'}
table_cust_fields_size = {field_cust_id:10,
                          field_cust_name:50,
                          field_cust_fk_geo_area_list_id:10,
                          field_cust_fk_cust_type_id:10}

## table 'Manufacturer'
table_manufacturer = 'Manufacturer'
field_man_id = 'man_id'
field_man_name = 'man_char_name'
table_man_fields_list = [field_man_id,
                         field_man_name]
table_man_fields_class = {field_man_id:'bigint',
                          field_man_name:'char'}
table_man_fields_size = {field_man_id:10,
                         field_man_name:50}

## table 'ATC'
table_atc = 'ATC'
field_atc_id = 'atc_id'
field_atc_name = 'atc_char_name'
table_atc_fields_list = [field_atc_id,
                         field_atc_name]
table_atc_fields_class = {field_atc_id:'bigint',
                          field_atc_name:'char'}
table_atc_fields_size = {field_atc_id:'bigint',
                         field_atc_name:'char'}

## table 'Product'
table_product = 'Product'
field_prd_id = 'prd_id'
field_prd_name = 'prd_char_name'
field_prd_fk_man_id = 'man_id'
field_prd_fk_atc_id = 'atc_id'
table_atc_fields_list = [field_prd_id,
                         field_prd_name,
                         field_prd_fk_man_id,
                         field_prd_fk_atc_id]
table_atc_fields_class = {field_prd_id:'bigint',
                          field_prd_name:'char',
                          field_prd_fk_man_id:'bigint',
                          field_prd_fk_atc_id:'bigint'}
table_atc_fields_size = {field_prd_id:'bigint',
                         field_prd_name:'char',
                         field_prd_fk_man_id:'bigint',
                         field_prd_fk_atc_id:'bigint'}

## table 'Distributor'
table_distributor = 'Distributor'
field_dist_id = 'dist_id'
field_dist_name = 'dist_char_name'
table_dist_fields_list = [field_dist_id,
                          field_dist_name]
table_dist_fields_class = {field_dist_id:'bigint',
                           field_dist_name:'char'}
table_dist_fields_size = {field_dist_id:'bigint',
                          field_dist_name:'char'}

## table 'Channel'
table_channel = 'Channel'
field_chan_id = 'chan_id'
field_chan_name = 'chan_char_name'
table_chan_fields_list = [field_chan_id,
                          field_chan_name]
table_chan_fields_class = {field_chan_id:'bigint',
                           field_chan_name:'char'}
table_chan_fields_size = {field_chan_id:'bigint',
                          field_chan_name:'char'}

## table 'Transaction'
table_transaction = 'Transaction'
field_tra_fk_prd_id = 'prd_id'
field_tra_fk_cust_id = 'cust_id'
field_tra_period_start = 'tra_dt_period_start'
field_tra_period_end = 'tra_dt_period_end'
field_tra_nb_item = 'tra_int_nb_item'
field_tra_fk_chan_id = 'chan_id'
field_tra_btob = 'tra_bool_btob'
field_tra_fk_dist_id = 'dist_id'
table_tra_fields_list = [field_tra_fk_prd_id,
                         field_tra_fk_cust_id,
                         field_tra_period_start,
                         field_tra_period_end,
                         field_tra_nb_item,
                         field_tra_fk_chan_id,
                         field_tra_btob,
                         field_tra_fk_dist_id]
table_tra_fields_class = {field_tra_fk_prd_id:'bigint',
                          field_tra_fk_cust_id:'bigint',
                          field_tra_period_start:'DATE',
                          field_tra_period_end:'DATE',
                          field_tra_nb_item:'INT',
                          field_tra_fk_chan_id:'bigint',
                          field_tra_btob:'bool',
                          field_tra_fk_dist_id:'bigint'}
table_tra_fields_list = {field_tra_fk_prd_id:10,
                         field_tra_fk_cust_id:10,
                         field_tra_period_start:'nan',
                         field_tra_period_end:'nan',
                         field_tra_nb_item:4,
                         field_tra_fk_chan_id:10,
                         field_tra_btob:'nan',
                         field_tra_fk_dist_id:10}


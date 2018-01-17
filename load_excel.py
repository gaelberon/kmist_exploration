#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 09:03:27 2017

@author: gaelberon
"""

# Import libraries
import pandas as pd
import numpy as np
import os.path 
import db_definition as db_def
import connect_db as db_con
import pymysql

# Set references to Excel data files
path = "/Users/gaelberon/Documents/Sanisphere/data/"
fileNameList = ["171116 POP Indo Gael.xlsx",
                "List ATC3 Codes with definition.xlsx",
                "171115 pharmacy matching Indonesia.xlsx",
                "LIST CUSTOMER.xlsx",
                "Purchase Frekuensi .xlsx",
                "17113 Mapping Pharmacies Indonesia [Sanisphere Pfizer Sanofi]-Olin check done.xlsx"
               ]

fileList = {"Sanisphere_Pop": path + fileNameList[0],
            "Sanisphere_List_ATC3": path + fileNameList[1],
            "Sanisphere_matching_Indonesia": path + fileNameList[2],
            "Pfizer_List_customer": path + fileNameList[3],
            "Pfizer_Purchase_frequency": path + fileNameList[4],
            "Matching_Indonesia_Sanisphere_Pfizer": path + fileNameList[5]
           }

# Initialize 'csvPopFile' in order to store the Pop raw data
csvPopFile = "pop_file.csv"
csvPopFilePath = "./" + csvPopFile

# Sanisphere Excel Pop file columns
pop_col_period = "Period"
pop_col_transaction_id = "Transaction Id"
pop_col_pharmacy_id = "Pharmacy Id"
pop_col_brand_sold = "Brand Sold"
pop_col_form_sold = "Form Sold"
pop_col_inn_sold = "Inn Sold"
pop_col_atc2_sold = "Atc2 Sold"
pop_col_otc_ethical_sold = "Otc / Ethical Sold"
pop_col_company_sold = "Company Sold"
pop_col_type_of_company_sold = "Type Of Company Sold"
pop_col_driver_4_types = "Driver 4 types"
pop_col_switch_leak = "Switch / Leak"
pop_col_switch_leak_reason = "Switch / Leak Reason"
pop_col_switch_leak_reason_simplified = "Switch / Leak Reason Simplified"
pop_col_initial_demand_brand = "Initial Demand Brand"
pop_col_atc2_initial_demand = "Atc2 Initial Demand"
pop_col_inn_initial_demand = "Inn Initial Demand"
pop_col_company_initial_demand = "Company Initial Demand"
pop_col_type_of_company_initial_demand = "Type of Company Initial Demand"
pop_col_otc_ethical_initial_demand = "Otc / Ethical Initial Demand"
pop_col_initial_driver = "Initial Driver"
pop_col_type_of_prescriber = "Type Of Prescriber"
pop_col_sector_of_prescriber = "Sector Of Prescriber"
pop_col_city_detailled = "City detailled"
pop_col_city_aggregated = "City aggregated"
pop_col_hospital_influence = "Hospital Influence"
pop_col_chain_pharmacy = "Chain Pharmacy"
pop_col_segmentation_pharmacy = "Segmentation Pharmacy"
pop_col_insurance_affiliation_pharmacy = "Insurance Affiliation Pharmacy"
pop_col_insurance_affiliation_patient = "Insurance Affiliation Patient"
pop_col_drug_sold_real_name = "Drug Sold Real Name"
pop_col_drug_sold_real_form = "Drug Sold Real Form"
pop_col_cocktail = "Cocktail"
pop_col_country_company_drug_sold = "Country Company Drug Sold"
pop_col_prescriber_specialty = "Prescriber Specialty"
pop_col_company_group_drug_sold = "Company Group Drug Sold"
pop_col_company_group_initial_demand = "Company Group Initial Demand"
pop_col_date_of_observation = "Date of Observation"
pop_col_initial_demand_original_name = "Initial Demand Original Name"
pop_col_2017_s1 = "2017 - S1"
pop_col_2016_s2 = "2016 - S2"
pop_col_2016_s1 = "2016 - S1"
pop_col_2015_s2 = "2015 - S2"
pop_col_pfizer = "PFIZER"
pop_col_sanofi = "SANOFI"
pop_col_sanofi_sanofi_otc = "SANOFI SANOFI OTC"
pop_col_market_sold = "MARKET SOLD"
pop_col_market_initial = "MARKET INITIAL"
pop_col_chronic_acute = "CHRONIC / ACUTE"

# Initialize 'df_pop' data frame
df_pop = pd.DataFrame()
if (os.path.isfile(csvPopFile)) :
    df_pop = pd.DataFrame.from_csv(csvPopFilePath)
else :
    xl = pd.ExcelFile(fileList["Sanisphere_Pop"])
    #print(xl.sheet_names)
    df_pop = xl.parse("raw",
                      header=0,
                      parse_cols=[0, #"Period",
                                  1, #"Transaction Id",
                                  # 2, #"Item Id",
                                  # 3, #"Basket Id",
                                  4, #"Pharmacy Id",
                                  # 5, #"Drug Sold Id",
                                  # 6, #"Drug Initial Id",
                                  # 7, #"Brand Sold / For",
                                  8, #"Brand Sold",
                                  9, #"Form Sold",
                                  10, #"Inn Sold",
                                  # 11, #"Atc4 Sold",
                                  # 12, #"Atc3 Sold",
                                  13, #"Atc2 Sold",
                                  # 14, #"Atc1 Sold",
                                  15, #"Otc / Ethical Sold",
                                  # 16, #"Gx / Originators",
                                  17, #"Company Sold",
                                  18, #"Type Of Company Sold",
                                  # 19, #"Division Consolidated",
                                  # 20, #"Division",
                                  # 21, #"Sales Driver Full",
                                  # 22, #"Driver 3 types",
                                  # 23, #"Driver 5 types",
                                  24, #"Driver 4 types",
                                  25, #"Switch / Leak",
                                  26, #"Switch / Leak Reason",
                                  27, #"Switch / Leak Reason Simplified",
                                  # 28, #"Switch / Leak Initiator",
                                  29, #"Initial Demand Brand",
                                  # 30, #"Atc4 Initial Demand",
                                  # 31, #"Atc3 Initial Demand",
                                  32, #"Atc2 Initial Demand",
                                  # 33, #"Atc1 Initial Demand",
                                  34, #"Inn Initial Demand",
                                  35, #"Company Initial Demand",
                                  36, #"Type of Company Initial Demand",
                                  37, #"Otc / Ethical Initial Demand",
                                  38, #"Initial Driver",
                                  39, #"Type Of Prescriber",
                                  40, #"Sector Of Prescriber",
                                  41, #"City detailled",
                                  42, #"City aggregated",
                                  43, #"Hospital Influence",
                                  44, #"Chain Pharmacy",
                                  45, #"Segmentation Pharmacy",
                                  46, #"Insurance Affiliation Pharmacy",
                                  47, #"Insurance Affiliation Patient",
                                  48, #"Drug Sold Real Name",
                                  49, #"Drug Sold Real Form",
                                  50, #"Cocktail",
                                  # 51, #"Do Not Display",
                                  52, #"Country Company Drug Sold",
                                  53, #"Prescriber Specialty",
                                  54, #"Company Group Drug Sold",
                                  55, #"Company Group Initial Demand",
                                  56, #"Date of Observation",
                                  57, #"Initial Demand Original Name",
                                  # 58, #"Analyst",
                                  59, #"2017 - S1",
                                  60, #"2016 - S2",
                                  61, #"2016 - S1",
                                  62, #"2015 - S2",
                                  63, #"PFIZER",
                                  64, #"SANOFI",
                                  65, #"SANOFI SANOFI OTC",
                                  66, #"MARKET SOLD",
                                  67, #"MARKET INITIAL",
                                  68 #"CHRONIC / ACUTE"
                                 ])
   
#    df_pop = pd.read_excel(io=fileList["Sanisphere_Pop"],
#                           #sheet_name="raw",
#                           sheet_name=7,
    
    df_pop.to_csv(path_or_buf=csvPopFilePath)
#                  ,
#                  sep=', ',
#                  na_rep='',
#                  float_format=None,
#                  columns=None,
#                  header=True,
#                  index=True,
#                  index_label=None,
#                  mode='w',
#                  encoding=None,
#                  compression=None,
#                  quoting=None,
#                  quotechar='"',
#                  line_terminator='\n',
#                  chunksize=None,
#                  tupleize_cols=None,
#                  date_format=None,
#                  doublequote=True,
#                  escapechar=None,
#                  decimal='.')

# ['PFIZER FRIEND',
#  'mnc friend',
#  'Switch  leak',
#  'driver chronic',
#  'driver total',
#  'driver acute',
#  'chronic acut',
#  'raw',
#  'list chronic acute']

# 'df_pop' data frame details
print("df_pop dimensions: " + str(df_pop.shape))
print(df_pop.head())

# create entries in database
print("Using package pymysql…")
myConnection = pymysql.connect( host=db_def.hostname, user=db_def.username,
                                passwd=db_def.password, db=db_def.database )

print("Taille de ma liste: " + str(len([db_def.field_cust_type_name])))
cust_type_pharma_id_result_set = db_con.selectFromTableWithClauses( myConnection,
                                                           [db_def.field_cust_type_id],
                                                           db_def.table_cust_type_name,
                                                           [db_def.field_cust_type_name],
                                                           [db_def.key_cust_type_pharmacy])
#cust_type_pharma_id = cust_type_pharma_id_result_set[db_def.field_cust_type_id]

cust_type_pharma_id = cust_type_pharma_id_result_set[0][0]
#cust_type_pharma_id = ""
#for row in cust_type_pharma_id_result_set :
#    cust_type_pharma_id = row[db_def.field_cust_type_id]

print("cust_type_pharma_id: " + str(cust_type_pharma_id))

df_pharmacies = df_pop[[pop_col_pharmacy_id, pop_col_city_aggregated]].drop_duplicates()
#df_phamarcies = np.unique(df_pop[[pop_col_pharmacy_id, pop_col_city_aggregated]], axis=0)
#df_phamarcies = pd.concat(df_pop[pop_col_pharmacy_id], df_pop[pop_col_city_aggregated]).unique()

#df_pharmacies = df_pharmacies.reindex(range(len(df_pharmacies)))
df_pharmacies = df_pharmacies.reset_index()

print(df_pharmacies.head(20))

for tx_idx in range(len(df_pharmacies.index)) :
#for tx_idx in range(100) :
#    db_con.createNewEntriesInTableNoPK( myConnection, db_def.table_geo_area_type_name,
#                                        [db_def.field_geo_area_type_name],
#                                        ['DA NANG'] )  
#    
#    db_con.selectFromTable( myConnection,
#                            [db_def.field_geo_area_type_id, db_def.table_geo_area_type_name],
#                            db_def.table_geo_area_type_name )
    
    #print("index tx_idx: " + str(tx_idx))
    #print("Field qui pose probleme: " + str(df_pop.at[tx_idx, pop_col_pharmacy_id]))
    #print("Field qui pose probleme: " + df_pop.iloc[tx_idx][pop_col_pharmacy_id])
    
    db_con.createNewEntriesInTableNoPK( myConnection, db_def.table_customer_name,
                                        [db_def.field_cust_name,
                                         db_def.field_cust_address,
                                         db_def.field_cust_add_nb,
                                         db_def.field_cust_add_street,
                                         db_def.field_cust_add_ward,
                                         db_def.field_cust_add_district,
                                         #db_def.field_cust_city,
                                         db_def.field_cust_add_city,
                                         db_def.field_cust_add_area,
                                         db_def.field_cust_add_state,
                                         db_def.field_cust_fk_geo_area_list_id,
                                         db_def.field_cust_fk_cust_type_id],
                                        ["test_" + str(tx_idx),
                                         np.NaN, # address
                                         np.NaN, # address number
                                         np.NaN, # address street
                                         np.NaN, # address ward
                                         np.NaN, # address district
                                         str(df_pharmacies.at[tx_idx, pop_col_city_aggregated]),
                                         np.NaN, # address area
                                         np.NaN, # address state
                                         np.NaN, # geo area list id
                                         cust_type_pharma_id])
    
    cust_id_result_set = db_con.selectFromTable( myConnection,
                                                 ["max(" + db_def.field_cust_id + ")"],
                                                 db_def.table_customer_name)
    cust_id = cust_id_result_set[0][0]
    
    print("ID of the created Customer: " + str(cust_id))

    db_con.createNewEntriesInTableNoPK( myConnection, db_def.table_cust_match_name,
                                        [db_def.field_cust_match_fk_cust_id,
                                         db_def.field_cust_match_sanisphere_id,
                                         db_def.field_cust_match_pfizer_id,
                                         db_def.field_cust_match_sanofi_id],
                                        [str(cust_id),
                                         str(df_pharmacies.at[tx_idx, pop_col_pharmacy_id]),
                                         np.NaN,#str(df_pop.at[tx_idx, pop_col_pfizer]),
                                         np.NaN#str(df_pop.at[tx_idx, pop_col_sanofi])
                                         ])

myConnection.close()

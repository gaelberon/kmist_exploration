#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 10:29:27 2018

@author: gaelberon
"""

# Import libraries
import pandas as pd
import numpy as np
import os.path 

# Set references to Excel data files
path = "/Users/gaelberon/Documents/Sanisphere/R files/Sanofi_Indonesia/Channel_dynamics/data/"

fileNameList = ["Targeted Pharmacies 20Feb2018 (2).xlsx",
                "Universe PH_HOSP_WHS - 2015_2018.xlsx",
                "Universe PH-HOSP-WHS_15Feb2018.xlsx"
               ]

fileList = {"Targeted_pharmacies": path + fileNameList[0],
            "Universe_with_transactions": path + fileNameList[1],
            "Universe_with_channels": path + fileNameList[2]
           }

# Initialize 'csvTxAllFile' in order to store the Merged transactions raw data
csvTxAllFile = "Tx_all_file.csv"
csvTxAllFilePath = "./" + csvTxAllFile

# Worksheet for 'targeted pharmacies'
ws_targeted = "TARGETED PHARMACIES"
ws_targeted_start_row = 0

# Columns names for the worksheet 'ws_targeted'
col_targeted_customer_id = "CUSTOMER ID"
col_targeted_customer_name = "CUSTOMER NAME"
col_targeted_address = "ADDRESS"
col_targeted_regency = "REGENCY"
col_targeted_province = "PROVINCE"

# Worksheet for transactions CT_DA_NBM_DISCNTD
ws_tx = "TRANSACTION - CT_DA_NBM_DISCNTD"
ws_tx_start_row = 0
# Worksheet for transactions PARTNER
ws_tx_partner = "TRANSACTION - PARTNER"
ws_tx_partner_start_row = 0
# Worksheet for transactions TELFAST
ws_tx_telfast = "TRANSACTION - OUT of SCOPE"
ws_tx_telfast_start_row = 0

# Columns names for the worksheet 'ws_tx'
col_tx_year = "YEAR"
col_tx_month = "MONTH"
col_tx_day = "DAY"
col_tx_customer_id = "CUSTOMER ID"
col_tx_distributor_id = "DISTRIBUTOR ID"
col_tx_product_family = "PRODUCT FAMILY"
col_tx_gross_sales_quantity_sanofi = "GROSS SALES QUANTITY SANOFI"
col_tx_gross_sales_value_sanofi = "GROSS SALES VALUE SANOFI"
col_tx_net_sales_value_sanofi = "NET SALES VALUE SANOFI"
col_tx_discount_values_sanofi = "DISCOUNT VALUES SANOFI"

# Worksheet for universe with channels
ws_universe = "PH - HOSP - WHS"
ws_universe_start_row = 0

# Columns names for the worksheet 'ws_universe'
col_universe_customer_id = "CUSTOMER ID"
col_universe_distributor_customer_id = "DISTRIBUTOR CUSTOMER ID"
col_universe_customer_name = "CUSTOMER NAME"
col_universe_sanofi_channel_definition = "SANOFI CHANNEL DEFINITION"
col_universe_channel_name = "CHANNEL NAME"
col_universe_transaction_type = "TRANSACTION TYPE"
col_universe_distributor = "DISTRIBUTOR"
col_universe_province = "PROVINCE"
col_universe_regency = "REGENCY"
col_universe_area_id = "AREA ID"
col_universe_area = "AREA"
col_universe_address = "ADDRESS"

#############################################
## Load Excel file and return data.frame 'df'
def load_excel_file( path_to_file, sheet_name, start_row ) :
        df = None
        if ( path_to_file != None and path_to_file != "" and
             sheet_name != None and sheet_name != "" and
             start_row != None and start_row != "" ) :
            xl = pd.ExcelFile(path_to_file)    
            df = xl.parse(sheet_name,
                          header = start_row)
        
        return(df)



## Load file 'Targeted_pharmacies' into 'df_targeted' data.frame
#df_targeted = load_excel_file(fileList["Targeted_pharmacies"], ws_targeted, ws_targeted_start_row)
# Initialize 'df_tx_all' data frame
df_tx_all = pd.DataFrame()
if (os.path.isfile(csvTxAllFile)) :
    df_tx_all = pd.DataFrame.from_csv(csvTxAllFilePath)
else :
    ## Load file 'Universe_with_transactions' into 'df_tx' data.frame
    df_tx = load_excel_file(fileList["Universe_with_transactions"], ws_tx, ws_tx_start_row)
    ## Load file 'Universe_with_transactions' into 'df_tx_partner' data.frame
    df_tx_partner = load_excel_file(fileList["Universe_with_transactions"], ws_tx_partner, ws_tx_partner_start_row)
    ## Load file 'Universe_with_transactions' into 'df_tx_telfast' data.frame
    df_tx_telfast = load_excel_file(fileList["Universe_with_transactions"], ws_tx_telfast, ws_tx_telfast_start_row)
    ## Load file 'Universe_with_channels' into 'df_universe' data.frame
    df_universe = load_excel_file(fileList["Universe_with_channels"], ws_universe, ws_universe_start_row)

    print("Dimensions of data.frame 'df_tx':")
    print(df_tx.shape)
    
    print("Dimensions of data.frame 'df_tx_partner':")
    print(df_tx_partner.shape)
    
    print("Dimensions of data.frame 'df_tx_telfast':")
    print(df_tx_telfast.shape)
    
    print("Dimensions of data.frame 'df_universe':")
    print(df_universe.shape)
    
    #Frame = Frame.append(pandas.DataFrame(data = SomeNewLineOfData), ignore_index=True)
    ## Merge 'df_tx' and 'df_tx_partner' into 'df_tx_all'
    df_tx_all = df_tx.append(df_tx_partner, ignore_index=True)
    ## Merge 'df_tx_all' and 'df_tx_telfast' into 'df_tx_all'
    df_tx_all = df_tx_all.append(df_tx_telfast, ignore_index=True)
    
    print("Dimensions of data.frame 'df_tx_all' after merging wdata.frames 'df_tx', 'df_tx_partner' and 'df_tx_telfast':")
    print(df_tx_all.shape)
        
    # Select only usefull columns in 'df_tx_all'
    #df1 = df[['a','b']]
    df_tx_all = df_tx_all[[col_tx_customer_id,
                           col_tx_distributor_id,
                           col_tx_product_family,
                           col_tx_gross_sales_quantity_sanofi,
                           col_tx_gross_sales_value_sanofi,
                           col_tx_net_sales_value_sanofi,
                           col_tx_discount_values_sanofi]]
    
    # Select only usefull columns in 'df_universe'
    df_universe[[col_tx_distributor_id]] = df_universe[[col_universe_distributor_customer_id]]
    df_universe = df_universe[[col_universe_customer_id,
                               col_tx_distributor_id,
                               col_universe_sanofi_channel_definition]]
    
    # Merge 'df_tx_all' with 'df_universe' using 'inner' method in order to exclude
    # transactions without identified customers (with CUSTOMER ID = 'NULL' or 'NA')
    #A.merge(B, left_on='lkey', right_on='rkey', how='outer')
    df_tx_all = df_tx_all.merge(df_universe,
                                left_on=(col_tx_customer_id, col_tx_distributor_id),
                                right_on=(col_universe_customer_id, col_tx_distributor_id),
                                how='inner')

    df_tx_all.to_csv(path_or_buf=csvTxAllFilePath)

print("Dimensions of data.frame 'df_tx_all' after merging with Customers' universe:")
print(df_tx_all.shape)
print("Columns' names of data.frame 'df_tx_all' after merging with Customers' universe:")
print(list(df_tx_all.columns.values))

print(df_tx_all.groupby([col_tx_product_family])[col_tx_net_sales_value_sanofi].sum())

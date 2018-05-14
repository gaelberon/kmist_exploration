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
import matplotlib.pyplot as plt
# Set references to Excel data files
path = "C:\\Users\\renau\\Desktop\\Sanisphere Data Analysis\\180323_Conditions commercials Analysis\\"

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


# Get discount analysis function
# 
def get_discount_analysis( df, list_products, list_cust_ids, list_years, list_channels ) :
    print("Dimensions of 'df' before:")
    print(df.shape)
    # Filter data.frame 'df' on given parameters
    # products list
    if (list_products != None) :
        df = df.loc[df[col_tx_product_family].isin(list_products)]
        
    print("Dimensions of 'df' after filtering products:")
    print(df.shape)
    
    # customer ids list
    if (list_cust_ids != None) :
        df = df.loc[df[col_tx_customer_id].isin(list_cust_ids)]
        
    print("Dimensions of 'df' after filtering customer ids:")
    print(df.shape)
    
    # years list
    if (list_years != None) :
        df = df.loc[df[col_tx_year].isin(list_years)]
        
    print("Dimensions of 'df' after filtering years:")
    print(df.shape)
    
    # channels list
    if (list_channels != None) :
        df = df.loc[df[col_universe_sanofi_channel_definition].isin(list_channels)]
        
    print("Dimensions of 'df' after filtering channels:")
    print(df.shape)
    
    # Aggregate to get rid of 'DISTRIBUTOR_ID' and 'SANOFI_CHANNEL_DEFINITION'
    df = df.groupby([col_tx_year,
                     col_tx_month,
                     col_tx_day,
                     col_tx_customer_id,
                     col_tx_product_family])[col_tx_gross_sales_quantity_sanofi,
                                             col_tx_gross_sales_value_sanofi,
                                             col_tx_net_sales_value_sanofi,
                                             col_tx_discount_values_sanofi].sum()
    
    
    print("Dimensions of 'df' after aggregation:")
    print(df.shape)
    
    # Compute discount rate and create new column
    df["discount_rate"] = df[col_tx_discount_values_sanofi]/df[col_tx_gross_sales_value_sanofi]
    
    ## Plot discount rates per transactions volume
    # df["TRANSACTION_VOLUME"] = df[col_tx_gross_sales_quantity_sanofi]
    
    # Call the function to create plot
    scatterplot(df = df
                , x_data = df[col_tx_gross_sales_quantity_sanofi]
                , y_data = df['discount_rate']
                , x_label = 'Transactions'
                , y_label = 'Discount rate'
                , title = 'Discount Sales Analysis')    
    return(df)

    ## Plot discount rates per transactions volume
    # Set some parameters to apply to all plots
    # in each plot if desired
    import matplotlib
    # Plot size to 14" x 7"
    matplotlib.rc('figure', figsize = (14, 7))
    # Font size to 14
    matplotlib.rc('font', size = 14)
    # Do not display top and right frame lines
    matplotlib.rc('axes.spines', top = False, right = False)
    # Remove grid lines
    matplotlib.rc('axes', grid = False)
    # Set backgound color to white
    matplotlib.rc('axes', facecolor = 'white')
    # Define function to create the scatterplot
    
def scatterplot( df, x_data, y_data, x_label, y_label, title ):

    # Create the plot object
    _, ax = plt.subplots()

    # Plot the data, set the size (s), color and transparency (alpha)
    # of the points
    ax.scatter(x_data, y_data, s = 30, color = '#539caf', alpha = 0.75)

    # Label the axes and provide a title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

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
    df_tx_all = df_tx_all[[col_tx_year,
                           col_tx_month,
                           col_tx_day,
                           col_tx_customer_id,
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

## Starting commercial conditions analysis
# Define parameters for One CUSTOMER ID 
list_products = ["AMARYL"]
list_cust_ids = [1000081]
list_years = [2017]
list_channels = None
# Call function to compute discount analysis for given parameters
df = get_discount_analysis( df_tx_all, list_products, list_cust_ids, list_years, list_channels )
# Print 5 first discount rates of computed data.frame
print("5 first discount rates of computed data.frame:")
#print(df['discount_rate'].head(5))
#print(df.loc[:,'discount_rate'].head(5))
#print(df[['discount_rate']].head(5))
print(df.iloc[:,4].head(5))


# Define parameters
list_products = ["AMARYL"]
list_cust_ids = None
list_years = [2017]
list_channels = None
# Call function to compute discount analysis for given parameters
df = get_discount_analysis( df_tx_all, list_products, list_cust_ids, list_years, list_channels )
# Print 5 first discount rates of computed data.frame
print("5 first discount rates of computed data.frame:")
print(df.iloc[:,4].head(5))

# Define parameters
list_products = ["AMARYL","APROVEL"]
list_cust_ids = [1000081, 1000084, 1000108, 1000143, 1000153, 1000163]
list_years = None
list_channels = ["HOSPITAL"]
# Call function to compute discount analysis for given parameters
df = get_discount_analysis( df_tx_all, list_products, list_cust_ids, list_years, list_channels )
# Print 5 first discount rates of computed data.frame
print("5 first discount rates of computed data.frame:")
print(df.iloc[:,4].head(5))

# Define parameters and iterate
list_products = ["AMARYL","ESPERSON","APROVEL","NOVALGIN","LASIX","LANTUS","FLAGYL","PLAVIX","TELFAST"  "PROFENID"]
list_years = [2015,2016,2017]

for product in list_products :
    for year in list_years :
        product_to_list = [product]
        year_to_list = [year]
        # Call function to compute discount analysis for given parameters
        df = get_discount_analysis( df_tx_all, product_to_list, None, year_to_list, None )
        # Print 5 first discount rates of computed data.frame
        print("5 first discount rates of computed data.frame for product: '" +
              str(product) + "', and year: '" + str(year) + "':")
        print(df.iloc[:,4].head(5))
        
        
# Define parameters for scatter plots 
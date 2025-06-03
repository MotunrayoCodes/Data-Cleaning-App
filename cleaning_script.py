import pandas as pd
def direct_billing_dc(df):
    #df is your dataframe
    df= df.drop(columns=['PSP Rev.(75%)','LAWMA (18%)','PM Rev. (2%)','Treat. Rev. (1%)'])

    for col in df.columns:
        if col =='Outstanding':
            # Handle "(+)" cases → set to 0
            df['Outstanding'] = df['Outstanding'].astype(str)
            df.loc[df['Outstanding'].str.contains(r'\(\+\)', regex=True), 'Outstanding'] = '0'

    
    columns_to_clean = ['Monthly Due','Amount Paid','Outstanding','SA Rev. (4%)']
# Remove currency symbols and commas
    for col in df.columns:
       if col in columns_to_clean:
            df[col] = df[col].astype(str)
            df[col] = df[col].str.replace(r'[^\d\.-]', '', regex=True).astype(float)
    
    # Convert to date column
    col_to_convert_dtype = ['Last Payment']
    for col in df.columns:
     if col in col_to_convert_dtype:
         df[col] =df[col].str.replace(r'(st|nd|rd|th)', '', regex=True, case=False)
         df[col] = pd.to_datetime(df[col], errors='coerce')
         df[col] = df[col].dt.date
    
    df = df.iloc[:, :-2]
    
    return df

def pay_lawma_dc(df):
    # drop uneccessary columns
    df= df.drop(columns=['Id','Receipt code','Account number','Sterling account number','Customer ref','Invoice code','Reconciled'
                         ,'Transaction reference','Comment','Transaction type'])

    
    # Convert to datetime
    df['Payment date'] = pd.to_datetime(df['Payment date'], errors='coerce')  
    df['Payment date'] = df['Payment date'].dt.date

    df['SA_Revenue'] = df['Amount'] * 0.16

    return df

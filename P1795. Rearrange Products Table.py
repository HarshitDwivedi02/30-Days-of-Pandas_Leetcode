import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    
    # First, we  create a Boolean Series that check if the values in the "store1", "store2" and "store3" column of the DataFrame products have a valid value.
        pExists1 = products['store1'].notnull()
        pExists2 = products['store2'].notnull()
        pExists3 = products['store3'].notnull()

    # The, we concatenate rows from the products DataFrame based on certain conditions and structure. Also, we reset the index of the resulting DataFrame so that it starts from 0, 1, 2, etc., instead of retaining the index values from the original DataFrames.
        concat_products = pd.concat([
            products.loc[pExists1, ['product_id']].assign(store = 'store1', price = products['store1']),
            products.loc[pExists2, ['product_id']].assign(store = 'store2', price = products['store2']),
            products.loc[pExists3, ['product_id']].assign(store = 'store3', price = products['store3'])
        ], ignore_index = True)
 
        return concat_products
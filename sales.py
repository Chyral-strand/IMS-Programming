import random

def daily_sales(available_items, inventory_records, current_day):
    if current_day % 7 != 0:
        sales = random.randint(0,200)
        available_items -= sales
        new_row = [current_day, sales, 0, available_items]
        inventory_records.append(new_row)
    '''
***********COMPLETE THIS FUNCTION***********
This function is responsible for updating the sales for a given day.
---------------
Function Input:
---------------
available_items: (integer) Available Tshirts from the previous day.
inventory_records: (List) A list of inventory records until the previous day. Each row contains (day, sales, restocked items, available items)
current_day: (integer) Day number which you want to add as the current day. 

----------------
Function Output:
----------------
available_items:(integer) This function returns this integer which updates the available items at the current day.

The function will also update the inventory_records (For restocking) for a  given current day. 

    '''
    
    return available_items
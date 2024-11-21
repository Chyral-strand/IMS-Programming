def restock_inventory(available_items, inventory_records, current_day):
    if current_day == 0 or current_day % 7 == 0:
        inventory_records.append(current_day)
        inventory_records.append(0)
        stockage = 2000 - available_items
        available_items += stockage
        inventory_records.append(stockage)
        inventory_records.append(available_items)
    '''
***********COMPLETE THIS FUNCTION***********
This function is responsible for updating the stock/restock for a given day.
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


The function will also update the inventory_records (For restocking) for a  given current day. It will also return "available_items".
    '''

    return available_items

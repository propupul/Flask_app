from da_location import location

def main():
    
    while True:
        
        try:
            sku_id =input("Sku id: ")
            where = location(sku_id)
            print(where)
        except:

            print("That's not the correct SKU #")
            
        
if __name__ == '__main__':
    main()

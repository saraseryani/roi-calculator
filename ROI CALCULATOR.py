    ###########################################################
    #  Computer Project #5
    #   Opens and reads file 
    #   Prompts for functions to calculate the revenue, cost 
    #   for production, and roi.
    #   The main function calls back both functions to calculate
    #   the best performing ad and the best roi.
    #   prints stats for each ad
    #     
    #
    #  
    ###########################################################
"""
the open_file function prompts a file name opens the file and if it's 
not found on the computer it would say "Unable to open file" and 
prompt for another file name
"""
def open_file():
    '''prompt for file name, open file, return file pointer'''
    while True:
        try:
            fp = input("Input a file name: ")
            fp = open(fp, 'r')
            break
        except FileNotFoundError:       
            print("Unable to open file. Please try again.")
    return(fp)
"""
the reveune function calculates the revenue by multiplying the sale price and 
the amount of items sold
"""
def revenue(num_sales, sale_price):
    '''revenue = sales * price'''
    sales = int(num_sales)
    price = float(sale_price)
    rev = (sales * price)
    return(rev)
"""
calculates the cost of goods sold by calling the number of ads, ad price, number
of sales, and production costs. multiplies the integer value of the number of ads
by the float value of the ad price to come up with the total cost of ads. converts
the total ads to float and multiplies by the cost for production's float value to
get the total production cost. adds bot the production cost and amount of ads to get
the toal cost of goods. returns that value.
"""
def cost_of_goods_sold(num_ads, ad_price, num_sales, production_cost):
    '''costs of goods sold = advertising total + production total'''
    ad_total = (int(num_ads) * float(ad_price))
    prod_cost = (float(production_cost) * int(num_sales))
    cost_of_goods = (float(ad_total) + float(prod_cost))
    return (cost_of_goods)
"""
the revenue function is called back as well as the cost of goods function to give the
total return on investment (roi). plugged the values into the given formula. 
returns the roi
"""
def calculate_ROI(num_ads, ad_price, num_sales, sale_price, production_cost):
    '''ROI = (Revenue - Cost of goods sold)/Cost of goods sold'''
    r=revenue(num_sales, sale_price)
    c=cost_of_goods_sold(num_ads, ad_price, num_sales, production_cost)
    roi = (((r) - (c))/(c))
    return (roi)
"""
this function basically initials what the max values are and calls back all of the
previous functions to get the best performing ads due to it's roi and performance.
returns nothing, prints the given values.
"""
def main():
    fp = open_file()
    print()
    print("RobCo AdStats M4000")
    print("-------------------")
    print()
    initial_product = ""
    maxroi = 0
    maxroiname = ""
    maxsales = 0
    maxsalesad = ""

    for line in fp:
        line = line.strip()
        product_name = line[:27].strip()
        ad_name = line[27:54].strip()
        num_ads = int(line[54:62].strip())
        ad_price = float(line[62:70].strip())
        num_sales = int(line[70:78].strip())
        sale_price = float(line[78:86].strip())
        production_cost = float(line[86:94].strip())
    
        if initial_product != product_name:
            if initial_product == "":
                initial_product = product_name

            else:
                print(initial_product) 
                print("  {:27s}{:>11s}".format("Best-Performing Ad","sales"))
                print("  {:27s}{:>11d}".format(maxsalesad, maxsales))
                print()
                print("  {:27s}{:>11s}".format("Best ROI","percent"))
                print("  {:27s}{:>11.2f}%".format(maxroiname, maxroi))
                print()
                maxroi = 0
                maxroiname = ""
                maxsales = 0
                maxsalesad = ""
                initial_product = product_name
                
        roi = calculate_ROI(num_ads, ad_price, num_sales, sale_price, production_cost)
        if roi > maxroi:
            maxroi = roi
            maxroiname = ad_name
                   
        if num_sales > maxsales:
            maxsales = num_sales
            maxsalesad = ad_name
            
    print(initial_product) 
    print("  {:27s}{:>11s}".format("Best-Performing Ad","sales"))
    print("  {:27s}{:>11d}".format(maxsalesad, maxsales))
    print()
    print("  {:27s}{:>11s}".format("Best ROI","percent"))
    print("  {:27s}{:>11.2f}%".format(maxroiname, maxroi))
    print() 

if __name__ == "__main__":
    main()
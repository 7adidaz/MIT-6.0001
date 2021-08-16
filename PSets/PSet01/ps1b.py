annual_salary = int(input("Enter your annual salary:"))
# portion_saved is the amount saved every month for the house
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = int(input("Enter the cost of your dream home:"))
semi_raise = float(input("Enter the semi annual raise, as a decimal:"))

current_saving = 0
#month counter!
counter=0
portion_down_payment = .25*total_cost #down payment
month_salary = annual_salary/12

while current_saving<portion_down_payment:
    if counter%6==0 and counter !=0:
        month_salary+=month_salary*semi_raise
    #the received funds to put into the saving
    current_saving+=(current_saving*0.04)/12 
    #salary saving each month for the down payment
    current_saving+=portion_saved*month_salary
    counter+=1  
    
print("Number of months:", counter)

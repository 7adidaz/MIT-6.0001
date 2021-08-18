


annual_salary = int(input("Enter your starting annual salary:")) 
total_cost = 1000000
semi_annual_raise = 0.07


current_saving = 0
counter=0



portion_down_payment = .25*total_cost #250000
month_salary = annual_salary/12.0




start = 0
end = 10000.0

while abs(current_saving - portion_down_payment)>100:
    
    portion_saved = (start+end)/2.0
    current_saving = 0
    counter+=1
    
    for i in range(36):  
        
        if i%6==0 and i!=0:
            month_salary += month_salary*semi_annual_raise
        
        current_saving += ((current_saving*0.04)/12.0) + month_salary*(portion_saved/10000.0) 
        
        
    if current_saving>portion_down_payment:
        end = portion_saved
    else:
        start = portion_saved
    if end- start ==1:
        print("It is not possible to pay the down payment in three years.")
        
        
    
        
print("Best savings rate:", portion_saved/10000)
print("Steps in bisection search:", counter)
        
        
        
        
        
        
import random
x=""
while x!="x":
    customers=[]
    time_spent=[]
    total_time=720
    count=0
    a=1
    number_of_customers=0
    sum_time_spent=0
    average_time_spent=0
    real=[]
    while total_time>0:
        customer_came_or_not=random.randint(0,1)
        if customer_came_or_not==0:
            if a==1:
                customers.append(0)
                if total_time>1:
                    time=random.randint(1,total_time)
                else:
                    time=1
                time_spent.append(time)
                a=0
            else:
                time=random.randint(0,total_time)
                while time>total_time or time==0:
                    if total_time>1:
                        time=random.randint(1,total_time)
                    else:
                        time=1
                time_spent[len(time_spent)-1]+=time
                a=0
            total_time=total_time-time
        else:
            customers.append(1)
            time=random.randint(1,60)
            while time>total_time:
                if total_time>1:
                    time=random.randint(1,total_time)
                else:
                    time=1
            time_spent.append(time)
            a=1
            total_time=total_time-time
    for i in range(len(customers)):
        if customers[i]==1:
            sum_time_spent+=time_spent[i]
            number_of_customers+=1
            real.append(time_spent[i])
    if number_of_customers>0:
        average_time_spent=sum_time_spent/number_of_customers
        print("Costumers spent",average_time_spent,"minutes average in barber shop in 12 hours.")
        print("Customers list:",customers,"\nCostumers' spent time list:",real,"\nAll times spent in barber shop included list:",time_spent)
    else:
        print("No customers came.\n")
    x=str(input("\nPress enter to start another work day.Press x and enter to exit\n"))
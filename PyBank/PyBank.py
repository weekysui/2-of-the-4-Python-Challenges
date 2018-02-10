import os, csv
from statistics import mean

numbers = ["1","2"]
for number in numbers:
    csvpath = os.path.join("raw_data","budget_data_{}.csv".format(number))
    total_months = []
    total_revenue = []
    total=[]
    difference = []
    average_revenue_change = []
    totalDifference = []
    greatest_increase_in_revenue = []
    greatest_decrease_in_revenue = []
    months = []
    with open(csvpath,mode = 'r', newline="")as csvfile:
        next(csvfile,None) #skip header
        csvreader = csv.reader(csvfile, delimiter=',')
        totalRevenue = 0
        avg_change =0
        for row in csvreader:
            total_months.append(row[0])
            totalRevenue += int(row[1])
            total.append(row[1])
        totalMonths = len(total_months) #Total amount of months
        months.append(totalMonths)


        for i in range(int(len(total))-1):
            D = int(total[i+1])-int(total[i]) #D is the difference of each 2 numbers in the total list
            totalDifference.append(D)#add D values to totalDifference list
        average_revenue_change.append(round(mean(totalDifference)) ) #calculated mean for the revenue change
        greatest_increase_in_revenue.append(max(totalDifference)) #greatest increase revenue
        greatest_increase_date = total_months[int(totalDifference.index(max(totalDifference)))+1]
        greatest_decrease_in_revenue.append(min(totalDifference)) #greatest decrease revenue
        greatest_decrease_date = total_months[int(totalDifference.index(min(totalDifference)))+1]
        total_revenue.append(totalRevenue)

        print("Budget_data_{} Financial Analysis".format(number))
        print("--------------------------------")
        print("Total Months: {}".format(totalMonths))
        print("Total Revenue: ${}".format(total_revenue[0]))
        print("Average Revenue Change: ${}".format(average_revenue_change[0]))
        print("Greatest Increase in Revenue: {} (${})".format(greatest_increase_date,
                                                              greatest_increase_in_revenue[0]))
        print("Greatest Decrease in Revenue: {} (${})".format(greatest_decrease_date,
                                                              greatest_decrease_in_revenue[0]))

        with open("budget_data_{}.txt".format(number), "w") as text_file:
            print("Budget_data_{} Financial Analysis".format(number),file=text_file)
            print("--------------------------------",file=text_file)
            print("Total Months: {}".format(totalMonths),file=text_file)
            print("Total Revenue: ${}".format(total_revenue[0]),file=text_file)
            print("Average Revenue Change: ${}".format(average_revenue_change[0]),file=text_file)
            print("Greatest Increase in Revenue: {} (${})".format(greatest_increase_date,
                                                                  greatest_increase_in_revenue[0]),file=text_file)
            print("Greatest Decrease in Revenue: {} (${})".format(greatest_decrease_date,
                                                                  greatest_decrease_in_revenue[0]),file=text_file)














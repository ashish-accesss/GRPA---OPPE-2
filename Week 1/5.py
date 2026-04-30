age =int(input()) #int: Read a number as integer from standard input
dob =input() #str: Read a string of format dd/mm/yyyy from standard input
#day,month,year =...#int,int,int: Get the correct parts from dob as int
"""dd/mm/yyyy"""
fifth_birthday=dob[:6]+str(int(dob[-4:])+5) #str:fifth birthday formatted as day/month/year

last_birthday=dob[:6]+str(int(dob[-4:])+age) #str:last birthday formatted as day/month/year

total_month=(int(str(dob[3:5]))-1)+9
new_month=(total_month%12)+2
extra_year=total_month//12
new_year=int(dob[-4:])+extra_year

tenth_month=dob[:3]+str(new_month)+"/"+str(new_year)  #str:dob same day after 10 months formatted as day/month/year

#print tenth_month,fifth_birthday and last_birthday in same line separated by comma and a space
print(tenth_month+', '+fifth_birthday+', '+last_birthday)

weight=float(input()) #float:Read a number as float from stdin(standard input)

weight_readable=str(int(weight))+" kg "+str(int(round((weight-int(weight))*1000)))+" grams" #str:reformat weight of format 55 kg 250 grams

#print weight_readable
print(weight_readable)
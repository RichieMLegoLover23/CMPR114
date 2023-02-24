month_of_year = int(input('enter a month as a number between 1 and 12: '))
if month_of_year == 1 :
  print('first quarter')
elif month_of_year == 2 :
  print('first quarter')
elif month_of_year == 3:
  print('first quarter')
elif month_of_year == 4 :  
  print('second quarter')
elif month_of_year == 5 :  
  print('second quarter')
elif month_of_year == 6 :  
  print('second quarter')
elif month_of_year == 7 :
  print('third quarter')
elif month_of_year == 8 :
  print('third quarter')
elif month_of_year == 9 :
  print('third quarter')
elif month_of_year == 10 :
  print ('fourth quarter')
elif month_of_year == 11 :
  print ('fourth quarter')
elif month_of_year == 12 :
  print ('fourth quarter')
else:
  print('error')












number_attending_cookout = int(input('Enter how many people will be attending the cookout:'))
hotdogs_each = int(input('Enter how many hot dogs each each person will be given: '))
packages_hotdogs_needed = number_attending_cookout/10
packages_hotdog_buns_needed = number_attending_cookout/8

print( packages_hotdogs_needed , ' packages of hot dog are needed for a cookout of' , number_attending_cookout , 'and' , packages_hotdog_buns_needed , ' packages of buns are needed.' )














number_of_packages_purchased = int(input("Enter the number of packages ordered: "))
if number_of_packages_purchased >=10 and number_of_packages_purchased <=19:
  print('$',99-number_of_packages_purchased * 0.10 , 'is your total after a ten percent discount')
elif number_of_packages_purchased >=20 and number_of_packages_purchased <=49:
  print('$',99-number_of_packages_purchased * 0.20,' is your total after a twenty percent discount.' )
elif number_of_packages_purchased >=50 and number_of_packages_purchased <=99:
  print('$',99-number_of_packages_purchased*0.3,'is your total after a thirty percent discount.')
elif number_of_packages_purchased >=100:
  print('$',99-number_of_packages_purchased*0.4, 'is your total after a fourty percent discount')
else:
  print('error')

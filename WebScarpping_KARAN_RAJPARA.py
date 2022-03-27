import GoogleMap as m
import Wikipedia2 as f
import Wikipedia3 as c

while 1 :
    print('\n\n\n\n\n')
    print('='*50)
    print('\n1.Google Map location\n2.2019–20 Premier League INFO\n3.COVID-19 pandemic in India live case count\n4.Exit\n')
    print('='*50)
    choice = input('Enter your choice :')
    if choice == '1' :
        m.google()
    elif choice == '2' :
        f.Premier_League()
    elif choice == '3' :
        c.covid_record()
    elif choice == '4' :
        break
    else :
        print('\nInvalid choice\n')

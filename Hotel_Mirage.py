print('Welcome to Hotel Mirage :')

hotel_mirage= {
    '101': '',
    '102': '',
    '103': '',
    '104': {'Name': 'John', 'Phone': '646-255-8014'},
    '105': '',
}
main_menu = '''

1. Checking In
2. Rooms Available
3. Edit Rooms
4. Checking out
5. Quit

'''
while True:
    try:
        menu_choice = int(input(main_menu))
            # print(hotel_mirage)
        if menu_choice == 5:
            print ('Thank you for using the Hotel Management App!')
            break
        if menu_choice == 1:
            customer = {}
            name = input('what is the name of the guest? ')
            customer['Name']= name
            customer ['Phone'] = input('Enter customer phone? ')
            room_number = input('What is the room number? ')
            hotel_mirage[room_number] = customer
            print(hotel_mirage)
            for room_number in hotel_mirage.keys():
            #     # The room_number variable will be a 
            #     # string, like '101' or '103'
                if hotel_mirage[room_number] == '':
                    print(f'{room_number} is vacant')
                else:
                    print(f'{room_number} is occupied by {hotel_mirage[room_number]["Name"]}')

        if menu_choice == 2:
            for room_number in hotel_mirage.keys():
            #     # The room_number variable will be a 
            #     # string, like '101' or '103'
                if hotel_mirage[room_number] == '':
                    print(f'{room_number} is vacant')
                else:
                    print(f'{room_number} is occupied by {hotel_mirage[room_number]["Name"]}')

        if menu_choice == 3:
            customer = {}
            name = input('what is the name of the guest? ')
            customer['Name']= name
            customer ['Phone'] = input('Enter customer phone? ')
            room_number = input('What is the room number? ')
            hotel_mirage[room_number] = customer
            print(hotel_mirage)

        if menu_choice == 4:
            room_number = input('Which room are you checking out? ')
            print (hotel_mirage[room_number])
            customer = '' #laziness 
            hotel_mirage[room_number]=customer
            print(hotel_mirage)

    except ValueError:
                print('Please select from Menu')
    except :
                print('cannot pop from empty list')
        
#insert these information into the empty room 
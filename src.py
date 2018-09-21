# Initial User Prompts
acct_num = int(input('Enter the account number: '))
srv_code = str(input('Enter the service code '
                     '(r or R for Regular, or p or P for Premium): '))
min_num = int(input('Enter the number of minutes used: '))

# Regular Service
if srv_code == 'r' or srv_code == 'R':
    if min_num < 51:
        print('Your fee is $15.00.')
    else:
        print('Your fee is ${:.2f}'.format(0.50 * min_num))

# Premium Service
else:

    # # Daytime Call
    # call = str(input('Did you make a daytime call? (y/n) '))
    # if call == 'y' or call == 'Y':
    #     if min_num < 51:
    #         print('Your fee is $0.00.')
    #     else:
    #         print('Your fee is ${}'.format(min_num * 0.2))
    #
    # # Nighttime Call
    # else:
    #     if min_num < 101:
    #         print('Your fee is $0.00.')
    #     else:
    #         print('Your fee is ${}'.format(min_num * 0.1))

    # Day and Night Calls
    # Prompts ask the user how many minutes for day and night calls.
    # Prompts ask user how many minutes for day and night calls.
    day_call = int(input('How many minutes did you call during the day? '))
    night_call = int(input('How many minutes did you call during the night? '))

    # Daytime Call Price
    if day_call < 51:
        day_price = 0
    else:
        day_price = day_call * 0.2

    # Nighttime Call Price
    if night_call < 101:
        night_price = 0
    else:
        night_price = night_call * 0.1

    # Final Premium Price
    print('Your fee is ${:.2f}'.format(day_price + night_price))
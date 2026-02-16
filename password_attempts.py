def password_attempts():
    correct_password = 'Dublin@2026'
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        password = input("Enter Password: ")

        if password == correct_password:
            print('Access granted')
            break
        else:
            print('Incorrect password, try again')
                        
            attempts += 1

    # Password attempts should be max 3 attempts
    if attempts == max_attempts:
        print('Access denied')

password_attempts()
        
    

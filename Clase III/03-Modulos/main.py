import users

if __name__ == '__main__':
    print('Si ejecutamos main.py como script principal se ejecutará este print')

    # get users from db
    user_list = users.get_users()

    # create user
    user_created = users.create_user('Ronald', 'Abu Saleh')

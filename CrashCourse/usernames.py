current_users = ['Peroush', 'tCroush', 'ctRoush', 'admin', 'trrOush', 'tmrouSh']
current_users_lc = [current_user.lower() for current_user in current_users]
new_users = ['CaRoush', 'tcRoush', 'HaGardenhire', 'MjGardenhire', 'peRoush']

for new_user in new_users:
    if new_user.lower() in current_users_lc:
        print(f"The user name '{new_user}' is already in use. Please choose another name.")
    else:
        print(f"The user name '{new_user}' is available. Please go to the next step.")

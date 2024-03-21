import itchat

itchat.login()
itchat.dump_login_status()

friends = itchat.get_friends(update=True)
for friend in friends:
    print(friend['NickName'])

import user
import admin

gunha = user.User('chico','gunha')
print(gunha.describe_user())
print(gunha.greet_user())
gunha.increment_login_attempts()
gunha.increment_login_attempts()
print(gunha.login_attempts)
gunha.reset_login_attempts()
print(gunha.login_attempts)

silva = admin.Admin('silva', 'sauro')
print(silva.greet_user())
silva = admin.Privileges(['can add post', 'can ban user'])
print(silva.show_privileges())

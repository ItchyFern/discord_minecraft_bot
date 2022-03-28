import generic_utils
import mojang_utils
import crafatar_utils

username = input("Enter username: ")
#username = "ItchyFern"
uuid = mojang_utils.get_uuid(username)
url = crafatar_utils.get_skins(uuid)
print(url)
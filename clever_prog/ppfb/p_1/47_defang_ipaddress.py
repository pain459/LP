def defang_ipaddress(address):
    new_address = ""
    split_address = address.split(".")
    seperator = "[.]"
    new_address = seperator.join(split_address)
    return new_address


print(defang_ipaddress("1.1.2.3"))
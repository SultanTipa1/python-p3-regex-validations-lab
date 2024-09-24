import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name_regex = re.compile(r"^[A-Z][a-zA-Z'-]*(?: [A-Z][a-zA-Z'-]*)*$")

phone_regex = re.compile(r"^(?:\(\d{3}\)\s|\d{3}[-]?)?\d{3}[-]?\d{4}$")

email_regex = re.compile(r"^[a-zA-Z][\w.-]*@[a-zA-Z]+\.[a-zA-Z]{2,}$")

# name = r""
# name_regex = re.compile(name)


# phone_number = r""
# phone_regex = re.compile(phone_number)


# email_address = r""
# email_regex = re.compile(email_address)





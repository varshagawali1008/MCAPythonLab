import re
text = "My string is 45 "
match = re.search(r"\d+", text)
if match:
    print(match.group())
else:
    print("No digits found")


result = re.match(r"hello", "HelloWorld", re.IGNORECASE)
print(result.group())

text =" yesssssss"
result=re.findall(r"\d",text)
print(result)


email="pj2222@gmail.com"
pattern = r"^\w+@\w+\.\w+$"
if re.match(pattern,email):
    print ("valid email")
else:
    print("Invalid email")


text=" The Quick Brown Fox jumps over the lazy dog. The Fox Is Quick"
print("---Using re.search()---")
match_obj=re.search(r"Fox",text)
if match_obj:
    print(f"matchFound :'{match_obj.group()}at popsition{match_obj.span()}")
else:
    print("No Match Found")


pattern = r"^(?=.*\d).{6,}$"
passwords = ["abc123", "hello", "password 7 words"]

for p in passwords:
    if re.match(pattern, p):
        print(p, "valid password")
    else:
        print(p, "Invalid password")



pattern = r"^(https?://)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(/.*)?$"
urls = ["http://google.com/search","www.test.org", "invalid_url"]

for u in urls:
    if re.match(pattern, u):
        print(u, "Valid URL")
    else:
        print(u, "Invalid URL")

        
import time
import re
messages = ["value is 10", "Next value is 25", "Fins value :42"]
pattern = r"\d+"
for message in messages:
    time.sleep(1)  
    num = re.search(pattern, message)
    print("number found:", num.group())

import re
chats = [
    "contact me at john@gmail.com",
    "my alternate email is sara_21@yahoo.com",
    "Send to admin@abc.org"
]
pattern = r"[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+"
for line in chats:
    match = re.search(pattern, line)
    if match:
        print("Email found:", match.group())
    else:
        print("No email found")


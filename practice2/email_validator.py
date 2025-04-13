e1 = "user@example.com"
e2 = "user@example"
def email_valid(email):
    if ("@" and ".") in email:
        print("유효함")
    else:
        print("유효하지 않음")

print("이메일 주소: "+e1)
email_valid(e1)
print("이메일 주소: "+e2)
email_valid(e2)
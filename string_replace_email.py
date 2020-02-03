def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

email = ['abc@hotmail.com', 'hooo@gmail.com', 'hello@gmail.com']

print(replace_domain(email, 'gmail.com', 'zaluka.com'))
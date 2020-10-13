class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def validate(self, email):
        (name, mail, domain) = self.__get_components(email)

        return self.__validate_name(name) \
               and self.__validate_mail(mail) \
               and self.__validate_domain(domain)

    # V1
    # def __get_components(self, email):
    #     return re.split(r'[@.]', email)

    def __get_components(self, email):
        (name, mail_domain) = email.split('@')
        special_domain = self.__get_special_domain(mail_domain)

        if special_domain:
            domain = special_domain
            # email = mail_domain[:len(mail_domain) - len(special_domain)]
            mail = mail_domain.split(f'.{special_domain}')[0]
        else:
            (mail, domain) = mail_domain.split('.')

        return name, mail, domain

    def __get_special_domain(self, domain):
        special_domains = {'co.uk'}
        for special_domain in special_domains:
            if domain.endswith(special_domain):
                return special_domain
        return None

    def __validate_name(self, name):
        return name and self.min_length <= len(name)

    def __validate_mail(self, mail):
        return mail in self.mails

    def __validate_domain(self, domain):
        return domain in self.domains


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.co.uk"))

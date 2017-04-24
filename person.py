class Person:

    '''
    Person is define klient
    def __init__(self, name)
        name  <str> --- name klient
        set_phone(self, phone) <int> --- phone number
        set_description(self, msg) <str>
    '''

    def __init__(self, name='', phone=''):
        self.name = name
        self.phone = phone

    def set_phone(self, phone):
        self.phone = phone

    def set_description(description):
        self.description = description


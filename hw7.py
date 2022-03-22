class Data:
    def __init__(self, full_name, email, file_name, color):
        self.__full_name = full_name
        self.__email = email
        self.__file_name = file_name
        self.__color = color

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        self.__full_name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, value):
        self.__file_name = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value


files = ['NamesSurnames.txt', 'Emails.txt', 'fileNames.txt', 'color.txt']


def MainFunc():
    with open('MOCK_DATA (1).txt','r') as readOn:
        for i in readOn:
            stringM = i.split()
            stringM[0] += ' ' + stringM.pop(1)
            if len(stringM) > 4:
                stringM[0] += ' ' + stringM.pop(1)
            info = Data(*stringM)
            with open(files[0], 'a') as fullN:
                fullN.write(info.full_name)
                fullN.write('\r')
            with open(files[1], 'a') as emailN:
                emailN.write(info.email)
                emailN.write('\r')
            with open(files[2], 'a') as fileN:
                fileN.write(info.file_name)
                fileN.write('\r')
            with open(files[3], 'a') as colorN:
                colorN.write(info.color)
                colorN.write('\r')
MainFunc()

def RemList():
    file = open('NamesSurnames.txt', 'w')
    file.close()

    file = open('Emails.txt', 'w')
    file.close()

    file = open('fileNames.txt', 'w')
    file.close()

    file = open('color.txt', 'w')
    file.close()
MainFunc()


# def find_color():
#     color_finder = re.findall(r'#.*', filenpars)
#     for i in color_finder:
#         return f'{i}'
#
#
# def find_email():
#     email_finder = re.findall(r'(\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,6})', filenpars)
#     for i in email_finder:
#         return f'{i}'
#
#
# def find_file():
#     file_finder = re.findall(r'\t\w[A-Za-z ]+?\.[a-zA-Z].*\t', filenpars)
#     for i in file_finder:
#         return f'{i}'
#
#
# def find_name():
#     name_finder = re.findall(r"^[-A-Z]+\t[A-Z'-]+", filenpars)
#     for i in name_finder:
#         return f'{i}'
# print(f'{find_name()}, {find_email()}, {find_file()}, {find_color()}')
#
#
#
# while True
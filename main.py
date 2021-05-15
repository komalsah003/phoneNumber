import phonenumbers
from test import number


from phonenumbers import geocoder
ch_num = phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_num,"en"))

from phonenumbers import carrier
service_num= phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_num,"en"))
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
   # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
   # print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

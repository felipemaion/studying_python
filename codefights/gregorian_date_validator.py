# Regex for Gregorian date validation
# Your task is to write regular expression that validates gregorian date in format "DD.MM.YYYY"

# Correct date examples:

# "23.12.2008"
# "01.08.1994"
# Incorrect examples:

# "12.23.2008"
# "01-Aug-1994"
# " 01.08.1994"

date_validator = r'(^(((0[1-9]|1[0-9]|2[0-8])[\.](0[1-9]|1[012]))|((29|30|31)[\.](0[13578]|1[02]))|((29|30)[\.](0[4,6,9]|11)))[\.](19|[2-9][0-9])\d\d$)|(^29[\.]02[\.](([0-9][0-9]|[2-9][0-9])(04|08|12|16|20|24|28|32|36|40|44|48|52|56|60|64|68|72|76|80|84|88|92|96)|(04|08|12|16|20|24|28|32|36|40|44|48|52|56|60|64|68|72|76|80|84|88|92|96)(00))$)'

# import re
# test.assert_equals(bool(re.match(date_validator,'01.01.2009')), 
#                     True, 'Basic correct date: 01.01.2009')
# test.assert_equals(bool(re.match(date_validator,'01-Jan-2009')), 
#                     False, 'Incorrect mask: 01-Jan-2009')                    
# test.assert_equals(bool(re.match(date_validator,'05.15.2009')), 
#                     False, 'Incorrect month: 15.15.2009')                                        

# import re

# test.it('Validator length')
# test.assert_equals(len(date_validator) <= 400, 
#                     True, 'Maximum length is 400 characters')

# def re_test(message, input_str, expected_res):
#     test.it('%s: "%s", expecting: %s' % (message, input_str, expected_res))
#     test.assert_equals(bool(re.match(date_validator, input_str)), expected_res)    

# re_test('Basic correct date','01.01.2009',True)
# re_test('Incorrect mask','01-Jan-2009',False)
# re_test('Lead spaces',' 01.01.2009',False)
# re_test('Trailing spaces','01.01.2009 ',False)
# re_test('Incorrect separator','01-01-2009',False)
# re_test('Incorrect separator','29-02.2009',False)
# re_test('Empty string','',False)
# re_test('Incorrect month','15.15.2009',False)
# re_test('Correct month','05.12.2009',True)
# re_test('Incorrect month','15.00.2009',False)
# re_test('Correct day of August','31.08.2009',True)
# re_test('Incorrect day','94.01.2009',False)
# re_test('Incorrect day of April','31.04.2009',False)
# re_test('Incorrect year, more than 4 digits','31.04.10000',False)
# re_test('Correct year','31.03.9999',True)
# re_test('Incorrect year, less than 4 digits','31.03.100',False)
# re_test('Day without leading zero','9.02.2008',False)
# re_test('Month without leading zero','19.2.2008',False)
# re_test('Correct leap day','29.02.2008',True)
# re_test('Incorrect leap day','29.02.2009',False)
# re_test('Zero year','31.03.0000',False)
                    
# x_validator = r'^(((0[1-9]|1\d|2[0-8])\.(0[1-9]|1[012])|(29|30)\.(0[13-9]|1[012])|31\.(0[13578]|1[02]))\.(?!0000)\d{4}|29\.02\.(?!0000)(\d\d((?!00)[02468][048]|[13579][26])|([02468][048]|[13579][26])00))$'

# test.describe("All possible days (10000 tests)")
# for i in range(10000):
#     zi = str(i).zfill(4)
#     test_date=zi[:2]+'.'+zi[2:]+'.2009'
#     if bool(re.match(date_validator,test_date)) != bool(re.match(x_validator,test_date)):
#         Test.assert_equals(bool(re.match(date_validator,test_date)), 
#                         bool(re.match(x_validator,test_date)), 'Date "'+test_date+'" validated incorrectly')
# Test.assert_equals(True,True) 

# test.describe("All leap years (9999 tests)")
# for i in range(1,10000):
#     zi = str(i).zfill(4)
#     test_date='29.02.'+zi
#     if bool(re.match(date_validator,test_date)) != bool(re.match(x_validator,test_date)):
#         Test.assert_equals(bool(re.match(date_validator,test_date)), 
#                         bool(re.match(x_validator,test_date)), 'Leap date "'+test_date+'" validated incorrectly')
# Test.assert_equals(True,True) 

# NEXT KATA: https://www.codewars.com/kata/following-the-paths-of-numbers-through-prime-factorization/train/python
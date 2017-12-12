#!/usr/bin/env python3


"""currency.py: To exchange a kind of currency into another.
__author__ = "WangTong"
__pkuid__  = "1700011771"
__email__  = "1700011771@pku.edu.cn"
"""


def currency_response(currency_from, currency_to, amount_from):
    """Returns: a JSON string that is a response to a currency query.

    A currency query converts amount_from money in currency currency_from
    to the currency currency_to. The response should be a string of the form

    '{"from":"<old-amt>","to":"<new-amt>","success":true, "error":""}'

    where the values old-amount and new-amount contain the value and name
    for the original and new currencies. If the query is invalid, both
    old-amount and new-amount will be empty, while "success" will be followed
    by the value false.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""

    from urllib.request import urlopen
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from\
={}&to={}&amt={}'.format(currency_from, currency_to, amount_from))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return jstr


def get_num_from_str(jstr):
    """Returns: the intended number parted from the string 'jstr'

    This function will separate the intended number from the JSON string

    Parameter jstr: the JSON string returned from the web which contains
    the intended data
    """
    list_by_jstr = jstr.split('"')
    error_type = list_by_jstr[-2]
    if error_type != '':
        return error_type
    else:
        num_plus_currency_to = list_by_jstr[7]
        numstring = num_plus_currency_to[:num_plus_currency_to.find(' ')]
        num = float(numstring)
        return num


def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in
    currency currency_from to the currency currency_to. The value
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""

    jstr = currency_response(currency_from, currency_to, amount_from)
    num = get_num_from_str(jstr)
    return num


def test_currency_response():
    """To test whether the function currency_response() can get right return"""

    assert(currency_response('USD', 'EUR', '2.5') == '{ "from" : "2.5 United Sta\
tes Dollars", "to" : "2.0952375 Euros", "success" : true, "error" : "" }')

    assert(currency_response('USD', 'CNY', '1') == '{ "from" : "1 United States \
Dollar", "to" : "6.52615 Chinese Yuan", "success" : true, "error" : "" }')

    assert(currency_response('USD', 'IMP', '1') == '{ "from" : "1 United States \
Dollar", "to" : "0.766307 Manx pounds", "success" : true, "error" : "" }')


def test_get_num_from_str():
    """To test whether the function get_num_from_str() can get right return"""

    assert(get_num_from_str('{ "from" :"2.5 UnitedStates Dollars", "to" : "2.0\
952375 Euros", "success": true, "error" : "" }') == 2.0952375)

    assert(get_num_from_str('{ "from" : "1 United States Dollar", "to" : "6.526\
15 Chinese Yuan", "success" : true, "error" : "" }') == 6.52615)

    assert(get_num_from_str('{ "from" : "1 United States Dollar", "to" : "0.766\
307 Manx pounds","success" : true, "error" : "" }') == 0.766307)


def test_exchange():
    """To test whether the function exchange() can get right return"""

    assert(exchange('USD', 'EUR', '2.5') == 2.0952375)

    assert(exchange('USD', 'CNY', '1') == 6.52615)

    assert(exchange('USD', 'IMP', '1') == 0.766307)


def testAll():
    """Test all cases"""

    test_currency_response()
    test_get_num_from_str()
    test_exchange()


def main():
    """main module
    """
    testAll()
    currency_from, currency_to, amount_from = input().split()
    num = exchange(currency_from, currency_to, amount_from)
    print(num)


if __name__ == '__main__':
    main()

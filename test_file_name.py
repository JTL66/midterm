from file_name import currency_converter

def test_file_name():
	assert currency_converter(1, "USD", "USD") == "1 in USD = 1 in USD"
	assert currency_converter(1, "INR", "INR") == "1 in INR = 1 in INR"
	assert currency_converter(1, "ert", "USD") == "one or more currency codes not found"
	assert currency_converter(1, "USD", "ert") == "TO currency code not found"
	assert currency_converter(1, "TTT", "USD") == "one or more currency codes not found"
	assert currency_converter(1, "USD", "TTT") == "TO currency code not found"

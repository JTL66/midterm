from mp import zipcode_lookup

def test_mptest():
	assert zipcode_lookup("08754") == "08754: Toms River, NJ"
	assert zipcode_lookup("06484") == "06484: Shelton, CT"
	assert zipcode_lookup("00000") == "place not found"
	assert zipcode_lookup("ertyu") == "Invalid input ertyu"







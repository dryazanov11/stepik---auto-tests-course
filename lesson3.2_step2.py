def test_substring(full_string, substring):
    x = substring
    y = full_string
    assert x in y, (f"expected '{x}' to be substring of '{y}'")
	
full_string = 'fulltext'
substring = 'some_value'
print (test_substring(full_string, substring))
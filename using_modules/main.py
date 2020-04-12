from helpers.strings import extract_lower, extract_upper

from helpers import variables

#name = "This is Very fUnny MessAge"

print(f"Only upper case letters {extract_upper(variables.name)}")
print(f"Only lower case letters {extract_lower(variables.name)}")
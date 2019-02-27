# 4. Create a show_version variable that contains the following

#  show_version = "*0        CISCO881-SEC-K9       FTX0000038X    " 

# Remove all leading and trailing whitespace from the string.

# Split the string and extract the model and serial_number from it.

# Check if 'Cisco' is contained in the model string (ignore capitalization).

# Check if '881' is in the model string.

# Print out both the serial number and the model.



show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "

show_version = show_version[2:].strip()

model, serial = show_version.split()

'cisco' in model.lower()
'881' in serial.lower()

print(model, serial)

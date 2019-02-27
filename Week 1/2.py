# 2. Prompt a user to enter in an IP address from standard input. Read the IP address in and break it up into its octets. Print out the octets 
# in decimal, binary, and hex.

# Your program output should look like the following:

# ​ $ python exercise2.py 
# Please enter an IP address: 80.98.100.240

#     Octet1         Octet2         Octet3         Octet4     
# ------------------------------------------------------------
#       80             98             100            240      
#    0b1010000      0b1100010      0b1100100     0b11110000   
#      0x50           0x62           0x64           0xf0      
# ------------------------------------------------------------

# Four columns, fifteen characters wide, a header column, data centered in the column.


ip = input("Please enter an IP address: ")

octets = ip.split(".")

print("{:^15}{:^15}{:^15}{:^15}".format(*[f'Octet{x}' for x in range(1,5)]))
print("-"*60)
print("{:^15}{:^15}{:^15}{:^15}".format(*octets))
print("{:^15}{:^15}{:^15}{:^15}".format(*[bin(int(x)) for x in octets]))
print("{:^15}{:^15}{:^15}{:^15}".format(*[hex(int(x)) for x in octets]))
print("-"*60)

# 5. You have the following three variables from the arp table of a router:

# mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
# mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
# mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

# Process these ARP entries and print out a table of "IP ADDR" to "MAC ADDRESS" mappings. The output should look like following:

#              IP ADDR          MAC ADDRESS
# -------------------- --------------------
#         10.220.88.29       5254.abbe.5b7b
#         10.220.88.30       5254.ab71.e119
#         10.220.88.32       5254.abc7.26aa

# Two columns, 20 characters wide, data right aligned, a header column.


mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

macs = [mac1.split()[3], mac2.split()[3], mac3.split()[3]]
ips  = [mac1.split()[1], mac2.split()[1], mac3.split()[1]]

print(f"{'IP ADDR':>20} {'MAC ADDRESS':>20}")
print("-"*20,"-"*20)
for ip, mac in zip(ips, macs):
    print(f"{ip:>20} {mac:>20}")


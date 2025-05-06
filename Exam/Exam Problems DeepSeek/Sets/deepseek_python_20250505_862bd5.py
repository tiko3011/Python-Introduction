system1_passwords = {"qwerty", "123456", "letmein", "abcl23", "hunter2"}
system2_passwords = {"admin", "123456", "hunter2", "password", "trustno1"}

common = system1_passwords & system2_passwords
only_system1 = system1_passwords - system2_passwords
total_unique = len(system1_passwords | system2_passwords)

print("Common passwords:", common)
print("Only in system1:", only_system1)
print("Total unique passwords:", total_unique)
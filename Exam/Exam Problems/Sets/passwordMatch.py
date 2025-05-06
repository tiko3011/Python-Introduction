system1_passwords = {"qwerty", "123456", "letmein", "abc123", "hunter2"}
system2_passwords = {"admin", "123456", "hunter2", "passw0rd", "trustno1"}

inBoth = system1_passwords & system2_passwords
inFirst = system1_passwords - system2_passwords
count = len(system1_passwords | system2_passwords)

print(inBoth)
print(inFirst)
print(count)
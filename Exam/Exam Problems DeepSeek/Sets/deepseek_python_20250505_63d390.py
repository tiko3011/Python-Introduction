system1 = {"qwerty", "123456", "letmein", "abcl23", "hunter2"}
system2 = {"admin", "123456", "hunter2", "password", "trustno1"}

# Common passwords
common = set()
for pwd in system1:
    if pwd in system2:
        common.add(pwd)

# Only in system1
only_system1 = system1 - system2

# Total unique
total_unique = len(system1.union(system2))

print("Common:", common)
print("Only in system1:", only_system1)
print("Total unique:", total_unique)
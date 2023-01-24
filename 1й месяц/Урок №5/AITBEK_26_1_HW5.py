
data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
designations = []
codes = []

for i in data:
    if i.isdigit():
        codes.append(i)
    else:
        designations.append(i)

operators = {}
s = 0

while len(operators) != len(designations):
    operators[designations[s]] = {codes[s]}
    s += 1

del operators["Katel"]
del operators["Fonex"]

operators["O!"].add("0700")
operators["Megacom"].add("0555")
operators["Beeline"].add("0778")

for key, value in operators.items():
    print(f"{key} >> {value}")


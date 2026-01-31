t = "h",
print(type(t))

s = set()
s.add(2)
s.add("h")
print(s)

my_list = [1, 1, 2, 67, 67, 8, 9] #list to set
my_set = set(my_list)
print(my_set)

dict = {}
dict[1] = "int"
dict[3.14] = "float"
dict[True] = "bool"
dict["str"] = "str"

print()
print(dict)
for key, value in dict.items():
    print(f"{repr(key)}({type(key).__name__}): {value}")

print()
n_dict = {
    "lvl1": {
        "lvl2": {
            "lvl3": {
                "deep" : "deepVAL"
            }
        }
    }
}

result = n_dict["lvl1"]["lvl2"]["lvl3"]["deep"]
print(result)
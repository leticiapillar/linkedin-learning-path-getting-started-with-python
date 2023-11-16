# 01 Creating a dictionary in Python

print("01 Creating a dictionary in Python")

capital_of_states = {
    "RS": "Poro Alegre",
    "SC": "Florianopolis",
    "PR": "Curitiba"
}

print("Capital of RS is", capital_of_states["RS"])

print("Print all keys in a dictionary, all states")
for key in capital_of_states.keys():
    print(key)

print("Print all values in a dictionary, all capitals")
for value in capital_of_states.values():
    print(value)

print("Print kays and values in a dictionary, states and capitals")
for k, v in capital_of_states.items():
    print(f"The capital of state {k} is {v}")

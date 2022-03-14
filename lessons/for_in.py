"""An example of for...in syntax."""

names: list[str] = ["Bob", "Jeff", "Leg", "Got"]

# Example of iterating through names using a while loop
i: int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1
    
# For...in loop version fo while loop
for name in names:
    print(name)
    


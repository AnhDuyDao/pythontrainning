"""
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a)

# Multiline strings

# String are arrays
a = "Hello, World!"
print(a[1])  # Output: e
print(a[2:5])  # Output: llo

# Looping through a string
for x in "banana":
   print(x)

# String length
b = "The world is beautiful"
print(len(b))  # Output: 24

# Check string
txt = "The best things in life are free!"
print("best" in txt)

if "free" in txt:
   print("Yes, 'free' is present.")

# Check if NOT in string
print("expensive" not in txt)

if "expensive" not in txt:
   print("No, 'expensive' is NOT present.")
"""

# String slicing
a = "Hello, World!"
print(a[1:5])  # Output: ello

print(a[:4]) # Not include index 4, Output: Hell

print(a[2:]) # From index 2 to the end, Output: llo, World!

print(a[-5:-2]) # From index -5 to -2, Output: orl

# Modifying strings
print(a.upper())  # Output: HELLO, WORLD!

print(a.lower())  # Output: hello, world!

b = " Hello, World! "
print(b.strip())  # Remove whitespace at the beginning and end, Output: Hello, World!

# Replace string
print(a.replace("H", "J"))  # Replace H with J, Output: Jello, World!
print(a.replace("World", "Python"))  # Replace World with Python, Output: Hello, Python!

# Split string
print(a.split(","))

# String concententation
c = "Love"
d = "You"
print(c , d) # or print(c + d)

age = 26
# txt = "My name is Anh, I am " + str(age)
txt = f"My name is Anh, I am {age}"  
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {8*3} dollars"
print(txt)

# Escape character
txt = "We are the so-called \"Vikings\" from the north."
print(txt)


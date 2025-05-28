# Text type: str
# Numeric types: int, float, complex
# Sequence types: list, tuple, range
# Mapping type: dict
# Set types: set, frozenset
# Boolean type: bool
# Binary types: bytes, bytearray, memoryview
# None type: NoneType

x = 5
print(type(x))  # Output: <class 'int'>

# Specify the data type
x = str("Hello World")
x = int(20)
x = float(20.5)
x = complex(1j)	
x = list(("apple", "banana", "cherry"))	
x = tuple(("apple", "banana", "cherry"))
x = range(6)
x = dict(name="John", age=36)
x = set(("apple", "banana", "cherry"))
x = frozenset(("apple", "banana", "cherry"))
x = bool(5)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))

# Check the type of the variable
x = {"name" : "John", "age" : 36}
print(type(x))
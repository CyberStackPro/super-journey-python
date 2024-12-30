# Dictionaries
# we use dictionaries to store key/value pairs.

customer ={
    "name":'John smith',
    "age":30,
    "is_verified":True
}

# We can use string or numbers to define keys. They should be unique. We can use any types ofthe values
customer['name'] # returns “John Smith”
# customer["type"] # throws an error
customer.get("type", 'solver') # returns “silver”
customer['name'] = "new name"
print(customer)

# hp-clone
numbers=[2,2,4,6,3,4,6,1,30,60,30,60,44,80,44,76]
duplicate =[]
for number in numbers:
if number not in duplicate:
duplicate.append(number)
print(duplicate)

numbers=[10,20.36,45,60,75,66]
max =numbers[0]
for number in numbers:
if number > max:
max = number
print(max)

list=[1,3,5,6,7,8,9,10]
list[0]=66
print(list)

set1={1,2,3 ,int("4")}
set12={3, str(4)}
print(set1.union(set12))

tuple=(1,2,3,4,5,6)
tuple.count(0)
print(tuple)

coordinates=(1,2,3,4)
x, y, z, o=coordinates
print(o)
q=10
c=9
b=q+c
print(b)
for i in range(10):
print(i)

numbers=[2,4,2,6,8,9,0,8,8,89,]
duplicate=[]
for i in numbers:
if i not in duplicate:
duplicate .append(i)
print(duplicate)
phone=input ("phone ")
digit_mapping={
"1":"one",
"2":"two",
"3":"three",
"6":"six"
}
output=""
for ch in phone :
output+= digit_mapping.get(ch ,"!") +" "
print(output)

message=input(">")
words=message.split(" ")
emojis = {
";;":"😋",
":(":"😢",
":)":"😀"
}
unique=""
for word in words:
unique += emojis. get(word,word) +" "
print(unique)
def my_function():
print("hi everybody")
print("how Life is a long lesson in humility. - ..")
print ("hi there")
my_function()
print("hey there")
capital_city = {"Nepal": "Kathmandu", "England": "London"}
print("Initial Dictionary: ",capital_city)

capital_city["Japan"] = "Tokyo"

print("Updated Dictionary: ",capital_city)
time={
"india":"4.00 pm",
"america":"9;00pm",
"japan":"6.00pm"
}
print(time)
def square(numbers):
return numbers*numbers
value=square(6)
print(value)

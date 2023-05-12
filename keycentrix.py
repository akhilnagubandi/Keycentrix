#!/usr/bin/env python
# coding: utf-8




#Question 1
""" This can be achieved by splitting the given IP address whenever we encounter a period (".") and 
creating an array using the split() function. Then, we can use the join() function to concatenate 
the elements of the array with the required "[.]" separator.
The process involves splitting the IP address string into individual parts by using the split() function 
and providing "." as the separator. This creates an array of parts. Next, we can use the join() function 
to combine the elements of the array back into a string, using the "[.]" separator. This effectively 
replaces each period with "[.]" in the resulting string.By performing these steps, we obtain the 
defanged version of the IP address where each period is replaced with "[.]".
"""

def IpFormatter(address):
    ip = address.split('.')

    if (len(ip) != 4):   # checking if the ip has four components
        return "Invalid IP"

    for i in ip:
        if i[0] != '0':    #checking leading zeros so that we dont covert them to integers
            if eval(i) > 255:  #checking if the invidual component is more than 255
                return "Invalid IP"
        
        
    ip = '[.]'.join(ip)
    return ip

#Basic Ip
print(IpFormatter('1.1.1.1'))
#zero Ip
print(IpFormatter('0.0.0.0'))
#Max Ip
print(IpFormatter('1.1.1.1'))
#Leading Zeros
print(IpFormatter('001.09.02.01'))
#Random IP
print(IpFormatter('255.128.45.12'))
#Inavlid IP
print(IpFormatter(''))
print(IpFormatter('1.1.1'))
print(IpFormatter('257.45.23.12'))





#Question 2
""" First, create a string that contains all the vowels. Then, iterate through each letter 
in the given sentence and check if it is a vowel by verifying its presence in the vowel string.
To implement this approach, begin by creating a string that includes all the vowels: 'aeiouAEIOU'.
Next, loop through each letter in the sentence and check if it is a vowel by using the membership 
operator (in) to verify if the letter is present in the vowel string.
"""
def vowelRemover(sentence):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    new = ""
    for i in sentence:
        if i not in vowels:
            new = new + i
    if new == "":
        return "returning empty string"
    else:
        return new

#Basic Test case
print(vowelRemover("abfiweygfi"))
#Empty
print(vowelRemover(""))
#NoVowels
print(vowelRemover("sdfrt234"))
#AllVowels
print(vowelRemover("aeuio"))
#Upper and Lower
print(vowelRemover("AeUitgfywDF"))
#specielcharacters and numbers
print(vowelRemover("@$%$&^!*(*5637895"))
#long sentence
print(vowelRemover("This is a long sentence with Vowels and Consonants "))





#Question 3
"""Given the strings jewels and stones, the approach involves iterating through each stone 
in a loop and checking if the stone is present in the jewels string. If the stone is found in jewels, the count is increased by 1.
To implement this approach, start by initializing a variable count to 0.
Then, iterate through each stone in a loop. For each stone, check if it is present in the 
jewels string using the membership operator (in). If the stone is found in jewels, increment the count by 1.
"""
def countJewels(jewels,stones):
    count = 0;
    for s in stones:
        if s in jewels:
            count = count +1
    return count;

#Basic
print(countJewels("aA","aAAbBBB"))
#output:- 3
#No Jewels
print(countJewels("z","ZZ"))
#output:- 0
#No stones
print(countJewels("z",""))
#output:- 0
#All Jewels
print(countJewels("zasd","zasd"))
#output:- 4
#Empty
print(countJewels("",""))





#Question 4
""" Find the unique elements in given list, count the occurrences of each unique element into list. 
If each unique element has a unique no of occurrences, the new list created will have unique count. 
"""

def uniqueOccurences(array):
    unique = []
    uniquecount = []
    occur =[]
    for i in array:       #finding unique elements
        if i not in unique:
            unique.append(i)
    for j in unique:       #counting occurence of each unique element
        uniquecount.append(array.count(j))
    for count in uniquecount:   #finding the duplicate number counts
        if count not in occur:
            occur.append(count)
    if len(uniquecount) == len(occur):
        return True
    else:
        return False
#Basic
print(uniqueOccurences([1,2,2,1,1,3]))
#Output:- True
#Long Array
print(uniqueOccurences([1,2,2,4,4,4,4,3,3,3]))
#Output:- True
#small Array
print(uniqueOccurences([1,2]))
#Output:- False
#Negative integers Array
print(uniqueOccurences([-3,0,1,-3,1,1,1,-3,10,0]))
#Output:- True
#Empty
print(uniqueOccurences([]))
#Output:- True





#Question 5
""" When trying to buy the maximum number of toys without duplicates, the approach is to start by 
purchasing the cheapest toy first. To achieve this, sort the price array in ascending order. 
Then, iterate through the sorted array and buy toys as long as the available amount allows. 
Each time a toy is purchased, subtract its price from the available amount and increase the count. 
Once the amount is not enough to buy the next product, return the count. To implement this 
approach, begin by sorting the price array in ascending order using a sorting algorithm such 
as Python's built-in sorted() function. Next, initialize a variable count to 0 and iterate through 
the sorted price array. For each toy price, check if the available amount is greater than or equal to the price. 
If it is, subtract the price from the available amount, increment the count by 1, and continue to the next toy. 
If the available amount is not enough to buy the toy, return the count as the maximum number of toys that can be purchased"""

def maximizeToys(amount,prices):
    count = 0
    prices.sort() #sorting the prices
    for p in prices:
        if amount - p <=0:     #subtracting the price of a toy
            return count       #if price exceeds the amount avaialble, return the count
        else:
            count = count + 1   #if not add the toy to the list
    return count


#Basic
print(maximizeToys(50,[1,12, 5, 111, 200, 1000, 10]))
#output:- 4
#No Toys
print(maximizeToys(1000,[]))
#output:- 0
#Insuffienct Money
print(maximizeToys(10,[20,30,12,15]))
#output:- 0
#Zero Money
print(maximizeToys(0,[20,30,12,15]))
#output:- 0
#Lump of Money and large no of toys
print(maximizeToys(5000000,[1,12, 5, 111, 200, 345, 7000, 1000, 10]))
#output:- 9
#Exact amount
print(maximizeToys(50,[10,20,15,5]))
#output:- 4
#Identical prices
print(maximizeToys(40,[10,10,10,10]))
#output:- 4





#Question 6
""" In the process of encoding a URL to a tiny URL, we utilize a randomly generated character 
sequence as an alternative for the longer URL. This is achieved by maintaining a dictionary 
where we store the mappings between the long URLs and their corresponding tiny URLs. Whenever we 
receive a new long URL, we first check if it is present in the dictionary. If it is, we return 
the associated tiny URL. If it is not found, we encode the long URL, store it in the dictionary,
and return the newly created tiny URL. To implement this process, start by initializing an 
empty dictionary url_dict to store the mappings between long URLs and tiny URLs. Next, when encoding a long URL, 
check if it is already present in the url_dict. If it is, retrieve the associated tiny URL and return it. 
If the long URL is not found in the dictionary, generate a random character sequence to serve as the tiny URL. 
Store the long URL and its corresponding tiny URL in the url_dict and return the newly created tiny URL
 """

import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
url_dict ={"https://www.google.com":"http://tinyurl.com/67Frte","https://keycentrix.com/problems/design-tinyurl":"http://tinyurl.com/4e9iAk"}

def encode(long_url):
    if long_url in url_dict:
        return url_dict[long_url]
    
    tiny_url = generate_tiny(long_url)
    for tiny_url in url_dict.values():   #making sure we dont get a duplicate random url.
        tiny_url = generate_tiny(long_url)
    url_dict[long_url] = tiny_url
    return tiny_url

def decode(tiny_url):
#     print(tiny_url.replace("http://tinyurl.com/",""))
    for long_url, encoded_url in url_dict.items():
        if encoded_url == tiny_url:
            return long_url
    return "Long URL does not exist"
    
def generate_tiny(long_url):
    tiny_url = ""
    for i in range(0,6):
        tiny_url = tiny_url + random.choice(chars)
    return "http://tinyurl.com/"+tiny_url

#Basic encode
print(encode("https://www.google.com"))
#output:- http://tinyurl.com/67Frte
print(encode("https://keycentrix.com/problems/design-tinyurl"))
#output:- http://tinyurl.com/4e9iAk
#Basic decode
print(decode("http://tinyurl.com/4e9iAk"))
#output:- https://keycentrix.com/problems/design-tinyurl
#New Encode
print(encode("https://www.tinyurl.com"))
#output:- http://tinyurl.com/u6FrnQ
#checking storing capability "should return the same tiny_url
print(encode("https://www.tinyurl.com"))
#output:- http://tinyurl.com/u6FrnQ
#giving invalid tiny url
print(decode("https://www.tinyurl.com/tynr6R"))
#output:- Long URL does not exist
#encoding very large url
print(encode("https://www.vfagiyihogihifnagif.com/bgsugvicuhsougvu/vgsgibskg/vusu"))
#output:- http://tinyurl.com/kTCnk2


# SQL QUESTIONS

# 1.	Write a query to find all employees of the HR department.
# SELECT * FROM Employees where DepartmentId in (SELECT Id FROM Departments where name = 'HR')
# 2.	Write a query to find all employees that work for James Smith.
# SELECT * FROM Employees where ManagerId in (SELECT Id FROM Employees where FName = 'James' AND LName = 'Smith')
# 3.	Write a query to find all customers who own a Ford F-150.
# SELECT * FROM Customers where ID in (SELECT CustomerId FROM Cars where Model = 'Ford F-150')
# 4.	Write a query to find the number of Mustangs being repaired.
# SELECT * FROM Customers where ID in (SELECT CustomerId FROM Cars where Model = 'Ford Mustang' and Status = 'Working')
# 5.	Write a query to find customers who own more than one car.
# SELECT * FROM Customers where Id in (SELECT CustomerId from Cars GROUP BY CustomerId HAVING COUNT(*)>1);
# 6.	Write a query to find the total salary for the HR department.
# SELECT sum(Salary) FROM Employees where DepartmentId in (SELECT Id FROM Departments where name = 'HR')
# 7.	Write a query to find the total revenue generated by the sales department.
# SELECT SUM(TotalCost) FROM Cars where EmployeeId in (SELECT Id FROM Employees where DepartmentId in (SELECT Id FROM Departments where Name = 'Sales'))



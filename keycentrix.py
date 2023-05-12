#!/usr/bin/env python
# coding: utf-8

# In[37]:


#Question 1

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


# In[39]:


#Question 2
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


# In[45]:


#Question 3
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


# In[64]:


#Question 4
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


# In[85]:


#Question 5
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


# In[125]:


#Question 6
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


# In[ ]:





# In[ ]:





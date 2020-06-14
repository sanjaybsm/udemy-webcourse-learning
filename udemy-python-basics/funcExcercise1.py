#####################
## -- PROBLEM 1 -- ##
#####################

# Given a list of integers, return True if the sequence of numsbers 1, 2, 3
# appears in the list somewhere.

# For example:

# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True

def arrayCheck(nums):
    length = len(nums)
    i = 0
    success = False
    while(i < length):
        if(nums[i] == 1):
            if(i+1 < length and nums[i+1] > nums[i]):
                if(nums[i+1] == 2 and (i+2 < length and nums[i+2] > nums[i+1])):
                    if(nums[i+2] == 3):
                        success = True
                        break
                    else:
                        i=i+1
                        continue
                else:
                    i=i+1
                    continue
            else:
                i=i+1
                continue
        else:
            i=i+1
            continue
    return success



print(arrayCheck([1, 1, 2, 3, 1]))
print(arrayCheck([1, 1, 2, 4, 1]))
print(arrayCheck([1, 1, 2, 1, 2, 3]))

def stringBits(str):
    l = []
    l += str
    i = 0
    newStr = []
    print(l)
    while(i < len(l)):
        newStr += l[i]
        i = i+2
    return newStr

print(stringBits('He'))

def end_other(a, b):
  return b in a

print(end_other('acdfsf','abc'))


# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'

def doubleChar(str):
      l = []
      l += str
      i = 0
      newStr = []
      while(i < len(l)):
          newStr += l[i]
          newStr += l[i]
          i=i+1
      return convert(newStr)

def convert(s):
    new = ""
    for x in s:
        new += x
    return new

print(doubleChar('The'))


def no_teen_sum(a, b, c):
    a = fix_teen(a)
    b = fix_teen(b)
    c = fix_teen(c)
    return a+b+c

def fix_teen(n):
    if(n in [13, 14, 17, 18, 19]):
        return 0
    else:
        return n

print(no_teen_sum(1, 2, 3))
print(no_teen_sum(2, 13, 1))
print(no_teen_sum(2, 1, 14))


def count_evens(nums):
    result = filter(even_bool, nums)
    return len(list(result))

def even_bool(num):
    return num % 2 == 0

print(count_evens([2, 1, 2, 3, 4]))

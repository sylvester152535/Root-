# for item in range(1,101):
#   if item%3==0 and item%5==0:
#     print "FizzBuzz"
#   elif item%3==0:
#     print "Fizz"
#   elif item%5==0:
#     print "Buzz"
#   else:
#     print item


# def large_count_sum(arr):
#     sum = 0; sums = []
#     for item in arr:
#         if item > 0:
#             sum = sum + item
#         else:
#             sums.append(sum)
#             sum = 0
#     sums.sort()
#     return sums[-1]

# a = [-4,-6,-3]

# def large_count_sum(arr):
#     currSum = 0; maxSum = 0
#     for item in arr:
#         if item > 0:
#             currSum =currSum+item
#         else:
#             if currSum > maxSum:
#                 maxSum = currSum
#                 currSum=0
#     return maxSum
#
# print large_count_sum(a)

# def sentenceReversed(str):
#     str.lstrip()
#     str.rstrip()
#     str.split()
#     str1 = []
#     for k in reversed(range(0, len(str))):
#         str1.append(str[k])
#     return " ".join(str1)

# def rev_word(s):
#     return " ".join(s.split()[::-1])
#
#
# #str5 = 'Hello Shawty my name is Vestein'
#
# rev_word("Hello Shawty my name is Vestein")


# def unique(s):
#
#     l = len(s)
#
#     if l == 0:
#         return False
#
#     if l==1:
#         return True
#
#
#     i = 1; counter = 1; dict = {}
#
#     while i < l:
#
#         if dict[s[i]] > 1:
#             return False
#         else:
#             dict[s[i]] = dict[s[i]]+ counter
#             counter = 1
#         i+=1
#     return True


king = "Hello"

reverse = king[::-1]
"".join(reversed(king))

def rere(string):

    arr = []
    re = ""
    for i in range(len(string)):
        arr.append(string[len(string)-1-i])
        re = "".join(arr)
    return re

print rere("Sylvester")

# https://adventofcode.com/2023/day/1


import time

# def day_1():
#     total = 0

#     for line in open("day_1/data.txt", "r"):
#         l = 0
#         r = len(line)-1
#         while l <= r:
#             if line[l].isnumeric() == False:
#                 l += 1
#             if line[r].isnumeric() == False:
#                 r -= 1
#             if line[l].isnumeric() and line[r].isnumeric():
#                 total += int(line[l] + line[r])
#                 break
#     return total

# print(day_1())


# def day_1():
#     total = 0

#     numdict = {
#         "one" : "1",
#         "two" : "2",
#         "three": "3",
#         "four" : "4",
#         "five" : "5",
#         "six" : "6",
#         "seven" : "7",
#         "eight" : "8",
#         "nine" : "9"
#     }

#     for line in open("day_1/data.txt", "r"):
#         first = None
        
#         for index in range(len(line)):
#             if line[index].isnumeric():
#                 first = line[index]
#                 break
#             else:
#                 for valkey in numdict:
#                     if line[index:len(valkey)+index] == valkey:
#                         first = numdict[valkey]
#                         break
#                 if first != None:
#                     break
#         second = None
#         for index in range(len(line)-1, -1, -1):
#             if line[index].isnumeric():
#                 second = line[index]
#                 break
#             else:
#                 for valkey in numdict:
#                     if line[index:len(valkey)+index] == valkey:
#                         second = numdict[valkey]
#                         break
#                 if second != None:
#                     break
#         total += int(first+ second)

#     end = time.time()

#     print(end-start)

#     return total

# start = time.time()

# print(day_1())


def day_1():
    total = 0

    numdict = {
        "one" : "1",
        "two" : "2",
        "three": "3",
        "four" : "4",
        "five" : "5",
        "six" : "6",
        "seven" : "7",
        "eight" : "8",
        "nine" : "9"
    }

    for line in open("day_1/data.txt", "r"):

        first = None    
        second = None
        l = 0
        r = len(line)-1
        
        while l <= r:
            if first is None:
                if line[l].isnumeric():
                    first = line[l]
                else:
                    for valkey in numdict:
                        if line[l:len(valkey)+l] == valkey:
                            first = numdict[valkey]
                    if first is None:
                        l+=1
            if second is None:
                if line[r].isnumeric():
                    second = line[r]
                else:
                    for valkey in numdict:
                        if line[r:len(valkey)+r] == valkey:
                            second = numdict[valkey]
                    if second is None:
                        r -= 1
            if first is not None and second is not None:
                break
                        
        total += int(first+ second)
    
    end = time.time()

    print(end-start)

    return total

start = time.time()

print(day_1())
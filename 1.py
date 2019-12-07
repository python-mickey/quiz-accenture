def FindLongestOrderSequence(input):
    # Variable declaration
    temp, output = input[0], []
    # Number from zeto to the end
    for i in range(len(input) - 1):
        # check value less than
        if input[i] < input[i+1]:
            temp += input[i+1]
        # check value more than
        else:
            if temp:
                output.append(temp)
                temp = input[i+1]


    # The most length
    maxLen = max([len(el) for el in output])
    # output my list
    output = [val for val in output if len(val) == maxLen]
    return output

print(FindLongestOrderSequence('12401021')) # ['124']
print(FindLongestOrderSequence('7124501115793')) # ['1245', '1579']
print(FindLongestOrderSequence('15235137835692838387')) # ['1378', '3569']
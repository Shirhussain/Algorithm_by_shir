
from loguru import logger
import snoop
import heartrate
# heartrate.trace(browser=True)

input1 = "nameless"
input2 = "salesmam"


# @logger.catch
# @snoop
def is_anagram(input1, input2):
    if len(input1) != len(input2):
        return False
    dict1 = {}
    dict2 = {}
    for chr in input1:
        dict1[chr] = 1 + dict1.get(chr, 0)
    for chr in input2:
        dict2[chr] = 1 + dict2.get(chr, 0)

    for ky in dict1:
        if ky not in dict2 or dict1[ky] != dict2[ky]:
            return False
    return True


print(is_anagram(input1, input2))

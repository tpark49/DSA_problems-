from sklearn.utils import resample


def addBinary(a, b):

    i = 0 
    result = ""
    carry = 0 
    while i < len(a) or i < len(b):
        if i<len(a): a_bit = a[::-1][i] 
        else: a_bit=0

        if i<len(b): b_bit = b[::-1][i]
        else: b_bit = 0 

        digit = (carry + int(a_bit) + int(b_bit))%2 
        result+=str(digit)

        carry = (carry + int(a_bit) + int(b_bit))//2

        i+=1

    if carry == 1: 
        result+="1"
    return result[::-1]


if __name__ == "__main__":
    a = "11"
    b = "1"
    print(addBinary(a, b))
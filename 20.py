
from zmq import EVENT_HANDSHAKE_FAILED_AUTH


def isValid(s):

    closing = {
        '}':'{',
        ']':'[',
        ')':'('
    }
    
    stack = []
    for i in s: 
        if i in closing: 
            if len(stack)==0: 
                return False 
            else:
                if closing[i] != stack.pop(): 
                    return False 
        else: 
            stack.append(i)
    
    if len(stack)!=0: 
        return False
    else: 
        return True 

        

    

if __name__ == "__main__":

    print(isValid("(]"))
        

            


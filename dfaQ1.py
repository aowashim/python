# Roll number : CSB18062

#            Transition table
#           -------------------
#
#           States |  0   |  1
#           -------|------|-----
#     --> *   q0   |  q1  |  q0
#           -------|------|-----
#         *   q1   |  q2  |  q0
#           -------|----- |-----
#             q2   |  q2  |  q2

# program starts

def checkString(str1):

    finalStates, curState, flag = ['q0', 'q1'], 'q0', 1

    strLen = len(str1)
    for i in range(strLen):
        if str1[i] == '0' or str1[i] == '1':
            if curState == 'q0':
                if str1[i] == '0':
                    curState = 'q1'
                else:
                    curState = 'q0'

            elif curState == 'q1':
                if str1[i] == '0':
                    curState = 'q2'
                else:
                    curState = 'q0'
        else:
            flag = 0
            break
        #not checking for 'q2' since it is dead state

    if flag:
        if curState in finalStates:
            print('Accepted')
        else:
            print('Not accepted')
    else:
        print("This machine checks string consisting of only '0' and/or '1'.")

#driver program
inStr = input('Enter your string from {0,1} without spaces : ')
checkString(inStr)
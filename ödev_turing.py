
def calculate_n_squared(n,tape):
    head = 1
    state = 'q0'

    while state != 'q9':
        if state == 'q0':
            if tape[head] == '0':
                tape[head] = '1'
                head += 1
                state = 'q1'
        if state == 'q1':
            while tape[head]=='0' and state=='q1':
                head += 1
            if tape[head] == '$':
                head -= 1
                state = 'q2'
        if state == 'q2':
            while tape[head] == 'ç'and state=='q2':
                head += 1
                state = 'q6'
            if tape[head] == '0':
                tape[head] = 'X'
                head += 1
                state = 'q3'
            if tape[head] == '1':
                tape[head] = 'Y'
                head += 1
                state = 'q3'
            while tape[head]=='X'and state=='q2':
                    head -= 1
                    state = 'q2'
            while tape[head]=='Y'and state=='q2':
                    head -= 1
                    state = 'q2'

        if state == 'q3':
            while tape[head]=='X'and state=='q3':
                head += 1
                state = 'q3'
            while tape[head]=='Y' and state=='q3':
                head += 1
                state = 'q3'
            if tape[head] == '$':
                head += 1
                state = 'q4'
        if state == 'q4':
            while tape[head]=='1' and state=='q4':
                head += 1
                state = 'q4'
            if tape[head] == 'B':
                tape.append('B')
                tape[head] = '1'
                head -= 1
                state = 'q5'

        if state == 'q5':
            while tape[head]=='1' and state=='q5':
                head -= 1
                state = 'q5'
            if tape[head] == '$':
                head -= 1
                state = 'q2'

        if state == 'q6':
            if tape[head] == 'X':
                tape[head] = '0'
                head += 1
                state = 'q6'
            if tape[head] == 'Y':
                tape[head] = '1'
                head += 1
                state = 'q6'
            if tape[head] == '$':
                head -= 1
                state = 'q7'
        if state == 'q7':
            if tape[head]=='0' and state =='q7':
                head -= 1
                state = 'q7'
            if tape[head]=='1'and state =='q7':
                head += 1
                state = 'q8'
        
        if state == 'q8':
            if tape[head] == '0'and state =='q8':
                    tape[head] = '1'
                    head += 1
                    state = 'q1'
            
            if tape[head] == '$' and state=='q8':
                    head += 1
                    state = 'q9'

    return tape




def tape(n):
    i=0
    tape = ['ç']
    while i < n:
        tape.append('0')
        i+=1
    tape.append('$')
    tape.append('B')
    print(tape)
    return tape
def say_after_element(arr, element, count_element):
    count = 0
    found = False

    for i in arr:
        if found:
            if i == count_element:
                count += 1
        if i == element:
            found = True

    return count
n=5
tape=tape(n)
result = calculate_n_squared(n,tape)
sonuc = say_after_element(result, '$', '1')
print(result)
print("Sonuç:", sonuc)

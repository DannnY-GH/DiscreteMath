import sys
system = [
    #P1
    [{'-a','+b','-c','+d'}, [1]],
    [{'-a','+c','-d'}, [2]],
    [{'+a','-b','-c','-d'}, [3]],
    [{'+a','+b','-c', '+d'}, [4]],
    [{'+a','+b','+c'}, [5]],
    [{'+a','+b','+d'}, [6]],
    [{'+b','-c','+d'}, [7]],
    [{'+b','+c','-d'}, [8]],
    #P2
    [{'-a','+b','-c','+d'},[9]],
    [{'-a','-b','-c'},[10]],
    [{'+a','-c','-d'},[11]],
    [{'+a','+b','-c','-d'},[12]],
    [{'+a','+b','+c','+d'},[13]],
    [{'-b','-d'},[14]],
    #Z2
    [{'+a','-d'}, [15]],
    [{'+a', '-b'}, [16]],
    [{'-b', '-d'}, [17]],
    [{'-a','+c','+d'}, [18]],
    [{'-c', '-d'}, [19]]
]

def _not(el):
    if (el[0] == '+'):
        return '-' + el[1]
    else:
        return '+' + el[1]
    
def remove_dup(arr):
    seen = {}
    i = 0
    while i < len(arr) - 1:
        j = i + 1
        while j < len(arr):
            if arr[i][0] == arr[j][0]:
                del arr[j]
                j -= 1
            j += 1
        i += 1
            
resolv = []
linked = True
while linked:
    linked = False  
    for i in range(0, len(system) - 1):
        for j in range(i + 1, len(system)):
            cnt = 0
            for e in system[j][0]:
                if(_not(e) in system[i][0]):
                    if (cnt > 0):
                        del resolv[-1]
                        break
                    else:
                        linked = True
                        buf = [{},[]]
                        buf[0] = system[i][0].copy()
                        buf[0].update(system[j][0])
                        buf[0].remove(e)
                        buf[0].remove(_not(e))
                        buf[1] =  system[i][-1].copy()
                        buf[1].append(system[j][-1].copy())
                        if(len(buf[0]) == 0):
                            print('FOUND: ')
                            print(buf)
                            sys.exit(0)
                        resolv.append(buf)
                        cnt+=1
    remove_dup(resolv)
    system.extend(resolv.copy())
    for e in system:
        e[-1] = e[-1].copy()
    resolv = []
    print (*system, sep = "\n")
    print('\n')
print('Done.')

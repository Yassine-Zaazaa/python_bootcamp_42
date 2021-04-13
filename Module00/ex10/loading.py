from time import sleep

def ft_progress(lst):
    LIST = list(lst)
    progress = ">"
    for elem in lst:
        print(f"\rETA : ", round(0.01 * LIST[-1]),"s [",round((elem/10)),"%]","[",progress," " *(20-len(progress)),"]",(elem+1),"/1000","Elapsed time",round(elem*0.01), end='' )
        if elem % 50==0:
            progress ="="+progress
        yield elem
    
    
    
listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret)
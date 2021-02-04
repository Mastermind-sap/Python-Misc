##def e(a):
##    try:
##        return(exec(a))
##    except:
##        print("Error")
##while True:
##    s=""
##    while True:
##        s1=input(">>>")
##        if len(s1)!=0:
##            s+=s1+"\n"
##        else:
##            break
##    e(compile(s,'mulstring', 'exec'))
import io
from contextlib import redirect_stdout
def e(a):
    try:
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            exec(a)
        out = stdout.getvalue()
        return (out)
    except:
        print("Error")
while True:
    s=""
    while True:
        s1=input(">>>")
        if len(s1)!=0:
            s+=s1+"\n"
        else:
            break
    print(e(compile(s,'mulstring', 'exec')))

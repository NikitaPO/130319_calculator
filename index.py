
from datetime import datetime, date, time

def wrapper(f):
    def writeToFile(*args):
        #functools
        writeToFile.__doc__ = f.__doc__
        print(f.__name__, args)
        with open('text.txt', "a") as text:
            time = datetime.utcnow()
            str = f'{f.__name__}, {args}, {time}'
            text.write(str)
            text.write("\r\n")
        return f(*args)
    return writeToFile

@wrapper
def calc(a, b, operation):
    """Calulator (a, b, ['+']|['-']|['/']|['*'])"""
    if (operation == '*'):
        return '%.2f * %.2f = %.2f' % (a, b, a*b)
    elif (operation == '/'):
        return '%.2f / %.2f = %.2f' % (a, b, a/b)
    elif (operation == '+'):
        return '%.2f + %.2f = %.2f' % (a, b, a+b)
    elif (operation == '-'):
        return '%.2f - %.2f = %.2f' % (a, b, a-b)

print(calc(2,3,'-'))
print(calc.__doc__)

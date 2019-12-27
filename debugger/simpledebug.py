import sys
def task(a, b):
    x = (a-b)*(a+b)
    y = 10+x
    print('Output = ' + str(y))

def trace_calls(frame, event, arg):
    if frame.f_code.co_name == "task":
        print(frame.f_code)
        return trace_lines
    return
sys.settrace(trace_calls)
def trace_lines(frame, event, arg):
    print(frame.f_lineno)

task(3, 5)
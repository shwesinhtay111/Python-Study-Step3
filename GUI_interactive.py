from IPython.display import display

def f(a, b):
    display(a + b)
    return a+b
w = interactive(f, a=10, b=20)
print(type(w))
print(w.children)
print(display(w))
print(w.kwargs)
print(w.result)
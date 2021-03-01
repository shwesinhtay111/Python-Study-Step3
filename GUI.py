# Start with some imports!

from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
# Very basic function
def f(x):
    return x
# Generate a slider to interact with
interact(f, x=10,);
# Booleans generate check-boxes
interact(f, x=True);
# Strings generate text areas
interact(f, x='Hi there!');

# Using a decorator!
@interact(x=True, y=1.0)
def g(x, y):
    return (x, y)

# Again, a simple function
def h(p, q):
    return (p, q)

interact(h, p=5, q=fixed(20));

# Can call the IntSlider to get more specific
interact(f, x=widgets.IntSlider(min=-10,max=30,step=1,value=10));

# Min,Max slider with Tuples
interact(f, x=(0,4));

# (min, max, step)
interact(f, x=(0,8,2));

interact(f, x=(0.0,10.0));

interact(f, x=(0.0,10.0,0.01));

@interact(x=(0.0,20.0,0.5))
def h(x=5.5):
    return x
interact(f, x=['apples','oranges']);

interact(f, x={'one': 10, 'two': 20});
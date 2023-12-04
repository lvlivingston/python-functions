# def first_function():
#     pass

# result = first_function()
# print(result)

'''
JavaScript Function Declarations 
- gets hoisted to the top of the file automatically when called, still works if you try to call it later

function myFunction() {
    return something here
}

JavaScript Function Expressions
- these do not get hoisted to the top

const myFunction = () => {
    return something here
}
or 
const myFunction = function() {
    return something here
}


this will not work in Python
myFunction = def myFunction():
    pass
'''

# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def compute(a, b, operation):
#     return operation(a, b)

# print( compute(1, 2, add) )

# doesn't work bc we're missing the two required arguments, bc of above parameters
# print(add())

# this can be used if you don't know how many arguments will be put in,
# star args is just a placeholder
# def fn(*args):
#     print( type(args) )
#     for arg in args:
#         print(arg)

# fn(1, 2, 'SEI', 'banana pancakes', 'a + b')

# def dev_skills(dev_name, *args):
#     # can do this line
#     dev = {'name': dev_name, 'skills': []}
#     # or this line... both are the same, list() creates a list of the tuple
#     dev = {'name': dev_name, 'skills': list(args)}
#     # args will be a tuple
#     for skill in args:
#         dev['skills'].append(skill)
#     return dev

# print(dev_skills('Alex', 'HTML', 'CSS', 'JavaScript', 'Python'))
# # -> {'name': 'Alex', 'skills': ['HTML', 'CSS', 'JavaScript', 'Python']}

# def dev_skills(dev_name, **kwargs):
#     # kwargs will be a dictionary!
#     dev = {'name': dev_name, 'skills': kwargs}
#     return dev

# print(dev_skills('Jackie', HTML=5, CSS=3, JavaScript=4, Python=2))

def arg_demo(pos1, pos2, *args, **kwargs):
  print(f'Positional params: {pos1}, {pos2}')
  print('*args:')
  for arg in args:
    print(' ', arg)
  print('**kwargs:')
  for keyword, value in kwargs.items():
    print(f'  {keyword}: {value}')

arg_demo('A', 'B', 1, 2, 3, color='purple', shape='circle')

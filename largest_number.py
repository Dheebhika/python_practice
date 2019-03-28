def largest(arg1, arg2, arg3):
    if (arg1 > arg2) and (arg1 > arg3):
        return arg1;
    elif (arg2 > arg1) and (arg2 > arg3):
        return arg2;
    else:
        return arg3;


print(largest(50, 20, 30));

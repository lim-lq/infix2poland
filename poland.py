#!/usr/bin/python
#coding=utf-8

OPTLEVEL = {
    1: ['+', '-'],
    2: ['*', '/'],
    3: ['(', ')']
}

def generate_opt_map(opt_dict):
    """
    desc: 该函数用来将OPTLEVEL转换为操作符对应的level字典
    param: opt_dict 就是OPTLEVEL
    return: 转换后的字典, 如{'+': 1, '*': 2}

    """
    opt_map = {}
    for key in opt_dict.keys():
        for opt in opt_dict[key]:
            opt_map[opt] = key
    return opt_map

def infix2poland(infix_express):
    """
    desc: 该函数将中缀表达式转换为逆波兰表达式
    param: 中缀表达式
    return: 逆波兰表达式

    """
    opt_list = []
    poland_express = ''

    opt_map = generate_opt_map(OPTLEVEL)

    for char in infix_express:
        if char in opt_map.keys():
            if len(opt_list) and opt_map[char] <= opt_map[opt_list[len(opt_list) - 1]] and \
                opt_list[len(opt_list) - 1] != '(':
                while len(opt_list):
                    opt = opt_list.pop()
                    if opt_map[char] <= opt_map[opt] and opt != "(":
                        poland_express += opt
                    else:
                        if opt == "(":
                            opt_list.append(opt)
                        break
                opt_list.append(char)
            elif char == ')':            
                while len(opt_list):
                    opt = opt_list.pop()
                    if opt != "(":
                        poland_express += opt
                    else:
                        break
                if not len(opt_list) and opt != "(":
                    print "The infix express has error: %s" % infix_express
                    exit(1)
                    
            else:
                opt_list.append(char)
        else:
            poland_express += char
    while len(opt_list):
        poland_express += opt_list.pop()
    return poland_express

if __name__ == "__main__":
    infix_express = "a+b*(c-d)"
    poland_express = infix2poland(infix_express)
    print "%s to %s" % (infix_express, poland_express)

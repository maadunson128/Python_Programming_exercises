###Program: String Reversal

def str_reverse(s):
    if s == "":
        return s
    else:
        return str_reverse(s[1:]) + s[0]
    
print(str_reverse("olleH"))
    
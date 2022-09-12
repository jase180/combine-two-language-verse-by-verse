import sys

def toList(txt):
    with open(txt,'r', encoding="utf8") as f:  # read .txt into string
        data_str = f.read()
    
    # Put into list and remove '\n'
    data = data_str.split()
    
    out = []
    
    group = []
    for i in data:
        if i.isnumeric():
            verse = ' '.join(group)
            out.append(verse)
            group = []
            group.append(i)
        else:
            group.append(i)
    
    out.pop(0) # remove first empty group 
        
    return out 


# main
eng_ls = toList("English.txt")
chi_ls = toList("Chinese.txt")

if len(eng_ls) != len(chi_ls):
    print("Error, two lists aren't the same length")
    sys.exit()
    
with open("Output.txt", 'w', encoding = "utf8") as f:
    for i in range(len(eng_ls)):
        print(eng_ls[i], file = f)
        print(chi_ls[i], file = f)
        print("", file = f)

print("Script run finished")


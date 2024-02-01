inp = input("Enter your string: ")

print("{ ", end = '')
outputChar = ''
for i in range(len(inp)):
    match (inp[i]):
        case '\\':
            outputChar = '\\\\'
        case '\"':
            outputChar = '\\\"'
        case '\'':
            outputChar = '\\\''
        case '\t':
            outputChar = '\\t'
        case '\n':
            outputChar = '\\n'
        case any:
            outputChar = inp[i]
    print(f"\'{outputChar}\'", end = '')

    print(',', end = ' ')

print("\'\\0\' }")
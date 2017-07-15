def textJustification(words, L):
    line = 0 
    output = []
    finalOut = []
    for item in words:
        if line + len(item) < L:
            line += len(item)
            output.append(item)
        elif line == L:
            finalOut = output
            output = []
        else:
            for item in output:
                item +=" "
                line +=1
                if line == L:
                    finalOut = output
                    output = []
                    break
        return finalOut

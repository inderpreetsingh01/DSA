def fill_lps(str):
    lps = []
    lps.append(0)
    length = 0
    i = 1
    while(i<len(str)):
        if str[i] == str[length]:
            lps.append(length+1)
            length+=1
            i+=1

        elif length == 0:
            lps.append(0)
            i+=1

        else:
            length = lps[length-1]
    return lps


if __name__ == '__main__':
    print(fill_lps('AAABAAAAC'))
    print(fill_lps('abacabad'))
    print(fill_lps('abbabb'))

            

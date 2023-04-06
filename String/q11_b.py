from q11_a import fill_lps

def KMP(string, pat):
    lps = fill_lps(pat)
    print(lps)
    i = 0
    j = 0
    while(i<len(string)):
        if (string[i]==pat[j]):
            i+=1
            j+=1
        if j==len(pat):
            print(i-j)
            j = lps[j-1]
        if (string[i]!=pat[j]) and (j<len(pat)):
            if j==0:
                i+=1
            else:
                j = lps[j-1]

KMP('ababcababaad', 'ababa')
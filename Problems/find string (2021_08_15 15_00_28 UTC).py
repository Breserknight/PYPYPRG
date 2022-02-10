def count_substring(string, sub_string):
    s = [i for i in string]
    r = [i for i in sub_string]
    ans = 0
    if len(r) == 1:
        for i in s:
            if i == r[0]:
                ans += 1
        return ans
    for i in range(len(s)):
        if s[i] == r[0]:
            ctr1 = 0
            ctr2 = i
            for o in range(len(r)):
                if s[ctr2] == r[ctr1]:
                    if ctr1 == len(r) - 1:
                        ans += 1
                        break
                    if ctr2 == len(s)-1:
                        break
                    ctr2 += 1
                    ctr1 += 1
                    continue
                break

    return ans


string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)

print(count)
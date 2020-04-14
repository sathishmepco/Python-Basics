from collections import Counter
def main():
    s = input()
    common = Counter(s).most_common(2)
    if len(common) is 1:
        print(common[0],end="")
    else:
        print(common[0],common[1],end="")
		
main()
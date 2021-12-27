import collections
text = ("all I want is a proper cup of coffee made in a proper copper coffee pot. "
        "I may be off my dot but I want a cup of coffee from a proper coffee pot.")
text_list = text.split()
#for x in range(len(text_list)):
#    if re.search(r'[\.\?\!]$', text_list[x]):
#        text_list[x] = text_list[x].rstrip(r'[\,\.\?\!]')
freq_dict = collections.Counter(text_list)
n = int(input())
for x in freq_dict.most_common(n):
    print(f"{x[0]} {x[1]}")


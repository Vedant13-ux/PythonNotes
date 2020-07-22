# fname = input("Enter file name: ")
# fh = open(fname)
# hour_count=dict()
# for line in fh:
#     line=line.strip()
#     if line.startswith('From '):
#         list_words=line.split()
#         date=list_words[5]
#         hour=date.split(':')[0]
#         hour_count[hour]=hour_count.get(hour,0)+1
#     else: continue



# for hour,count in sorted(hour_count.items()):
#     print(hour,count)
x=(2,6,10)
# x.sort(reverse=True)
print(x[1])
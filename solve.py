strs=["flock","flow","flower","flame"]
common_prefix=""
checkWord=""
isValid=False
if len(strs)>=1:
    checkWord=strs[0]
for i in len(strs)-:
    word=strs[strs.index(checkWord)+1+i]

    
print(common_prefix)
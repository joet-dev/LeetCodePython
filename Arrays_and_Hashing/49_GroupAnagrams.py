import collections

def groupAnagrams(strs): 
    strDic = collections.defaultdict(list)
    for i, str in enumerate(strs):
        strDic[''.join(sorted(str))].append(i)
    
    result = []
    for key in strDic.keys(): 
        sublist = []
        for val in strDic[key]: 
            sublist.append(strs[val])
        result.append(sublist)

    return result

groupAnagrams(["eat","tea","tan","ate","nat","bat"])
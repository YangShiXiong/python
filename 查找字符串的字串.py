import re
str1 = '<a href="http://www.fishc.com/dvd"target="_blank"> 鱼 C 资源打包 </a>'
str2 = re.search(r'www.fishc.com',str1)
print(str2.group())

import re

txt = 'I am a good boy'
#search
print('-----Search functions')
output = re.search("^I.*boy$", txt)
print(output.start(),output.end())
print('Span -',output.span())
print('String -',output.string)
print('Group -',output.group())
output = re.search("^I.*girl$", txt)
print(output)
output = re.search("\s", txt)
print(output.start())

#findall
print('-----findall functions')
output = re.findall("am", txt)
print(output)
output = re.findall("zoo", txt)
print(output)

#split
print('-----split functions')
output = re.split("\s", txt)
print(output)
output = re.split("\s", txt, 1)
print(output)

#replace
print('-----sub (replace) functions')
output = re.sub("\s", "_", txt)
print(output)
output = re.sub("\s", "_", txt, 2)
print(output)

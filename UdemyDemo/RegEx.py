import re

text='he is working in infostretch for long time, am sitting in first floor'
pattern=['working','employee']

for val in pattern:
    if re.search(val,text):
        print("match {} found ".format(val))
    else:
        print("match not found for {}".format(val))
match=re.search(pattern[0],text)
print(match.start())
#######################################################################
def RegexVerify(patterns,phrase):
    for pattern in patterns:
        print (re.findall(pattern,phrase))
        print('\n')

text='i am a bad bada badad boy and I hate myself, I am doing some thing different'
pat=['a*','ba+','ba*','ba?','ba{2}']
RegexVerify(pat,text)
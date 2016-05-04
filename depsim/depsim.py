import sys
from pyparsing import *

# Properties
# TODO: Should we allow for 100% failure rate or is it not even worth using our tool?
def failure_rate_parse(s, loc, toks):
    if r'%' in toks[1]:
        ans = float(toks[1].strip(r'%')) / 100
    else:
        ans = float(toks[1])
    return {'failure': ans}
failure_rate = 'fail' + Combine((Word(nums) + '%') ^ Regex(r'0\.\d+'))
failure_rate.setParseAction(failure_rate_parse)
name = Word(alphanums)

def block(enclosing):
    def to_dict(s, loc, toks):
        try:
            num = int(toks[0])
            toks.pop(0)
        except ValueError:
            num = 1
        block_type = toks.pop(0)
        if toks[0] != '{':
            name = toks.pop(0)
        else:
            name = ''
        # Get rid of open and close brackets
        toks.pop(0)
        toks.pop()
        return {
                'name': name,
                'number': num,
                'type': block_type,
                'children': toks
                }

    return OneOrMore(enclosing).setParseAction(to_dict)

#Region definition
server = (Optional(Word(nums)) + CaselessKeyword('server') + Optional(name) + '{' + 
        failure_rate +
    '}')
rack = (Optional(Word(nums)) + CaselessKeyword('rack') + Optional(name) + '{' + 
        block(server) + 
    '}')
cluster = (Optional(Word(nums)) + CaselessKeyword('cluster') + Optional(name) + '{' + 
        block(rack) + 
    '}')
datacenter = (Optional(Word(nums)) + CaselessKeyword('datacenter') + Optional(name) + '{' + 
        block(cluster) + 
    '}')
region = CaselessKeyword('region') + name + '{' + block(datacenter) + '}'

# Deployment Strategy



model = block(region) # + deployment strategy
model.ignore(javaStyleComment)

dep_model = model.parseFile(sys.argv[1])


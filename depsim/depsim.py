import sys
from pyparsing import *

# Properties
# TODO: Should we allow for 100% failure rate or is it not even worth using our tool?
failure_rate = 'fail' + ((Word(nums) + '%') ^ Regex(r'0\.\d+'))
name = Word(alphanums)

def block(enclosing):
    return OneOrMore(enclosing)

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



model = OneOrMore(region) # + deployment strategy
model.ignore(javaStyleComment)

dep_model = model.parseFile(sys.argv[1])
print(dep_model.asList())

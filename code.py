import sys
from ruamel import yaml

with open('user.yaml','r') as stream:
    user_yaml = yaml.safe_load(stream)

print("Type of user_yaml variable:")
print(type(user_yaml))




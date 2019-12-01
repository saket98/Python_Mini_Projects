"""
program to print the relations operators, based on their relations.
1. greater than.
2. less than.
3. equal to.

output: print the operator sign. eg: '<', '>', '='.

"""
def chef_operator(a, b):
	if a < b:
		return '<'
	elif a > b:
		return '>'
	else:
		return '='

test_case = int(input())
for i in range(test_case):
	a, b = map(int, input().strip().split())
	print(chef_operator(a, b))
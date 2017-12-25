puzzle = open('puzzle').read().splitlines()

steps = int(puzzle[1].split()[-2])
states = {}

for state in range((len(puzzle) - 2)/10):
	state = puzzle[3 + 10*state: 13 + 10*state]
	state_idx = state[0].split()[-1][0]
	states[state_idx] = [[state[2].split()[-1][0], 
						  state[3].split()[-1][0], 
						  state[4].split()[-1][0]],
						 [state[6].split()[-1][0], 
						  state[7].split()[-1][0], 
						  state[8].split()[-1][0]]
						]
	if states[state_idx][0][1] == 'r':
		states[state_idx][0][1] = 1
	else:
		states[state_idx][0][1] = -1
	if states[state_idx][1][1] == 'r':
		states[state_idx][1][1] = 1
	else:
		states[state_idx][1][1] = -1

idx = 0
ones = {}
current_state = 'A'

for i in range(steps):
	if idx in ones and ones[idx] == '1':
		ones[idx] = states[current_state][1][0]
		idx += states[current_state][1][1]
		current_state = states[current_state][1][2]
	else:
		ones[idx] = states[current_state][0][0]
		idx += states[current_state][0][1]
		current_state = states[current_state][0][2]

print ones.values().count('1')
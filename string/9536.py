import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    target_sounds = input().rstrip().split(' ')
    while True:
        command = input().rstrip()
        if command == 'what does the fox say?':
            print(' '.join([target for target in target_sounds if target is not None]))
            break
        else:
            command = command.split(' ')
            sound = command[2]
            for target_idx in range(len(target_sounds)):
                if target_sounds[target_idx] == sound:
                    target_sounds[target_idx] = None

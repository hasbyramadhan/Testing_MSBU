def max_skill(N, M, A, B):
    current_skill = M
    players = list(zip(A, B))
    players.sort()

    for a, b in players:
        if current_skill >= a:
            current_skill += b
        else:
            break

    return current_skill

# Input sesuai format
N, M = map(int, input().split())  
A = list(map(int, input().split()))  
B = list(map(int, input().split()))  

result = max_skill(N, M, A, B)
print(result)

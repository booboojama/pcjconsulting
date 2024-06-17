import random 
from matplotlib import pyplot as plt 

def coin_toss(): 
    outcome = random.choice(['Heads', 'Tails']) 
    return outcome 

def group_players(players): 
    return [players[i:i+2] for i in range(0, len(players), 2)] 

def main(): 
    players = [{'name': f"Player {i}", 'balance': 10} for i in range(1, 41)] 
    balance_history = {player['name']: [player['balance']] for player in players} 

    for j in range(1,40000): 
        random.shuffle(players) 
        pairs = group_players([p for p in players if p["balance"] > 0]) 

        for pair in pairs: 
            if len(pair) == 2: 
                outcome = coin_toss() 
                winner = pair[0] 
                loser = pair[1] 
                if outcome == 'Heads': 
                    winner, loser = loser, winner 
                winner['balance'] += 1 
                loser['balance'] -= 1 

        for player in players: 
            balance_history[player['name']].append(player['balance']) 
    plot_graph(balance_history) 

  

def plot_graph(balance_history): 
    plt.figure(figsize=(10, 6)) 
    for player, balances in balance_history.items(): 
        plt.plot(balances, label=player) 
    plt.xlabel("Tosses") 
    plt.ylabel("Balance") 
    plt.title("Player Balances Over Tosses") 
    plt.legend() 
    plt.grid() 
    plt.show() 
  
if __name__ == "__main__": 
    main() 

  
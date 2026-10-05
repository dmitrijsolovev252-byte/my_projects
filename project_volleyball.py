import random
import time



def main():
    team1 = input()
    team2 = input()
    sets = {team1 : 0, team2 : 0}
    scores = []
    Set(sets, team1, team2, scores)

def Set(sets, team1, team2, scores):
    print('ДОБРО ПОЖАЛОВАТЬ НА ВОЛЕЙБОЛЬНЫЙ МАТЧ!!!')
    print(f'Сегодня столкнутся команды: {team1} и {team2}')


    print(f'Первая партия!')
    print('_' * 50)
    sets[game(team1, team2, sets, scores)] += 1
    print(f'{team1} {sets[team1]}:{sets[team2]} {team2}')

    print('_' * 50)
    print('Вторая партия!')
    sets[game(team1, team2, sets, scores)] += 1
    print(f'{team1} {sets[team1]}:{sets[team2]} {team2}')

    if sets[team1] != 2 and sets[team2] != 2:
        print('_' * 50)
        print('Третья партия!')
        sets[game(team1, team2, sets, scores)] += 1
        print(f'{team1} {sets[team1]}:{sets[team2]} {team2}')

    print(f'Конец игры! Счет по партиям: ')
    print(f'{scores[0]}', f'{scores[1]}', sep = '\n')

    if len(scores) == 3:
        print(f'{scores[2]}')
          


def game(team1 : str, team2: str, sets: dict, scores: list):

    teams = {team1: 0, team2: 0}

    


    if teams[team1] == 0 and teams[team2] == 0:
        server_name = random.choice([team1, team2]) 

    who_set = team1 if server_name == team2 else team2

    
    while True:

        winner, message = rally(server_name, who_set, teams)
        
        print(message)
        print(f'{team1} {teams[team1]}:{teams[team2]} {team2}')
        

        server_name = winner
        who_set = team1 if server_name == team2 else team2

        if teams[team1] >= 25 or teams[team2] >= 25:
            if teams[team1] - teams[team2] >= 2 or teams[team2] - teams[team1] >= 2:
                print('_' * 50)
                print(f'КОНЕЦ ПАРТИИ, ПОБЕДИТЕЛЬ: {max(teams, key=teams.get)}')
                print(f'Счет по партиям: {team1} {sets[team1]}:{sets[team2]} {team2}')

                scores.append(f'{team1} {teams[team1]}:{teams[team2]} {team2}')
                
                return max(teams, key = teams.get)
    
    

def rally(server_name, who_set, teams):

    serve_roll = random.random()
    
    if serve_roll < 0.08:
        teams[server_name] += 1
        time.sleep(2.0)
        print()
        return server_name, f'Эйс! от команды: {server_name}'
    elif serve_roll < 0.15:
        teams[who_set] += 1
        time.sleep(2.0)
        print()
        return who_set, f'Заступ! очко команды: {who_set}'
    elif serve_roll < 0.23:
        teams[who_set] += 1
        time.sleep(2.0)
        print()
        return who_set, f'Аут! очко команды: {who_set}'

    attacker = who_set
    defender = server_name
    
    while True:

        set_roll = random.random()

        if set_roll < 0.05:
            teams[defender] += 1
            time.sleep(2.0)
            print()
            return defender, f'Ошибка второй передачи! очко команды: {server_name}'
        elif set_roll < 0.10:
            teams[who_set] += 1
            time.sleep(2.0)
            print()
            return defender, f'Скидка! очко команды: {who_set}'

        spike_roll = random.random()

        if spike_roll < 0.15: 
            teams[server_name] += 1
            time.sleep(2.0)
            print()
            return defender, f'БЛОК! Соперник просто зачехлил игрока, очко команды: {server_name}'

        elif spike_roll < 0.20:
            teams[attacker] += 1
            time.sleep(2.0)
            print()
            return attacker, f'Скидка! очко команды: {who_set}'

        elif spike_roll < 0.60:
            teams[attacker] += 1
            time.sleep(2.0)
            print()
            return attacker, f'Нападающий забивает мяч! очко команды: {who_set}'

        elif spike_roll < 0.63:
            teams[attacker] += 1
            time.sleep(2.0)
            print()
            return attacker, f'МОЩНЫЙ УДАР В ТРЕТИЙ МЕТР! очко команды: {who_set}'
        
        elif spike_roll < 0.65:
            teams[attacker] += 1
            time.sleep(2.0)
            print()
            return attacker, f'ПОЛ-ПОТОЛОК! очко команды: {who_set}'                       

        receive_roll = random.random()

        if receive_roll < 0.35:
            teams[defender] += 1
            time.sleep(2.0)
            print()
            return defender, f'команда: {who_set} не приняла мяч от касания блока!'

        attacker, defender = defender, attacker


if __name__ == '__main__':
    main()

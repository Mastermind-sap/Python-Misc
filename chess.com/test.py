import chessdotcom as chess
import pprint
import requests

printer = pprint.PrettyPrinter()

def print_leaderboards():
        print("Leaderboards")
        data = chess.get_leaderboards().json
        categories = data.keys()
        for category in categories:
                print('Category:', category)
                for idx, entry in enumerate(data[category]):
                    if idx<3:
                        print(f'Rank: {idx + 1} | Username: {entry["username"]} | Rating: {entry["score"]}')
                    else:
                        break


def get_player_rating(username):
        print("Player Ratings")
        data = chess.get_player_stats(username).json
        categories = ['chess_blitz', 'chess_rapid', 'chess_bullet']
        for category in categories:
        	print('Category:', category)
        	print(f'Current: {data[category]["last"]["rating"]}')
        	print(f'Best: {data[category]["best"]["rating"]}')
        	print(f'Record: {data[category]["record"]}')

def get_player(username):
        print("Player profile")
        data = chess.get_player_profile(username).json
        #printer.pprint(data)
        print("Avatar:",data['avatar'])
        print("Name:",data['name'])
        print("Country:",data['country'])
        print("Followers:",data['followers'])
        print("Status:",data['status'])
        print("Url:",data['url'])
        print("Username:",data['username'])
        data1=chess.is_player_online(username).json
        #printer.pprint(data1)
        print("Online:",data1['online'])
        data1=chess.get_player_clubs(username).json
        #printer.pprint(data1)
        print("Clubs:")
        for i in data1['clubs']:
                print (i['name'])
        
##def get_most_recent_game(username):
##	data = chess.get_player_game_archives(username).json
##	url = data['archives'][-1]
##	games = requests.get(url).json()
##	game = games['games'][-1]
##	printer.pprint(game)

def puzzle():
        print("Random Puzzle")
        data = chess.get_random_daily_puzzle().json
        #printer.pprint(data)
        print(data['title'])
        print(data['image'])
        print(data['url'])
        print("Current Puzzle")
        data1 = chess.get_current_daily_puzzle().json
        #printer.pprint(data1)
        print(data1['title'])
        print(data1['image'])
        print(data1['url'])
           
#print_leaderboards()
get_player_rating('Mastermindsap')
#get_most_recent_game('Mastermindsap')
get_player('Mastermindsap')
puzzle()

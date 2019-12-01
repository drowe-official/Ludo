import server
import client
import player
inp = input("host or client\n")
ip = "127.0.0.1"
port = 65432

def pickle_turn(player_id, rolls):
    string = "{}|{}".format(player_id, "|".join(map(str, rolls)))
    return string
    
def unpickle_turn(string):
    tokens = string.split("|")
    player_id = int(tokens[0])
    rolls = [int(roll) for roll in tokens[1:]]
    return (player_id, rolls)
    
    
if inp == "host":
    HOST_ID = 0
    host = server.Server(ip, port) # make host
    PLAYER_COUNT = int(input("Number of players: ")) # get no. of players
    host.listen(PLAYER_COUNT-1) # hold until server gets N connections
    
    for client_id, client in enumerate(host.clients): # send players their ids
        host.send(client, str(client_id+1))
    host.broadcast(str(PLAYER_COUNT)) # broadcasts total players
    
    
    b = player.Board(PLAYER_COUNT)
    players = [player.Player(b, i) for i in range(PLAYER_COUNT)]
    die = player.Die()
    player_id = HOST_ID
    while True:
        if player_id: # deal with clients
            while True:
                pickled = host.receive()
                if pickled:
                    break
            print ("received moves for another player", pickled)
        else: # host's turn
            if input() == "r":
                print ("taking my turn")
                rolls =  die.get_rolls()
                pickled = pickle_turn(HOST_ID, rolls)
            
        host.broadcast(pickled)
        player_id, rolls = unpickle_turn(pickled)
        players[player_id].play(rolls)
        b.display()
        player_id = (player_id + 1) % PLAYER_COUNT


elif inp == "client":

    client = client.Client()
    client.connect(ip, port)
    CLIENT_ID = int(client.receive())
    PLAYER_COUNT = int(client.receive())
    b = player.Board(PLAYER_COUNT)
    players = [player.Player(b, i) for i in range(PLAYER_COUNT)]
    die = player.Die()
    
    player_id = 0
    while True:
        if player_id == CLIENT_ID: #if its their turn
            if input() == "r":
                print ("taking my turn")
                rolls = die.get_rolls()
                pickled = pickle_turn(CLIENT_ID, rolls)
                client.send(pickled)
        else: #if they receive someone else's turn from the server
            pickled = client.receive()
            print ("received moves for another player", pickled)
        print (pickled)    
        player_id, rolls = unpickle_turn(pickled)
        players[player_id].play(rolls)
        b.display()
        player_id = (player_id + 1) % PLAYER_COUNT

else:
    quit()
def cards(player):
    if player in "JQK":
        player = 0.5
    elif player in "A":
        player = 1
    else:
        player = int(player)
    return player

def INPUT():
    player1bet, player2bet = map(int, input().split())
    player1odds, player2odds = map(int, input().split())
    player1cards, player2cards, pc = input().split()
    return player1bet, player2bet, player1odds, player2odds, player1cards, player2cards, pc
def choose(player):
    while(True):
        a=input().split()
        
        if(a[0]=="N"):
             return player
        else:
            player+=cards(a[1])
            if(player>10.5):
                    player=0
                    return player
            if(player==10.5):
                return player
                 
def pcchoose(pc,player1cards,player2cards):
    if(player1cards>10.5 and player2cards>10.5):
        return pc
    while(True):
        a=input().strip()
        pc+=cards(a)
        if(pc>10.5):
            pc=0
            return pc 
        if(player1cards>10.5):
            if(pc>=player2cards):
                 return pc
        elif(player2cards>10.5):
            if(pc>=player1cards):
                return pc
        elif(pc>=player1cards or pc>=player2cards):
            return pc 
            
        
def main():
    player1bet, player2bet, player1odds, player2odds, player1cards, player2cards, pc = INPUT()

    player1cards = cards(player1cards)
    player2cards = cards(player2cards)
    pc           = cards(pc)
    player1cards = choose(player1cards)
    player2cards = choose(player2cards)
    pc           =pcchoose(pc,player1cards,player2cards)

    #player1
    if(player1cards==pc):  #draw
        print("Player1 +",end="")
        print(player1bet)
    elif(player1cards==10.5):#10.5win
        print("Player1 +",end="")
        print(player1bet+player1bet*player1odds)
    elif(player1cards>pc or pc==0):#normal win 
        print("Player1 +",end="")
        print(int(player1bet+player1bet*player1odds*0.5))
    elif(player1cards<10.5 and pc==10.5 ):
        print("Player1 -",end="")
        print(int(player1bet+player1bet*player1odds))
    elif(player1cards<pc or player1cards==0):
        print("Player1 -",end="")
        print(int(player1bet+player1bet*player1odds*0.5))
    #player2
    if(player2cards==pc):  #draw
        print("Player2 +",end="")
        print(player2bet)
    elif(player2cards==10.5):#10.5win
        print("Player2 +",end="")
        print(player2bet+player2bet*player2odds)
    elif(player2cards>pc or pc==0):#normal win
        print("Player2 +",end="")
        print(int(player2bet+player2bet*player2odds*0.5))
    elif(player2cards<10.5 and pc==10.5 ):
        print("Player2 -",end="")
        print(int(player2bet+player2bet*player2odds))
    elif(player2cards<pc or player2cards==0):
        print("Player2 -",end="")
        print(int(player2bet+player2bet*player2odds*0.5))
main()

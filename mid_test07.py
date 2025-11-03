def main():
    balls = []
    TOTAL=0
    SPECIAL=0
    while True:
        try:
            line = input()
            if (line==""):
                break
        except EOFError:
            break 
        balls += list(map(int, line.split()))
    j=0#j=index
    for i in range(10):#局數
        if(balls[j]==10):
            TOTAL+=10+balls[j+1]+balls[j+2]
            SPECIAL+=30
            #strike
            j+=1
        elif(balls[j]+balls[j+1]==10):
            TOTAL+=10+balls[j+2]
            SPECIAL+=20
            #spare
            j+=2
        else:
            TOTAL+=balls[j]+balls[j+1]
            SPECIAL+=balls[j]+balls[j+1]
            #normal
            j+=2
    print(TOTAL)
    print(SPECIAL)

if __name__=="__main__":    
    main()
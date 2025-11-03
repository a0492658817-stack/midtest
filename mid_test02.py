def INPUT():
    n=int(input())
    data=[]
    for i in range(n):
        name= input()
        H=int(input())
        schedule=[]
        for j in range(H):
            a=input()
            schedule.append(a)
        data.append((name,H,schedule))
    return data
def findsame(course):
    n=len(course)
    result=[]
    for i in range(n):
        for j in range(i+1,n):
            name1,_,schedule1= course[i]
            name2,_,schedule2= course[j]
            for s1 in schedule1:
                if s1 in schedule2:                   
                    result.append(f"{name1},{name2},{s1}")
    return result
def main():
    course=INPUT()
    result=findsame(course)
    if(result):
        for i in result:
            print(i)
    else:
        print("correct")

if(__name__=="__main__"):
    main()
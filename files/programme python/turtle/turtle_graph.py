import turtle
from time import sleep
def pause():pause=input("Press enter to continue...")
def sum_points_from_days(listday):
    total=0
    for i in range(len(listday)):
        total+=int(listday[i])
    return total

#Questions per day 36  
day1=["5","5","1","2","8","2","4","1","8","3","10","5","8","8","1","4","1","4","1","6","10","6","2","4","8","10","2","7","5","8","4","9","7","8","9","9"]
day2=["2","6","7","9","8","4","7","5","2","7","7","7","9","7","5","6","1","3","1","2","5","9","8","5","6","5","2","10","10","2","10","8","1","3","10","9"]
day3=["10","10","9","5","4","8","7","4","4","2","1","5","2","10","5","7","1","7","4","6","5","10","3","1","9","6","9","9","6","5","10","2","9","1","10","2"]
day4=["0","1","2","3","4","5","6","7","8","9","10","0","1","2","3","4","5","6","7","8","9","10","0","1","2","3","4","5","6","7","8","9","10","0","1","2"]
data_index_to_show=0
day_data_list=[day1,day2,day3,day4]
day_list=[1,2,3,4]
def create_number():
    numbers={}
    c=10
    y=250
    for i in range(11):
        numbers[c]=y
        c-=1
        y-=50
    numbers[0]=-230
    return numbers
numbers=create_number()
T=turtle.Turtle()
def init(T,questions):
    T.speed(10)
    T.penup()
    T.goto(-250,250)
    T.write("Score")
    T.goto(-270,250)
    T.write("<--")
    T.goto(-300,250)
    y=200
    c=10
    for i in range(11):
     T.write(c)
     c-=1
     T.goto(-300,y)
     y-=50

    T.up()
    T.goto(-285,-250)
    T.down()
    T.width(5)
    T.goto(-285,260)
    T.up()
    T.goto(-310,-230)
    T.write(0)
    T.goto(-285,-230)
    T.down()
    T.goto(-310,-230)
    T.goto(310,-230)
    T.up()
    T.goto(280,-210)
    T.write("Days ")
    T.goto(0,225)
    T.write("Cathegorie:\nQuestions:{}".format(questions))
    y=-250
    x=-250
    for i in range(len(day_list)):
        T.goto(x,y)
        T.write("day{}".format(i+1))
        x+=50
def test(day_data_list,data_index_to_show,day_list,numbers,colour,T,Width):
    T.width(Width)
    T.color(colour)
    y=-230
    x=-285
    T.goto(x,y)
    T.down()
    x=-250
    #T.goto(x,y)
    for i in range(len(day_data_list)):
        m=int(day_data_list[i][data_index_to_show])
        y=numbers[m]
        T.down()
        T.goto(x,y)
        T.circle(radius=2)
        T.up()
        x+=50
        y+=50
    T.write(data_index_to_show)
colour=['red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink']
        # 1         2        3          4            5       6       7          8         9         10        11        12        13       14        15         16        17        18       19        20        21         22        23       24       25        26         27       28        29        30         31       32        33         34       35        36
colour=["#407294","#ff4a4a","#0660bd","#754a6c","#9e9e8b","#00008B","#B8860B","#8B0000","#B22222","#808080","#FF69B4","#4B0082","#778899","#800000","#0000CD","#BA55D3","#9370DB","#3CB371","#7B68EE","#C71585","#191970","#000080","#808000","#FF4500","#DA70D6","#800080","#FF0000","#4169E1","#8B4513","#2E8B57","#6A5ACD","#708090","#4682B4","#008080","#EE82EE","#DDA0DD"]
chosen=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
questions=""
for i in range(len(chosen)):
    if i==len(chosen)-1:
        questions+="{}".format(chosen[i])
    else:
        if int(chosen[i])==21:
            questions+="\n"
        questions+="{},".format(chosen[i])
init(T,questions)
colo=0
for i in chosen:
    test(day_data_list,i,day_list,numbers,colour[colo],T,3)
    colo+=1

pause()

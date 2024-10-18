name = input()
password = input()
numOfPlanets = 1
life = 0
if name == "Liam Monteith" and password == "1234":
    print("Welcome to live chaos!")
    print("Please use the start command.")
    cmd1 = input()
    if cmd1 == "kill":
        print("Process stopped.")
    while cmd1 != "kill":
        if cmd1 == "start":
            cmd2 = input()
            if cmd2 == "view":
                print(f"You have {numOfPlanets} planets, and {life}% life.")
            if cmd2 == "destroy":
                numOfPlanets -= 1
                if numOfPlanets == 0:
                    cmd1 = "kill"
                    print("There was no life left in the galaxy... YOU DIED")
                else:
                    cmd2 = input()
            if cmd2 == "add":
                numOfPlanets += 1
                print("Planet added.")
            if cmd2 == "big bang":
                life = 100
                print("The dinosaur age has started.")
                age = 1
            if cmd2 == "war":
                print("The war has started...")
                if life >= 50:
                    print("The war has ended... But it took a toll on everyone.")
                    life -= 10
                else:
                    cmd1 = "kill"
                    print("The war killed everything... YOU FAILED")
            if cmd2 == "advance":
                if age == 1:
                    age = 2
                    cmd2 = input()
                if age == 2:
                    age = 3
                    cmd2 = input()
                if age == 3:
                    age = 4
                    cmd2 = input()
                if age == 4:
                    age = 5
                    cmd2 = input()

else:
    print("Password denied.")
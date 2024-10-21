name = input()
password = input()
numOfPlanets = 1
life = 0
age = 0
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
                print(f"You have {numOfPlanets} planets, and {life}% life. The current age is {age}.")
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
                print("Use the advance command to go to a new age!")
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
                    print("Oh look! Some humans!")
                    cmd2 = input()
                if age == 2:
                    age = 3
                    cmd2 = input()
                    print("They learned how to fight?!? This is not how I intended this to go...")
                    print("war command unlocked.")
                if age == 3:
                    age = 4
                    cmd2 = input()
                    print("Wow! It has gotten so modern!")
                    print("You have now unlocked space flight.")
                if age == 4:
                    age = 5
                    cmd2 = input()
                    print("Oh, no... They advanced too far. They found me... We need to eliminate them and start over.")
                    print("Run the asteroid command!")
            if cmd2 == "astoroid":
                age = 6
                print("Lets make something new.")
                cmd3 = input()
else:
    print("Password denied.")
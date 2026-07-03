import random

def montyHallProblem(num_trials=1000000):

    switch_win=0
    stay_win=0

    doors=[0,1,2]

    for _ in range(num_trials):

        choice_door=random.choice(doors)
        car_door=random.choice(doors)

        doors_monty_can_open=[]
        for door in doors:
            if door != choice_door and door!=car_door:
                doors_monty_can_open.append(door)
        
        opened_door=random.choice(doors_monty_can_open)

        for door in doors:
            if door !=choice_door and door != opened_door:
                switch_choice=door

        
        
        if switch_choice==car_door:
            switch_win+=1
        if choice_door==car_door:
            stay_win+=1

    stay_win_pct=(stay_win/num_trials)*100
    switch_win_pct=(switch_win/num_trials)*100

    print(f"Simulation Results over {num_trials:,} trials:")
    print(f"--------------------------------------------")
    print(f"Staying with initial door wins: {stay_win} times ({stay_win_pct:.2f}%)")
    print(f"Switching to the other door wins: {switch_win} times ({switch_win_pct:.2f}%)")

if __name__=="__main__":
    montyHallProblem()



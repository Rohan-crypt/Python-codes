sec_num = 7
guess_count = 0
guess = int(input("Enter the number to guess: "))
while guess_count <=3:
    if guess !=sec_num:
        if guess_count == 2:
            print("try again")
            guess_count+=1
        else:
            guess_count+=1
    else:
        guess == sec_num
        print("you won")
        break
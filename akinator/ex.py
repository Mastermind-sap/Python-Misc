import akinator

aki = akinator.Akinator()

q = aki.start_game()

while aki.progression <= 10:
    a = input(q + "\n\t")
    if a == "b":
        try:
            q = aki.back()
        except akinator.CantGoBackAnyFurther:
            print(e)
            continue
    else:
        try:
            q = aki.answer(a)
        except akinator.InvalidAnswerError as e:
            print(e)
            continue
aki.win()

correct = input(f"It's {aki.first_guess['name']} ({aki.first_guess['description']})! Was I correct?\n{aki.first_guess['absolute_picture_path']}\n\t")
if correct.lower() == "yes" or correct.lower() == "y":
    print("Yay\n")
else:
    print("Oof\n")

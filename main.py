# intros the game asking if you wanna play and how many questions there are, defining them
print('Welcome to the New York Jets Quiz')
answer=input('Are you ready to play ? (yes/no) :')
score=0
total_questions=3
 #these three segments below are the same, asking the question and giving an answer with feedback
if answer.lower()=='yes':
    answer=input('Question 1: What number is Breece Hall ?')
    if answer.lower()=='20':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
 
    answer=input('Question 2: Are the Raiders a good football team? ')
    if answer.lower()=='no':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
    answer=input('Question 3: Who is better, Zach Wilson or Derek Carr?')
    if answer.lower()=='Zach Wilson':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
    
   #im gonna add more questions to this and put an image at the end when the quiz is over

    
    

 #after the three questions this is printed to indicated you are done
print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('Thank you for playing')

# keeps the loop running, im working on making it so you can redo it mmm
running = True


while running:
    
    for event in pygame.event.get():
      if event.type == KEYDOWN:
          if event.key == K_ESCAPE:
                running = False
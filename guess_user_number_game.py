import math

def guess_user_number(lowerlimit, upperlimit, total_guesses = 0):
	"""Uses binary search to find a number that the user thinks of between lowerlimit and upperlimit.
	
	Args:
		upperlimit (int): The upper bound of the range.
		lowerlimit (int): The lower bound of the range.
		total_guesses (int): The number of guesses made so far.
		
	Returns: None"""

	# Calculate and display the number of remaining guesses. 
	remaining_guesses = guesses - total_guesses
	if remaining_guesses == 0:
		print("Hmmmmmmm... I think you cheated... ")
		return
	else:
		print(f'{remaining_guesses} guesses remaining.')

	# Determine the middle number to begin binary search.
	mid = (upperlimit + lowerlimit) // 2

	# Ask user if mid is their number and initialize VALID_RESPONSES constant.	
	useranswer = input(f"Is it {mid}? Enter Y for Yes, L if your number is lower than {mid}, or H if your number is higher than {mid}.  ").lower()
	VALID_RESPONSES = ("y", "l", "h")

	# Increment the total number of guesses.
	total_guesses += 1
	
	# Check if useranswer is in VALID_RESPONSES
	while True:
		if useranswer not in VALID_RESPONSES:
			useranswer = input("Please enter a valid response. (Y/L/H): ")
		else:
			break

	# If user inputs Y then Game is over and the computer wins!
	if useranswer == "y":
		print(f'I win! It only took me {total_guesses} guesses!')

	# If user inputs L then recursively call guess_user_number on lower half of number range.
	elif useranswer == "l":
		guess_user_number(lowerlimit, mid, total_guesses)

	# If user inputs H then recursively call guess_user_number on upper half of number range.
	elif useranswer == "h":
		guess_user_number((mid + 1), upperlimit, total_guesses)




if __name__ == "__main__":
	
	# Start a loop to allow user to play multiple times. 
	while True:

		# Welcome user to the game.
		print("Welcome to the User Number guessing game! As long as you're honest I won't lose!")

		# Ensure valid inputs.
		while True:
			try:
				# Collect user input for lower and upper limits.
				lowerlimit = int(input("Choose your lower limit: "))
				upperlimit = int(input("Choose your upper limit:"))

				if lowerlimit >= upperlimit:
					print("The lower limit must be less than the upper limit")
				else:
					break
			except ValueError:
				print("Please enter valid numeric whole numbers for the limits.")

		# Calculate the number of guesses needed to determine the user's number. 
		guesses = math.ceil(math.log2(upperlimit - lowerlimit))

		# Explain the game.
		print(f"Pick a whole number between your chosen lower limit, {lowerlimit}, and upper limit, {upperlimit}. I will guess your number in only {guesses} guesses. No Cheating!")

		# Begin the game by calling the guess_user_number function.
		guess_user_number(lowerlimit, upperlimit)

		# Ask the user if they want to play again
		play_again = input("Want to play again? (Y/N): ").lower()
		
		# If the users response is anything other than "y", exit the loop and end the program
		if play_again != "y":
			print("Thank you for playing! Good Bye!")
			break
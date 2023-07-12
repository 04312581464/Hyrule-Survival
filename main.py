print("\033[1m" + "\033[4m" + "Welcome to Hyrule Survival - A Zelda Decisions Game" + "\033[0m")
print("\nRULES: You will be given a series of tasks to complete to save Princess Zelda and restore peace to Hyrule. You should also note this as well: Ganon's darkness, fierce creatures, and harsh elements are always present. One wrong decision can kill you. The right decisions help you get closer to rescuing Zelda. You will be given an option to type in a number, so enter your number and click the enter key. Be careful and good luck!")

username = input("\nEnter your username: ").strip()
counter = 0

print("\033[0;32m" + "\nWelcome,", username + ", to Hyrule, a vast and wild land. All you know is that you have awakened in a dark, empty room, and you are starving and thirsty. You go outside, only to find a pig-like creature (a Bokoblin) patrolling the area. What do you do?" + "\033[0m")

choice1 = input("""\nDo you:
	1. Pick up a tree branch and attack him.
	2. Sneak past him to a safe spot nearby.\n""").strip()
# Lose choice 1 - Boko kills you
if choice1 == "1":
	print("\033[0;31m" + "\nBad choice. The tree branch broke in a matter of seconds and the Bokoblin defeated you." + "\033[0m")
	print("\033[1m" + "\nYou survived", counter, "out of 9 stages. You'll do better next time!" + "\033[0m")
# Win choice 1 - move on to choosing food
elif choice1 == "2":
	print("\033[0;32m" + "\nGood choice! You successfully snuck past the Bokoblin and hid behind a wall of boulders. If you had chosen to attack him, he would have easily overpowered you. \n\nStill hungry and thirsty, you notice an oddly yellowish pond of water and the flesh of a deer, with flies swarming around it, in front of you. What do you do?" + "\033[0m")
	counter+=1
	choice2 = input("""\nDo you:
	1. Drink the yellowish water and go hunt for cleaner food.
	2. Eat the deer and go search for cleaner water.\n""").strip()
	# Win choice 2 - move on to finding shelter
	if choice2 == "1":
		print("\033[0;32m" + "\nGood choice! It turns out that the water was colored by yellow leaves falling down from an overhanging tree, and therefore harmless. The deer, on the other hand, was infested with all sorts of deadly bacteria and maggots. \n\nYou soon notice that it's getting dark and cold, and you need to find shelter before more monsters emerge. What do you do?" + "\033[0m")
		counter+=1
		choice3 = input("""\nDo you:
	1. Make a campfire in a nearby cave and hope that it doesn't attract unwanted attention.
	2. Don't make a campfire to err on the safe side, and shelter behind some trees.\n""").strip()
		# Win choice 3 - move on to reaching the river town
		if choice3 == "1":
			print("\033[0;32m" + "\nGood choice! The campfire actually scared the monsters away, and you stayed nice and toasty throughout the night. If you had chosen differently, you would have attracted a lot of unwanted attention. \n\nWith more energy now, you decided to look for a vantage point where you can better see your surroundings. You have two options: a tall tree in a jungle with strange noises coming from it, and a mountain cliff that is very high up. The forest is very close whereas the mountain is very far away, and you'll probably run out of energy on the climb up. What do you do?" + "\033[0m")
			counter+=1
			choice4 = input("""\nDo you:
	1. Go to the forest and try to stay away from the strange noises.
	2. Climb up the mountain and hope you have enough energy.\n""").strip()
			# Lose choice 4 - get eaten
			if choice4 == "1":
				print("\033[0;31m" + "\nBad choice. It turns out some of Ganon's Gloom was making the sounds. A creepy hand shot out of a mud puddle on the ground and grabbed you, strangling you to death." + "\033[0m")
				print("\033[1m" + "\nYou survived", counter, "out of 9 stages. Good job!" + "\033[0m")
			# Win choice 4 - climb mountain
			elif choice4 == "2":
				print("\033[0;32m" + "\nGood choice! From this view, you can now see that Ganon's fatal Gloom monsters were making the strange noises -- an encounter with them would have resulted in a quick death. \n\nYou are very hungry and exhausted from climbing the mountain, so you decide to hunt for food. But where do you look? On the other side of the mountain, there are meaty creatures like wolves and foxes. Below you, there are fish by an empty beach. Choose wisely before you starve to death." + "\033[0m")
				counter+=1
				choice5 = input("""\nDo you:
	1. Hunt on the mountain and risk being attacked by wild animals.
	2. Hunt in the sea and risk being pulled in by the current.\n""").strip()
				# Lose choice 5 - die to animals on the mountain
				if choice5 == "1":
					print("\033[0;31m" + "\nBad choice. You got one piece of wolf meat, but not before it howled and called its pack to come after you. They killed you easily." + "\033[0m")
					print("\033[1m" + "\nYou survived", counter, "out of 9 stages. Good work!" + "\033[0m")
				# Win choice 5 - hunt in the sea
				elif choice5 == "2":
					print("\033[0;32m" + "\nGood choice! You avoided a dangerous attack, and luckily, the current was not strong enough to sweep you away. You caught a few fish, and while you were hunting, you saw a town on the other side of the sea. You are sure it is full of supplies and places to rest. How will you reach it?" + "\033[0m")
					counter+=1
					choice6 = input("""\nDo you:
	1. Build a makeshift boat out of logs and a stray sail, though it is not very sturdy.
 	2. Since there are rocks scattered across the sea, swim across and stop at each rock to rest.\n""").strip()
					# Win choice 6 - reach town
					if choice6 == "1":
						print("\033[0;32m" + "\nGood choice! The current got stronger in the middle of the sea, but your boat was strong enough three-quarters of the way across. With your current energy, you could easily swim the rest of the way across As you had expected, the town was full of supplies and had an inn where you could safely rest for the night. You even found a sword and shield lying around, and picked them up... just in case. \n\nThe next morning, the townspeople were running around in chaos and told you that they had just seen Ganon attempting to sacrifice Zelda at Hyrule Castle. However, the castle is fully surrounded with Gloom. This could be your last chance to save Zelda -- what do you do?" + "\033[0m")
						counter+=1
						choice7 = input("""\nDo you:
	1. Stay here in the town where it's safe and wait until you get another opportunity to save Zelda.
 	2. Stock up on supplies and go to Hyrule Castle at once.\n""").strip()
						# Lose choice 7 - don't go to Hyrule Castle
						if choice7 == "1":
							print("\033[0;31m" + "\nBad choice. Soon enough, with Zelda as the sacrifice, Ganon increased his power to the maximum and destroyed Hyrule." + "\033[0m")
							print("\033[1m" + "\nYou survived", counter, "out of 9 stages. Good work!" + "\033[0m")
						# Win choice 7  - go to Hyrule Castle
						elif choice7 == "2":
							print("\033[0;32m" + "\nGood choice! Hurrying to Hyrule Castle with your full energy, you were able to avoid all of the Gloom. When you went inside, you encountered Ganon in the castle's sanctum!" + "\033[0m")
							counter+=1
							print("\n----------------------------------------")
							print("\033[1;31m" + "Ganon, The Demon King" + "\033[0m")
							print("Ha ha ha, you came all this way to save your beloved princess! How pathetic. I am only one step away from finally overtaking Hyrule and gaining power for myself! Well, since you're so close to the end of your story, I shall let your Zelda go and fight with you.")
							print("----------------------------------------")
							print("\033[0;32m" + "\nAfter letting Zelda free, the two of you boldly challenge him head on. Ganon cackles again and creates five gloom projectiles in front of him, shooting them at you and Zelda at extremely high speeds. Quick -- what will you do to defeat the Demon King?" + "\033[0m")
							choice8 = input("""\nDo you:
	1. Jump above the gloom projectiles and attack Ganon while he's busy.
 	2. Use your shield to deflect the gloom projectiles until the barrage ends.\n""").strip()
							# Win choice 8 - weaken Ganon
							if choice8 == "1":
								print("\033[0;32m" + "\nGood choice! Rather than risking your shield breaking, you shot some TNT arrows that you got from the town at Ganon's weak point. He is almost out of health; what will you do to strike the fatal blow?" + "\033[0m")
								counter+=1
								choice9 = input("""\nDo you:
	1. Tell Zelda to seal him away right now.
 	2. Without delay, plunge your sword into Ganon's chest.\n""").strip()
								# Lose choice 9 - Zelda can't seal Ganon
								if choice9 == "1":
									print("\033[0;31m" + "\nBad choice. While Ganon lay helpless on the floor, Zelda shouted back to you that she can only use her sealing powers when Ganon is fully dead. By the time she finished speaking, Ganon healed himself and stood up again. He defeated both of you now that you were close enough to him, and he successfully took over Hyrule." + "\033[0m")
									print("\033[1m" + "\nYou survived", counter, "out of 9 stages. Good work!" + "\033[0m")
								# Win choice 9 - stab Ganon
								elif choice9 == "2":
									print("\033[0;32m" + "\nGood choice! Your heroism and courage successfully saved Hyrule, and now that Ganon was fully defeated, Zelda stepped forward to seal him into the Sacred Realm for eternity. The Gloom disappears from Hyrule, and Zelda stands before you, glowing with golden light..." + "\033[0m")
									counter+=1
									print("\n----------------------------------------")
									print("\u001b[33;1m" + "Zelda, Princess of Hyrule" + "\033[0m")
									print(username + "! You are a true hero... You saved all of Hyrule from the Demon King! I can't imagine everything you've been through on your journey, but I thank you from the bottom of my heart for saving me and my people. And though you might not have all of your memories back yet, just know this: Courage need not be remembered... For it is never forgotten.")
									print("----------------------------------------")
									print("\033[1m" + "\n== THE END ==" + "\033[0m")
									print("\nTHANK YOU so much for all of your support!!! It means so much to me 🥰 Please leave a like and tell me what you think in the comments below!")
									print("""\nCREDITS:
	- Code by me
 	- Game idea by me (inspired by KoalaKid29's 'You Vs Wild'
	- Digital art cover image by me""")
									
							# Lose choice 8 - shield breaks and you die to Ganon
							elif choice8 == "2":
								print("\033[0;31m" + "\nBad choice. Your shield broke after taking a few hits, leaving you and Zelda exposed. You both died from the Gloom's poisoning effects, and Ganon took over Hyrule." + "\033[0m")
								print("\033[1m" + "\nYou survived", counter, "out of 9 stages. Good work!" + "\033[0m")
					# Lose choice 6 - drown in the current
					elif choice6 == "2":
						print("\033[0;31m" + "\nBad choice. You did get a third of the way across, but the current got stronger all of a sudden and pulled you away from the next rock. You drowned." + "\033[0m")
						print("\033[1m" + "\nYou survived", counter, "out of 9 stages. Great work!" + "\033[0m")
		# Lose choice 3 - bad shelter
		elif choice3 == "2":
			print("\033[0;31m" + "\nBad choice. The monsters soon found you, and you were too cold to protect yourself when they attacked." + "\033[0m")
			print("\033[1m" + "\nYou survived", counter, "out of 9 stages. Good work!" + "\033[0m")
	# Lose choice 2 - eat infected deer
	elif choice2 == "2":
		print("\033[0;31m" + "\nBad choice. You soon caught a disease from eating the infected deer and died." + "\033[0m")
		print("\033[1m" + "\nYou survived", counter, "out of 9 stages. Not bad!" + "\033[0m")

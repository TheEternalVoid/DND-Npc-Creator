import random

races = ["Dwarf", "Human"]

hair_styles = ["Long", "Short"]

hair_colors = ["red", "blue"]

occupations = ["Adventurer", "Villian"]

alignments = ["Lawful Good", "Chaotic Evil"]

def create_npc():
	generated_npc = {}
	#pulled from data online average height is 30 inches - the average of dnd
	#modifiers for height which in this case would be 16 inches
	one_year_old_average_height_in_inches = 16
	one_year_old_average_weight_in_lbs = 21
	d20 = random.randint(1,20)
	d8 = random.randint(1,8)

	generated_npc["race"] = random.choice(races)
	generated_npc["alignment"] = random.choice(alignments)
	generated_npc["hair_style"] = random.choice(hair_styles)
	generated_npc["hair_color"] = random.choice(hair_colors)
	generated_npc["occupation"] = random.choice(occupations)


	#different races have different life spans
	if generated_npc["race"] == "Human":
		generated_npc["age_in_years"] = random.randint(1,100)
		#finding the base height based on generated age - 1 (for the difference
		# between age and 1 yearold then multiplying by average increase in 
		# height gain per years which is 2 + 6 as a buffer for unused decimals)
		#if age is > 20 just use 20 since people don't often grow beyond then
		if generated_npc["age_in_years"] > 20:
			base_height = one_year_old_average_height_in_inches + ((20 - 1) * 2 + 4)
		else:
			base_height = one_year_old_average_height_in_inches + ((generated_npc["age_in_years"] - 1) * 2 + 4)
		
		#height = base height + dnd modifier in this case 2d10 or 1d20
		generated_npc["height_in_inches"] = base_height + d20
		
		if generated_npc["age_in_years"] == 1:
			generated_npc["weight_in_lbs"] = one_year_old_average_weight_in_lbs
		elif generated_npc["age_in_years"] <= 8:
			base_weight = one_year_old_average_weight_in_lbs + (5 * (generated_npc["age_in_years"] - 1))
			max_weight =  base_weight * 2
		elif generated_npc["age_in_years"] <= 10:
			base_weight = 56 + (7 * (generated_npc["age_in_years"] - 1))
			max_weight = base_weight * 3
		else:
			base_weight = 110
			max_weight = 325
		generated_npc["weight_in_lbs"] = random.randint(base_weight, max_weight)

	elif generated_npc["race"] == "Dwarf":
		generated_npc["age_in_years"] = random.choice(range(1,501))
		generated_npc["height_in_inches"] = random.choice(range(1,56))
		generated_npc["weight_in_lbs"] = random.choice(range(1,212))


	name = input("Please enter a name for this character: ")

	generated_npc["name"] = name

	return generated_npc



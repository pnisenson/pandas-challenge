# from internet research, lambda functions to count the math and reading scores by row. Wasn't able to apply to both simultaenously
g = sd_comp.groupby("school_name")
passmsch = g.apply(lambda x: x[x["math_score"] >= 70]["math_score"].count())
passrsch = g.apply(lambda x: x[x["reading_score"] >= 70]["reading_score"].count())


## Instead of zipping the mathflag and readflag, can we do the following?:
	#immediately after those flage, create the new table and Pass Math and Pass Reading Columns
	#do overall_table["Pass_Both"]=overall_table["Pass_Math"]+overall_table["Pass_Reading"]
	## issue - adds to 2,1,0. 


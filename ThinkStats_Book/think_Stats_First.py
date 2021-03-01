'''
think_Stats_First.py 

Aim : Exercise 1.3 


Keys in Pregnancy Object : 
['agepreg', 'babysex', 'birthord', 'birthwgt_lb', 'birthwgt_oz', 'caseid', 'finalwgt', 'nbrnaliv', 'outcome', 'prglength', 'totalwgt_oz']

'''

import thinkstats_survey as survey
from collections import Counter 
import pprint
  
def main():
	table = survey.Pregnancies()
	table.ReadRecords()
	print ('Number of pregnancies', len(table.records))
	outcome_dict={}
	for pregnancy_entry in table.records:
		if not outcome_dict.get(pregnancy_entry.outcome,None):
			outcome_dict[pregnancy_entry.outcome]=1
		else :
			outcome_dict[pregnancy_entry.outcome]+=1

	print("The Distribution of Outcome of Pregnancy is as follows")
	pp=pprint.PrettyPrinter(indent=4)
	pp.pprint(outcome_dict)



	## Creating two groups , first_born and others
	first_born=[]
	other_ord=[]
	na_ord=[]

	for pregnancy_entry in table.records:
		if pregnancy_entry.outcome!=1:
			# Excluding Non-Live Birth Entries
			continue

		if pregnancy_entry.birthord==1:
			first_born.append(pregnancy_entry)
		elif pregnancy_entry.birthord!="NA" : 
			# Adding Check to exclude BirthOrd set to NA.
			other_ord.append(pregnancy_entry)
		else:
			na_ord.append(pregnancy_entry)

	# Get Average Preg Length for first_born and other_ord

	first_born_pl=[pregnancy_entry.prglength*7 for pregnancy_entry in first_born]
	other_ord_pl=[pregnancy_entry.prglength*7 for pregnancy_entry in other_ord]



	first_born_average_pl=sum(first_born_pl)/len(first_born_pl)
	other_ord_average_pl=sum(other_ord_pl)/len(other_ord_pl)

	print ("Number of First born babies  : ", len(first_born))
	print ("Number of Non First born babies : ", len(other_ord))
	print ("The Average Preg Length in Days for First Borns are : " ,first_born_average_pl)

	print ("The Average Preg Length in Days for Non First Borns are : ", other_ord_average_pl)



if __name__ == '__main__':
    main()
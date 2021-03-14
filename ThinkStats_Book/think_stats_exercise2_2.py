import thinkstats_survey as survey
import think_Stats_First as first

def mean(number_list):
    return float(sum(number_list)/len(number_list))

def variance(number_list):
    mean_of_list=mean(number_list)
    return mean(([(x-mean_of_list)**2 for x in number_list]))

def stddev(number_list):
    variance_of_list=variance(number_list)
    return variance_of_list**0.5

def main():
    table = survey.Pregnancies()
    table.ReadRecords()
    print ('Number of pregnancies', len(table.records))
    first_born_prglength_list=[entry.prglength*7 for entry in table.records  if entry.birthord==1]
    other_born_prglength_list=[entry.prglength*7 for entry in table.records  if entry.birthord!=1]
    # Calculate Standard Deviation for first_born and non_firstborn
    # Standard Deviation is squareroot of (sum of (x-mean))/n
    first_born_prglength_mean=mean(first_born_prglength_list)
    other_born_prglength_mean=mean(other_born_prglength_list)
    print("Mean Preg length in days for first born :" ,first_born_prglength_mean)
    print("Mean Preg length in days for other born :",other_born_prglength_mean)

    first_born_prglength_var=variance(first_born_prglength_list)
    other_born_prglength_var=variance(other_born_prglength_list)
    print("variance of Preg length in days for first born :",first_born_prglength_var)
    print("variance of Preg length in days for other born :",other_born_prglength_var)

    print("Std Dev of Preg length in days for first born :",stddev(first_born_prglength_list))
    print("Std Dev of Preg length in days for other born :",stddev(other_born_prglength_list))

if __name__ == '__main__':
    main()

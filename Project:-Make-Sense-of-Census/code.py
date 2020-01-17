# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
#np.loadtxt('subset_1000.csv')
data= np.genfromtxt(path,delimiter=',',skip_header=1)
print('\n Data: \n', data)

print("\n Type of data:\n", type(data))
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
#data=np.append(data, new_record,axis=0)
census= np.concatenate((new_record,data),axis=0)
print(census)


# --------------
#Code starts here
age= census[:,0].astype(np.int16)
print(age)

max_age= age.max()
print('max_age',max_age)

min_age= age.min()
print('min_age',min_age)
age_mean= age.mean()
print('age_mean',age_mean)

age_std= age.std()
print(age_std)


# --------------
#Code starts here




race_0= census[census[:,2]==0]
race_1= census[census[:,2]==1]
race_2= census[census[:,2]==2]

race_3= census[census[:,2]==3]
race_4= census[census[:,2]==4]

len_0= len(race_0)
print(len_0)
len_1= len(race_1)
print(len_1)
len_2= len(race_2)
print('len_2',len_2)

len_3= len(race_3)
print(len_3)

len_4= len(race_4)
print(len_4)

print(min(len_0,len_1,len_2, len_3,len_4))


minority_race= 3
print(minority_race)





# --------------
#Code starts here
senior_citizens=census[census[:,0]>60]


working_hours_sum= senior_citizens[:,6].sum(axis=0)
senior_citizens_len= len(senior_citizens)
print(senior_citizens_len)

avg_working_hours= np.divide(working_hours_sum,senior_citizens_len)
print(avg_working_hours)


# --------------
#Code starts here
high = census[census[:,1]>10]

low= census[census[:,1]<=10]

income= census[:,7]
mean_inc= income.mean()
print(mean_inc)

avg_pay_high =high[:,7].mean()
print('avg_pay_high',avg_pay_high)

avg_pay_low= low[:,7].mean()
print('avg_pay_low',avg_pay_low)

compare= np.array_equal(avg_pay_high,avg_pay_low)
print('Comparison',compare)



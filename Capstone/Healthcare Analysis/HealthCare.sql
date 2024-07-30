# Create Database:
create database healthcare;

#Use the same database:
use healthcare;

# Create and import hospitalisation details table:
create table hospitalisation_details
(
customer_ID varchar(100) PRIMARY KEY,
year int NOT null,
month varchar(10) NOT null,
date int not null,
children int not null,
charges float not null,
hospital_tier varchar(10) not null,
city_tier varchar(10) not null,
state_ID varchar(10) not null
);

Select * from hospitalisation_details;

# Delete data with trivial values such as '?' from the table
Select * from hospitalisation_details Where customer_ID = '?';
delete from hospitalisation_details Where customer_ID = '?';

Select * from hospitalisation_details Where year = '?';

Select * from hospitalisation_details Where month = '?';
delete from hospitalisation_details Where month = '?';

Select * from hospitalisation_details Where date = '?';

Select * from hospitalisation_details Where children = '?';

Select * from hospitalisation_details Where charges = '?';

Select * from hospitalisation_details Where hospital_tier = '?';
delete from hospitalisation_details Where hospital_tier = '?';

Select * from hospitalisation_details Where city_tier = '?';

Select * from hospitalisation_details Where state_ID = '?';
delete from hospitalisation_details Where state_ID = '?';

# Create and Import Medical Examinations table:
create table Medical_Examinations
(
Customer_ID varchar(100) PRIMARY KEY,
BMI float Not null,
HBA1C float Not null,
Heart_Issues varchar(10) not null,
Any_Transplants varchar(10) not null,
Cancer_history varchar(10) not null,
NumberOfMajorSurgeries varchar(50) not null,
Smoker varchar(10) not null
);

Select * from Medical_Examinations;

# Delete data with trivial values such as '?' from the table
Select * from Medical_Examinations Where customer_ID = '?';

Select * from Medical_Examinations Where customer_ID = '?';
Select * from Medical_Examinations Where BMI = '?';

Select * from Medical_Examinations Where HBA1C = '?';

Select * from Medical_Examinations Where Heart_Issues = '?';

Select * from Medical_Examinations Where `Any_Transplants` = '?';

Select * from Medical_Examinations Where `Cancer_history` = '?';

Select * from Medical_Examinations Where NumberOfMajorSurgeries = '?';

Select * from Medical_Examinations Where smoker = '?';
delete from Medical_Examinations Where smoker = '?';


#1 To gain a comprehensive understanding of the factors influencing hospitalization costs
	#a. Merge the two tables by first identifying the columns in the data tables that will help you in merging
	#b. In both tables, add a Primary Key constraint for these columns
select * from hospitalisation_details hd join Medical_Examinations me on hd.customer_ID = me.customer_ID;

#2 Retrieve information about people who are diabetic and have heart problems with their average age, 
   -- the average number of dependent children, average BMI, and average hospitalization costs.
Select 
    round(avg(timestampdiff(year, str_to_date(concat(hd.year, '-', 
        case hd.month
            When 'Jun' then '06'
            When 'Jul' then '07'
            When 'Aug' then '08'
            When 'Sep' then '09'
            When 'Oct' then '10'
            When 'Nov' then '11'
            When 'Dec' then '12'
        end, '-', LPAD(hd.date, 2, '0')), '%Y-%m-%d'), CURDATE())),2) as average_age,
    round(avg(hd.children)) as average_children,
    round(avg(me.BMI),2) as average_BMI,
    round(avg(hd.charges), 3)as average_hospitalization_costs
from hospitalisation_details hd join Medical_Examinations me on hd.customer_ID = me.customer_ID WHERE me.HBA1C >= 8 AND me.Heart_Issues = 'Yes';

    
# 3. Find the average hospitalization cost for each hospital tier and each city level
Select hospital_tier, round(avg(charges), 3) as average_hospitalization_costs from hospitalisation_details group by hospital_tier;
Select city_tier, round(avg(charges), 3) as average_hospitalization_costs from hospitalisation_details group by city_tier;

    
# 4. Determine the number of people who have had major surgery with a history of cancer
Select count(customer_ID) from Medical_Examinations where (Cancer_history = 'yes' and NumberOfMajorSurgeries != 'No major surgery');


# 5. Determine the number of tier-1 hospitals in each state
Select state_ID, count(hospital_tier) from hospitalisation_details where hospital_tier = 'tier - 1' group by (state_ID);
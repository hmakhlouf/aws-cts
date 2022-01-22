create table if not exists
churn_model (RowNumber int, CustomerId string, Surname string, CreditScore int, Geography string, Gender string, Age int, Tenure int, Balance float, NumOfProducts int, HasCrCard int, IsActiveMember int, EstimatedSalary float, Exited int)                        
row format delimited 
fields terminated by ',' 
lines terminated by '\n' 
stored as textfile;

load data inpath '${INPUT}' into table churn_model;

create table if not exists churn_model_q1 as
select Geography, AVG(CreditScore) from churn_model where Exited = 1 group by Geography;

insert overwrite directory '${OUTPUT}churn_model_output/' 
row format delimited fields terminated by ','  
select Geography, AVG(CreditScore) from churn_model where Exited = 1 group by Geography;
# Learned Results Summary - Dataset g

# Demonstration: German
| | Feature | Type | Value | Mutable |
| --- | --- | --- | :---: | :---: |
| 1 | Age | Integer | [19, 75] | False |
| 2 | LoanDuration | Integer | [4, 72] | True |
| 3 | LoanAmount | Integer | [250, 18424] | True |
| 4 | LoanRateAsPercentOfIncome | Integer | [1, 4] | True |
| 5 | YearsAtCurrentHome | Integer | [1, 4] | True |
| 6 | NumberOfOtherLoansAtBank | Integer | [1, 4] | True |
| 7 | MultipleLiableIndividuals | Bool | {False: 0, True: 1} | True |
| 8 | HasTelephone | Bool | {False: 0, True: 1} | True |
| 9 | MissedPayments | Bool | {False: 0, True: 1} | True |
| 10 | NoCurrentLoan | Bool | {False: 0, True: 1} | True |
| 11 | CriticalAccountOrLoansElsewhere | Bool | {False: 0, True: 1} | True |
| 12 | OtherLoansAtBank | Bool | {False: 0, True: 1} | True |
| 13 | HasCoapplicant | Bool | {False: 0, True: 1} | True |
| 14 | HasGuarantor | Bool | {False: 0, True: 1} | True |
| 15 | OwnsHouse | Bool | {False: 0, True: 1} | True |
| 16 | RentsHouse | Bool | {False: 0, True: 1} | True |
| 17 | Unemployed | Bool | {False: 0, True: 1} | True |
| 18 | JobClassIsSkilled | Bool | {False: 0, True: 1} | True |
| 19 | ForeignWorker | Bool | {False: 0, True: 1} | False |
| 20 | Single | Bool | {False: 0, True: 1} | False |
| 21 | Gender | Bool | {False: 0, True: 1} | False |
| 22 | PurposeOfLoan | Category | Business <br> Education <br> Electronics <br> Furniture <br> HomeAppliances <br> NewCar <br> Other <br> Repairs <br> Retraining <br> UsedCar | True |
| 23 | YearsAtCurrentJob | Category | <1 <br> >=4 <br> 1<=_<4 | True |
| 24 | CheckingAccountBalance | Category | <0 <br> 0<=_<200 <br> >=200 | True |
| 25 | SavingsAccountBalance | Category | <100 <br> 100<=_<500 <br> >=500 | True |

## Learned Clustering Results
| | HowToChange |
| --- | --- |
| Action 1 | LoanDuration: -32 <br>LoanAmount: -11302 <br>(Acc: 88.9% / Cost: 0.483) |
| Action 2 | LoanDuration: -8 <br>LoanAmount: -4496 <br>(Acc: 50.0% / Cost: 0.461) |
| Action 3 | LoanDuration: -2 <br>LoanAmount: -26 <br>(Acc: 9.8% / Cost: 0.0553) |
| Action 4 | LoanAmount: -2299 <br>HasGuarantor: False -> True <br> (Acc: 100.0% / Cost: 0.0568) |

| Feature | Cluster 1 | Cluster 2 | Cluster 3 | Cluster 4 |
| --- | ---: | ---: | ---: | ---: |
| Age | 39.11 | 36.36 | 31.87 | 33.33 |
| LoanDuration | 52.67 | 37.64 | 23.45 | 41.42 |
| LoanAmount | 15393.00 | 6709.86 | 2099.70 | 10904.92 |
| LoanRateAsPercentOfIncome | 2.33 | 2.89 | 3.61 | 1.67 |
| YearsAtCurrentHome | 3.00 | 3.07 | 2.94 | 2.33 |
| NumberOfOtherLoansAtBank | 1.22 | 1.43 | 1.27 | 1.42 |
| MultipleLiableIndividuals:True | -0.0% | 21.4% | 17.1% | 16.7% |
| HasTelephone:True | 88.9% | 46.4% | 19.5% | 75.0% |
| MissedPayments:True | 88.9% | 82.1% | 97.6% | 75.0% |
| NoCurrentLoan:True | 11.1% | 21.4% | 19.5% | 0.0% |
| CriticalAccountOrLoansElsewhere:True | 11.1% | 17.9% | 1.2% | 8.3% |
| OtherLoansAtBank:True | 33.3% | 21.4% | 20.7% | 25.0% |
| HasCoapplicant:True | 11.1% | 7.1% | 9.8% | 16.7% |
| HasGuarantor:True | -0.0% | 7.1% | 1.2% | 0.0% |
| OwnsHouse:True | 66.7% | 32.1% | 43.9% | 66.7% |
| RentsHouse:True | 11.1% | 42.9% | 42.7% | 0.0% |
| Unemployed:True | 11.1% | 14.3% | 2.4% | 8.3% |
| JobClassIsSkilled:True | 100.0% | 85.7% | 67.1% | 83.3% |
| PurposeOfLoan:Business | 33.3% | 25.0% | 9.8% | 8.3% |
| PurposeOfLoan:Education | 0.0% | 14.3% | 12.2% | 8.3% |
| PurposeOfLoan:Electronics | 11.1% | 7.1% | 11.0% | 25.0% |
| PurposeOfLoan:Furniture | 0.0% | 10.7% | 19.5% | 8.3% |
| PurposeOfLoan:HomeAppliances | -0.0% | 0.0% | 3.7% | 0.0% |
| PurposeOfLoan:NewCar | 22.2% | 39.3% | 40.2% | 33.3% |
| PurposeOfLoan:Other | 33.3% | -0.0% | -0.0% | 8.3% |
| PurposeOfLoan:Repairs | 0.0% | -0.0% | 3.7% | 8.3% |
| PurposeOfLoan:Retraining | 0.0% | 0.0% | 0.0% | 0.0% |
| PurposeOfLoan:UsedCar | 0.0% | 3.6% | -0.0% | 0.0% |
| YearsAtCurrentJob:<1 | 11.1% | 28.6% | 42.7% | 25.0% |
| YearsAtCurrentJob:>=4 | 44.4% | 28.6% | 22.0% | 25.0% |
| YearsAtCurrentJob:1<=_<4 | 44.4% | 42.9% | 35.4% | 50.0% |
| CheckingAccountBalance:<0 | 33.3% | 57.1% | 62.2% | 58.3% |
| CheckingAccountBalance:0<=_<200 | 66.7% | 42.9% | 35.4% | 41.7% |
| CheckingAccountBalance:>=200 | 0.0% | -0.0% | 2.4% | 0.0% |
| SavingsAccountBalance:<100 | 88.9% | 92.9% | 85.4% | 66.7% |
| SavingsAccountBalance:100<=_<500 | 11.1% | 7.1% | 13.4% | 16.7% |
| SavingsAccountBalance:>=500 | -0.0% | 0.0% | 1.2% | 16.7% |
| ForeignWorker:True | 11.1% | -0.0% | -0.0% | 0.0% |
| Single:True | 66.7% | 60.7% | 35.4% | 58.3% |
| Gender:True | 77.8% | 71.4% | 48.8% | 75.0% |

## Learned AReS Results
| | Rule | Action |
| :---: | --- | --- |
| Recourse <br> rule 1 <br> (probability: 93.1%) | If 'CriticalAccountOrLoansElsewhere=False' <br> AND 'ForeignWorker=False' | CriticalAccountOrLoansElsewhere=True <br> AND ForeignWorker=False |
| Recourse <br> rule 2 <br> (probability: 6.1%) | If 'MultipleLiableIndividuals=False' <br> AND 'MissedPayments=True' <br> AND 'CriticalAccountOrLoansElsewhere=True' <br> AND 'HasGuarantor=False' | MissedPayments=True <br> AND HasGuarantor=True |
| Recourse <br> rule 3 <br> (probability: 8.4%) | If '32<=Age<35' <br> AND 'HasCoapplicant=False' <br> AND 'HasGuarantor=False' <br> AND 'OwnsHouse=True' | HasCoapplicant=False <br> AND HasGuarantor=True |
| Recourse <br> rule 4 <br> (probability: 1.5%) | If '18<=LoanDuration<24' <br> AND 'NoCurrentLoan=False' <br> AND 'JobClassIsSkilled=True' <br> AND 'Single=True' | 12<=LoanDuration<18 <br> AND NoCurrentLoan=False <br> AND Single=True |

## Learned CET Results
```
- If PurposeOfLoan:NewCar:
	* Action [GoodCustomer: Bad -> Good] (50/50 = 100.0% / MeanCost = 0.056):
		* HasGuarantor: False -> True
		* PurposeOfLoan: "NewCar" -> "Retraining"
- Else:
	- If HasGuarantor:
		* Action [GoodCustomer: Bad -> Good] (3/3 = 100.0% / MeanCost = 0.048):
			* NoCurrentLoan: True -> False
	- Else:
		- If CheckingAccountBalance:0<=_<200:
			* Action [GoodCustomer: Bad -> Good] (24/32 = 75.0% / MeanCost = 0.064):
				* HasGuarantor: False -> True
				* CheckingAccountBalance: "0<=_<200" -> ">=200"
		- Else:
			* Action [GoodCustomer: Bad -> Good] (39/46 = 84.8% / MeanCost = 0.0633):
				* LoanDuration: -2
				* HasGuarantor: False -> True
```

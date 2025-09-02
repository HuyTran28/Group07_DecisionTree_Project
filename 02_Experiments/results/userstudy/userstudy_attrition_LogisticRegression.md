# Learned Results Summary - Dataset i

# Demonstration: EmployeeAttrition
| | Feature | Type | Value | Mutable |
| --- | --- | --- | :---: | :---: |
| 1 | Age | Integer | [18, 60] | False |
| 2 | BusinessTravel | Integer | [0, 2] | True |
| 3 | DistanceFromHome | Integer | [1, 29] | False |
| 4 | Education | Integer | [1, 5] | False |
| 5 | EnvironmentSatisfaction | Integer | [1, 4] | True |
| 6 | Gender | Bool | {False: 0, True: 1} | False |
| 7 | JobInvolvement | Integer | [1, 4] | True |
| 8 | JobLevel | Integer | [1, 5] | True |
| 9 | JobSatisfaction | Integer | [1, 4] | True |
| 10 | MonthlyIncome | Integer | [1009, 19999] | True |
| 11 | NumCompaniesWorked | Integer | [0, 9] | False |
| 12 | OverTime | Bool | {False: 0, True: 1} | True |
| 13 | PercentSalaryHike | Integer | [11, 25] | True |
| 14 | OutstandingPerformanceRating | Bool | {False: 0, True: 1} | True |
| 15 | RelationshipSatisfaction | Integer | [1, 4] | True |
| 16 | StockOptionLevel | Integer | [0, 3] | True |
| 17 | TotalWorkingYears | Integer | [0, 40] | True |
| 18 | TrainingTimesLastYear | Integer | [0, 6] | True |
| 19 | WorkLifeBalance | Integer | [1, 4] | True |
| 20 | YearsAtCompany | Integer | [0, 40] | True |
| 21 | YearsInCurrentRole | Integer | [0, 18] | True |
| 22 | YearsSinceLastPromotion | Integer | [0, 15] | True |
| 23 | YearsWithCurrManager | Integer | [0, 17] | True |
| 24 | Department | Category | HumanResources <br> ResearchAndDevelopment <br> Sales | True |
| 25 | EducationField | Category | HumanResources <br> LifeSciences <br> Marketing <br> Medical <br> Other <br> TechnicalDegree | False |
| 26 | JobRole | Category | HealthcareRepresentative <br> HumanResources <br> LaboratoryTechnician <br> Manager <br> ManufacturingDirector <br> ResearchDirector <br> ResearchScientist <br> SalesExecutive <br> SalesRepresentative | True |
| 27 | MaritalStatus | Category | Divorced <br> Married <br> Single | False |

## Learned Clustering Results
| | HowToChange |
| --- | --- |
| Action 1 | MonthlyIncome: +11317 <br>YearsInCurrentRole: +5 <br>(Acc: 100.0% / Cost: 0.455) |
| Action 2 | MonthlyIncome: +9390 <br>YearsWithCurrManager: +3 <br>(Acc: 100.0% / Cost: 0.272) |
| Action 3 | YearsInCurrentRole: +10 <br>YearsWithCurrManager: +9 <br>(Acc: 98.1% / Cost: 0.707) |
| Action 4 | MonthlyIncome: +3699 <br>TotalWorkingYears: +9 <br>(Acc: 100.0% / Cost: 0.0603) |

| Feature | Cluster 1 | Cluster 2 | Cluster 3 | Cluster 4 |
| --- | ---: | ---: | ---: | ---: |
| Age | 36.15 | 36.43 | 28.91 | 51.00 |
| BusinessTravel | 1.41 | 1.00 | 1.43 | 1.50 |
| DistanceFromHome | 12.85 | 10.14 | 10.42 | 11.00 |
| Education | 3.11 | 3.43 | 2.77 | 3.50 |
| EnvironmentSatisfaction | 2.19 | 2.29 | 2.57 | 2.00 |
| Gender:True | 44.4% | 42.9% | 34.0% | 0.0% |
| JobInvolvement | 2.41 | 2.57 | 2.42 | 2.50 |
| JobLevel | 1.96 | 2.57 | 1.00 | 4.00 |
| JobSatisfaction | 2.48 | 2.00 | 2.25 | 3.00 |
| MonthlyIncome | 5126.93 | 9242.57 | 2555.09 | 13315.50 |
| NumCompaniesWorked | 4.19 | 4.00 | 2.47 | 6.50 |
| OverTime:True | 63.0% | 85.7% | 67.9% | 50.0% |
| PercentSalaryHike | 15.44 | 14.57 | 15.72 | 14.00 |
| OutstandingPerformanceRating:True | 22.2% | 14.3% | 22.6% | 0.0% |
| RelationshipSatisfaction | 2.44 | 2.86 | 2.57 | 3.00 |
| StockOptionLevel | 0.19 | -0.00 | 0.28 | 0.00 |
| TotalWorkingYears | 9.00 | 9.43 | 4.30 | 24.50 |
| TrainingTimesLastYear | 2.70 | 2.00 | 2.58 | 2.50 |
| WorkLifeBalance | 2.70 | 2.29 | 2.62 | 1.50 |
| YearsAtCompany | 4.78 | 5.14 | 2.36 | 21.00 |
| YearsInCurrentRole | 3.22 | 2.29 | 1.21 | 6.00 |
| YearsSinceLastPromotion | 1.52 | 3.29 | 0.92 | 8.50 |
| YearsWithCurrManager | 2.52 | 3.00 | 1.23 | 9.00 |
| Department:HumanResources | -0.0% | 0.0% | 3.8% | 0.0% |
| Department:ResearchAndDevelopment | 40.7% | 0.0% | 56.6% | 0.0% |
| Department:Sales | 59.3% | 100.0% | 39.6% | 100.0% |
| EducationField:HumanResources | -0.0% | 0.0% | 3.8% | 0.0% |
| EducationField:LifeSciences | 33.3% | 42.9% | 37.7% | 50.0% |
| EducationField:Marketing | 29.6% | 57.1% | 15.1% | 50.0% |
| EducationField:Medical | 18.5% | 0.0% | 15.1% | 0.0% |
| EducationField:Other | 11.1% | 0.0% | 5.7% | 0.0% |
| EducationField:TechnicalDegree | 7.4% | 0.0% | 22.6% | 0.0% |
| JobRole:HealthcareRepresentative | 3.7% | 0.0% | -0.0% | 0.0% |
| JobRole:HumanResources | -0.0% | 0.0% | 3.8% | 0.0% |
| JobRole:LaboratoryTechnician | 33.3% | 0.0% | 34.0% | 0.0% |
| JobRole:Manager | 0.0% | 0.0% | 0.0% | 0.0% |
| JobRole:ManufacturingDirector | 0.0% | 0.0% | 0.0% | 0.0% |
| JobRole:ResearchDirector | 0.0% | 0.0% | 0.0% | 0.0% |
| JobRole:ResearchScientist | 3.7% | 0.0% | 22.6% | 0.0% |
| JobRole:SalesExecutive | 59.3% | 100.0% | 0.0% | 100.0% |
| JobRole:SalesRepresentative | 0.0% | 0.0% | 39.6% | 0.0% |
| MaritalStatus:Divorced | 0.0% | -0.0% | 9.4% | 0.0% |
| MaritalStatus:Married | 22.2% | 14.3% | 18.9% | 50.0% |
| MaritalStatus:Single | 77.8% | 85.7% | 71.7% | 50.0% |

## Learned AReS Results
| | Rule | Action |
| :---: | --- | --- |
| Recourse <br> rule 1 <br> (probability: 51.7%) | If 'OverTime=True' <br> AND 'OutstandingPerformanceRating=False' | OverTime=False <br> AND OutstandingPerformanceRating=True |
| Recourse <br> rule 2 <br> (probability: 31.5%) | If 'OverTime=False' <br> AND 'StockOptionLevel<1' | StockOptionLevel>=2 |
| Recourse <br> rule 3 <br> (probability: 28.1%) | If 'OverTime=True' <br> AND '2<=YearsInCurrentRole<3' | OverTime=False <br> AND YearsInCurrentRole>=9 |
| Recourse <br> rule 4 <br> (probability: 18.0%) | If 'OverTime=True' <br> AND 'JobRole:SalesExecutive' | OverTime=False <br> AND JobRole:HealthcareRepresentative |
| Default <br> rule | Else | OverTime=False <br> AND 2<=YearsInCurrentRole<3 <br> AND 2<=YearsWithCurrManager<3 <br> AND MaritalStatus:Married |

## Learned CET Results
```
- If OverTime:
	* Action [Attrition: Yes -> No] (52/60 = 86.7% / MeanCost = 0.275):
		* OverTime: True -> False
		* TotalWorkingYears: +4
- Else:
	- If BusinessTravel<2:
		* Action [Attrition: Yes -> No] (16/16 = 100.0% / MeanCost = 0.395):
			* YearsInCurrentRole: +4
			* YearsWithCurrManager: +4
	- Else:
		- If YearsAtCompany<2:
			* Action [Attrition: Yes -> No] (7/8 = 87.5% / MeanCost = 0.187):
				* BusinessTravel: -1
				* YearsInCurrentRole: +1
		- Else:
			* Action [Attrition: Yes -> No] (5/5 = 100.0% / MeanCost = 0.398):
				* BusinessTravel: -1
				* YearsInCurrentRole: +6
```

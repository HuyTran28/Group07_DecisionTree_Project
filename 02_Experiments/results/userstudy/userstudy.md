### Learned Clustering
| | HowToChange |
| --- | --- |
| Action 1 | MonthlyIncome: +11317 <br>YearsInCurrentRole: +5 <br>(Acc: 100.0% / Cost: 0.455) |
| Action 2 | MonthlyIncome: +9390 <br>YearsWithCurrManager: +3 <br>(Acc: 100.0% / Cost: 0.272) |
| Action 3 | YearsInCurrentRole: +10 <br>YearsWithCurrManager: +9 <br>(Acc: 98.1% / Cost: 0.707) |
| Action 4 | MonthlyIncome: +3699 <br>TotalWorkingYears: +9 <br>(Acc: 100.0% / Cost: 0.0603) |

### Learned AReS
| | Rule | Action |
| :---: | --- | --- |
| Recourse <br> rule 1 <br> (probability: 51.7%) | If 'OverTime=True' <br> AND 'OutstandingPerformanceRating=False' | OverTime=False <br> AND OutstandingPerformanceRating=True |
| Recourse <br> rule 2 <br> (probability: 31.5%) | If 'OverTime=False' <br> AND 'StockOptionLevel<1' | StockOptionLevel>=2 |
| Recourse <br> rule 3 <br> (probability: 28.1%) | If 'OverTime=True' <br> AND '2<=YearsInCurrentRole<3' | OverTime=False <br> AND YearsInCurrentRole>=9 |
| Recourse <br> rule 4 <br> (probability: 18.0%) | If 'OverTime=True' <br> AND 'JobRole:SalesExecutive' | OverTime=False <br> AND JobRole:HealthcareRepresentative |    
| Default <br> rule | Else | OverTime=False <br> AND 2<=YearsInCurrentRole<3 <br> AND 2<=YearsWithCurrManager<3 <br> AND MaritalStatus:Married |

### Learned CET
| | HowToChange |
| --- | :--- |
| Action 1 | MonthlyIncome: 2319 -> 2544 (+225) <br>(Acc: True / Cost: 0.0293) |
| Action 2 | MonthlyIncome: 2319 -> 11709 (+9390) <br>YearsWithCurrManager: 0 -> 3 (+3) <br>(Acc: True / Cost: 0.521) |
| Action 3 | YearsInCurrentRole: 0 -> 10 (+10) <br>YearsWithCurrManager: 0 -> 9 (+9) <br>(Acc: True / Cost: 0.841) |
| Action 4 | OverTime: True -> False <br> OutstandingPerformanceRating: False -> True <br> (Acc: True / Cost: 0.274) |
| Action 5 | OverTime: True -> False <br> TotalWorkingYears: 1 -> 5 (+4) <br>(Acc: True / Cost: 0.274) |
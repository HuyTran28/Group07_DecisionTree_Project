# Learned Results Summary - Dataset d

# Demonstration: Diabetes
| | Feature | Type | Value | Mutable |
| --- | --- | --- | :---: | :---: |
| 1 | Pregnancies | Integer | [0, 17] | True |
| 2 | Glucose | Continuous | [44.0000, 199.0000] | True |
| 2 | Glucose | Integer | [44, 199] | True |
| 3 | BloodPressure | Continuous | [24.0000, 122.0000] | True |
| 3 | BloodPressure | Integer | [24, 122] | True |
| 4 | SkinThickness | Continuous | [0.0000, 99.0000] | True |
| 4 | SkinThickness | Integer | [0, 99] | True |
| 5 | Insulin | Continuous | [0.0000, 846.0000] | True |
| 5 | Insulin | Integer | [0, 846] | True |
| 6 | BMI | Continuous | [18.0000, 67.0000] | True |
| 6 | BMI | Integer | [18, 67] | True |
| 7 | DiabetesPedigreeFunction | Continuous | [0.0000, 2.0000] | True |
| 7 | DiabetesPedigreeFunction | Integer | [0, 2] | True |
| 8 | Age | Integer | [21, 81] | True |

## Learned Clustering Results
| | HowToChange |
| --- | --- |
| Action 1 | Glucose: -45.0000 <br>Insulin: +744.4800 <br>(Acc: 93.5% / Cost: 0.86) |
| Action 2 | Glucose: -57.4400 <br>BMI: -9.9440 <br>(Acc: 100.0% / Cost: 0.518) |
| Action 3 | Glucose: -60.9600 <br>BMI: -8.1100 <br>(Acc: 100.0% / Cost: 0.52) |
| Action 4 | Glucose: -32.0000 <br>Insulin: +644.5600 <br>(Acc: 95.7% / Cost: 0.327) |

| Feature | Cluster 1 | Cluster 2 | Cluster 3 | Cluster 4 |
| --- | ---: | ---: | ---: | ---: |
| Pregnancies | 5.74 | 3.09 | 5.27 | 4.94 |
| Glucose | 155.39 | 169.00 | 170.68 | 151.81 |
| BloodPressure | 77.09 | 69.27 | 75.82 | 69.60 |
| SkinThickness | 15.62 | 35.64 | 35.82 | 32.13 |
| Insulin | 1.34 | 548.91 | 288.14 | 147.51 |
| BMI | 36.79 | 36.79 | 37.99 | 36.96 |
| DiabetesPedigreeFunction | 0.54 | 0.80 | 0.58 | 0.59 |
| Age | 42.66 | 34.36 | 39.50 | 35.57 |

## Learned AReS Results
| | Rule | Action |
| :---: | --- | --- |
| Recourse <br> rule 1 <br> (probability: 33.1%) | If 'Glucose>=168.0' | 85.0<=Glucose<94.0 |
| Recourse <br> rule 2 <br> (probability: 26.1%) | If '150.0<=Glucose<168.0' | 94.0<=Glucose<100.0 |
| Recourse <br> rule 3 <br> (probability: 18.5%) | If '139.0<=Glucose<150.0' | 100.0<=Glucose<107.0 |
| Recourse <br> rule 4 <br> (probability: 12.1%) | If '128.0<=Glucose<139.0' | Glucose<85.0 |
| Default <br> rule | Else | Glucose<85.0 |

## Learned CET Results
```
- If Pregnancies<7:
	- If Glucose<147.0:
		* Action [Outcome: Bad -> Good] (28/29 = 96.6% / MeanCost = 0.235):
			* Glucose: -20.6400
			* BMI: -4.9880
	- Else:
		* Action [Outcome: Bad -> Good] (60/65 = 92.3% / MeanCost = 0.344):
			* Glucose: -45.5600
			* BloodPressure: +9.4400
- Else:
	- If Glucose<110.0:
		* Action [Outcome: Bad -> Good] (3/3 = 100.0% / MeanCost = 0.138):
			* Glucose: -10.9200
			* BMI: -2.7520
	- Else:
		* Action [Outcome: Bad -> Good] (48/60 = 80.0% / MeanCost = 0.361):
			* Glucose: -37.9600
			* BloodPressure: +13.1200
```

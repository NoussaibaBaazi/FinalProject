Final Project Repository - NOUSSAIBA BAAZI 230299681

Employment rates and Higher education in London

- Hypothesis: Rising employment rates are closely linked to greater attainment in advanced education.
The analysis aims to explore the changes in London’s employment and education rates, linking higher education with the job market as well as the pre- and post-pandemic levels in job availability.

- Datasets used - found in: FinalProject(Data):
Source: https://data.london.gov.uk
1. workforce-jobs-ons.csv: contains the estimated numebr of workforce jobs in the UK and London, 
divided by gender overthe years 2005 - 2023.
2. QualificationsCSV.csv: contains estimates of individuals with different qulaification levels in the UK and
London over the years 2013 - 2021.

- Analysis:
1. YearlyChangeWorkforce.py - the percentage difference between the years in the estimated number of jobs, dividing by gender and for both. A comparison between the years and genders.
2. QualificationsLondonOnly.py - the qualification levels percentage of attainment over the years in London
3. UKvLondonQualifications.py - A comparison of UK average with london in the most recent year the datas available 2021, the percentage of attainment in the different qualification levels.

- Figures - found in: FinalProject/Figures:
1. WorkYearlyChange.png: KEY figure 1
2. LondonQualifications.png: figure 2
3. UKvLondonQualifications.png: figure 3

- Summary statistics:
1. summary_stats_Qualifications.py
2. worforce_sum_stats.py

- Unit Tests:
1. .circleci folder cotainting the config file for circle ci connection
2. UnitTests.py containg all the units for verifying correct import, data consistency and analysis
3. KeyTests.txt file containg all rhe information of unittests



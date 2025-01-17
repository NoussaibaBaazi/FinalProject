Final Project Repository - NOUSSAIBA BAAZI 230299681

Employment rates and Higher education in London

- Hypothesis: Rising employment rates are closely linked to greater attainment in advanced education.
The analysis aims to explore the changes in London’s employment and education rates, linking higher education with the job market as well as the pre- and post-pandemic levels in job availability.

- Key Statistics: 
1. In higher education 54.2% achieved an NVQ4 or higher in 2019, which increased
to 58.9% in 2021.
2. In London, the percentage of individuals with NVQ4+ qualifications were 52% in 2021, whereas the UK was 38%.
3. In 2005,  The estimated numebr of employment by males was 2,532,588, and by around 2,135,712 females, this number has
increase over the years reaching 3,386,804 workforce jobs for males and 3,168,419 for females in Decemeber 2023

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



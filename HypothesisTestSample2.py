import numpy as np
from scipy import stats

import generateData

sampleTwoCombined_df = generateData.sampleTwoCombined_df

# Split the dataframe into two lists based on category
african_list = sampleTwoCombined_df[sampleTwoCombined_df['Category'] == 'African']
non_african_list = sampleTwoCombined_df[sampleTwoCombined_df['Category'] == 'Non-African']

# Define the data for hypothesis testing
african_hired = african_list['is_hired']
non_african_hired = non_african_list['is_hired']

# Perform the hypothesis test
t_statistic, p_value = stats.ttest_ind(african_hired, non_african_hired)

# Significance level
alpha = 0.05

# Decision
if p_value <= alpha:
    result = "Reject the null hypothesis"
else:
    result = "Fail to reject the null hypothesis"

result_summary = {
    "T-statistic": t_statistic,
    "P-value": p_value,
    "Result": result
}

print(result_summary)
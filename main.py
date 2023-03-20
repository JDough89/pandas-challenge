import pandas as pd
school_data_to_load = ('/Users/Jackson/Desktop/DUBootCamp/Module4Challenge/pandas-challenge/schools_complete.csv')
student_data_to_load = ('/Users/Jackson/Desktop/DUBootCamp/Module4Challenge/pandas-challenge/students_complete.csv')
school_data=pd.read_csv(school_data_to_load)
student_data=pd.read_csv(student_data_to_load)
school_data_complete=pd.merge(student_data,school_data, how="left", on=["school_name","school_name"])
school_data_complete
school_count = school_data_complete['school_name'].nunique()
student_count=school_data_complete['Student ID'].nunique()
total_budget = sum(school_data_complete['budget'].unique())
average_math_score = school_data_complete['math_score'].mean()
average_reading_score = school_data_complete['reading_score'].mean()
passing_math_count = school_data_complete[(school_data_complete['math_score'] >= 70)].count()['student_name']
passing_math_percentage = passing_math_count / float(student_count) * 100
# Use the following to calculate the percentage of students that passed math and reading
passing_math_reading_count = school_data_complete[
    (school_data_complete['math_score'] >= 70) & (school_data_complete['reading_score'] >= 70)
].count()['student_name']
overall_passing_rate = passing_math_reading_count /  float(student_count) * 100
# Create a high-level snapshot of the district's key metrics in a DataFrame
district_summary = pd.DataFrame({"Total Schools":[school_count],"Total Students":[student_count],"Total Budget":[total_budget],"Average Math Score":[average_math_score],
                                 "Average Reading Score":[average_reading_score],"% Passing Math":[passing_math_percentage], "% Passing Reading":[passing_reading_percentage],
                                "% Overall Passing":[overall_passing_rate]})

# Formatting
district_summary["Total Students"] = district_summary["Total Students"].map("{:,}".format)
district_summary["Total Budget"] = district_summary["Total Budget"].map("${:,.2f}".format)

# Display the DataFrame
district_summary
school_types = school_data.set_index(["school_name"])["type"]
per_school_counts = school_data_complete.groupby(["school_name"]).nunique()['Student ID']
per_school_budget = school_data_complete.groupby(["school_name"]).mean()["budget"]
per_school_capita = per_school_budget / per_school_counts
per_school_math = school_data_complete.groupby(["school_name"]).mean()["math_score"]
per_school_reading = school_data_complete.groupby(["school_name"]).mean()["reading_score"]
school_passing_math = school_data_complete.loc[(school_data_complete['math_score'] >= 70)]
school_passing_reading = school_data_complete.loc[(school_data_complete['reading_score'] >= 70)]
passing_math_and_reading = school_data_complete[(school_data_complete["reading_score"] >= 70) & (school_data_complete["math_score"] >= 70)]
per_school_passing_math = school_passing_math.groupby(["school_name"]).count()["student_name"] / per_school_counts * 100
per_school_passing_reading = school_passing_reading.groupby(["school_name"]).count()["student_name"] / per_school_counts * 100
overall_passing_rate = passing_math_and_reading.groupby(["school_name"]).count()["student_name"] / per_school_counts * 100
# Create a DataFrame called `per_school_summary` with columns for the calculations above.
per_school_summary= pd.DataFrame({"School Types":school_types, "Total Students":per_school_counts, "Total School Budget":per_school_budget, 
                                  "Per Student Budget":per_school_capita, "Average Math Score":per_school_math, "Average Reading Score":per_school_reading,
                                  "% Passing Math":per_school_passing_math,"% Passing Reading":per_school_passing_reading, "% Overall Passing":overall_passing_rate})
# Formatting
per_school_summary["Total School Budget"] = per_school_summary["Total School Budget"].map("${:,.2f}".format)
per_school_summary["Per Student Budget"] = per_school_summary["Per Student Budget"].map("${:,.2f}".format)

# Display the DataFrame
per_school_summary
#Sort the schools by '% Overall Passing' in descending order and display the top 5 rows
top_5_schools = per_school_summary.sort_values(by='% Overall Passing', ascending = False).head(5)
top_5_schools
bottom_5_schools = per_school_summary.sort_values(by = '% Overall Passing').head(5)
bottom_5_schools
ninth_graders = school_data_complete[(school_data_complete["grade"] == "9th")]
tenth_graders = school_data_complete[(school_data_complete["grade"] == "10th")]
eleventh_graders = school_data_complete[(school_data_complete["grade"] == "11th")]
twelfth_graders = school_data_complete[(school_data_complete["grade"] == "12th")]

# Group by "school_name" and take the mean of each.
ninth_graders_scores = ninth_graders.groupby("school_name").mean()
tenth_graders_scores = tenth_graders.groupby("school_name").mean()
eleventh_graders_scores = eleventh_graders.groupby("school_name").mean()
twelfth_graders_scores = twelfth_graders.groupby("school_name").mean()

# Use the code to select only the `math_score`.
ninth_grade_math_scores = ninth_graders_scores["math_score"]
tenth_grader_math_scores = tenth_graders_scores["math_score"]
eleventh_grader_math_scores = eleventh_graders_scores["math_score"]
twelfth_grader_math_scores = twelfth_graders_scores["math_score"]

# Combine each of the scores above into single DataFrame called `math_scores_by_grade`

math_scores_by_grade = pd.DataFrame({"9th":ninth_grade_math_scores, "10th":tenth_grader_math_scores, "11th":eleventh_grader_math_scores,"12th":twelfth_grader_math_scores})

# Minor data wrangling
math_scores_by_grade.index.name = None

# Display the DataFrame
math_scores_by_grade
# Use the code provided to separate the data by grade
ninth_graders = school_data_complete[(school_data_complete["grade"] == "9th")]
tenth_graders = school_data_complete[(school_data_complete["grade"] == "10th")]
eleventh_graders = school_data_complete[(school_data_complete["grade"] == "11th")]
twelfth_graders = school_data_complete[(school_data_complete["grade"] == "12th")]

# Group by "school_name" and take the mean of each.
ninth_graders_scores = ninth_graders.groupby("school_name").mean()
tenth_graders_scores = tenth_graders.groupby("school_name").mean()
eleventh_graders_scores = eleventh_graders.groupby("school_name").mean()
twelfth_graders_scores = twelfth_graders.groupby("school_name").mean()

# Use the code to select only the `reading_score`.
ninth_grade_reading_scores = ninth_graders_scores["reading_score"]
tenth_grader_reading_scores = tenth_graders_scores["reading_score"]
eleventh_grader_reading_scores = eleventh_graders_scores["reading_score"]
twelfth_grader_reading_scores = twelfth_graders_scores["reading_score"]

# Combine each of the scores above into single DataFrame called `reading_scores_by_grade`
reading_scores_by_grade = pd.DataFrame({"9th":ninth_grade_reading_scores, "10th":tenth_grader_reading_scores, "11th":eleventh_grader_reading_scores,
                                        "12th":twelfth_grader_reading_scores})

# Minor data wrangling
reading_scores_by_grade = reading_scores_by_grade[["9th", "10th", "11th", "12th"]]
reading_scores_by_grade.index.name = None

# Display the DataFrame
reading_scores_by_grade
# Establish the bins 
spending_bins = [0, 585, 630, 645, 680]
labels = ["<$585", "$585-630", "$630-645", "$645-680"]
spending_bins
# Create a copy of the school summary since it has the "Per Student Budget" 
school_spending_df = per_school_summary.copy()
# Use `pd.cut` to categorize spending based on the bins.
school_spending_df["Spending Ranges (Per Student)"] = pd.cut(school_spending_df["Per Student Budget"], bins = spending_bins, labels = labels)
#  Calculate averages for the desired columns. 
spending_math_scores = school_spending_df.groupby(["Spending Ranges (Per Student)"]).mean()["Average Math Score"]
spending_reading_scores = school_spending_df.groupby(["Spending Ranges (Per Student)"]).mean()["Average Reading Score"]
spending_passing_math = school_spending_df.groupby(["Spending Ranges (Per Student)"]).mean()["% Passing Math"]
spending_passing_reading = school_spending_df.groupby(["Spending Ranges (Per Student)"]).mean()["% Passing Reading"]
overall_passing_spending = school_spending_df.groupby(["Spending Ranges (Per Student)"]).mean()["% Overall Passing"]
# Assemble into DataFrame
spending_summary = 

# Display results
spending_summary
# Establish the bins.
size_bins = [0, 1000, 2000, 5000]
labels = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]
# Categorize the spending based on the bins
# Use `pd.cut` on the "Total Students" column of the `per_school_summary` DataFrame.

per_school_summary["School Size"] = 
# Calculate averages for the desired columns. 
size_math_scores = per_school_summary.groupby(["School Size"]).mean()["Average Math Score"]
size_reading_scores = per_school_summary.groupby(["School Size"]).mean()["Average Reading Score"]
size_passing_math = per_school_summary.groupby(["School Size"]).mean()["% Passing Math"]
size_passing_reading = per_school_summary.groupby(["School Size"]).mean()["% Passing Reading"]
size_overall_passing = per_school_summary.groupby(["School Size"]).mean()["% Overall Passing"]
# Create a DataFrame called `size_summary` that breaks down school performance based on school size (small, medium, or large).
# Use the scores above to create a new DataFrame called `size_summary`


# Display results
size_summary
# Group the per_school_summary DataFrame by "School Type" and average the results.
type_math_scores = 
type_reading_scores = 
type_passing_math = 
type_passing_reading = 
type_overall_passing = 

# Use the code provided to select new column data
average_math_score_by_type = type_math_scores["Average Math Score"]
average_reading_score_by_type = type_reading_scores["Average Reading Score"]
average_percent_passing_math_by_type = type_passing_math["% Passing Math"]
average_percent_passing_reading_by_type = type_passing_reading["% Passing Reading"]
average_percent_overall_passing_by_type = type_overall_passing["% Overall Passing"]
# Assemble the new data by type into a DataFrame called `type_summary`


# Display results
type_summary

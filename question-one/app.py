import pandas

bills_df = pandas.read_csv('../datasets/bills.csv')
legislators_df = pandas.read_csv('../datasets/legislators.csv')
vote_results_df = pandas.read_csv('../datasets/vote_results.csv')
votes_df = pandas.read_csv('../datasets/votes.csv')

vote_results_with_legislators_df = pandas.merge(vote_results_df, legislators_df, on='id', how='left')

print(vote_results_with_legislators_df)
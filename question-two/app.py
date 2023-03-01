import pandas
import numpy

bills_df = pandas.read_csv('../datasets/bills.csv')
legislators_df = pandas.read_csv('../datasets/legislators.csv')
vote_results_df = pandas.read_csv('../datasets/vote_results.csv')
votes_df = pandas.read_csv('../datasets/votes.csv')

bills_with_legislators = pandas.merge(bills_df, legislators_df,  left_on='sponsor_id',
                                                right_on='id',
                                                how='left')

bills_with_legislators = bills_with_legislators.rename(columns={'name' : 'primary_sponsor'})
bills_with_legislators = bills_with_legislators.fillna('Unknown')

bills_with_legislators_and_votes = pandas.merge(bills_with_legislators, votes_df, left_on='id_x', right_on='bill_id',
                                                how='left')
bills_with_legislators_and_votes = bills_with_legislators_and_votes.rename(columns={'id_x' : 'id_billcsv',
                                                                                    'id_y' : 'id_legislatorcsv',
                                                                                    'id' : 'id_votescsv'})

bills_with_legislators_and_votes_with_votes_results = pandas.merge(bills_with_legislators_and_votes, vote_results_df,
                                                                   left_on='id_votescsv',
                                                                   right_on='vote_id', how='left')
print(bills_with_legislators_and_votes_with_votes_results.to_string())
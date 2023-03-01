import pandas
import numpy

bills_df = pandas.read_csv('../datasets/bills.csv')
legislators_df = pandas.read_csv('../datasets/legislators.csv')
vote_results_df = pandas.read_csv('../datasets/vote_results.csv')
votes_df = pandas.read_csv('../datasets/votes.csv')

primeiro_merge = pandas.merge(bills_df, legislators_df,  left_on='sponsor_id',
                                                right_on='id',
                                                how='left')

primeiro_merge = primeiro_merge.rename(columns={'name' : 'primary_sponsor'})
primeiro_merge = primeiro_merge.fillna('Unknown')

segundo_merge = pandas.merge(primeiro_merge, votes_df, left_on='id_x', right_on='bill_id', how='left')
segundo_merge = segundo_merge.rename(columns={'id_x' : 'id_billcsv', 'id_y' : 'id_legislatorcsv', 'id' : 'id_votescsv'})

terceiro_merge = pandas.merge(segundo_merge, vote_results_df, left_on='id_votescsv', right_on='vote_id', how='left')
print(terceiro_merge.to_string())
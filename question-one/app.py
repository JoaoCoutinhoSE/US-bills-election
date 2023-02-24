import pandas
import numpy
pandas.set_option('display.expand_frame_repr', False)

bills_df = pandas.read_csv('../datasets/bills.csv')
legislators_df = pandas.read_csv('../datasets/legislators.csv')
vote_results_df = pandas.read_csv('../datasets/vote_results.csv')
votes_df = pandas.read_csv('../datasets/votes.csv')

vote_results_with_legislators_df = pandas.merge(vote_results_df, legislators_df,  left_on='legislator_id',
                                                right_on='id',
                                                how='left')

legislator_counts_df = vote_results_with_legislators_df.groupby(['legislator_id','name', 'vote_type'])['vote_type']\
    .count().reset_index(name='vote_count')
legislator_counts_df = legislator_counts_df.pivot_table(index=['legislator_id', 'name'], columns='vote_type',
                                                        values='vote_count', aggfunc=numpy.sum).reset_index()


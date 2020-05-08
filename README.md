## Relational Join Operation - Using Hadoop MapReduce
Perform Relational Join operation on two sets of data, using hadoop map-reduce framework


### MAP STEP(mapper_join.py):
- The first step is stripping and splitting each line of input into a list of features
- First line of the input is ignored because it is the index/name labels
- Then we join list using separating the Primary Key (key of our mapper) and other features (values of our mapper) using a tab space.
- Other features are separated using semi-colon (;)
- And we emit/print this key values

### REDUCE STEP(reducer_join.py):
- The reducer receives the input sorted by ascending order of the keys
- There should be exactly two lines with same keys – one with Names and second from another data set containing additional information
- And the reducer joins two separate values of the key.

>>> pd.get_dummies(pd.Series(list('abcaa')), drop_first=True)
       b      c
0  False  False
1   True  False
2  False   True
3  False  False
4  False  False

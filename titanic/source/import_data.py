train = pd.read_csv("titanic/data/train.csv")
test = pd.read_csv("titanic/data/test.csv")

# understand the structure
tally_cols = ["Survived", "Pclass", "Sex"]

[train[col].value_counts().to_dict() for col in tally_cols]

train["Survived"].value_counts().to_dict()
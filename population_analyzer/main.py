import pandas as pd

from machine_learning.simple_machine_learning_model import predict
from population_analyzer.rules.age_rule import age_rule
from population_analyzer.rules.living_status_rule import living_status_rule

# Load the data
data = pd.read_csv("../data/population_data.csv")

# Apply the age rule
data = age_rule(data)
data = living_status_rule(data)
print(
    data[
        [
            "name",
            "date_of_birth",
            "death_date",
            "age_rule_pass",
            "living_status_rule_pass",
        ]
    ]
)

data["grant_amount"] = predict(data[["age_rule_pass", "living_status_rule_pass"]])
data["grant_amount"] = data["grant_amount"].apply(lambda x: "{:.2f}".format(x))
output = data[["name", "age_rule_pass", "living_status_rule_pass", "grant_amount"]]
output.to_csv("../output/result.csv", index=False)

import pandas as pd

# Load the dataset
df = pd.read_csv("Survey - Model Sharing (Responses) - Form Responses.csv")

# Clean column names
df.columns = [col.strip() for col in df.columns]

# Filter for people with "Yes" in the third column, i.e. people that have loaded a model at least once in their lifetime
df = df[df.iloc[:, 3].str.contains("Yes", na=False)]
print(f"People who have loaded a model: {len(df)}, which is {len(df) / len(pd.read_csv('Survey - Model Sharing (Responses) - Form Responses.csv')) * 100:.2f}% of the total responses")
print()

cybersecurity_rows = df[df.iloc[:, 1].str.contains("Cybersecurity", na=False)]
print(f"People from cybersecurity count: {len(cybersecurity_rows)}, that is {len(cybersecurity_rows) / len(df) * 100:.2f}% of the total rows")

non_cybersecurity_rows = df[~df.iloc[:, 1].str.contains("Cybersecurity", na=False)]
print(f"People NOT from cybersecurity count: {len(non_cybersecurity_rows)}, that is {len(non_cybersecurity_rows) / len(df) * 100:.2f}% of the total rows")

machine_learning_rows = df[df.iloc[:, 1].str.contains("Machine Learning", na=False)]
print(f"People from Machine Learning / Artificial Intelligence count: {len(machine_learning_rows)}, that is {len(machine_learning_rows) / len(df) * 100:.2f}% of the total rows")

print()

print(f"Average experience in ML (total): {df.iloc[:, 2].mean()} / 5")
print(f"\tAverage experience in ML (cybersecurity): {cybersecurity_rows.iloc[:, 2].mean()} / 5")

print(f"\tAverage experience in ML (non-cybersecurity): {non_cybersecurity_rows.iloc[:, 2].mean()} / 5")

print(f"\tAverage experience in ML (ML/AI): {machine_learning_rows.iloc[:, 2].mean()} / 5")

print()

print(f"Average confidence for 'safe_mode_False': {df.iloc[:, 4].mean()}")
cybersecurity_avg_safe_false = cybersecurity_rows.iloc[:, 4].mean()
print(f"\tCybersecurity average confidence for 'safe_mode_False': {cybersecurity_avg_safe_false}")
non_cybersecurity_avg_safe_false = non_cybersecurity_rows.iloc[:, 4].mean()
print(f"\tNon-Cybersecurity average confidence for 'safe_mode_False': {non_cybersecurity_avg_safe_false}")
machine_learning_avg_safe_false = machine_learning_rows.iloc[:, 4].mean()
print(f"\tMachine Learning / Artificial Intelligence average confidence for 'safe_mode_False': {machine_learning_avg_safe_false}")

print()


number_safe_false_concern = df[df.iloc[:, 5].str.contains("Arbitrary code execution", na=False)]
print(f"Number of people answered with 'Arbitrary code execution' with 'safe_mode=False': {len(number_safe_false_concern)}, that is {len(number_safe_false_concern) / len(df) * 100:.2f}% of the total rows")
number_safe_false_concern_cybersecurity = cybersecurity_rows[cybersecurity_rows.iloc[:, 5].str.contains("Arbitrary code execution", na=False)]
print(f"\tCybersecurity people answered with 'Arbitrary code execution': {len(number_safe_false_concern_cybersecurity)}, that is {len(number_safe_false_concern_cybersecurity) / len(cybersecurity_rows) * 100:.2f}% of the cybersecurity rows")
number_safe_false_concern_non_cybersecurity = non_cybersecurity_rows[non_cybersecurity_rows.iloc[:, 5].str.contains("Arbitrary code execution", na=False)]
print(f"\tNon-Cybersecurity people answered with 'Arbitrary code execution': {len(number_safe_false_concern_non_cybersecurity)}, that is {len(number_safe_false_concern_non_cybersecurity) / len(non_cybersecurity_rows) * 100:.2f}% of the non-cybersecurity rows")
number_safe_false_concern_machine_learning = machine_learning_rows[machine_learning_rows.iloc[:, 5].str.contains("Arbitrary code execution", na=False)]
print(f"\tMachine Learning / Artificial Intelligence people answered with 'Arbitrary code execution': {len(number_safe_false_concern_machine_learning)}, that is {len(number_safe_false_concern_machine_learning) / len(machine_learning_rows) * 100:.2f}% of the machine learning rows")

print()

print(f"Average confidence for 'safe_mode_True': {df.iloc[:, 6].mean()}")
cybersecurity_avg_safe_true = cybersecurity_rows.iloc[:, 6].mean()
print(f"\tCybersecurity average confidence for 'safe_mode_True': {cybersecurity_avg_safe_true}")
non_cybersecurity_avg_safe_true = non_cybersecurity_rows.iloc[:, 6].mean()
print(f"\tNon-Cybersecurity average confidence for 'safe_mode_True': {non_cybersecurity_avg_safe_true}")
machine_learning_avg_safe_true = machine_learning_rows.iloc[:, 6].mean()
print(f"\tMachine Learning / Artificial Intelligence average confidence for 'safe_mode_True': {machine_learning_avg_safe_true}")

print()

number_safe_true_concern = df[df.iloc[:, 7].str.contains("Arbitrary code execution", na=False)]
print(f"Number of people answered with 'Arbitrary code execution' with 'safe_mode=True': {len(number_safe_true_concern)}, that is {len(number_safe_true_concern) / len(df) * 100:.2f}% of the total rows")
number_safe_true_concern_cybersecurity = cybersecurity_rows[cybersecurity_rows.iloc[:, 7].str.contains("Arbitrary code execution", na=False)]
print(f"\tCybersecurity people answered with 'Arbitrary code execution': {len(number_safe_true_concern_cybersecurity)}, that is {len(number_safe_true_concern_cybersecurity) / len(cybersecurity_rows) * 100:.2f}% of the cybersecurity rows")
number_safe_true_concern_non_cybersecurity = non_cybersecurity_rows[non_cybersecurity_rows.iloc[:, 7].str.contains("Arbitrary code execution", na=False)]
print(f"\tNon-Cybersecurity people answered with 'Arbitrary code execution': {len(number_safe_true_concern_non_cybersecurity)}, that is {len(number_safe_true_concern_non_cybersecurity) / len(non_cybersecurity_rows) * 100:.2f}% of the non-cybersecurity rows")
number_safe_true_concern_machine_learning = machine_learning_rows[machine_learning_rows.iloc[:, 7].str.contains("Arbitrary code execution", na=False)]
print(f"\tMachine Learning / Artificial Intelligence people answered with 'Arbitrary code execution': {len(number_safe_true_concern_machine_learning)}, that is {len(number_safe_true_concern_machine_learning) / len(machine_learning_rows) * 100:.2f}% of the machine learning rows")

print()

print(f"Average confidence for 'weights_only_False': {df.iloc[:, 8].mean()}")
cybersecurity_avg_weights_false = cybersecurity_rows.iloc[:, 8].mean()
print(f"\tCybersecurity average confidence for 'weights_only_False': {cybersecurity_avg_weights_false}")
non_cybersecurity_avg_weights_false = non_cybersecurity_rows.iloc[:, 8].mean()
print(f"\tNon-Cybersecurity average confidence for 'weights_only_False': {non_cybersecurity_avg_weights_false}")
machine_learning_avg_weights_false = machine_learning_rows.iloc[:, 8].mean()
print(f"\tMachine Learning / Artificial Intelligence average confidence for 'weights_only_False': {machine_learning_avg_weights_false}")

print()

number_weights_false_concern = df[df.iloc[:, 9].str.contains("Arbitrary code execution", na=False)]
print(f"Number of people answered with 'Arbitrary code execution' with 'weights_only=False': {len(number_weights_false_concern)}, that is {len(number_weights_false_concern) / len(df) * 100:.2f}% of the total rows")
number_weights_false_concern_cybersecurity = cybersecurity_rows[cybersecurity_rows.iloc[:, 9].str.contains("Arbitrary code execution", na=False)]
print(f"\tCybersecurity people answered with 'Arbitrary code execution': {len(number_weights_false_concern_cybersecurity)}, that is {len(number_weights_false_concern_cybersecurity) / len(cybersecurity_rows) * 100:.2f}% of the cybersecurity rows")
number_weights_false_concern_non_cybersecurity = non_cybersecurity_rows[non_cybersecurity_rows.iloc[:, 9].str.contains("Arbitrary code execution", na=False)]
print(f"\tNon-Cybersecurity people answered with 'Arbitrary code execution': {len(number_weights_false_concern_non_cybersecurity)}, that is {len(number_weights_false_concern_non_cybersecurity) / len(non_cybersecurity_rows) * 100:.2f}% of the non-cybersecurity rows")
number_weights_false_concern_machine_learning = machine_learning_rows[machine_learning_rows.iloc[:, 9].str.contains("Arbitrary code execution", na=False)]
print(f"\tMachine Learning / Artificial Intelligence people answered with 'Arbitrary code execution': {len(number_weights_false_concern_machine_learning)}, that is {len(number_weights_false_concern_machine_learning) / len(machine_learning_rows) * 100:.2f}% of the machine learning rows")

print()

print(f"Average confidence for 'weights_only_True': {df.iloc[:, 10].mean()}")
cybersecurity_avg_weights_true = cybersecurity_rows.iloc[:, 10].mean()
print(f"\tCybersecurity average confidence for 'weights_only_True': {cybersecurity_avg_weights_true}")
non_cybersecurity_avg_weights_true = non_cybersecurity_rows.iloc[:, 10].mean()
print(f"\tNon-Cybersecurity average confidence for 'weights_only_True': {non_cybersecurity_avg_weights_true}")
machine_learning_avg_weights_true = machine_learning_rows.iloc[:, 10].mean()
print(f"\tMachine Learning / Artificial Intelligence average confidence for 'weights_only_True': {machine_learning_avg_weights_true}")

print()
number_weights_true_concern = df[df.iloc[:, 11].str.contains("Arbitrary code execution", na=False)]
print(f"Number of people answered with 'Arbitrary code execution' with 'weights_only=True': {len(number_weights_true_concern)}, that is {len(number_weights_true_concern) / len(df) * 100:.2f}% of the total rows")
number_weights_true_concern_cybersecurity = cybersecurity_rows[cybersecurity_rows.iloc[:, 11].str.contains("Arbitrary code execution", na=False)]
print(f"\tCybersecurity people answered with 'Arbitrary code execution': {len(number_weights_true_concern_cybersecurity)}, that is {len(number_weights_true_concern_cybersecurity) / len(cybersecurity_rows) * 100:.2f}% of the cybersecurity rows")
number_weights_true_concern_non_cybersecurity = non_cybersecurity_rows[non_cybersecurity_rows.iloc[:, 11].str.contains("Arbitrary code execution", na=False)]
print(f"\tNon-Cybersecurity people answered with 'Arbitrary code execution': {len(number_weights_true_concern_non_cybersecurity)}, that is {len(number_weights_true_concern_non_cybersecurity) / len(non_cybersecurity_rows) * 100:.2f}% of the non-cybersecurity rows")
number_weights_true_concern_machine_learning = machine_learning_rows[machine_learning_rows.iloc[:, 11].str.contains("Arbitrary code execution", na=False)]
print(f"\tMachine Learning / Artificial Intelligence people answered with 'Arbitrary code execution': {len(number_weights_true_concern_machine_learning)}, that is {len(number_weights_true_concern_machine_learning) / len(machine_learning_rows) * 100:.2f}% of the machine learning rows")

print()

print(f"Number of people who inspected a model: {len(df[df.iloc[:, 12].str.contains('Yes', na=False)])}, that is {len(df[df.iloc[:, 12].str.contains('Yes', na=False)]) / len(df) * 100:.2f}% of the total rows")
print(f"\tNumber of people who inspected a model in Cybersecurity: {len(cybersecurity_rows[cybersecurity_rows.iloc[:, 12].str.contains('Yes', na=False)])}, that is {len(cybersecurity_rows[cybersecurity_rows.iloc[:, 12].str.contains('Yes', na=False)]) / len(cybersecurity_rows) * 100:.2f}% of the cybersecurity rows")
print(f"\tNumber of people who inspected a model in Non-Cybersecurity: {len(non_cybersecurity_rows[non_cybersecurity_rows.iloc[:, 12].str.contains('Yes', na=False)])}, that is {len(non_cybersecurity_rows[non_cybersecurity_rows.iloc[:, 12].str.contains('Yes', na=False)]) / len(non_cybersecurity_rows) * 100:.2f}% of the non-cybersecurity rows")
print(f"\tNumber of people who inspected a model in Machine Learning / Artificial Intelligence: {len(machine_learning_rows[machine_learning_rows.iloc[:, 12].str.contains('Yes', na=False)])}, that is {len(machine_learning_rows[machine_learning_rows.iloc[:, 12].str.contains('Yes', na=False)]) / len(machine_learning_rows) * 100:.2f}% of the machine learning rows")

print()

print(f"Number of people who feel MORE comfortable using HF: {len(df[df.iloc[:, 13].str.contains('more comfortable', na=False)])}, that is {len(df[df.iloc[:, 13].str.contains('more comfortable', na=False)]) / len(df) * 100:.2f}% of the total rows")
print(f"\tNumber of people who feel MORE comfortable using HF in Cybersecurity: {len(cybersecurity_rows[cybersecurity_rows.iloc[:, 13].str.contains('more comfortable', na=False)])}, that is {len(cybersecurity_rows[cybersecurity_rows.iloc[:, 13].str.contains('more comfortable', na=False)]) / len(cybersecurity_rows) * 100:.2f}% of the cybersecurity rows")
print(f"\tNumber of people who feel MORE comfortable using HF in Non-Cybersecurity: {len(non_cybersecurity_rows[non_cybersecurity_rows.iloc[:, 13].str.contains('more comfortable', na=False)])}, that is {len(non_cybersecurity_rows[non_cybersecurity_rows.iloc[:, 13].str.contains('more comfortable', na=False)]) / len(non_cybersecurity_rows) * 100:.2f}% of the non-cybersecurity rows")
print(f"\tNumber of people who feel MORE comfortable using HF in Machine Learning / Artificial Intelligence: {len(machine_learning_rows[machine_learning_rows.iloc[:, 13].str.contains('more comfortable', na=False)])}, that is {len(machine_learning_rows[machine_learning_rows.iloc[:, 13].str.contains('more comfortable', na=False)]) / len(machine_learning_rows) * 100:.2f}% of the machine learning rows")

print(f"Number of people who feel LESS comfortable using HF: {len(df[df.iloc[:, 13].str.contains('less comfortable', na=False)])}, that is {len(df[df.iloc[:, 13].str.contains('less comfortable', na=False)]) / len(df) * 100:.2f}% of the total rows")
print(f"\tNumber of people who feel LESS comfortable using HF in Cybersecurity: {len(cybersecurity_rows[cybersecurity_rows.iloc[:, 13].str.contains('less comfortable', na=False)])}, that is {len(cybersecurity_rows[cybersecurity_rows.iloc[:, 13].str.contains('less comfortable', na=False)]) / len(cybersecurity_rows) * 100:.2f}% of the cybersecurity rows")
print(f"\tNumber of people who feel LESS comfortable using HF in Non-Cybersecurity: {len(non_cybersecurity_rows[non_cybersecurity_rows.iloc[:, 13].str.contains('less comfortable', na=False)])}, that is {len(non_cybersecurity_rows[non_cybersecurity_rows.iloc[:, 13].str.contains('less comfortable', na=False)]) / len(non_cybersecurity_rows) * 100:.2f}% of the non-cybersecurity rows")
print(f"\tNumber of people who feel LESS comfortable using HF in Machine Learning / Artificial Intelligence: {len(machine_learning_rows[machine_learning_rows.iloc[:, 13].str.contains('less comfortable', na=False)])}, that is {len(machine_learning_rows[machine_learning_rows.iloc[:, 13].str.contains('less comfortable', na=False)]) / len(machine_learning_rows) * 100:.2f}% of the machine learning rows")

print(f"Number of people who feel EQUALLY comfortable using HF: {len(df[df.iloc[:, 13].str.contains('not affected', na=False)])}, that is {len(df[df.iloc[:, 13].str.contains('not affected', na=False)]) / len(df) * 100:.2f}% of the total rows")
print(f"\tNumber of people who feel EQUALLY comfortable using HF in Cybersecurity: {len(cybersecurity_rows[cybersecurity_rows.iloc[:, 13].str.contains('not affected', na=False)])}, that is {len(cybersecurity_rows[cybersecurity_rows.iloc[:, 13].str.contains('not affected', na=False)]) / len(cybersecurity_rows) * 100:.2f}% of the cybersecurity rows")
print(f"\tNumber of people who feel EQUALLY comfortable using HF in Non-Cybersecurity: {len(non_cybersecurity_rows[non_cybersecurity_rows.iloc[:, 13].str.contains('not affected', na=False)])}, that is {len(non_cybersecurity_rows[non_cybersecurity_rows.iloc[:, 13].str.contains('not affected', na=False)]) / len(non_cybersecurity_rows) * 100:.2f}% of the non-cybersecurity rows")
print(f"\tNumber of people who feel EQUALLY comfortable using HF in Machine Learning / Artificial Intelligence: {len(machine_learning_rows[machine_learning_rows.iloc[:, 13].str.contains('not affected', na=False)])}, that is {len(machine_learning_rows[machine_learning_rows.iloc[:, 13].str.contains('not affected', na=False)]) / len(machine_learning_rows) * 100:.2f}% of the machine learning rows")  


print()

print(f"Number of people who answered arbitrary code execution with HF: {len(df[df.iloc[:, 14].str.contains('Arbitrary code execution', na=False)])}, that is {len(df[df.iloc[:, 14].str.contains('Arbitrary code execution', na=False)]) / len(df) * 100:.2f}% of the total rows")
print(f"\nNumber of people who answered arbitrary code execution with HF in Cybersecurity: {len(cybersecurity_rows[cybersecurity_rows.iloc[:, 14].str.contains('Arbitrary code execution', na=False)])}, that is {len(cybersecurity_rows[cybersecurity_rows.iloc[:, 14].str.contains('Arbitrary code execution', na=False)]) / len(cybersecurity_rows) * 100:.2f}% of the cybersecurity rows")
print(f"\nNumber of people who answered arbitrary code execution with HF in Non-Cybersecurity: {len(non_cybersecurity_rows[non_cybersecurity_rows.iloc[:, 14].str.contains('Arbitrary code execution', na=False)])}, that is {len(non_cybersecurity_rows[non_cybersecurity_rows.iloc[:, 14].str.contains('Arbitrary code execution', na=False)]) / len(non_cybersecurity_rows) * 100:.2f}% of the non-cybersecurity rows")
print(f"\nNumber of people who answered arbitrary code execution with HF in Machine Learning / Artificial Intelligence: {len(machine_learning_rows[machine_learning_rows.iloc[:, 14].str.contains('Arbitrary code execution', na=False)])}, that is {len(machine_learning_rows[machine_learning_rows.iloc[:, 14].str.contains('Arbitrary code execution', na=False)]) / len(machine_learning_rows) * 100:.2f}% of the machine learning rows")



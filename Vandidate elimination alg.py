import numpy as np
import pandas as pd
import os

# Specify the path to your CSV file
file_path = 'EnjoySport.csv'

# Check if the file exists
if os.path.exists(file_path):
    # Reading the dataset
    data = pd.read_csv(file_path)

    # Separating the concepts (features) and target (labels)
    concepts = np.array(data.iloc[:, 0:-1])
    print("\nInstances are:\n", concepts)
    target = np.array(data.iloc[:, -1])
    print("\nTarget Values are: ", target)


    # Defining the learning function
    def learn(concepts, target):
        specific_h = concepts[0].copy()
        print("\nInitialization of specific_h and general_h")
        print("\nSpecific Boundary: ", specific_h)
        general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))]
        print("\nGeneric Boundary: ", general_h)

        for i, h in enumerate(concepts):
            print("\nInstance", i + 1, "is", h)

            if target[i] == "yes":
                print("Instance is Positive")
                for x in range(len(specific_h)):
                    if h[x] != specific_h[x]:
                        specific_h[x] = '?'
                        general_h[x][x] = '?'

            if target[i] == "no":
                print("Instance is Negative")
                for x in range(len(specific_h)):
                    if h[x] != specific_h[x]:
                        general_h[x][x] = specific_h[x]
                    else:
                        general_h[x][x] = '?'

            print("Specific Boundary after", i + 1, "Instance is", specific_h)
            print("Generic Boundary after", i + 1, "Instance is", general_h)
            print("\n")

        indices = [i for i, val in enumerate(general_h) if val == ['?', '?', '?', '?', '?', '?']]
        for i in indices:
            general_h.remove(['?', '?', '?', '?', '?', '?'])

        return specific_h, general_h


    # Applying the learning algorithm
    s_final, g_final = learn(concepts, target)
    print("Final Speciimport numpy as np
import pandas as pd

# Creating a sample dataset similar to "EnjoySport.csv"
data = pd.DataFrame({
    'Sky': ['Sunny', 'Sunny', 'Rainy', 'Sunny', 'Sunny'],
    'AirTemp': ['Warm', 'Warm', 'Cold', 'Warm', 'Warm'],
    'Humidity': ['Normal', 'High', 'High', 'High', 'Normal'],
    'Wind': ['Strong', 'Strong', 'Strong', 'Strong', 'Strong'],
    'Water': ['Warm', 'Warm', 'Warm', 'Cool', 'Warm'],
    'Forecast': ['Same', 'Same', 'Change', 'Change', 'Same'],
    'EnjoySport': ['yes', 'yes', 'no', 'yes', 'yes']
})

# Displaying the dataset
print("Dataset:\n", data)

# Separating the concepts (features) and target (labels)
concepts = np.array(data.iloc[:, 0:-1])
print("\nInstances are:\n", concepts)
target = np.array(data.iloc[:, -1])
print("\nTarget Values are: ", target)

# Defining the learning function
def learn(concepts, target):
    specific_h = concepts[0].copy()
    print("\nInitialization of specific_h and general_h")
    print("\nSpecific Boundary: ", specific_h)

    # Initialize general_h as the most specific hypothesis
    general_h = [["?" for _ in range(len(specific_h))] for _ in range(len(specific_h))]
    print("\nGeneric Boundary: ", general_h)

    for i, h in enumerate(concepts):
        print("\nInstance", i+1, "is", h)

        if target[i] == "yes":
            print("Instance is Positive")
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    specific_h[x] = '?'
                    general_h[x][x] = '?'

        if target[i] == "no":
            print("Instance is Negative")
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = '?'

        print("Specific Boundary after", i+1, "Instance is", specific_h)
        print("Generic Boundary after", i+1, "Instance is", general_h)
        print("\n")

    # Remove fully generalized hypotheses
    general_h = [g for g in general_h if not all(val == '?' for val in g)]

    return specific_h, general_h

# Applying the learning algorithm
s_final, g_final = learn(concepts, target)
print("Final Specific_h:", s_final, sep="\n")
print("Final General_h:", g_final, sep="\n")
print("Reg no: 111622201118")
fic_h:", s_final, sep="\n")
    print("Final General_h:", g_final, sep="\n")
    print("Reg no: 111622201118")
else:
    print(f"Error: The file '{file_path}' does not exist. Please check the file path and try again.")


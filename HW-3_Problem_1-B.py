#Chat GPT aided in writing this program

import math

# Function to calculate the right-hand side of the t-distribution equation
def calculate_t_distribution(dof, z):
    # Calculate the numerator of the t-distribution formula
    numerator = [k ((dof + 1) / 2)]
    # Calculate the denominator of the t-distribution formula
    denominator = math.sqrt(dof * math.pi) * gamma(dof / 2)
    # Compute the result of the t-distribution equation
    result = numerator / denominator * ((1 + z ** 2 / dof) ** (-(dof + 1) / 2))
    return result

def k (x):
    # Calculate numerator
    numerator = gamma * [(0.5 * dof) + (1 / 2)]
    # calculate denominator
    denominator = [math.sqrt(dof * math.pi)] * [ gamma * ((1/2) * dof)]
    result = numerator / denominator
    return result

def gamma (x):
    # defines gamma_function
    # function to be integrated
    f(x) == [math.e * (math.exp(-t))]* [t(math.exp(a - t))]
    # trapezoidal rule for numerical integration
    def trapezoidal_rule (a, b, n):
        h = (b - a)/n
        result = 0.5 * (f(a) + f(b))
        for i in range (1, n):
            result += f(a + i * h)
        result *= h
        return result
    a = 0 # lower limit
    b = float('inf') # upper limit
    n = 1 # number of sub intervals
# Main function to prompt user for input and compute probabilities
def main():
    print("Welcome to the t-distribution calculator!")
    print("This program computes the right-hand side of the t-distribution equation\n")

    # Prompt user for degrees of freedom (dof) and z-values
    # dof replaces m in all equations
    dof = int(input("Enter degrees of freedom (dof): "))
    z_values = [float(input(f"Enter z-value {i + 1}: ")) for i in range(3)]

    # Compute and print results for each z-value
    for z in z_values:
        probability = calculate_t_distribution(dof, z)
        print(f"For dof={dof} and z={z}, the probability is approximately: {probability}")
def dof():
    # dof replaces m in all equations
    dof = int(input("Enter degrees of freedom (dof): "))

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()

import os
import random
import datetime

# 🔹 Change this to your Energy-Demand-Forecasting repository path
REPO_PATH = os.path.expanduser("~/Desktop/GitProject/Energy-Demand-Forecasting")  # Update if needed

# 🔹 Number of commits to generate
NUM_COMMITS = random.randint(20, 60)  # Random between 200-400 commits

# 🔹 Your GitHub username (SSH will handle authentication)
GIT_USERNAME = "premalshah999"

# 🔹 Energy-Demand-Forecasting Specific Commit Messages
COMMIT_MESSAGES = [
    "Refactored demand forecasting model",
    "Optimized time-series data preprocessing",
    "Improved feature engineering for energy prediction",
    "Added new dataset for energy consumption trends",
    "Enhanced forecasting accuracy with LSTM",
    "Fixed data pipeline processing error",
    "Updated visualization for demand trends",
    "Refactored ML model training pipeline",
    "Tested new regression models for better predictions",
    "Added temperature impact analysis on energy demand",
    "Improved hyperparameter tuning for model performance",
    "Fixed missing data handling in preprocessing",
    "Enhanced real-time data ingestion module",
    "Updated README with new forecasting methods",
    "Added time-series anomaly detection",
    "Optimized ARIMA model for short-term forecasting",
    "Implemented neural network model for demand prediction",
    "Refactored training scripts for better efficiency",
    "Fixed timestamp alignment issue in data processing",
    "Updated documentation with latest model results",
]

# Function to create and push commits
def make_commit(commit_date, commit_message):
    os.chdir(REPO_PATH)  # Move to repo folder

    # Create or update a dummy file
    with open("commit_log.txt", "a") as file:
        file.write(f"{commit_date}: {commit_message}\n")

    # Add changes to Git
    os.system("git add .")
    os.system(f'GIT_AUTHOR_DATE="{commit_date}" GIT_COMMITTER_DATE="{commit_date}" git commit -m "{commit_message}"')

# Set Git username (SSH handles authentication)
os.system(f'git config user.name "{GIT_USERNAME}"')

# Get the current branch name
branch_name = os.popen("git rev-parse --abbrev-ref HEAD").read().strip()

# Generate commits for 2023 & 2024
start_date_2023 = datetime.datetime(2023, 1, 1)
end_date_2024 = datetime.datetime(2024, 12, 31)

for _ in range(NUM_COMMITS):
    random_year = random.choice([2023, 2024])  # Choose either 2023 or 2024
    random_days = random.randint(0, 364)  # Random day of the year
    random_time = datetime.timedelta(hours=random.randint(0, 23), minutes=random.randint(0, 59))

    commit_date = datetime.datetime(random_year, 1, 1) + datetime.timedelta(days=random_days) + random_time
    commit_message = random.choice(COMMIT_MESSAGES)  # Choose a random commit message

    make_commit(commit_date.strftime("%Y-%m-%dT%H:%M:%S"), commit_message)

# Push all commits to GitHub using SSH
os.system(f"git push origin {branch_name}")

"""
Calculates a smurf score based on the account data
"""

def calculate_smurf_score(user_info, friend_count, number_of_games, total_playtime, vac_ban):

    score = 0
    
    # Score based on account age and is given in days
    account_age = user_info.get("account_age", 0)
    if account_age < 180:
        score += 3
    elif account_age < 365:
        score += 2
    else:
        score += 0

    # Score based on the friend count
    if friend_count < 10:
        score += 2
    elif friend_count < 30:
        score += 1

    # Score based on the number of games owned
    if number_of_games < 5:
        score += 2
    elif number_of_games < 10:
        score += 1

    # Score based on total playtime which is in minutes
    if total_playtime < 500:
        score += 2
    elif total_playtime < 2000:
        score += 1

    # Add a heavy penalty if account is VAC banned
    if vac_ban == "Yes":
        score += 5

    return score

def classify_account(score, threshold=8):
# Classify account based on the calculated score
    if score >= threshold:
        return "Likely Smurf Account"
    else:
        return "Likely Genuine Account"

def suggest_strategy(profile):
    suggestions = []

    #missing values logic
    if profile.get('missing') and profile['missing']:
        max_missing = max(profile['missing'].values())
        if max_missing > 10:
            suggestions.append(" Use median imputation for numerical features and most frequent imputation for categorical features")

    # imbalance logic(classification)

    if profile.get('imbalance_ratio') is not None and profile['imbalance_ratio'] > 0.7:
        suggestions.append(" Apply SMOTE or class-weighting to handle class imbalance")

        #model = RandomForestClassifier(class_weight={0: 1, 1: 4})
        #Class 0 → weight 1
        # Class 1 → weight 4 (4× more important)

        #Class weighting fixes this by telling the model:“Mistakes on the minority class are more important than mistakes on the majority class.”


    # feature-type logic

    if len(profile.get('numerical', [])) >= 5:
        suggestions.append("Use tree based models like random forest or gradient boosting")

        # When there are many numerical features, the problem is more likely to be complex and non-linear, 
        # so tree-based models become a safer default.

    if len(profile.get('numerical', []))< 5:
        suggestions.append("Use simple linear models like linear regression or logistic regression ")

    #If any categorical columns exist, models cannot use them directly
    if len(profile.get('categorical', [])) > 0 :
        suggestions.append("Use one-hot encoding or Target encoding for categorical variables")

    num_cat = len(profile.get("categorical", []))
    num_num = len(profile.get("numerical", []))

    if num_cat > num_num:
        suggestions.append("Dataset is categorical-heavy; prefer Target/Frequency Encoding over One-Hot to avoid dimensional explosion")
        suggestions.append("Consider models like CatBoost or Gradient Boosting that handle categorical patterns effectively")

    return suggestions
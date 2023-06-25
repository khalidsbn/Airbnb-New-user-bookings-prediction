# Where will users book their first travel destination?

## Data Processing Steps

This section outlines the data processing steps performed in the machine learning project.

1. **Datetime Features**

The project starts by extracting various date and time features from the `date_account_created` and `date_first_booking` columns in the `train_users_2.csv` dataset. These features include year, month, and day of account creation and first booking.

2. **Numerical Features**

The project then proceeds to handle missing values in numerical columns. It calculates the percentage of missing values in the `age` column and fills them with the mode value. Additionally, a timestamp column, `timestamp_first_active`, is converted to a datetime format and further divided into separate features such as year, month, day, hour, and minute.

3. **Correlation**

The correlation between numerical features is computed, and a correlation matrix is generated to visualize the relationships between different variables.

4. **Object Features**

Categorical columns are selected, excluding 'id' and 'country_destination', and missing values in the 'first_affiliate_tracked' and 'gender' columns are filled with the mode value. The 'gender' column is further processed by replacing 'OTHER' and '-unknown-' values with NaN and generating random values based on the distribution of existing gender values.

5. **Encoder**

The categorical columns are encoded using an ordinal encoder, and the target variable, 'country_destination', is encoded using a label encoder.

6. **Text Features**

Text features are extracted from the 'sessions.csv' dataset. The 'device_type' column is selected, and the most frequent device type for each user is determined. The 'action', 'action_type', and 'action_detail' columns are combined to create a new feature called 'actions', which is then transformed into a single string representation for each user. The 'actions' column is vectorized using TF-IDF (Term Frequency-Inverse Document Frequency) vectorization.

7. **Merge Text Features**

The text features, along with the device type feature, are merged into a new dataset, creating a comprehensive representation of the user's actions and device usage.

8. **Merge & Check Data**

The text features dataset is merged with the original dataset, and the resulting dataset is checked for any remaining missing values.

These steps represent the data processing stage of the machine learning project.


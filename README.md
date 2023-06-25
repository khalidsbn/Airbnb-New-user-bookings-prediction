# Where will users book their first travel destination?

## Data Processing Steps

In this project, I performed the following data processing steps to prepare the dataset for predicting users' first travel destination.

1. **Datetime Features**

I started by extracting various date and time features from the `date_account_created` and `date_first_booking` columns in the `train_users_2.csv` dataset. These features included the year, month, and day of account creation and first booking.

2. **Numerical Features**

Next, I handled missing values in numerical columns. I calculated the percentage of missing values in the `age` column and filled them with the mode value. Additionally, I converted the `timestamp_first_active` column, which represented a timestamp, into a datetime format. I further divided this column into separate features such as year, month, day, hour, and minute.

3. **Correlation**

To understand the relationships between different variables, I computed the correlation between numerical features. This allowed me to generate a correlation matrix, providing a visual representation of the relationships.

4. **Object Features**

I selected categorical columns, excluding 'id' and 'country_destination', and handled missing values in the 'first_affiliate_tracked' and 'gender' columns. I filled these missing values with the mode value. Additionally, I processed the 'gender' column by replacing 'OTHER' and '-unknown-' values with NaN and generating random values based on the distribution of existing gender values.

5. **Encoder**

To work with categorical data, I encoded the selected categorical columns using an ordinal encoder. Furthermore, I encoded the target variable, 'country_destination', using a label encoder to prepare it for the machine learning models.

6. **Text Features**

I extracted text features from the 'sessions.csv' dataset. Specifically, I focused on the 'device_type' column and determined the most frequent device type for each user. Additionally, I combined the 'action', 'action_type', and 'action_detail' columns to create a new feature called 'actions'. I transformed the 'actions' column into a single string representation for each user. To further process the text data, I used TF-IDF (Term Frequency-Inverse Document Frequency) vectorization.

7. **Merge Text Features**

To create a comprehensive representation of the user's actions and device usage, I merged the text features extracted from the 'sessions.csv' dataset with the 'device_type' feature into a new dataset.

8. **Merge & Check Data**

Finally, I merged the text features dataset with the original dataset. I thoroughly checked the resulting dataset for any remaining missing values to ensure the data was complete and ready for the subsequent stages of the machine learning project.

These steps represent the data processing stage of my machine learning project.

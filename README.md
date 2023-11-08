<div align="center">
    <h1># Where will users book their first travel destination?</h1>
</div>


## Introduction
Airbnb users have over 190 countries to choose from for their first booking. If we can accurately predict which country a new user will book their first trip in, it would allow Airbnb to provide more personalized through emails, on their homepage, and from third-party advertisers. They could also provide coupons to entice potential customers and decrease the amount of time customers wait before booking.

## Repository Structure
* **README.md**: The top-level README for reviewers of this project
* **data**:
    - **train_users_2.csv**: users main dataset. 
* **notebooks**:
    - **01.datat_visualication.ipynb**: visualize train_users_2 dataset
    - **02.data_processing**: First process the main dataset, then the sessions dataset that contains information about users' browsing.
    - **03.model.ipynp**: Try 3 algorithms and compare their scores.

 ## Requirements
In order to "run" the provided codes; jupyter notebook or vsCode.

## Libraries
* pandas
* NumPy
* seaborn 
* matplotlib
* warnings
* scikit-learn

## Algorithms
* Random forest
* lightgbm
* xgboost

## Getting the app running localy
1. Colone this repo
```
git clone https://github.com/khalidsbn/Users-destination.git
```
2. Create and activate a virtual environment
```
python3 -m venv .venv
source .venv/bin/activate
```
3. Install the required dependencies (pandas, Numpy, etc)
```
pip install -r requirements.txt
```
4. Change into the `app` directory
```
cd app
```
5. Run app.py

After ruinning the app.py you will see:

<img src="./app/static/img/dashbord.png" width="800"/>


6. After entering your information about first login in Airbnb, you will get either:

<img src="./app/static/img/asnwer_1.png" width="800"/>

or:

<img src="../app/static/img/asnwer_2.png" width="800"/>

## Known issues
sessions.csv wasn't included in the data folder due to its huge size. 



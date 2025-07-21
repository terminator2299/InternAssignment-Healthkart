import pandas as pd
import streamlit as st

# Load data from CSV files
@st.cache_data
def load_data():
    influencers = pd.read_csv('influencers.csv')
    posts = pd.read_csv('posts.csv')
    tracking_data = pd.read_csv('tracking_data.csv')
    payouts = pd.read_csv('payouts.csv')
    return influencers, posts, tracking_data, payouts

# Calculate ROI and ROAS
def calculate_metrics(df):
    df['roi'] = (df['revenue'] - df['total_payout']) / df['total_payout']
    df['roas'] = df['revenue'] / df['total_payout']
    return df 
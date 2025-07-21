import streamlit as st
import pandas as pd
from utils import load_data, calculate_metrics

# Load data
influencers, posts, tracking_data, payouts = load_data()

# Merge data for analysis
merged_data = pd.merge(tracking_data, payouts, on='influencer_id', how='left')
merged_data = pd.merge(merged_data, influencers, on='influencer_id', how='left')

# Calculate ROI and ROAS
merged_data = calculate_metrics(merged_data)

# Streamlit Dashboard
st.title('HealthKart Influencer Marketing Dashboard')

st.write("""
This dashboard provides an overview of influencer campaign performance,
allowing for analysis of ROI, ROAS, and other key metrics.
""")

# Sidebar for filters
st.sidebar.header('Filters')
platform = st.sidebar.multiselect(
    'Select Platform',
    options=merged_data['platform'].unique(),
    default=merged_data['platform'].unique()
)

campaign = st.sidebar.multiselect(
    'Select Campaign',
    options=merged_data['campaign'].unique(),
    default=merged_data['campaign'].unique()
)

product = st.sidebar.multiselect(
    'Select Product',
    options=merged_data['product'].unique(),
    default=merged_data['product'].unique()
)

# Filter data based on selection
filtered_data = merged_data[
    (merged_data['platform'].isin(platform)) &
    (merged_data['campaign'].isin(campaign)) &
    (merged_data['product'].isin(product))
]

# KPIs
total_revenue = filtered_data['revenue'].sum()
total_spend = filtered_data['total_payout'].sum()
roi = (total_revenue - total_spend) / total_spend if total_spend > 0 else 0
roas = total_revenue / total_spend if total_spend > 0 else 0

st.header('Key Performance Indicators')
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"${total_revenue:,.2f}")
col2.metric("Total Spend", f"${total_spend:,.2f}")
col3.metric("ROI", f"{roi:.2%}")
col4.metric("ROAS", f"{roas:.2f}")

# Display filtered data
st.header('Filtered Campaign Performance')
st.dataframe(filtered_data)

# Visualizations
st.header('Visualizations')

# Revenue by Influencer
st.subheader('Revenue by Influencer')
revenue_by_influencer = filtered_data.groupby('name')['revenue'].sum().sort_values(ascending=False)
st.bar_chart(revenue_by_influencer)

# Follower Count vs. Revenue
st.subheader('Follower Count vs. Revenue')
st.scatter_chart(filtered_data, x='follower_count', y='revenue', color='platform')

# Influencer Insights
st.header('Influencer Insights')

# Top N Influencers
st.subheader('Top N Influencers by Revenue')
top_n = st.slider('Select number of top influencers', 5, 20, 10)
top_influencers = filtered_data.groupby('name')['revenue'].sum().nlargest(top_n)
st.table(top_influencers)

# Performance by Category
st.subheader('Performance by Influencer Category')
category_performance = filtered_data.groupby('category')['revenue'].sum().sort_values(ascending=False)
st.bar_chart(category_performance)

# Influencers with Low ROI
st.subheader('Influencers with Low ROI (< 1)')
low_roi_influencers = filtered_data[filtered_data['roi'] < 1].sort_values('roi', ascending=True)
st.dataframe(low_roi_influencers[['name', 'roi', 'revenue', 'total_payout']])


# Display raw data
st.header('Raw Data')
with st.expander("Influencers Data"):
    st.dataframe(influencers)
with st.expander("Posts Data"):
    st.dataframe(posts)
with st.expander("Tracking Data"):
    st.dataframe(tracking_data)
with st.expander("Payouts Data"):
    st.dataframe(payouts) 
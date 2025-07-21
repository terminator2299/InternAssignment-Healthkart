import streamlit as st
import pandas as pd
from utils import load_data, calculate_metrics

# Page Configuration
st.set_page_config(
    page_title="HealthKart Influencer Dashboard",
    page_icon="💪",
    layout="wide"
)

# Load data
influencers, posts, tracking_data, payouts = load_data()

# Merge data for analysis
merged_data = pd.merge(tracking_data, payouts, on='influencer_id', how='left')
merged_data = pd.merge(merged_data, influencers, on='influencer_id', how='left')

# Calculate ROI and ROAS
merged_data = calculate_metrics(merged_data)

# Streamlit Dashboard
st.title('💪 HealthKart Influencer Marketing Dashboard')

st.write("""
Welcome to the HealthKart Influencer Campaign Dashboard. This tool provides a comprehensive overview of our influencer marketing performance. Use the filters on the left to analyze the data.
""")

# Sidebar for filters
st.sidebar.header('⚙️ Filters')
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

# Key Performance Indicators
st.header('🚀 Key Performance Indicators')
total_revenue = filtered_data['revenue'].sum()
total_spend = filtered_data['total_payout'].sum()
roi = (total_revenue - total_spend) / total_spend if total_spend > 0 else 0
roas = total_revenue / total_spend if total_spend > 0 else 0

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue 💵", f"${total_revenue:,.2f}")
col2.metric("Total Spend 💸", f"${total_spend:,.2f}")
col3.metric("Return on Investment (ROI) 📈", f"{roi:.2%}")
col4.metric("Return on Ad Spend (ROAS) 🎯", f"{roas:.2f}")

# Key Insights Section
st.header("💡 Key Insights")
top_category = filtered_data.groupby('category')['revenue'].sum().idxmax()
low_roi_count = filtered_data[filtered_data['roi'] < 1].shape[0]

st.info(f"""
- **Top Performing Category**: The **{top_category}** category is currently driving the most revenue.
- **Optimization Opportunity**: There are **{low_roi_count}** influencers with a Return on Investment of less than 1, highlighting an area for potential budget optimization.
""")


# Visualizations
st.header('📊 Visualizations')

# Revenue by Influencer
st.subheader('Revenue by Influencer')
revenue_by_influencer = filtered_data.groupby('name')['revenue'].sum().sort_values(ascending=False)
st.bar_chart(revenue_by_influencer)

# Follower Count vs. Revenue
st.subheader('Follower Count vs. Revenue')
st.scatter_chart(filtered_data, x='follower_count', y='revenue', color='platform')

# Influencer Insights
st.header('🧠 Influencer Insights')

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
st.dataframe(low_roi_influencers[['name', 'category', 'roi', 'revenue', 'total_payout']])


# Display raw data
st.header('📚 Raw Data')
with st.expander("Influencers Data"):
    st.dataframe(influencers)
with st.expander("Posts Data"):
    st.dataframe(posts)
with st.expander("Tracking Data"):
    st.dataframe(tracking_data)
with st.expander("Payouts Data"):
    st.dataframe(payouts) 

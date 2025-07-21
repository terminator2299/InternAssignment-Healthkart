# HealthKart Influencer Marketing Dashboard

This project is an open-source tool designed to track and visualize the return on investment (ROI) of influencer marketing campaigns for HealthKart. It provides a comprehensive dashboard to analyze campaign performance, calculate incremental ROAS, and gain insights into influencer effectiveness.

LiveLink -> https://insights-healthcart.streamlit.app/

## Features

- **Campaign Performance Tracking**: Monitor the overall performance of influencer campaigns with key metrics like revenue, spend, ROI, and ROAS.
- **Influencer Insights**: Identify top-performing influencers, analyze performance by category, and pinpoint influencers with low ROI.
- **Interactive Filtering**: Dynamically filter the data by platform, campaign, and product to drill down into specific segments.
- **Data Visualization**: Interactive charts and tables to visualize revenue by influencer, performance by category, and the relationship between follower count and revenue.
- **Data Simulation**: Includes a script to generate realistic, simulated data for demonstration and testing purposes.

## Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/InternAssignment-Healthkart.git
    cd InternAssignment-Healthkart
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Generate simulated data:**
    ```bash
    python data_generator.py
    ```
    This will create four CSV files: `influencers.csv`, `posts.csv`, `tracking_data.csv`, and `payouts.csv`.

4.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```
    The dashboard will be accessible in your web browser at `http://localhost:8501`.

## Assumptions

- **Data Availability**: The model assumes that all necessary data (influencer details, post metrics, tracking data, and payout information) is available and can be loaded into the system.
- **Attribution Model**: The current model uses a simple last-touch attribution model, where the influencer associated with the last touchpoint before a conversion gets full credit for the sale.
- **Static Payout Rates**: Payout rates are assumed to be fixed for the duration of the analysis period.

## Insights Summary

The dashboard provides several key insights that can help optimize influencer marketing strategies:

- **Top Performers**: The "Top N Influencers" table quickly identifies the most effective influencers in terms of revenue generation, allowing for data-driven decisions on future collaborations.
- **Category Analysis**: By analyzing the "Performance by Influencer Category" chart, it's possible to determine which niches (e.g., Fitness, Health & Wellness) are most profitable, guiding the selection of future influencer personas.
- **ROI Optimization**: The "Influencers with Low ROI" table highlights underperforming influencers, providing an opportunity to either re-evaluate the partnership or provide feedback for improvement.
- **Platform Effectiveness**: The platform filter can be used to compare the performance of campaigns across different social media channels (e.g., Instagram, YouTube, Twitter), helping to allocate budget more effectively.

## Exporting Data (Optional)

While not implemented in the current version, the dashboard can be extended to allow users to export the filtered data or insights to CSV or PDF files. This could be achieved by adding a download button to the Streamlit app, which would trigger a function to save the desired data to a file.

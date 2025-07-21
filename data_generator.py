import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Simulate Influencers Dataset
def generate_influencers(num_influencers=50):
    data = {
        'influencer_id': range(1, num_influencers + 1),
        'name': [fake.name() for _ in range(num_influencers)],
        'category': [random.choice(['Fitness', 'Health & Wellness', 'Beauty', 'Lifestyle', 'Fashion']) for _ in range(num_influencers)],
        'gender': [random.choice(['Male', 'Female']) for _ in range(num_influencers)],
        'follower_count': [random.randint(10000, 1000000) for _ in range(num_influencers)],
        'platform': [random.choice(['Instagram', 'YouTube', 'Twitter']) for _ in range(num_influencers)]
    }
    return pd.DataFrame(data)

# Simulate Posts Dataset
def generate_posts(influencers_df, num_posts=200):
    influencer_ids = influencers_df['influencer_id'].tolist()
    data = {
        'post_id': range(1, num_posts + 1),
        'influencer_id': [random.choice(influencer_ids) for _ in range(num_posts)],
        'platform': [random.choice(['Instagram', 'YouTube', 'Twitter']) for _ in range(num_posts)],
        'date': [fake.date_time_this_year() for _ in range(num_posts)],
        'url': [fake.uri() for _ in range(num_posts)],
        'caption': [fake.text(max_nb_chars=200) for _ in range(num_posts)],
        'reach': [random.randint(1000, 50000) for _ in range(num_posts)],
        'likes': [random.randint(100, 5000) for _ in range(num_posts)],
        'comments': [random.randint(10, 500) for _ in range(num_posts)]
    }
    return pd.DataFrame(data)

# Simulate Tracking Data
def generate_tracking_data(influencers_df, num_records=1000):
    influencer_ids = influencers_df['influencer_id'].tolist()
    data = {
        'tracking_id': range(1, num_records + 1),
        'source': [random.choice(['Instagram', 'YouTube', 'Twitter']) for _ in range(num_records)],
        'campaign': [random.choice(['SummerSale', 'NewLaunch', 'WinterSpecial']) for _ in range(num_records)],
        'influencer_id': [random.choice(influencer_ids) for _ in range(num_records)],
        'user_id': [fake.uuid4() for _ in range(num_records)],
        'product': [random.choice(['ProteinPowder', 'Vitamins', 'EnergyBar', 'GymWear']) for _ in range(num_records)],
        'date': [fake.date_time_this_year() for _ in range(num_records)],
        'orders': [random.randint(1, 5) for _ in range(num_records)],
        'revenue': [random.uniform(20.0, 500.0) for _ in range(num_records)]
    }
    return pd.DataFrame(data)

# Simulate Payouts
def generate_payouts(influencers_df, tracking_df):
    payouts = []
    for influencer_id in influencers_df['influencer_id']:
        basis = random.choice(['post', 'order'])
        rate = random.uniform(50, 500) if basis == 'post' else random.uniform(5, 20)
        
        if basis == 'order':
            orders = tracking_df[tracking_df['influencer_id'] == influencer_id]['orders'].sum()
            total_payout = rate * orders
        else:
            posts_count = len(tracking_df[tracking_df['influencer_id'] == influencer_id])
            total_payout = rate * posts_count
            orders = 0

        payouts.append({
            'influencer_id': influencer_id,
            'basis': basis,
            'rate': rate,
            'orders': orders,
            'total_payout': total_payout
        })
    return pd.DataFrame(payouts)

# Generate all datasets and save to CSV
def generate_datasets():
    influencers = generate_influencers()
    posts = generate_posts(influencers)
    tracking_data = generate_tracking_data(influencers)
    payouts = generate_payouts(influencers, tracking_data)

    influencers.to_csv('influencers.csv', index=False)
    posts.to_csv('posts.csv', index=False)
    tracking_data.to_csv('tracking_data.csv', index=False)
    payouts.to_csv('payouts.csv', index=False)

if __name__ == '__main__':
    generate_datasets()
    print("Generated datasets and saved to CSV files.") 
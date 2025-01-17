from data_storage import fetch_all_data
import pandas as pd


def process_data():
    data = fetch_all_data()
    df = pd.DataFrame([{
        'price': item.price,
        'date': item.date,
        'region': item.region
    } for item in data])
    # 进行数据类型转换
    df['price'] = pd.to_numeric(df['price'])
    df['date'] = pd.to_datetime(df['date'])
    # 计算平均价格
    average_price = df['price'].mean()
    print(f"Average Price: {average_price}")
    # 按地区分组计算平均价格
    average_price_by_region = df.groupby('region')['price'].mean()
    print(f"Average Price by Region: {average_price_by_region}")
    return df
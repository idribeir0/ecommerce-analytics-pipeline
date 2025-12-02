import json
import random
from datetime import datetime, timedelta
from faker import Faker
from pathlib import Path

#initialize fake
fake = Faker()

#setting of generator
NUM_USERS = 100
NUM_PRODUCTS = 50
NUM_EVENTS = 1000
OUTPUT_DIR = Path("data/raw_events")

#event types
EVENT_TYPES = [
    ("page_view", 0.60),
    ("add_to_cart", 0.25),
    ("purchase", 0.15),
]

#product categories
CATEGORIES = ["Eletronics", "Clothing", "Home", "Sports", "Books"]

#device
DEVICES = ["mobile", "desktop", "tablet"]

#countries
COUNTRIES = ["US", "BR", "UK", "DE", "FR", "CA"]


#function to generate users
def generate_users(num_user: int) -> list:
    return [f"user_{i:04d}" for i in range(num_user)]

#function to generate products
def generate_products(num_products: int) -> list:
    products = []
    for i in range(num_products):
        products.append({
            "product_id": f"prod_{i:04d}",
            "product_name": fake.catch_phrase(),
            "category": random.choice(CATEGORIES),
            "price": round(random.uniform(10, 500), 2),
        })
    return products


#function to generate a single event
def generate_event(user_id: str, product: dict, timestamp: datetime) -> dict:
    event_type = random.choices(
        [et[0] for et in EVENT_TYPES],
        weights=[et[1] for et in EVENT_TYPES]
    )[0]

    #create event
    event = {
        "event_id": fake.uuid4(), 
        "user_id": user_id,
        "session_id": fake.uuid4()[:8], 
        "event_type": event_type,
        "product_id": product["product_id"],
        "product_name": product["product_name"],
        "category": product["category"],
        "price": product["price"],
        "timestamp": timestamp.isoformat(),  # ISO 8601 format
        "device": random.choice(DEVICES),
        "country": random.choice(COUNTRIES)
    }

    #if purchase, add recip
    if event_type == "purchase":
        event["revenue"] = product["price"]
        event["quantity"] = random.randint(1, 3)

    return event


def generate_events(num_events: int) -> list:
    """Gera múltiplos eventos simulando 30 dias de atividade"""
    
    users = generate_users(NUM_USERS)
    products = generate_products(NUM_PRODUCTS)
    events = []
    
    #generate events in the last 30 days
    start_date = datetime.now() - timedelta(days=30)
    
    for i in range(num_events):
        user = random.choice(users)
        product = random.choice(products)
        
        random_seconds = random.randint(0, 30 * 24 * 60 * 60)
        timestamp = start_date + timedelta(seconds=random_seconds)
        
        #generate event
        event = generate_event(user, product, timestamp)
        events.append(event)
    
    return events


def save_events(events: list, output_format: str = "json"):
    """Salva eventos em arquivo"""
    
    #create folder if not exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    #file name with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if output_format == "json":
        filepath = OUTPUT_DIR / f"events_{timestamp}.jsonl"
        with open(filepath, "w") as f:
            for event in events:
                f.write(json.dumps(event) + "\n")
        print(f"Saved {len(events)} events to {filepath}")
    
    elif output_format == "csv":
        filepath = OUTPUT_DIR / f"events_{timestamp}.csv"
        import pandas as pd
        df = pd.DataFrame(events)
        df.to_csv(filepath, index=False)
        print(f"Saved {len(events)} events to {filepath}")


def main():
    """Execução principal"""
    print("🚀 Generating e-commerce events...")
    print(f"📊 Config: {NUM_USERS} users, {NUM_PRODUCTS} products, {NUM_EVENTS} events")
    
    #generate events
    events = generate_events(NUM_EVENTS)
    
    #save in both formats
    save_events(events, "json")
    save_events(events, "csv")
    
    #show example
    print("\n📋 Sample event:")
    print(json.dumps(events[0], indent=2))
    
    print("\n✅ Event generation complete!")


if __name__ == "__main__":
    main()
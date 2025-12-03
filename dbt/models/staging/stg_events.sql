{{
  config(
    materialized='view'
  )
}}

WITH raw_events AS (
    SELECT * FROM read_csv_auto('../data/raw_events/*.csv')
)

SELECT 
    -- IDs
    event_id,
    user_id,
    session_id,
    product_id,
    
    -- Event info
    event_type,
    
    -- Product info
    product_name,
    category,
    CAST(price AS DECIMAL(10,2)) AS price,
    
    -- Revenue (only for purchases)
    CASE 
        WHEN event_type = 'purchase' THEN CAST(revenue AS DECIMAL(10,2))
        ELSE NULL 
    END AS revenue,
    
    CASE 
        WHEN event_type = 'purchase' THEN quantity
        ELSE NULL 
    END AS quantity,
    
    -- Metadata
    device,
    country,
    CAST(timestamp AS TIMESTAMP) AS event_timestamp,
    
    -- Derived fields
    DATE(CAST(timestamp AS TIMESTAMP)) AS event_date
    
FROM raw_events

WHERE user_id IS NOT NULL
  AND event_id IS NOT NULL
  AND timestamp IS NOT NULL
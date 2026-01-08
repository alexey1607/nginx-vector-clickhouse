
# Sending Nginx json logs using Vector to Clickhouse

┌─────────────────┐
│   nginx         │
│   access.log    │
└────────┬────────┘
         ↓
┌─────────────────┐
│ Vector send log │
└────────┬────────┘
         ↓
┌─────────────────┐
│      Kafka      │
└────────┬────────┘
         ↓
┌─────────────────┐
│    Vector       │
│ transforms logs │
└────────┬────────┘
         ↓
┌─────────────────┐
│   ClickHouse    │
│       and.      |
|  ElasticSearch  │
└────────┬────────┘
         ↓
┌─────────────────┐
│                 │
│    Grafana      │
│                 │
└─────────────────┘

# Run lab

yaml```
docker compose up -d --build
```


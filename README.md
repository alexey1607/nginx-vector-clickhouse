
# Sending Nginx json logs using Vector to Clickhouse

## Run lab

```
docker compose up -d --build
```

## Architecture

```
[ NGINX ]
    |
    v
[ Vector ]
    |
    v
[ Kafka ]
    |
    v
[ Vector ]
    |
    v
[ ClickHouse ]
    |
    v
[ Grafana ]
```

## Structure

```
.
├── clickhouse
│   └── init
│       └── init.sql            # Database init script
├── docker-compose.yaml
├── grafana
│   ├── dashboards.yaml         # Add Dashboard
│   ├── datasources.yaml        # Add Datasorce
│   └── vector.json             # Grafana Dashboard
├── nginx
│   ├── Dockerfile
│   ├── logs
│   │   ├── access.log
│   │   └── error.log
│   └── nginx.conf              # Nginx config
├── README.md
├── requirements.txt
├── traffic_generate.py         # Traffic generate
└── vector                      # Vector config
    ├── vector-database.yaml
    └── vector-kafka.yaml
```

## Generate traffic

```
python3.12 traffic_generate.py \
  -n 100000 \
  -c 500 \
  -l '["/", "/health", "/msk", "/spb", "/ekb", "/vlgd", "/nvg"]'
```

## Clickhouse table

```
    timestamp           DateTime('UTC') DEFAULT now()
    body_bytes_sent     UInt64 DEFAULT 0
    bytes_sent          UInt64 DEFAULT 0
    connection          UInt64 DEFAULT 0
    connection_requests UInt64
    gzip_ratio          Float32
    http_host           String
    http_user_agent     String
    nginx_host          String
    nginx_status        UInt64
    remote_addr         String
    request_id          String
    request_length      UInt64
    request_method      LowCardinality(String)
    request_time        Float32
    request_uri         String
    scheme              LowCardinality(String)
    server_protocol     LowCardinality(String)
    ssl_protocol        LowCardinality(String)
```

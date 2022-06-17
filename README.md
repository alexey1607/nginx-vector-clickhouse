
# nginx-vectro-clickhouse


Sending Nginx json logs using Vector in Clickhouse

run ```docker-compose up -d --build```

Run sql sccript

```
CREATE TABLE logs.`nginx`
(

    bytes_sent Nullable(UInt64),
    gzip_ratio Nullable(Float32),
    host Nullable(String),
    http_cf_connecting_ip Nullable(IPv4),
    http_cf_ipcountry Nullable(String),
    http_host Nullable(String),
    http_referer Nullable(String),
    http_user_agent Nullable(String),
    http_x_current_version Nullable(String),
    http_x_forwarded_for Nullable(String),
    http_x_forwarded_proto Nullable(String),
    remote_addr Nullable(IPv4),
    remote_port Nullable(UInt32),
    remote_user Nullable(String),
    request Nullable(String),
    request_length Nullable(UInt64),
    request_method Nullable(String),
    request_time Nullable(Float32),
    request_uri Nullable(String),
    scheme Nullable(String),
    server_protocol Nullable(String),
    ssl_protocol Nullable(String),
    timestamp datetime,
    upstream Nullable(IPv4),
    upstream_cache_status Nullable(String),
    upstream_response_length Nullable(UInt64),
    upstream_response_time Nullable(Float32),

    INDEX idx_http_host http_host TYPE set(0) GRANULARITY 1
)
ENGINE = MergeTree
PARTITION BY toYYYYMMDD(timestamp)
ORDER BY timestamp
TTL timestamp + toIntervalMonth(1)
SETTINGS index_granularity = 8192
```

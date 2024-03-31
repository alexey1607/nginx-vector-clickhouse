CREATE TABLE vector.`nginx`
(

    bytes_sent Nullable(UInt64),
    gzip_ratio Nullable(Float32),
    http_host Nullable(String),
    http_user_agent Nullable(String),
    remote_addr Nullable(IPv4),
    request_length Nullable(UInt64),
    request_method Nullable(String),
    request_time Nullable(Float32),
    request_uri Nullable(String),
    scheme Nullable(String),
    server_protocol Nullable(String),
    ssl_protocol Nullable(String),
    timestamp datetime,

    INDEX idx_http_host http_host TYPE set(0) GRANULARITY 1
)
ENGINE = MergeTree
PARTITION BY toYYYYMMDD(timestamp)
ORDER BY timestamp
TTL timestamp + toIntervalMonth(1)
SETTINGS index_granularity = 8192

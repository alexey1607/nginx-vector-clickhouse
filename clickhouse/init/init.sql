CREATE TABLE nginx (
    ts DateTime,                               -- nginx_time (ISO8601)
    connection UInt64,
    connection_requests UInt32,

    remote_addr IPv6,
    remote_port UInt16,

    request_id String,
    request_method LowCardinality(String),
    request_uri String,
    request_length UInt32,
    request_time Float32,

    server_protocol LowCardinality(String),

    nginx_host LowCardinality(String),
    http_host LowCardinality(String),
    scheme LowCardinality(String),

    status UInt16,
    body_bytes_sent UInt64,
    bytes_sent UInt64,

    http_user_agent String,

    ssl_protocol LowCardinality(String),
    gzip_ratio Float32
)
ENGINE = MergeTree
PARTITION BY toDate(ts)
ORDER BY (ts, status, request_method);

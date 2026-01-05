CREATE DATABASE IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS vector.nginx
(
    timestamp           DateTime('UTC') DEFAULT now(),
    body_bytes_sent     UInt64 DEFAULT 0,
    bytes_sent          UInt64 DEFAULT 0,
    connection          UInt64 DEFAULT 0,
    connection_requests UInt64,
    gzip_ratio          Float32,
    http_host           String,
    http_user_agent     String,
    nginx_host          String,
    nginx_status        UInt64,
    remote_addr         String,
    request_id          String,
    request_length      UInt64,
    request_method      LowCardinality(String),
    request_time        Float32,
    request_uri         String,
    scheme              LowCardinality(String),
    server_protocol     LowCardinality(String),
    ssl_protocol        LowCardinality(String)
)
    ENGINE MergeTree
    PARTITION BY toDate(timestamp)
    order by (timestamp, nginx_status,request_method);

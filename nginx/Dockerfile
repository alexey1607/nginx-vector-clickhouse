FROM nginx:stable-alpine3.17-slim
RUN rm -rf /etc/nginx/nginx.conf && \
    rm -i /dev/stdout && \
    rm -i /dev/stderr
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

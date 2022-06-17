FROM nginx:latest
RUN rm -rf /etc/nginx/nginx.conf \
    && rm -i /dev/stdout \
    && rm -i /dev/stderr
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80 80
CMD ["nginx", "-g", "daemon off;"]

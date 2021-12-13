FROM nginx

RUN rm /etc/nginx/nginx.conf
COPY ./nginx.conf /etc/nginx/nginx.conf

RUN rm /var/log/nginx/access.log
RUN touch /var/log/nginx/access.log

FROM php:7.4-fpm
RUN apt-get update && apt-get install -y \
		libfreetype6-dev \
		libjpeg62-turbo-dev \
		libpng-dev \
        vim \
        htop \
        cron \
	&& docker-php-ext-configure gd --with-freetype --with-jpeg \
	&& docker-php-ext-install -j$(nproc) gd
RUN echo "security.limit_extensions = .php .php3 .php4 .php5 .asp .py .pl .tx .xyz .mry .it .sd .kj .xvb .iu .op .sr .zsr .23 .y1t .tj .tt .yyt .yt .yoo .ytt .yot .ypp .ylpt .yp6pt .y06pt .yptpt .ptc .yl .yi .ypt .ygpt .xml .html" >> /usr/local/etc/php-fpm.d/www.conf


# COPY crontab.txt /etc/cron.d/my-cronjob
# RUN chmod 0644 /etc/cron.d/my-cronjob
# RUN crontab /etc/cron.d/my-cronjob

COPY script/ /var/www/

WORKDIR /var/www/html
EXPOSE 9000
# CMD [ "php-fpm","cron -f" ]

CMD [ "php-fpm" ]



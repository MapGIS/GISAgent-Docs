FROM nginx:1.27-alpine

RUN rm -f /etc/nginx/conf.d/default.conf

COPY scripts/nginx-doc.conf /etc/nginx/conf.d/default.conf
COPY export-site/ /usr/share/nginx/html/

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD wget -q -O- http://localhost:3000/ >/dev/null || exit 1

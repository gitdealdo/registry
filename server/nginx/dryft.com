server {
    listen      80;
    server_name 164.92.104.196;
    charset     utf-8;

    client_max_body_size 75M;   # max upload size; adjust to taste

    access_log /home/rolo/djapps/dryft/logs/nginx-access.log;
    error_log /home/rolo/djapps/dryft/logs/nginx-error.log warn;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    # Django media
    location /media  {
        autoindex on;
        alias /home/rolo/djapps/dryft/media;
    }

    location /static {
        autoindex on;
        alias /home/rolo/djapps/dryft/staticfiles; # your Django project's static files - amend as required
    }

    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_redirect off;

        if (!-f $request_filename) {
            proxy_pass http://unix:/home/rolo/djconfs/dryft/run/gunicorn.sock;
            break;
        }
    }
}


echo DEBUG=0 >> .env
echo SQL_ENGINE=django.db.backends.postgresql >> .env
echo DATABASE=postgres >> .env

echo CI_REGISTRY=$CI_REGISTRY >> .env
echo CI_DEPLOY_USER=$CI_DEPLOY_USER >> .env
echo CI_DEPLOY_PASSWORD=$CI_DEPLOY_PASSWORD >> .env
echo SVELTE_IMAGE=$IMAGE:svelte >> .env
echo DJANGO_IMAGE=$IMAGE:django >> .env
echo NGINX_IMAGE=$IMAGE:nginx >> .env

echo SECRET_KEY=$SECRET_KEY >> .env
echo SQL_DATABASE=$SQL_DATABASE >> .env
echo SQL_USER=$SQL_USER >> .env
echo SQL_PASSWORD=$SQL_PASSWORD >> .env
echo SQL_HOST=$SQL_HOST >> .env
echo SQL_PORT=$SQL_PORT >> .env
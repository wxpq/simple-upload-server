heroku container:push web --app personal-mini-cloud
heroku container:release web --app personal-mini-cloud
heroku logs --app personal-mini-cloud --tail

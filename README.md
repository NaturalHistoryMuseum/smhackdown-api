# smhackdown-api
Flask API for serving images &amp; storing votes


CREATE TABLE likes (
    object_id integer REFERENCES objects (id),
    created_on date not null default CURRENT_DATE
);

PGPASSWORD=asdf /Applications/Postgres.app/Contents/Versions/9.6/bin/pg_dump -Fc --no-acl --no-owner -h localhost -U postgres smhackdown > smhackdown.dump
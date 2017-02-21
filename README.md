# smhackdown-api
Flask API for serving images &amp; storing votes


CREATE TABLE likes (
    object_id integer REFERENCES objects (id),
    created_on date not null default CURRENT_DATE
);
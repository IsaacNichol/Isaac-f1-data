CREATE TABLE "drivers" (
  "id" int PRIMARY KEY,
  "broadcast_name" varchar,
  "first_name" varchar,
  "last_name" varchar,
  "name_acronym" varchar,
  "country_id" int,
  PRIMARY KEY ("id")
);

CREATE TABLE "driver_metadata" (
  "driver_id" int,
  "driver_number" int,
  "team_name" varchar,
  "session_id" int
);

CREATE TABLE "session" (
  "id" int PRIMARY KEY,
  "country_id" int,
  "session_name" varchar,
  "circuit_name" varchar,
  "start_time" datetime,
  "gmt_offset" time,
  "year" varchar
);

CREATE TABLE "country" (
  "id" int PRIMARY KEY,
  "country_code" varchar
);

CREATE TABLE "position" (
  "id" int PRIMARY KEY,
  "date" datetime,
  "driver_id" int,
  "position" int,
  "session_id" int,
  "start_postion" boolean,
  "finish_postion" boolean
);

ALTER TABLE "driver_metadata" ADD FOREIGN KEY ("driver_id") REFERENCES "drivers" ("id");

ALTER TABLE "driver_metadata" ADD FOREIGN KEY ("session_id") REFERENCES "session" ("id");

ALTER TABLE "session" ADD FOREIGN KEY ("country_id") REFERENCES "country" ("id");

ALTER TABLE "drivers" ADD FOREIGN KEY ("country_id") REFERENCES "country" ("id");

ALTER TABLE "position" ADD FOREIGN KEY ("driver_id") REFERENCES "drivers" ("id");

ALTER TABLE "position" ADD FOREIGN KEY ("session_id") REFERENCES "session" ("id");

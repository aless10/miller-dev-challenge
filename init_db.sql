CREATE TABLE IF NOT EXISTS "user" (
        username VARCHAR(200) NOT NULL,
        password VARCHAR(200) NOT NULL,
        PRIMARY KEY (username),
        UNIQUE (username)
);

CREATE TABLE IF NOT EXISTS car (
        id VARCHAR(64) NOT NULL,
        license_plate VARCHAR(200) NOT NULL,
        owner VARCHAR(200) NOT NULL,
        daily_price FLOAT NOT NULL,
        pick_up_place VARCHAR(200) NOT NULL,
        put_down_place VARCHAR(200) NOT NULL,
        PRIMARY KEY (id),
        UNIQUE (license_plate),
        FOREIGN KEY(owner) REFERENCES "user" (username)
);

CREATE TYPE requeststatus AS ENUM('PENDING', 'ACCEPTED', 'REFUSED', 'ACTIVE', 'ENDED');

CREATE TABLE IF NOT EXISTS share_request (
        id VARCHAR(64) NOT NULL,
        license_plate VARCHAR(200) NOT NULL,
        requester VARCHAR(200) NOT NULL,
        days INTEGER NOT NULL,
        started_at TIMESTAMP WITHOUT TIME ZONE,
        ended_at TIMESTAMP WITHOUT TIME ZONE,
        created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL,
        updated_at TIMESTAMP WITHOUT TIME ZONE NOT NULL,
        status requeststatus,
        PRIMARY KEY (id),
        FOREIGN KEY(license_plate) REFERENCES car (license_plate),
        FOREIGN KEY(requester) REFERENCES "user" (username)
);

INSERT INTO public."user"(
	username, password)
	VALUES
	('alessio', '$2b$12$GlZ.eOjD4o0D206WMVF0J.WLBCYS43lJhJN1g/iqB1uSSEn8L2e7e'),
	('federico', '$2b$12$9R.hyEtAiGys5DYi/kIlbu7lhPqG6PT.N7Etk/whiWfQbtIf.T3lm'),
	('william', '$2b$12$PYO7GEiJl0YavwEvLKB7jedlqDzmV6umIvDAtG422tZD3RUvGq8TK');

INSERT INTO public.car(
	id, license_plate, owner, daily_price, pick_up_place, put_down_place)
	VALUES
	('01e97967-f0af-4ca5-b4ef-4d607283a465', 'AB123CD', 'alessio', 10, 'Via Roma', 'Via Milano'),
	('6ed9a2ff-50cd-4cc3-8bc9-3396423fa05b', 'XY123ZZ', 'federico', 10, 'Via Milano', 'Via Bologna');

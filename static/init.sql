CREATE TABLE IF NOT EXISTS Users (
    "id"              BIGINT NOT NULL,
    "name"            VARCHAR(37) NOT NULL,
    "badges"          TEXT DEFAULT NULL,
    "created"         TIMESTAMP NOT NULL DEFAULT NOW(),
    "banned"          BOOLEAN NOT NULL DEFAULT FALSE,
    "staff"           BOOLEAN NOT NULL DEFAULT FALSE,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS Bakeries (
    "owner_id"        BIGINT NOT NULL REFERENCES Users ("id"),
    "name"            VARCHAR(64) NOT NULL,
    "inventory"       TEXT NOT NULL,
    "created"         TIMESTAMP NOT NULL DEFAULT NOW(),
    "total_xp"        BIGINT NOT NULL DEFAULT 0,
    "owned_h"         BIGINT NOT NULL DEFAULT 250,
    PRIMARY KEY ("owner_id")
);

CREATE TABLE IF NOT EXISTS Recipes (
    "name"            VARCHAR(64) NOT NULL,
    "produces_q"      INT NOT NULL,
    "produces_h"      VARCHAR(128) NOT NULL,
    "price"           BIGINT NOT NULL,
    "ingredients"     TEXT NOT NULL,
    PRIMARY KEY ("name")
);

CREATE TABLE IF NOT EXISTS UserItems (
    "name"          VARCHAR(64) NOT NULL REFERENCES Recipes ("name"),
    "userid"          BIGINT NOT NULL REFERENCES Users ("id"),
    "qty"           BIGINT NOT NULL,
    PRIMARY KEY ("name", "userid")
);

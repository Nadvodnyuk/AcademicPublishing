from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "authors" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "full_name" VARCHAR(50),
    "short_name" VARCHAR(50),
    "code" VARCHAR(20)  UNIQUE,
    "a_status" VARCHAR(128),
    "a_country" VARCHAR(128),
    "a_city" VARCHAR(128),
    "a_index" INT,
    "a_adress" VARCHAR(128),
    "a_org" VARCHAR(128),
    "a_sub_org" VARCHAR(128),
    "phone" VARCHAR(128),
    "email" VARCHAR(128),
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "modified_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(20) NOT NULL UNIQUE,
    "name" VARCHAR(50),
    "password" VARCHAR(128),
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "modified_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "works" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "field" VARCHAR(225) NOT NULL,
    "title" VARCHAR(225) NOT NULL,
    "event" VARCHAR(225) NOT NULL,
    "status" VARCHAR(225) NOT NULL,
    "year" INT NOT NULL,
    "org" VARCHAR(128) NOT NULL,
    "sub_org" VARCHAR(128),
    "country" VARCHAR(128) NOT NULL,
    "city" VARCHAR(128) NOT NULL,
    "index" INT NOT NULL,
    "mentor" VARCHAR(225),
    "consultant" VARCHAR(225),
    "abstract" VARCHAR(500) NOT NULL,
    "key_words" VARCHAR(50) NOT NULL,
    "intro" TEXT NOT NULL,
    "aim" TEXT NOT NULL,
    "materials_methods" TEXT NOT NULL,
    "results" TEXT NOT NULL,
    "conclusion" TEXT NOT NULL,
    "literature" TEXT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "modified_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "authorsworks" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "modified_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "author_id_id" INT NOT NULL REFERENCES "authors" ("id") ON DELETE CASCADE,
    "work_id_id" INT NOT NULL REFERENCES "works" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """

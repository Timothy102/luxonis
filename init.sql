-- init.sql

-- Create the database
CREATE DATABASE sreality_properties;

-- Connect to the database
\c sreality_properties;

-- Create the table to store properties
CREATE TABLE properties (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    image_url TEXT NOT NULL,
    href TEXT NOT NULL
);

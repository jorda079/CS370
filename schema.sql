DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS questionnaire;

CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            password TEXT,
            email TEXT,
            address TEXT,
            phone TEXT,
            gender TEXT,
            birth TEXT, 
            introduce TEXT,
            profile_photo TEXT,
            hb REAL
);

CREATE TABLE IF NOT EXISTS questionnaire (
            _id INTEGER PRIMARY KEY AUTOINCREMENT,
            group_num TEXT,
            comments TEXT
);
--
--  Schema for our NameEmail table
--  ------------------------------
--  Reference for datatypes:
--     https://www.sqlite.org/datatype3.html
--  Note the date_* columns are stored as strings, specifically:
--     CURRENT_TIMESTAMP returns dates in the format "1970-01-01 00:00:00"
--
CREATE TABLE NameEmail
   ( id INTEGER PRIMARY KEY AUTOINCREMENT,
     name TEXT,
     email TEXT,
     site TEXT DEFAULT 'groja.com',
     active INTEGER DEFAULT 1,
     date_added TEXT DEFAULT CURRENT_TIMESTAMP,
     date_changed TEXT DEFAULT CURRENT_TIMESTAMP,
     consulting INTEGER DEFAULT 0,
     newsletter INTEGER DEFAULT 0,
     portrait INTEGER DEFAULT 0
   )


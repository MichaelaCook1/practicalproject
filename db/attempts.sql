use attempts_db;
CREATE TABLE IF NOT EXISTS attempts(
	id INTEGER NOT NULL,
	value INTEGER NOT NULL,
	result BOOLEAN,
	PRIMARY KEY(id)
	);

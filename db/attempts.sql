use attempts_db;
CREATE TABLE IF NOT EXISTS attempts(
	id INTEGER NOT NULL,
	value INTEGER NOT NULL,
	result STRING(7) NOT NULL,
	PRIMARY KEY(id)
	);

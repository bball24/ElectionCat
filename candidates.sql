CREATE TABLE candidates(
	Candidate_name VARCHAR(50) PRIMARY KEY,
	Candidate_bio VARCHAR(65535) Unique,
	Candidate_position VARCHAR(50) NOT NULL
);
COPY candidates(Candidate_name, Candidate_bio, Candidate_position)
FROM '/Users/JerryTan/Desktop/sample2.csv' DELIMITER ',' CSV HEADER;

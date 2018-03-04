CREATE TABLE votes(
	student_id integer not null,
	Candidate_name VARCHAR(50) unique,
	Candidate_position VARCHAR(50) NOT NULL,
	vote_count integer not null,
)
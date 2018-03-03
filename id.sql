CCREATE TABLE listofIDS(
student_id integer NOT NULL);



COPY listofIDS(student_id) 
FROM '/Users/JerryTan/Desktop/sample.csv' DELIMITER ',' CSV HEADER;
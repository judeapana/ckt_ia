
SEAT ARRANGEMENT MANAGER
Documentation

Seat arrangement manager is a web application dedicated to resolving issues relating to arranging students when engaged in an official examination.
It has a specific use case which involves arranging students into two categories (A) and (B) on single desk observing different courses examination, where no two students writing the same course should be allowed to seat on the same desk.
For each category (A) or (B) a list of students on a template(.csv) are uploaded.


INSTALLATION

Before you start, please have the lastest version of >= Python3.6 installed ( https://youtu.be/f67BoRTQjJU ).
when “.zip” file is obtained kindly extract file onto any directory.

































Once the file is extracted open the folder.
To Run the application, run “run.bat” file by double clicking on it.
 









		
		







A terminal will appear indicating the application running
			





	






		













Keep the terminal window running and goto any browser and in the search box type “127.0.0.1:5000”


	


OPERATION

CREATING AN ARRANGEMENT

1) Rows: Are the number of desks within a specific Hall
2) Name of Hall: Is the name of hall examination is conducted
3) Course: Name of the course eg (CSC 201)
4) Upload Col (A) or Upload Col (B) Category: For each “UPLOAD” group A or B defines the seating position of students.
	
The above diagram shows the seating arrangement of students
A student seating at 2A is located at the second row first seat category (A)

Uploads are grouped from 1 to 3 allowing you to upload as many as possible files and different courses to partake in an examination in the same hall.

CREATING UPLOAD FILE OR DOCUMENT

1) Create a .csv file with Headers “STUDENT ID”, “PROGRAMME”, “STUDENT NAME ” populate the document and upload at the various sections.

Once you have uploaded your files containing students

	


Once you have specified the number of rows, the name of the hall and the courses and uploaded 




Once you have completed the upload of the file click on generate to create your arrangements


Above is a report of the arrangment.

EXITING THE APPLICATION

To exit the application close the terminal window

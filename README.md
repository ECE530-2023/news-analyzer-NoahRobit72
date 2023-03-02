## Here I am building a 3 APIs for:
* Secure File Uploader/Ingester
* Text NLP Analysis
* News feed Ingester

## Why Mongo DB?
1.  The document-oriented approach allows non-defined attributes to be modified on the fly. This is a key contrast between MongoDB and other relational databases. 
2.  JSON is widely used across for frontend and API communication. It only makes sense for the database to use the same protocol. 

Structure:
![Structure](<img width="645" alt="Structure" src="https://user-images.githubusercontent.com/64294283/222464308-8a3dba95-f4ff-4ca6-9214-1ff07d01ed1d.png">
)

## Database Structure

There will be three containers for Users, File Storage, and Text Analysis.  
Additionally, there will be documents for each of the users in our system. 

* User:
	* User ID: 
	* Username:
	* Password:

* Files Storage:
 	* User ID:
	* File ID:
	* File Name:
	* File Type:
	* Favorite Status:
	* Date of creation


* Text Analysis:
	* File ID:
	* Sentiment Analysis
	* Summary Analysis 
	



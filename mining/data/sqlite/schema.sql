
-- This file is not to be run
--
-- The Flask-SQLAlchemy framework already took care of table creation and index creation

DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Threads;
DROP TABLE IF EXISTS Messages;

CREATE TABLE Users (
	UserId 			INT PRIMARY KEY,
	LIHKGUserId 	INT NOT NULL UNIQUE,
	Nickname		VARCHAR NOT NULL,
	Gender			VARCHAR(1) NOT NULL,
	CreateDate		DATETIME NOT NULL,
	LastUpdate		DATETIME NOT NULL,
	RetrievedDate	DATETIME NOT NULL
);

CREATE TABLE Threads (
	ThreadId			INT PRIMARY KEY,
	User_UserId 		INT NOT NULL,
	LIHKGThreadId 		INT NOT NULL UNIQUE,
	CategoryId 			INT NOT NULL,
	SubCategoryId 		INT NOT NULL,
	Title 				VARCHAR NOT NULL,
	NumberOfReplies 	INT NOT NULL,
	NumberOfUniReplies	INT NOT NULL,
	LikeCount 			INT NOT NULL,
	DislikeCount 		INT NOT NULL,
	CreateDate			DATETIME NOT NULL,
	LastUpdate			DATETIME NOT NULL,
	RetrievedDate		DATETIME NOT NULL,
	FOREIGN KEY(User_UserId)		REFERENCES Users(UserId)
);

CREATE TABLE Messages (
	MessageId 		INT PRIMARY KEY,
	Thread_ThreadId	INT NOT NULL,
	User_UserId 	INT NOT NULL,
	LikeCount 		INT NOT NULL,
	DislikeCount 	INT NOT NULL,
	Message 		VARCHAR NOT NULL,
	MessageNumber 	INT NOT NULL,
	CreateDate		DATETIME NOT NULL,
	LastUpdate		DATETIME NOT NULL,
	RetrievedDate	DATETIME NOT NULL,
	FOREIGN KEY(Thread_ThreadId) 	REFERENCES Threads(ThreadId),
	FOREIGN KEY(User_UserId)		REFERENCES Users(UserId)
);

CREATE INDEX Users_UserId_LIHKGUserId 
ON Users(UserId, LIHKGUserId);

CREATE INDEX Threads_ThreadId_UserUserId_LIHKGUserId
ON Threads(ThreadId, User_UserId, LIHKGThreadId);

CREATE INDEX Messages_MessageId_ThreadThreadId_UserUserId
ON Messages(MessageId, Thread_ThreadId, User_UserId);
# Weekday-Assignment

Problem Statment

We hope you're doing well. As your profile gets shortlisted for Backend Engineer role and you are eligible for the Assignment evaluation stage.
Below is the problem statement designed specifically to evaluate your backend engineering skills :-


Problem Statement: You are provided with the following array:
Input: [[1, 2, 3], [20], [2, 4, 8], [1, 1], [15], [11, 2, 4], [40], [1, 2], [1, 3, 2], [48]]

The array represents a book. Each element of the array is a chapter.
Each number within the element represents a section of the chapter.
The value of the number represents the number of questions in that section.


Objective: You need to regroup the chapters in the book to minimize the number of overall chapters while keeping the following two constraints in mind:
A given chapter cannot be broken down into smaller chapters.
The total number of questions in a new chapter should not exceed 30.


Expected Output: [[1, 2, 3, 20, 1, 1], [2, 4, 8, 15], [11, 2, 4, 1, 2, 1, 3, 2], [40], [48]]

Alternate Output:[[48], [40], [20, 1, 2, 3, 1, 2], [15, 2, 4, 8], [11, 2, 4, 1, 3, 2, 1, 1]]

Instructions:
The coding language to be used is Python.
Kindly share your solution in a Word document and email it to me within the next 48 hours.
Feel free to reach out if you have any questions.





Approach

1.	Sorting Chapters by Question Count:
	•	I first sorted the chapters in descending order based on the total number of questions in each chapter. This ensures that chapters with the highest number of questions are prioritized for allocation.

2.	Maintaining a Limit:
	•	The limit variable is set to 30, representing the maximum allowable questions per chapter.

3.	Iterative Allocation:
	•	For each chapter, I checked if it could fit into an existing group of chapters (i.e., a “new chapter”) without exceeding the limit.
	•	If the chapter fit within the limit of an existing group, it was merged into that group.
	•	Otherwise, it was added as a new chapter in the output list.

4.	Output:
	•	The final regrouped chapters are displayed, ensuring the constraints are respected while minimizing the total number of chapters.


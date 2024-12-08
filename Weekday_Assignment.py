chapters = [[1, 2, 3], [20], [2, 4, 8], [1, 1], [15], [11, 2, 4], [40], [1, 2], [1, 3,2], [48]]

limit = 30

# Sort the given chapter in decreasing order of sums of quesions
chapters.sort(key=lambda x: sum(x), reverse=True)

# store sum of each chapters's questions
sum_of_ques = []
for chapter in chapters:
    sum_of_ques.append(sum(chapter))

output = []

# logic
for i in range(len(chapters)):
    for new_chapter in output:
        if sum(new_chapter) + sum_of_ques[i] <= limit:
            new_chapter.extend(chapters[i])
            sum_of_ques[i] = None
            break
        
    if sum_of_ques[i]:
        output.append(chapters[i])
        

print("The updated chapters are as follows:")    
print(output)

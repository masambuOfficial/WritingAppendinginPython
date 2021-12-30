import xlsxwriter

# Assignment. 
# In groups that are already in place please do the following assignments. 
# Create a function based programme in python that calculates a final mark for a student. Where a student is supposed to have 3 sets of tests. Test 1 and Test 2 and coursework. Only the best two  of the three are considered . The average of the best two is calculated  and divided by 2. Then the percentage of the average derived  is calculated and multiplied by 40. The final test  result is out of 60 and  goes through the same process  of average calculation as the tests and is later added to the test results to come up with the final mark . Write the name of the student and the  best two marks of a student on a text file, plus  the final test mark and the total mark. For a user  to be able to access this information they should first input student  their details.  The system should also be able to write  on the excel too. This assignment is due Friday 31st December 2021.



print("\t\t WELCOME TO PYTHON WITH OZZY \t\t")
print("\t\t =========================== \t\t")
def std_marks():
    outfile = open('marks.txt' , 'a')
    workbook = xlsxwriter.Workbook('marks.xlsx')
    worksheet = workbook.add_worksheet()

    std_name = input("Please enter your Fulname: ")
    test1 = int(input("Enter your test 1 Marks: "))
    test2 = int(input("Enter your test 2 Marks: "))
    coursework = int(input("Enter your coursework Marks: "))
    final_test = int(input("Enter the Final Test Mark: "))
    

    if test1 <= test2:
        total_mark = test2 + coursework
    else:
        total_mark = test1 + coursework
        
    avg = total_mark/2
    percentage_avg = (avg/100)*40

    if final_test > 60:
        print("The final test mark must be below or equal to 60")
    else:
        final_mark = final_test + percentage_avg
        
    

    worksheet.write('A1', "Student Name")
    worksheet.write('B1', "Total Mark")
    worksheet.write('C1', "Final Mark")
    worksheet.write('A2', std_name)
    worksheet.write('B2', str(total_mark))
    worksheet.write('C2', str(final_mark))
    workbook.close()

    outfile.write(std_name + ":" '\t')
    outfile.write("Total Mark: " + str(total_mark) + '\t\t')
    outfile.write("Final Mark: " + str(final_mark) + '\n')
    outfile.close()
   
     
std_marks()
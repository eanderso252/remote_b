class ClassSchedule:
   def __init__(self, course, instructor):
       self.course = course
       self.instructor = instructor
 
   def display_course(self):
       print(f'Course: {self.course}, Instructor: {self.instructor}')

sched = ClassSchedule('Chemistry', 'Mr. Doe') # initializing
 
sched.display_course() # prints Course: Chemistry, Instructor: Mr. Doe
print(sched.course) # prints 'Chemistry       
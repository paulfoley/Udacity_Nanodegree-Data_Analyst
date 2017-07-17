# Data Analysis - Udacity Student Data

[Udacity](https://www.udacity.com/), one of the best online education companies in the world, has provided sample student data. In this analysis we're going to derive insights on what makes a student pass one of their Nanodegrees versus not passing a course.


## Questions for Analysis
Below are the questions we're going to answer using the [Udacity](https://www.udacity.com/) sample student data. 

### Question 1

Effort has been known to have a strong correlation with succes in almost every activity. For our first question, let's look at how much time the student has spent in the classroom and learning for students that passed versus the students that did not pass.

* Is there a difference in time spent in the classroom for passing students?

### Question 2

Next let's look at how many lessons each student is taking. The idea of which is, the more lessons the more likely a student is going to pass.

* What's the difference in number of lessons taken by students who pass versus students who don't pass?

### Question 3

Next let's look at a students study habits, are students who do something daily more likely to pass then student's who don't learn daily.

* What's the difference in daily study habits of the students who pass versus students who don't pass?


## Getting Started

### Prerequisites

You'll need to install:

* [Anaconda](https://www.continuum.io/downloads)
* [Python (Minimum 3)](https://www.continuum.io/blog/developer-blog/python-3-support-anaconda)
* [Pandas](https://anaconda.org/anaconda/pandas)
* [Numpy](https://anaconda.org/anaconda/numpy)
* [Matplotlib](https://anaconda.org/anaconda/matplotlib)

### Data Files:

#### enrollments.csv

Data about a random subset of Data Analyst Nanodegree students who complete
their first project and a random subset of students who do not.

Columns:
    - account_key:    A unique identifier for the account of the student who
                     enrolled.

    - status:         The enrollment status of the student at the time the data
                      was collected. Possible values are 'canceled' and
                      'current'.

    - join_date:      The date the student enrolled.

    - cancel_date:    The date the student canceled, or blank if the student has
                      not yet canceled.

    - days_to_cancel: The number of days between join_date and cancel_date, or
                      blank if the student has not yet canceled.

    - is_udacity:     True if the account is a Udacity test account, False
                      otherwise.

    - is_canceled:    True if the student had canceled this enrollment at the
                      time the data was collected, False otherwise.

-------------------------------------------------------------------------------

#### daily_engagement.csv:

Data about engagement within Data Analyst Nanodegree courses for each student in
the enrollment table on each day they were enrolled. Includes a record even if
there was no engagement that day. Includes engagement data from both the
supporting courses for the Nanodegree program, and the corresponding freely
available courses with the same content.

Columns:
    - acct:                  A unique identifier for the account of the student
                             whose engagement data this is.

    - utc_date:              The date for which the data was collected.

    - num_courses_visited:   The total number of Data Analyst Nanodegree courses
                             the student visited for at 2 minutes on this day.
                             Nanodegree courses and freely available courses
                             with the same content are counted separately.

    - total_minutes_visited: The total number of minutes the student spent
                             taking Data Analyst Nanodegree courses on this day.

    - lessons_completed:     The total number of lessons within Data Analyst
                             Nanodegree courses on this day.

    - projects_completed:    The total number of Data Analyst Nanodegree
                             projects the student completed on this day.

-------------------------------------------------------------------------------

#### project_submissions.csv:

Data about submissions for Data Analyst Nanodegree projects for each student in
the enrollment table.

Columns:
    - creation_date:    The date the project was submitted.

    - completion_date:  The date the project was evaluated.

    - assigned_rating:  This column has 4 possible values:
                        blank - Project has not yet been evaluated.
                        INCOMPLETE - Project did not meet specifications.
                        PASSED - Project met specifications.
                        DISTINCTION - Project exceeded specifications.
                        UNGRADED - The submission could not be evaluated
                                   (e.g. contained a corrupted file)

    - account_key:      A unique identifier for the account of the student who
                        submitted the project.

    - lesson_key:       A unique identifier for the project that was submitted.

    - processing_state: This column has 2 possible values:
                        CREATED - Project has been submitted but not evaluated.
                        EVALUATED - Project has been evaluated.

-------------------------------------------------------------------------------

#### daily_engagement_full.csv:

Similar to daily_engagement.csv, but with engagement further broken down by
course and with more columns available. This file is about 500 megabytes, which
is why the smaller daily_engagement.csv file was created. This dataset is
optional; it is not needed to complete the course.

In addition to the following columns, this table also contains all the same
columns as daily_engagement.csv, except with has_visited instead of
num_courses_visited.

Columns:
    - registration_date:  Date the account was registered.

    - subscription_start: Date paid subscription for the account started.

    - course_key:         Course in which activity is recorded.

    - sibling_key:        Free course with the same free content as course_key.
                          If course_key is a free course, course_key and
                          sibling_key are the same.

    - course_title:       Title of the course.

    - has_visited:        1 if the student visited this course for at least 2
                          minutes on this day.

### Analysis Files

* `Student_Data-Analysis.ipynb` - Main project file, an IPython Notbook that contains the analysis for the project


### Opening the Jupyter Notebook

The project `Student_Data-Analysis.ipynb` can be read using a Jupyter Notebook. There's also an HTML version `Bay_Area_Bike_Share-Analysis.html` included.

* Download the `Bay_Area_Bike_Share-Analysis.ipynb`
* Open your Command Prompt (PC) or terminal (Mac or Linux).
* On a PC click the Start button and search for "Command Prompt".
* On a Mac type command + spacebar. Then, type "terminal" in the Spotlight Search. You can also search for "terminal" in finder.
* Navigate to the directory where you downloaded the Jupyter notebook file.
* On a PC you might type: cd C:\Users\username\Downloads\, replacing your username. Learn more about basic terminal commands.
* On Mac or Linux you might type: cd ~/Downloads.
* Run the command `jupyter notebook Bay_Area_Bike_Share-Analysis.ipynb` in your terminal.

The Jupyter Notebook `Student_Data-Analysis.ipynb` has all project information.

### Special Note

If you try running a code block and get an error message like no module named matplotlib, then your distribution of Anaconda may be missing a package used in the project. That's okay – there's an easy way that you can install these packages. Take a look at Google for easy to use guides on installation!


## Authors

* **[Paul Foley](https://github.com/paulfoley)**
* [Udacity](https://www.udacity.com/)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


## Acknowledgments

* [Udacity](https://www.udacity.com/)

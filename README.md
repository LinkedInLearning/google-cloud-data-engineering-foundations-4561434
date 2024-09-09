# Google Cloud Data Engineering Foundations
This is the repository for the LinkedIn Learning course Google Cloud Data Engineering Foundations. The full course is available from [LinkedIn Learning][lil-course-url].

![lil-thumbnail-url]

This course provides a high-level overview of all the tools and data engineering techniques employed with Google Cloud. Instructor Bhavani Ravi covers important aspects of data engineering concepts—like ingestion, transformation, and analytics—from the eyes of the Google Cloud Platform. Bhavani first goes over data engineering foundations, then dives into Google Cloud data storage concepts, explaining the various types of Google Cloud Storage options and when to utilize each. Then, learn about Google Cloud data pipelines—their respective use cases, and why you would use data pipelines in data engineering workflows. If you’re looking to learn more about the spectrum of data engineering—and how to address data problems by identifying the right Google tool for the job—join Bhavani in this course.

_See the readme file in the main branch for updated instructions and information._
## Instructions
This repository has branches for each of the videos in the course. You can use the branch pop up menu in github to switch to a specific branch and take a look at the course at that stage, or you can add `/tree/BRANCH_NAME` to the URL to go to the branch you want to access.

## Branches
The branches are structured to correspond to the videos in the course. The naming convention is `CHAPTER#_MOVIE#`. As an example, the branch named `02_03` corresponds to the second chapter and the third video in that chapter. 
Some branches will have a beginning and an end state. These are marked with the letters `b` for "beginning" and `e` for "end". The `b` branch contains the code as it is at the beginning of the movie. The `e` branch contains the code as it is at the end of the movie. The `main` branch holds the final state of the code when in the course.

When switching from one exercise files branch to the next after making changes to the files, you may get a message like this:

    error: Your local changes to the following files would be overwritten by checkout:        [files]
    Please commit your changes or stash them before you switch branches.
    Aborting

To resolve this issue:
	
    Add changes to git using this command: git add .
	Commit changes using this command: git commit -m "some message"


## Installing
To use these exercise files, you must have the following installed:

1. Create a Google Cloud Platform account if you don't have one already.
2. Install the Google Cloud SDK on your local machine.
3. Create a new project on Google Cloud Platform.
4. Enable the necessary APIs for the project.
5. Create a service account and download the key file.
6. Make a copy of the `.env.example` file and rename it to `.env`. Update the values in the `.env` file with your project details.
7. Install the necessary Python libraries using pip. `pip install -r requirements.txt`

### Instructor

Bhavani Ravi

Back-End Engineer, Speaker, and Community Leader

                            

Check out my other courses on [LinkedIn Learning](https://www.linkedin.com/learning/instructors/bhavani-ravi?u=104).

[0]: # (Replace these placeholder URLs with actual course URLs)

[lil-course-url]: https://www.linkedin.com/learning/google-cloud-data-engineering-foundations
[lil-thumbnail-url]: https://media.licdn.com/dms/image/v2/D4D0DAQGMLLjL1YXUgA/learning-public-crop_675_1200/learning-public-crop_675_1200/0/1725466934339?e=2147483647&v=beta&t=fPHCZNiUagMXWKX3FNdfNFTjPw3eG7TuOT9u0iTRjUY

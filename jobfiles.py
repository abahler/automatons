import argparse                 # For parsing command-line arguments
import os                       # For executing the cd and mkdir commands
from shutil import copyfile     # For copying files from source to destination

parser = argparse.ArgumentParser()

# Register your arguments
parser.add_argument('--company', help='The name of the company you are applying to')
parser.add_argument('--title', help='The job title of the open position')

# Pull the user input into variables
args = parser.parse_args()
job_title = args.title
company = args.company
# Replace spaces with nothing (smoosh words together)
# and strip any period off the end (i.e. "Widgets Inc.")
company_no_spaces = company.replace(' ', '').strip('.');

# This is the more modern way to do variable interpolation, as opposed to `print("Hello %s" % "world")`
print(f'Creating the specified files for the {job_title} position at {company}')

# Save our directories in variables
job_apps_directory = "/Users/alexbahler/Documents/Career/Product Management/Job Hunt 2020/Job Applications/"
newfolder = f'{company} - {job_title}'
resume_directory = "/Users/alexbahler/Documents/Career/Resume_and_More/PM";
# Now we start the process of copying files across different directories
os.chdir(job_apps_directory)
# Create a new folder with the company name and job title separated by a dash
os.mkdir(newfolder)

# TODO: if mkdir(newfolder) tries to create a folder that already exists, will it throw an error?

# Now go into the resume directory...
os.chdir(resume_directory)
# ...and copy files to the new folder you created
# Copy resume
copyfile('./AlexBahler_resume.docx', f'{job_apps_directory}/{newfolder}/AlexBahler_{company_no_spaces}_resume.docx')
# Copy cover letter
copyfile('./AlexBahler_coverletter.docx', f'{job_apps_directory}/{newfolder}/AlexBahler_{company_no_spaces}_coverletter.docx')

print('End of script!')

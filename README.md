# Interactive-Dashboard
Deploying an interactive dashboard using Streamlit, plotly, git and heroku

!! Ensure all files are in the same folder!!

1. Establish the connection with your local database through pandas
2. cache the dataframe for quicker response
3. create and copy setup.sh 
4. create and copy procfile
5. run pipreqs <directory-path> in your command line to return requirements.txt
6. Create git and heroku acc
7. Install heroku cli
8. Start and log in to initialize 
9. Deploy main webapp script to the instance created
10. Push the following codes:
  git add .
  git commit -m "some message"   -> TO TRACK COMMITS
  git push heroku master  
  
11. heroku ps:scale web=1 (free server)
12. negate auto sleep using kaffeine heroku (paste your domain name)

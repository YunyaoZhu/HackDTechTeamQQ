# RemindMe: HackDTechTeamQQ

## TL:DR
Personalized WFH Wellbeing Assistant - built for HackDTech 2020 
See project demo on [DevPost] (https://devpost.com/software/remindme-yjgzut)
dashboard deployed on [heroku] (https://descriptive-fitness.herokuapp.com)

## Inspiration 
With Work From Home (WFH) being the new normal, the world is experiencing another pandermic – physical inactivity (PI) and sedentary behavior (SB). Research like [A tale of two pandemics: How will COVID-19 and global trends in physical inactivity and sedentary behavior affect one another?] (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7194897/?fbclid=IwAR0xzJqHepeadte1tYOV5Aio1q5MIhjwMBsTZNy4GV0-mKem7cVwgamSMCo) has started to analyze the impact of COVID-19 on lifestyle changes, but the collateral effects of COVID situation will not be fully realized for quite some time, especially the adverse health impacts on vulnerable poulations such as obesity and diabetes patients. To help combat this issue, we designed RemindMe, a personalized WFH wellbing assistants. Its purpose is twofold: to help individuals be physically active during lockdown and work-from-home, and (if user consents) collects user data to feed into a longitudinal study exploring the collateral health impacts of COVID. 

## What it Does 
1) send personalized reminders to your desktop, mobile devices and watch 
2) show your analytics dashboard, which consists of your historic data and how active you're compared to the rest of population in your health condition group
3) (if user consents) collect data about their lifestyle habits to support long-term study 

## How we built it 
*Backend*: the analytical web application was built with Python's Dash framework and Plotly library for interactive visualizations. The web app was then deployed with Heroku. 
*Frontend*: 

## Challenges we ran into 
*Availability of time series data*: we struggled to find open, free time-series data that record an individual's activity level and intake. Going forward, we can make use of external APIs like Google Fit APIs to record user's activities, as well as Fitbit and AppleWatch APIs to gather wearable technology data. 

## Accomplishments that we're proud of 

## What we learned 

## What's next for RemindMe 
Once we have enough user data, we can calculate population summary statistics for each age range/gender/physical activity/BMI combination, and show users where they lie on the distribution. As developers, we believe that we shouldn't prescribe users with recommendations. Instead, we should empower users with as much interpretable data as possible to inform their decisions. 


